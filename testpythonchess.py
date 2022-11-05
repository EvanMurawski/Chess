import chess.pgn
from BoardRep import BoardRep
from FENUtil import FENUtil

def generateCheckmateTest():
    pgn = open("GamesEndingInCheckmate.pgn")
    write_file= open("checkmate_test.txt", 'w')

    for i in range(0, 5000):
        if i%10 == 0:
            print("Checking num: ", i)
        try:
            game = chess.pgn.read_game(pgn)
        except UnicodeDecodeError:
            print("unicode error")
        except ValueError:
            print("value error")
        except AttributeError:
            print("att error")

        mainline = game.mainline()
        for move in mainline:
            fen = move.board().fen()
            write_file.write(fen+ "\n")

            if move.board().is_checkmate():
                write_file.write("True\n")
            else:
                write_file.write("False\n")

    pgn.close()
    write_file.close()


if __name__ == "__main__":
    generateCheckmateTest()




