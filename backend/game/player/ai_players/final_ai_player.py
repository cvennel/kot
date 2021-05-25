from enum import Enum
from game.player.ai_players.master_ai_player import Master_AI_Player
import random
from game.dice.dice import DieValue


class turn_policy(Enum):
    attack = 0
    star = 1


class Final_AI_Player(Master_AI_Player):

    def choose_dice_to_re_roll(self, dice):
        reroll = []

        # TODO: improve these heuristics,
        attack_heuristic = self.distance_from_attack_victory()
        star_heuristic = self.distance_from_star_victory()

        if star_heuristic < attack_heuristic:
            strategy = turn_policy.star
        else:
            strategy = turn_policy.attack

        if strategy == turn_policy.star:
            die_enum = DieValue.THREE
            current_count = dice.count(DieValue.THREE)

            if dice.count(DieValue.TWO) > current_count:
                current_count = dice.count(DieValue.TWO)
                die_enum = DieValue.TWO

            if dice.count(DieValue.ONE) > current_count:
                current_count = dice.count(DieValue.ONE)
                die_enum = DieValue.ONE

            for i in range(len(dice)):
                if dice[i] == die_enum:
                    continue
                if random.choice([True, False]):
                    reroll.append(i)
            return reroll
        else:
            for i in range(len(dice)):
                if dice[i] == DieValue.ATTACK:
                    continue
                if random.choice([True, False]):
                    reroll.append(i)
            return reroll
