from ConnectState import ConnectState
from mcts import MCTS

def play():
    state = ConnectState()
    mcts = MCTS(state)

    while not state.game_over():
        print("Current state:")
        state.print()

        user_move = int(input("Enter a move: "))
        while user_move not in state.get_legal_moves():
            print("Illegal move")
            user_move = int(input("Enter a move: "))

        state.move(user_move)

        print(mcts.move(user_move),"____________________________________")



        state.print()

        if state.game_over():
            print("Player one won!")
            break

        print("Thinking...")


        print(mcts.search(8),"THis search mtcs")

        num_rollouts, run_time = mcts.statistics()
        print("Statistics: ", num_rollouts, "rollouts in", run_time, "seconds")
        move = mcts.best_move()

        print("move. this is mcts best move")

        print("MCTS chose move: ", move)

        state.move(move)


        print(mcts.move(move),"This is mcts.move(move)")

        if state.game_over():
            print("Player two won!")
            break


play()
