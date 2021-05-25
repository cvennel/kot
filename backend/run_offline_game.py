from game.engine.terminal_board import TerminalBoardGame
from game.player.ai_players.chaos_ai_player import Chaos_AI_Player
from game.player.ai_players.final_ai_player import Final_AI_Player
from game.player.ai_players.attack_ai_player import Attack_AI_Player
from game.player.ai_players.points_ai_player import Points_AI_Player
from game.dice.dice_resolver import dice_resolution
from game.player.player import Player


if __name__ == "__main__":

    game_state = TerminalBoardGame()
    # game_state.add_player(Player(username="Real life Player"))
    game_state.add_player(Chaos_AI_Player(
        game_state.players, username="CHAOS AI George"))
    game_state.add_player(Final_AI_Player(
        game_state.players, username="Final AI Bob"))
    game_state.add_player(Attack_AI_Player(
        game_state.players, username="Attack AI Gandhi"))
    game_state.add_player(Points_AI_Player(
        game_state.players, username="Points AI Trump"))

    game_state.start_game()

    turn_counter = 1
    start_player = game_state.players.current_player
    while game_state.is_game_active():
        current_player = game_state.players.current_player
        print(f"\n{current_player.username} Turn {turn_counter}")

        # Tell the game to do initial turn actions such as the required first roll
        game_state.start_turn_actions(current_player)

        # Print what current player rolled
        print(f"{current_player.username} rolled {game_state.dice_handler.dice_values}")

        # Select what dice to re-roll as long as there are allowed re-rolls
        # (Press enter to select nothing)
        while game_state.dice_handler.re_rolls_left != 0:
            print(f"{current_player.username} has \
                {game_state.dice_handler.re_rolls_left} re-rolls left")

            # Get what user selected to re-roll
            to_re_roll = current_player.choose_dice_to_re_roll(
                game_state.dice_handler.dice_values)

            # log what was chosen
            print(f"{current_player.username} rerolls {to_re_roll}")

            # tell game state to perform re-roll
            game_state.re_roll(to_re_roll)
            print(f"{current_player.username} \
                    rolled {game_state.dice_handler.dice_values}")

        # Give a chance for real player to hit enter to continue, AI just returns
        current_player.acknowledge()

        # Game state acts on the resulting dice (heals, attacks, et)
        dice_resolution(game_state.dice_handler.dice_values, current_player,
                        game_state.players.get_all_alive_players_minus_current_player())

        # TODO: there is currently no opportunity to buy/use cards

        # Give everyone a chance to yield tokyo if they can
        for player in game_state.players.get_all_alive_players_minus_current_player():
            if player.allowed_to_yield:
                game_state.yield_tokyo_to_current_player(player)

        # Checks if anyone has won and give chance for special card actions
        game_state.post_roll_actions(game_state.players.current_player)

        # Advance the game to the next active player (also resets some states)
        game_state.get_next_player_turn()

        # Increment turn counter if back at starting player
        if game_state.players.current_player == start_player:
            turn_counter += 1
