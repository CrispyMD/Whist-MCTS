from games.game import Game
from games.tic_tac_toe.tic_tac_toe import TicTacToe
from agents.mcts_agent import mcts_agent
from games.tic_tac_toe.tic_tac_toe import number_to_position



game = TicTacToe()
agent = mcts_agent(game)

while not game.is_terminal_state():
    print("Enter current move: ")

    user_move = number_to_position(int(input()))
    print(user_move, "####")
    game.apply_move_rc(user_move[0], user_move[1])

    game.print_board()
    print(game.state.board)
    if game.is_terminal_state():
        break

    agent.make_move()
    game.print_board()
    if game.is_terminal_state():
            break

print("********************************")
result = game.get_result()[0]
if result == 0.5:
    print("Draw. ", end="")
else:
     print(f"Winner is {'X' if game.get_result()[0] == 1 else 'O'}. ", end="")
print("Final board state is:")
game.print_board()
