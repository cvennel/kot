from game.player.master_ai_player import Master_AI_Player


class Chaos_AI_Player(Master_AI_Player):

    def choose_dice_to_re_roll(self, dice):
        # TODO: replace with method to randomly select dice from 0 --> len(dice)
        return [0, 1, 2]
