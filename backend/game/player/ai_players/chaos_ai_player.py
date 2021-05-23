from game.player.ai_players.master_ai_player import Master_AI_Player
import random

class Chaos_AI_Player(Master_AI_Player):

    def choose_dice_to_re_roll(self, dice):
        saved = []
        for i in range(len(dice)):
            if random.choice([True, False]):
                saved.append(i)
        return saved
