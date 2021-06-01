from game.player.player import Player
import copy
from statistics import mean
from typing import DefaultDict

from game.engine.run_offline_game import run_game
from game.engine.terminal_board import TerminalBoardGame
from game.player.ai_players.attack_ai_player import Attack_AI_Player
from game.player.ai_players.chaos_ai_player import Chaos_AI_Player
from game.player.ai_players.final_ai_player import Final_AI_Player
from game.player.ai_players.points_ai_player import Points_AI_Player

MAIN_PLAYER_NAME = "Final AI Bob"


def run_multiple_games(title, players, count=100):
    print(f"\nRunning scenario: {title}")
    win_counts = DefaultDict(int)
    for i in range(count):
        player_copy = copy.deepcopy(players)
        print(f"Running game {i}\r", end="")

        game_state = TerminalBoardGame()

        for player in player_copy:
            player.player_queue = game_state.players
            game_state.add_player(player)

        winner = run_game(game_state)
        win_counts[winner.username] += 1

    print(f"Win percenteges:")
    for winner in win_counts:
        win_percent = win_counts[winner]/sum(win_counts.values())
        win_percent *= 100
        print(f"\t{win_percent:.2f}% {winner}")
    return win_counts


def test_final_vs_chaos(final_ai, count=1):
    players = [final_ai]
    for i in range(1, count + 1):
        players.append(Chaos_AI_Player(
            None, username=f"CHAOS AI George{i}"))
    return run_multiple_games(f"Final AI vs {count}x Chaos AI", players)


def test_final_vs_attack(final_ai, count=1):
    players = [final_ai]
    for i in range(1, count + 1):
        players.append(Attack_AI_Player(
            None, username=f"Attack AI George{i}"))
    return run_multiple_games(f"Final AI vs {count}x Attack AI", players)


def test_final_vs_points(final_ai, count=1):
    players = [final_ai]
    for i in range(1, count + 1):
        players.append(Points_AI_Player(
            None, username=f"Points AI George{i}"))
    return run_multiple_games(f"Final AI vs {count}x Points AI", players)


if __name__ == "__main__":

    aggression_win_rates = {}

    for aggression_level in range(1, 11):
        aggression_level /= 10

        print(f"\n\n----Testing Aggression level {aggression_level}----")
        main_player = Final_AI_Player(
            None, username=MAIN_PLAYER_NAME, aggression_level=aggression_level)

        win_percentages = []

        for opponent_count in range(1, 6):
            percentages_chaos = test_final_vs_chaos(
                main_player, count=opponent_count)
            percentages_attack = test_final_vs_attack(
                main_player, count=opponent_count)
            percentages_points = test_final_vs_points(
                main_player, count=opponent_count)

            chaos_win_percent = percentages_chaos[MAIN_PLAYER_NAME] / \
                sum(percentages_chaos.values())

            attack_win_percent = percentages_attack[MAIN_PLAYER_NAME] / \
                sum(percentages_attack.values())

            points_win_percent = percentages_points[MAIN_PLAYER_NAME] / \
                sum(percentages_points.values())

            win_percentages.append(chaos_win_percent)
            win_percentages.append(attack_win_percent)
            win_percentages.append(points_win_percent)

        mean_win_rate = mean(win_percentages) * 100

        print(f"Mean victory rate for final AI: {mean_win_rate:.2f}%")
        aggression_win_rates[aggression_level] = mean_win_rate

    best_key = max(aggression_win_rates, key=aggression_win_rates.get)
    print("Best:                                    ")
    print(f"\tAggression level: {best_key} ")
    print(f"\tWin rate: {aggression_win_rates[best_key]:.2f}%")
