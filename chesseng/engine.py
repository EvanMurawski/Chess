#todo, keep root node as global variable, check if the next move is already there, pass that node directly as the next root node

import sys
sys.path.extend(['/home/evan/Code/Chess'])
from chesseng.FENUtil import FENUtil
from chesseng.BoardRep import BoardRep
from chesseng.Node import Node
import chesseng.AlphaBetaNew as AlphaBetaNew
import random
import traceback
import time



def writelog(message):
    logfile = open("../log/log_1.txt", "a")
    logfile.write(message + "\n")
    logfile.close()

def handleuci(uci_line):
    if uci_line.startswith("isready"):
        print("readyok")
        writelog("TX: " + "readyok")
        return
    else:
        return

def randomMove():
    possible_next_boards = current_board.getLegalMoves()
    i = random.randint(0, len(possible_next_boards) - 1)
    move_string = BoardRep.numbersToAlg(possible_next_boards[i][1])
    writelog("legalmoves")
    writelog(str(len(possible_next_boards)))

    for i in range(0, len(possible_next_boards)):
        writelog(BoardRep.numbersToAlg(possible_next_boards[i][1]))

    print("bestmove " + move_string)
    writelog("TX: bestmove " + move_string)



def abmove():
    t = time.time()
    writelog("start analyzing")
    best_node = AlphaBetaNew.getBestMoveMulti(Node(current_board), current_board.whitemove)
    writelog("done analyzing" + str(time.time() - t))

    best_move = best_node.move_squares

    move_string = BoardRep.numbersToAlg(best_move)
    print("bestmove " + move_string)
    writelog("TX: bestmove " + move_string)



writelog("Start")
fen_position = ""
try:
    while True:
        line = sys.stdin.readline()
        if not line:
            break

        writelog("RX: " + line)
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
            abmove()

        sys.stdout.flush()

except Exception as e:
    with open("../log/errorlog.txt", 'a') as f:
        f.write(str(e))
        f.write(traceback.format_exc())

