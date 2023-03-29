from stockfish import Stockfish

stockfish = Stockfish()

listofmoves = []

bora = input("Are you [B] or [W]: ")
bora = bora.lower()


if bora == "w" or bora == "white":
    while True:
        best = stockfish.get_best_move()
        print(best)
        listofmoves.append(best)
        stockfish.set_position(listofmoves)
        print(stockfish.get_board_visual())
        opponent = input("Opponent's move: ")
        listofmoves.append(opponent)
        stockfish.set_position(listofmoves)
elif bora == "b" or bora == "black":
    while True:
        opponent = input("Opponent's move: ")
        listofmoves.append(opponent)
        stockfish.set_position(listofmoves)
        best = stockfish.get_best_move()
        print(best)
        listofmoves.append(best)
        stockfish.set_position(listofmoves)
        print(stockfish.get_board_visual(False))
else:
    print("You suck at cheating. Try again \"nerd\"")
        
        
