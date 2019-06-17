import sys
from FENUtil import FENUtil
from BoardRep import BoardRep
import random

def writelog(message):
    logfile = open("/home/evan/Code/Chess/log.txt", "a")
    logfile.write(message + "\n")
    logfile.close()

def handleuci(line):
    if line.startswith("isready"):
        print("readyok")
        writelog("TX: " + "readyok")
        return
    else:
        return


writelog("Start")

fen_position = ""

while True:
    line = sys.stdin.readline()
    if not line:
        break

    writelog(line)
    if line.startswith("isready"):
        print("readyok")
        writelog("TX: readyok")
    elif line.startswith("uci"):
        print("id evanchess")
        writelog("TX: id evanchess")
    elif line.startswith("position fen"):
        fen_position = line.strip("position fen")
        writelog("Saw position: " + fen_position)
        current_board = FENUtil.fenToBoard(fen_position)
    elif line.startswith("go"):
        possible_next_boards = current_board.getPseudoLegalMoves()
        i = random.randint(0, len(possible_next_boards))
        move_string = BoardRep.numbersToAlg(possible_next_boards[i][1])
        print("bestmove " + move_string)
        writelog("bestmove " + move_string)


    sys.stdout.flush()


