import chess.pgn
import pickle

print(chess.__file__)
pgn = open("checkmates.pgn")

not_checkmates = []

for i in range(0, 10000):
    try:
        first_game = chess.pgn.read_game(pgn)
        endnode = first_game.end()
        before_end = endnode.parent.board()
        not_checkmates.append(before_end.fen())
    except UnicodeDecodeError:
        print("unicode")
    except ValueError:
        print("value error")
    except AttributeError:
        print("att error")

f = open('storenotcheckmate.pck1', 'wb')
pickle.dump(not_checkmates, f)
f.close()



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




