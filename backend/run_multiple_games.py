from run_offline_game import run_game
from game.engine.terminal_board import TerminalBoardGame
from game.engine.terminal_board import TerminalBoardGame
from game.player.ai_players.chaos_ai_player import Chaos_AI_Player
from game.player.ai_players.final_ai_player import Final_AI_Player
from game.player.ai_players.attack_ai_player import Attack_AI_Player
from game.player.ai_players.points_ai_player import Points_AI_Player
from game.dice.dice_resolver import dice_resolution
from game.player.player import Player
from typing import DefaultDict, List
from enum import Enum


RUN_COUNTS = 1000
MAIN_PLAYER_NAME = "Final AI Bob"


class opponent_type(Enum):
    final_vs_chaos = 0
    final_vs_attack = 1
    final_vs_points = 2
    final_vs_final_ai_x1 = 3
    final_vs_final_ai_x2 = 4
    final_vs_final_ai_x3 = 5


def create_game(opponent: opponent_type):
    game_state = TerminalBoardGame()
    game_state.add_player(Final_AI_Player(
        game_state.players, username=MAIN_PLAYER_NAME))

    if opponent == opponent_type.final_vs_chaos:
        game_state.add_player(Chaos_AI_Player(
            game_state.players, username="CHAOS AI George"))
    elif opponent == opponent_type.final_vs_attack:
        game_state.add_player(Attack_AI_Player(
            game_state.players, username="Attack AI George"))
    elif opponent == opponent_type.final_vs_points:
        game_state.add_player(Points_AI_Player(
            game_state.players, username="Points AI George"))
    elif opponent == opponent_type.final_vs_final_ai_x1:
        game_state.add_player(Final_AI_Player(
            game_state.players, username="Final AI ONE"))
    elif opponent == opponent_type.final_vs_final_ai_x2:
        game_state.add_player(Final_AI_Player(
            game_state.players, username="Final AI ONE"))
        game_state.add_player(Final_AI_Player(
            game_state.players, username="Final AI TWO"))
    elif opponent == opponent_type.final_vs_final_ai_x3:
        game_state.add_player(Final_AI_Player(
            game_state.players, username="Final AI ONE"))
        game_state.add_player(Final_AI_Player(
            game_state.players, username="Final AI TWO"))
        game_state.add_player(Final_AI_Player(
            game_state.players, username="Final AI THREE"))
    return game_state


if __name__ == "__main__":
    for opponenet in [opponent_type.final_vs_chaos, opponent_type.final_vs_attack, opponent_type.final_vs_points]:
        print(f"\nGame type: {opponenet}")
        win_counts = DefaultDict(int)
        for i in range(RUN_COUNTS):
            print(f"Running game {i}\r", end="")
            game_state = create_game(opponenet)
            winner = run_game(game_state)
            win_counts[winner.username] += 1

        print(f"Win percenteges:")
        for winner in win_counts:
            win_percent = win_counts[winner]/sum(win_counts.values())
            win_percent *= 100
            print(f"\t{win_percent}% {winner}")

    percentages = {}

    for game_type in [opponent_type.final_vs_final_ai_x1, opponent_type.final_vs_final_ai_x2, opponent_type.final_vs_final_ai_x3]:
        print(f"\n\nPlaying game type {game_type}")
        for i in range(0, 11):
            win_counts = DefaultDict(int)
            for j in range(RUN_COUNTS):
                print(f"Running game {j}\r", end="")
                game_state = create_game(game_type)
                main_player = game_state.players.get_player_by_username_from_alive(
                    MAIN_PLAYER_NAME)

                main_player.aggression_level = i/10
                winner = run_game(game_state)
                win_counts[winner.username] += 1

            win_percent = win_counts[MAIN_PLAYER_NAME]/sum(win_counts.values())
            win_percent *= 100
            percentages[i] = win_percent

        best_key = max(percentages, key=percentages.get)
        print("Best:                                    ")
        print(f"\tAggression level: {best_key/10} ")
        print(f"\tWin rate: {percentages[best_key]}%")
