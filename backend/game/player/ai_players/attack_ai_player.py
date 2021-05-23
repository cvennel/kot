from game.player.ai_players.master_ai_player import Master_AI_Player
import random
from game.dice.dice import DieValue


class Attack_AI_Player(Master_AI_Player):

    def choose_dice_to_re_roll(self, dice):
        reroll = []
        for i in range(len(dice)):
            if dice[i] == DieValue.ATTACK:
                continue
            if random.choice([True, False]):
                reroll.append(i)
        return reroll
