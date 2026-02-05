from games.game import Game
from games.tic_tac_toe.tic_tac_toe import TicTacToe
from agents.random_agent import RandomAgent

def num_to_pos(n):
    if n < 1 or n > 9:
        raise ValueError("n must be between 1 and 9")
    
    n -= 1  # make it 0-based
    row = n // 3
    col = n % 3
    return (row, col)


game = TicTacToe()
agent = RandomAgent(game)

while not game.is_terminal_state():
    print("Enter current move: ")

    user_move = num_to_pos(int(input()))
    game.apply_move(user_move)

    if game.is_terminal_state():
        break

    agent.make_move()
    game.print_board()

print("********************************")
print(f"Winner is {game.get_result()}. Final board state is:")
game.print_board()
