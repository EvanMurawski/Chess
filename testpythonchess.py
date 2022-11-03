import chess.pgn
from BoardRep import BoardRep
from FENUtil import FENUtil

print(chess.__file__)
pgn = open("20kgames.pgn")


for i in range(0, 1000):
    if i%10 == 0:
        print("Checking num: ", i)
    try:
        game = chess.pgn.read_game(pgn)
    except UnicodeDecodeError:
        print("unicode")
    except ValueError:
        print("value error")
    except AttributeError:
        print("att error")

    mainline = game.mainline()
    for move in mainline:
        fen = move.board().fen()
        legals = list(move.board().legal_moves)
        num_legal = len(legals)
        legals_str = [str(move) for move in legals]

        my_boardrep = FENUtil.fenToBoard(fen)
        my_moves = my_boardrep.getLegalMoves()
        my_num_legal = len(my_moves)

        my_str = [BoardRep.moveToAlg(item) for item in my_moves]
        if my_num_legal != num_legal:
            print("Error found, game: ", i)

            print(fen)

            for movestring in my_str:
                if movestring not in legals_str:
                    print("My move ", movestring , " Is not in legal moves")

            for legalmove in legals_str:
                if legalmove not in my_str:
                    print("Legal move ", legalmove, " is not in my moves")




pgn.close()



#     try:
#         first_game = chess.pgn.read_game(pgn)
#         board = first_game.end().board()
#         if board.fen() != "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" and board.fen() != "rnbqkbnr/pppppppp/8/8/8/7P/PPPPPPP1/RNBQKBNR b KQkq - 0 1" and board.fen() != "rnbqkbnr/pppppppp/8/8/5P2/8/PPPPP1PP/RNBQKBNR b KQkq - 0 1":
#             fen_checkmates.append(board.fen())
#     except UnicodeDecodeError:
#         print("unicode")
#     except ValueError:
#         print("value error")
#
#
# print(fen_checkmates[500])
#
# f = open('store.pck1', 'wb')
# pickle.dump(fen_checkmates, f)
# f.close()




