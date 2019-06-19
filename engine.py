import sys
from FENUtil import FENUtil
from BoardRep import BoardRep
import random
import traceback

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
try:
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
            possible_next_boards = current_board.getLegalMoves()
            i = random.randint(0, len(possible_next_boards) - 1)
            move_string = BoardRep.numbersToAlg(possible_next_boards[i][1])
            writelog("legalmoves")
            writelog(str(len(possible_next_boards)))

            for i in range(0, len(possible_next_boards)):
                writelog(BoardRep.numbersToAlg(possible_next_boards[i][1]))

            print("bestmove " + move_string)
            writelog("bestmove " + move_string)


        sys.stdout.flush()
except Exception as e:
    with open("/home/evan/Code/Chess/errorlog.txt", 'a') as f:
        f.write(str(e))
        f.write(traceback.format_exc())
        f.write("i = " + str(i))

