from game.player.player import Player
from game.values import constants
from game.engine.player_queue import GamePlayers


class Master_AI_Player(Player):
    def __init__(self, player_queue, username=None, passiveness=.5):
        super().__init__(username=username)
        self.player_queue: GamePlayers = player_queue
        self.passiveness = passiveness

    def acknowledge(self):
        return

    def distance_from_star_victory(self):
        return constants.VICTORY_POINTS_TO_WIN - self.victory_points

    def distance_from_attack_victory(self):
        total_health = 0
        for player in self.player_queue.get_all_alive_players_minus_current_player():
            total_health += player.current_health
        return total_health

    def decide_to_yield(self):
        return True

    def distance_to_next_turn(self):
        i = 0

        current_index = self.player_queue.players.index(
            self.player_queue.current_player)

        turn_order = self.player_queue.players.copy()
        turn_order += self.player_queue.players.copy()

        for j in range(current_index, len(turn_order)):
            if turn_order[j] == self:
                break
            else:
                i += 1
        return i

    def attackable_players(self):
        attackables = []
        for player in self.player_queue.get_all_alive_players_minus_current_player():
            if player.location != self.location:
                attackables.append(player)
        return attackables
