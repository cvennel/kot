from game.player.player import Player
from game.values import constants
from game.engine.player_queue import GamePlayers


class Master_AI_Player(Player):
    def __init__(self, player_queue, username=None):
        super().__init__(username=username)
        self.player_queue: GamePlayers = player_queue

    def acknowledge(self):
        return

    def distance_from_star_victory(self):
        return constants.VICTORY_POINTS_TO_WIN - self.victory_points

    def distance_from_attack_victory(self):
        total_health = 0
        for player in self.player_queue.get_all_alive_players_minus_current_player():
            total_health += player.current_health
        return total_health
