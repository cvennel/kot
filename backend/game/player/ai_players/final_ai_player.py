from enum import Enum
from game.player.ai_players.master_ai_player import Master_AI_Player
import random
from game.dice.dice import DieValue


class turn_policy(Enum):
    attack = 0
    star = 1


class Final_AI_Player(Master_AI_Player):

    def get_current_policy(self):
        # TODO: improve these heuristics,
        attack_heuristic = self.distance_from_attack_victory() * self.passiveness
        star_heuristic = self.distance_from_star_victory() * (1 - self.passiveness)

        if star_heuristic < attack_heuristic:
            strategy = turn_policy.star
        else:
            strategy = turn_policy.attack

        return strategy

    def decide_to_yield(self):
        # return True
        strategy = self.get_current_policy()
        distance_to_next_turn = self.distance_to_next_turn()

        if strategy == turn_policy.star:
            if distance_to_next_turn * 2 > self.current_health:
                return True
        else:
            if distance_to_next_turn > 0:
                return True

        return False

    def choose_dice_to_re_roll(self, dice, verbose=False):
        reroll = []

        strategy = self.get_current_policy()

        if verbose:
            print(f"{self.username} strategy: {strategy}")

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
                else:
                    reroll.append(i)
            return reroll
