from game.engine.terminal_board import TerminalBoardGame
from game.player.ai_player import AI_Player
from game.dice.dice_resolver import dice_resolution


if __name__ == "__main__":

    game_state = TerminalBoardGame()
    game_state.add_player(AI_Player(username="AI George"))
    game_state.add_player(AI_Player(username="AI Bob"))

    game_state.start_game()

    i = 1
    while game_state.is_game_active():
        print(f"\n Turn {i}")

        game_state.start_turn_actions(game_state.players.current_player)
        cur_pname = game_state.players.current_player.username
        print(f"It's {cur_pname}'s turn")

        print(f"{cur_pname} rolled {game_state.dice_handler.dice_values}")
        while game_state.dice_handler.re_rolls_left != 0:
            print(
                f"{cur_pname} has {game_state.dice_handler.re_rolls_left} re-rolls left")
            print(f"{cur_pname} rerolls [0,1,2]")
            game_state.re_roll([0, 1, 2])
            print(f"{cur_pname} rolled {game_state.dice_handler.dice_values}")

        dice_resolution(game_state.dice_handler.dice_values, game_state.players.get_current_player(),
                        game_state.players.get_all_alive_players_minus_current_player())

        for player in game_state.players.get_all_alive_players_minus_current_player():
            if player.allowed_to_yield:
                game_state.yield_tokyo_to_current_player(player)

        game_state.post_roll_actions(game_state.players.current_player)

        game_state.get_next_player_turn()

        i += 1
