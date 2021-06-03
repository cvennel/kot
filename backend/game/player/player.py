import random
from typing import List

from game.cards.card import Card
from game.cards.keep_cards.energy_manipulation_cards.friend_of_children import FriendOfChildren
from game.cards.keep_cards.energy_manipulation_cards.were_only_making_it_stronger import WereOnlyMakingItStronger
from game.cards.keep_cards.health_manipulation_cards.it_has_a_child import ItHasAChild
from game.cards.keep_cards.health_manipulation_cards.regeneration import Regeneration
from game.cards.keep_cards.turn_manipulation_cards.GiantBrain import GiantBrain
from game.cards.keep_cards.health_manipulation_cards.armor_plating import ArmorPlating
from game.player.player_status_resolver import json_players_hand
from game.values import constants
from game.values.locations import Locations


class Player:
    def __init__(self, username=None):
        if username is None:
            self.username = "guest_{}".format(random.randint(1000, 9999))
        else:
            self.username = username
        self.monster_name = None
        self.maximum_health = self.current_health = constants.DEFAULT_HEALTH
        self.location = Locations.OUTSIDE
        self.is_alive = True
        self.victory_points = constants.DEATH_HIT_POINT
        self.energy = constants.DEFAULT_ENERGY_CUBE
        self.cards: List[Card] = []
        self.allowed_to_yield = False
        self.gets_bonus_turn = False
        self.newly_dead = False

    @property
    def dice_allowed(self):
        allowed_dice = constants.DEFAULT_DICE_TO_ROLL
        if self.has_instance_of_card(GiantBrain()):
            allowed_dice += 1
        return allowed_dice

    @property
    def is_newly_dead(self):
        if self.newly_dead:
            self.newly_dead = False
            return True
        else:
            return False

    def set_monster_name(self, monster_name):
        self.monster_name = monster_name

    def set_username(self, username):
        self.username = username

    def __eq__(self, other):
        return issubclass(type(other), Player) and self.username == other.username

    def is_in_tokyo(self):
        return self.location == Locations.TOKYO

    def move_to_tokyo(self):
        self.location = Locations.TOKYO

    def leave_tokyo(self):
        self.location = Locations.OUTSIDE

    def update_health_by(self, change_integer):
        if self.has_instance_of_card(WereOnlyMakingItStronger()) and change_integer <= -2:
            WereOnlyMakingItStronger().special_effect(self, None)
        if self.has_instance_of_card(Regeneration()):
            change_integer = Regeneration().special_effect(self, change_integer)
        if self.has_instance_of_card(ArmorPlating()):
            change_integer = ArmorPlating().special_effect(self, change_integer)
        self.current_health += change_integer
        if self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
        if self.current_health <= 0:
            if self.has_instance_of_card(ItHasAChild()):
                ItHasAChild().special_effect(self, None)
            else:
                self.is_alive = False
                self.newly_dead = True

    def update_max_health_by(self, change_integer):
        self.maximum_health += change_integer
        if self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
        if self.maximum_health < 0:
            self.maximum_health = 0

    def update_victory_points_by(self, change_integer):
        self.victory_points += change_integer
        if self.victory_points < 0:
            self.victory_points = 0

    def update_energy_by(self, change_integer):
        if self.has_instance_of_card(FriendOfChildren()):
            change_integer = FriendOfChildren.add_extra_energy(change_integer)
        self.energy += change_integer
        if self.energy < constants.DEFAULT_ENERGY_CUBE:
            self.energy = constants.DEFAULT_ENERGY_CUBE

    def lose_all_stars(self):
        self.victory_points = 0

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def has_instance_of_card(self, card: Card):
        for player_card in self.cards:
            if type(player_card) == type(card):
                return True
        return False

    def discard_all_cards(self):
        self.cards.clear()

    def generate_player_status_as_dictionary(self):
        location_string = "Out" if self.location == Locations.OUTSIDE else "In"
        return {
            "username": self.username,
            "current_health": self.current_health,
            "location": location_string,
            "is_alive": self.is_alive,
            "victory_points": self.victory_points,
            "energy": self.energy,
            "cards": json_players_hand(self.cards)
        }

    #######################################
    # Below methods just for offline game #
    #######################################

    def choose_dice_to_re_roll(self, dice):
        input_str = input("Choose which dice to re-roll (zero based index)")

        selected_dice = []
        for x in input_str.split():
            try:
                try:
                    dice[(int(x))]
                except IndexError:
                    print(f"{x} is out of range!")
                    return self.choose_dice_to_re_roll(dice)
                selected_dice.append(int(x))
            except:
                print("error getting dice indices! try again!")
                return self.choose_dice_to_re_roll(dice)

        return selected_dice

    def acknowledge(self):
        input("Press enter to contine")
        return

    def decide_to_yield(self):
        print(
            f"You have been attacked! Your health is now {self.current_health}")
        user_input = input("Would you like to yield Tokyo? Y/N")
        if "y" in user_input.lower():
            return True
        elif "n" in user_input.lower():
            return False
        else:
            return self.decide_to_yield()
