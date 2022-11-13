import random
import time
from chesseng.PieceFactors import getPieceFactors

class BoardRep:

    # IMPORT FILES #
    piece_factors_file = 'test.csv'
    # IMPORT FILES #

    # CONFIG SWITCHES #
    use_piece_factors = True
    # CONFIG SWITCHES

    numboards = 0
    numgetpseudo= 0
    numgetpseudocaptures=0
    numgetlegal= 0
    numgetcheck= 0
    numgetothercheck = 0
    numgetcheckmate= 0
    getlegalmovestime = 0
    getpseudolegaltime = 0
    getcheckmatetime = 0
    getchecktime = 0
    getotherchecktime = 0
    getpseudocapturestime = 0


    MAILBOX = [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
                -1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
                -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
                -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
                -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
                -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
                -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
                -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

    TO_MAILBOX = [  21, 22, 23, 24, 25, 26, 27, 28,
                    31, 32, 33, 34, 35, 36, 37, 38,
                    41, 42, 43, 44, 45, 46, 47, 48,
                    51, 52, 53, 54, 55, 56, 57, 58,
                    61, 62, 63, 64, 65, 66, 67, 68,
                    71, 72, 73, 74, 75, 76, 77, 78,
                    81, 82, 83, 84, 85, 86, 87, 88,
                    91, 92, 93, 94, 95, 96, 97, 98]

    NO_CASTLE = 0
    KS_CASTLE = 1
    QS_CASTLE = 2
    BOTH_CASTLE = 3

    EMPTY = 0
    WHITE_PAWN = 1
    WHITE_KNIGHT = 2
    WHITE_BISHOP = 3
    WHITE_ROOK = 4
    WHITE_QUEEN = 5
    WHITE_KING = 6
    BLACK_PAWN = 7
    BLACK_KNIGHT = 8
    BLACK_BISHOP = 9
    BLACK_ROOK = 10
    BLACK_QUEEN = 11
    BLACK_KING = 12

    STRING_DICT = {EMPTY: ".", BLACK_PAWN: "♙", BLACK_KNIGHT: "♘", BLACK_BISHOP: "♗", BLACK_ROOK: "♖", BLACK_QUEEN: "♕",
                   BLACK_KING: "♔", WHITE_PAWN: "♟", WHITE_KNIGHT: "♞", WHITE_BISHOP: "♝", WHITE_ROOK: "♜", WHITE_QUEEN: "♛", WHITE_KING: "♚"}

    WHITE_PIECES = [WHITE_PAWN, WHITE_KNIGHT, WHITE_BISHOP, WHITE_ROOK, WHITE_QUEEN, WHITE_KING]
    BLACK_PIECES = [BLACK_PAWN, BLACK_KNIGHT, BLACK_BISHOP, BLACK_ROOK, BLACK_QUEEN, BLACK_KING]

    # Important Squares

    WHITE_PAWN_START = [48, 49, 50, 51, 52, 53, 54, 55]
    BLACK_PAWN_START = [8,  9, 10, 11, 12, 13, 14, 15]

    WHITE_PAWN_PROMOTION = [0, 1, 2, 3, 4, 5, 6, 7]
    BLACK_PAWN_PROMOTION = [56, 57, 58, 59, 60, 61, 62, 63]

    WHITE_KING_START = 60
    WHITE_KING_KS_CASTLE = 62
    WHITE_KING_QS_CASTLE = 58

    BLACK_KING_START = 4
    BLACK_KING_KS_CASTLE = 6
    BLACK_KING_QS_CASTLE = 2

    WHITE_DOUBLE_ENPASSANT_SQUARES = [33, 34, 35, 36, 37, 38]
    WHITE_RIGHT_ENPASSANT_SQUARE = 39
    WHITE_LEFT_ENPASSANT_SQUARE = 32

    BLACK_DOUBLE_ENPASSANT_SQUARES = [25, 26, 27, 28, 29, 30]
    BLACK_RIGHT_ENPASSANT_SQUARE = 31
    BLACK_LEFT_ENPASSANT_SQUARE = 24

    LIGHT_SQUARES = [0,2,4,6,9,11,13,15,16,18,20,22,25,27,29,31,32,34,36,38,41,43,45,47,48,50,52,54,57,59,61,63]
    DARK_SQUARES =  [1,3,5,7,8,10,12,14,17,19,21,23,24,26,28,30,33,35,37,39,40,42,44,46,49,51,53,55,56,58,60,62]

    # Important Squares


    ROOK_OFFSETS = [-10, -1, 1, 10]
    BISHOP_OFFSETS = [-11, -9, 9, 11]
    QUEEN_OFFSETS = [-11, -10, -9, -1, 1, 9, 10, 11]
    KING_OFFSETS = [-11, -10, -9, -1, 1, 9, 10, 11]
    KNIGHT_OFFSETS = [-21, -19,-12, -8, 8, 12, 19, 21]

    NUMBER_TO_ALG = {0: "a8", 1: "b8", 2: "c8", 3: "d8", 4: "e8", 5: "f8", 6: "g8", 7: "h8",
                     8: "a7", 9: "b7",10: "c7", 11: "d7", 12: "e7", 13: "f7", 14: "g7", 15: "h7",
                     16: "a6", 17: "b6",18: "c6", 19: "d6", 20: "e6", 21: "f6", 22: "g6", 23: "h6",
                     24: "a5", 25: "b5",26: "c5", 27: "d5", 28: "e5", 29: "f5", 30: "g5", 31: "h5",
                     32: "a4", 33: "b4",34: "c4", 35: "d4", 36: "e4", 37: "f4", 38: "g4", 39: "h4",
                     40: "a3", 41: "b3",42: "c3", 43: "d3", 44: "e3", 45: "f3", 46: "g3", 47: "h3",
                     48: "a2", 49: "b2",50: "c2", 51: "d2", 52: "e2", 53: "f2", 54: "g2", 55: "h2",
                     56: "a1", 57: "b1",58: "c1", 59: "d1", 60: "e1", 61: "f1", 62: "g1", 63: "h1"}

    PIECE_VALUES = {EMPTY: 0, WHITE_PAWN: 1, WHITE_KNIGHT: 3, WHITE_BISHOP: 3.5, WHITE_ROOK: 5, WHITE_QUEEN: 9, WHITE_KING: 100,
                    BLACK_PAWN: -1, BLACK_KNIGHT: -3, BLACK_BISHOP: -3.5, BLACK_ROOK: -5, BLACK_QUEEN: -9, BLACK_KING: -100}

    PIECE_FACTORS = getPieceFactors()


    def __init__(self, array=None, whitemove=None, whitecastle=None, blackcastle=None, enpassant_square=None, is_promotion=False, is_capture = False):

        # These values need to be calculated and stored for every board
        self.whitemove = True
        self.whitecastle = self.BOTH_CASTLE
        self.blackcastle = self.BOTH_CASTLE
        self.enpassant_square = enpassant_square
        self.is_promotion = is_promotion
        self.is_capture = is_capture

        # These values don't always need to be calculated. Give them a default value and only caclulate them when needed
        # TODO: store ischeck status
        self.confirmedlegal = False
        self.ischeckmate = None
        self.legalmoves = None
        self.pseudolegalmoves = None
        self.king_square = None



        if array is None:
            self.array = [self.BLACK_ROOK, self.BLACK_KNIGHT, self.BLACK_BISHOP, self.BLACK_QUEEN, self.BLACK_KING, self.BLACK_BISHOP, self.BLACK_KNIGHT, self.BLACK_ROOK,
                          self.BLACK_PAWN, self.BLACK_PAWN, self.BLACK_PAWN, self.BLACK_PAWN, self.BLACK_PAWN, self.BLACK_PAWN, self.BLACK_PAWN, self.BLACK_PAWN,
                          self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY,
                          self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY,
                          self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY,
                          self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY, self.EMPTY,
                          self.WHITE_PAWN, self.WHITE_PAWN, self.WHITE_PAWN, self.WHITE_PAWN, self.WHITE_PAWN, self.WHITE_PAWN, self.WHITE_PAWN, self.WHITE_PAWN,
                          self.WHITE_ROOK, self.WHITE_KNIGHT, self.WHITE_BISHOP, self.WHITE_QUEEN, self.WHITE_KING, self.WHITE_BISHOP, self.WHITE_KNIGHT, self.WHITE_ROOK]
        else:
            self.array = array

        if whitecastle is None:
            self.whitecastle = self.BOTH_CASTLE
        else:
            self.whitecastle = whitecastle

        if blackcastle is None:
            self.blackcastle = self.BOTH_CASTLE
        else:
            self.blackcastle = blackcastle

        if whitemove is None:
            self.whitemove = True
        else:
            self.whitemove = whitemove


        BoardRep.numboards += 1

    @staticmethod
    def numbersToAlg(move_squares):
        return BoardRep.NUMBER_TO_ALG[move_squares[0]] + BoardRep.NUMBER_TO_ALG[move_squares[1]]

    @staticmethod
    def moveToAlg(move):
        alg = BoardRep.NUMBER_TO_ALG[move[1][0]] + BoardRep.NUMBER_TO_ALG[move[1][1]]

        if move[0].is_promotion:
            if move[0].array[move[1][1]] in [BoardRep.WHITE_QUEEN, BoardRep.BLACK_QUEEN]:
                alg += "q"
            elif move[0].array[move[1][1]] in [BoardRep.WHITE_ROOK, BoardRep.BLACK_ROOK]:
                alg += "r"
            elif move[0].array[move[1][1]] in [BoardRep.WHITE_BISHOP, BoardRep.BLACK_BISHOP]:
                alg += "b"
            else:
                alg += "n"

        return alg

    #Returns true if the player to move is in check
    @staticmethod
    def isInCheck(board):
        start_time = time.time()
        BoardRep.numgetcheck += 1
        flip_move_board = BoardRep(board.array, not board.whitemove, board.whitecastle, board.blackcastle)
        has_captures = flip_move_board.hasPseudoLegalCaptures()
        if not has_captures:
            BoardRep.getchecktime += time.time() - start_time
            return False
        BoardRep.getchecktime += time.time() - start_time
        return True

    #returns true if the player who moved previously is in check (i.e. illegal move)
    #todo think of a better way to calculate this.
    @staticmethod
    def isInCheckOtherPlayer(board):
        start_time = time.time()
        BoardRep.numgetothercheck += 1
        result = board.hasPseudoLegalCaptures()
        BoardRep.getotherchecktime += time.time() - start_time
        return result
        # next_boards = board.getPseudoLegalCaptures()
        #
        # if not next_boards:
        #     #print("legal move")
        #     BoardRep.getotherchecktime += time.time() - start_time
        #     return False
        #
        # #print("illegal move")
        # BoardRep.getotherchecktime += time.time() - start_time
        # return True


    def print(self):
        line = ""
        for i in range(0,64):
            line += self.STRING_DICT[self.array[i]] + " "
            if (i + 1) % 8 == 0:
                print(line)
                line = ""

    def isCheckmate(self):
        start_time = time.time()
        BoardRep.numgetcheckmate += 1
        if self.ischeckmate is None:

            if not BoardRep.isInCheck(self):
                self.ischeckmate = False
                self.getcheckmatetime += time.time() - start_time
                BoardRep.getcheckmatetime += time.time() - start_time
                return False

            self.ischeckmate = not self.getLegalMoves()

        BoardRep.getcheckmatetime += time.time() - start_time
        return self.ischeckmate


    def getCurrentSidePieces(self):
        if self.whitemove:
            return self.WHITE_PIECES
        else:
            return self.BLACK_PIECES

    def getScore(self):

        checkmate = self.isCheckmate()
        if checkmate and self.whitemove:
            return -999
        elif checkmate and not self.whitemove:

            return 999

        return self.getWeightedMaterial() + random.uniform(-0.1,0.1)

    def getWeightedMaterial(self):
        material = 0
        for square, piece in enumerate(self.array):
            material += self.PIECE_VALUES[piece]
            if self.use_piece_factors:
                material += self.PIECE_FACTORS[piece][square]

        return material


    def getMaterial(self):
        material = 0
        for square, piece in enumerate(self.array):
            material += self.PIECE_VALUES[piece]

        return material

    # TODO break into smaller functions
    def getBoard(self, oldSquare, newSquare, promotion_piece=None):
        newArray = self.array[:]
        movedPiece = newArray[oldSquare]
        if newArray[newSquare] != self.EMPTY:
            _is_capture = True
        else:
            _is_capture = False

        newArray[oldSquare] = self.EMPTY
        newArray[newSquare] = movedPiece
        _whitecastle = self.whitecastle
        _blackcastle = self.blackcastle
        _enpassant_square = None
        _confirmedlegal = False
        _is_promotion = False

        # Check for queen promotion
        if promotion_piece is not None:
            newArray[newSquare] = promotion_piece
            _is_promotion = True


        # Handle Kingside Castling
        if movedPiece == self.WHITE_KING and oldSquare == self.WHITE_KING_START and newSquare == self.WHITE_KING_KS_CASTLE:
            # move rook
            newArray[63] = self.EMPTY
            newArray[61] = self.WHITE_ROOK
            _whitecastle = self.NO_CASTLE
            _confirmedlegal = True

        elif movedPiece == self.BLACK_KING and oldSquare == self.BLACK_KING_START and newSquare == self.BLACK_KING_KS_CASTLE:
            # move rook
            newArray[7] = self.EMPTY
            newArray[5] = self.BLACK_ROOK
            _blackcastle = self.NO_CASTLE
            _confirmedlegal = True

        # Handle Queenside Castling
        if movedPiece == self.WHITE_KING and oldSquare == self.WHITE_KING_START and newSquare == self.WHITE_KING_QS_CASTLE:
            # move rook
            newArray[56] = self.EMPTY
            newArray[59] = self.WHITE_ROOK
            _whitecastle = self.NO_CASTLE
            _confirmedlegal = True

        elif movedPiece == self.BLACK_KING and oldSquare == self.BLACK_KING_START and newSquare == self.BLACK_KING_QS_CASTLE:
            # move rook
            newArray[0] = self.EMPTY
            newArray[3] = self.BLACK_ROOK
            _blackcastle = self.NO_CASTLE
            _confirmedlegal = True

        # Remove castling rights if moved pieces

        # Moved king
        if movedPiece == self.WHITE_KING:
            _whitecastle = self.NO_CASTLE

        elif movedPiece == self.BLACK_KING:
            _blackcastle = self.NO_CASTLE

        # Moved white kingside rook
        if oldSquare == 63:
            if _whitecastle == self.BOTH_CASTLE:
                _whitecastle = self.QS_CASTLE
            elif _whitecastle == self.KS_CASTLE:
                _whitecastle = self.NO_CASTLE

        # Moved white queenside rook
        if oldSquare == 56:
            if _whitecastle == self.BOTH_CASTLE:
                _whitecastle = self.KS_CASTLE
            elif _whitecastle == self.QS_CASTLE:
                _whitecastle = self.NO_CASTLE

        # Moved black kingside rook
        if oldSquare == 7:
            if _blackcastle == self.BOTH_CASTLE:
                _blackcastle = self.QS_CASTLE
            elif _blackcastle == self.KS_CASTLE:
                _blackcastle = self.NO_CASTLE

        # Moved black queenside rook
        if oldSquare == 0:
            if _blackcastle == self.BOTH_CASTLE:
                _blackcastle = self.KS_CASTLE
            elif _blackcastle == self.QS_CASTLE:
                _blackcastle = self.NO_CASTLE

        # En Passant Handling

        # If enpassant, remove captured pawn
        if movedPiece == self.WHITE_PAWN and newSquare == self.enpassant_square:
            newArray[newSquare + 8] = self.EMPTY

        if movedPiece == self.BLACK_PAWN and newSquare == self.enpassant_square:
            newArray[newSquare - 8] = self.EMPTY


        # if white moved a pawn two squares
        if movedPiece == self.WHITE_PAWN and abs(newSquare - oldSquare) == 16 and newSquare in self.WHITE_DOUBLE_ENPASSANT_SQUARES:
            if newArray[newSquare - 1] == self.BLACK_PAWN or newArray[newSquare + 1] == self.BLACK_PAWN:
                _enpassant_square = newSquare + 8
        elif newSquare == self.WHITE_LEFT_ENPASSANT_SQUARE:
            if newArray[newSquare + 1] == self.BLACK_PAWN:
                _enpassant_square = newSquare + 8
        elif newSquare == self.WHITE_RIGHT_ENPASSANT_SQUARE:
            if newArray[newSquare -1 ] == self.BLACK_PAWN:
                _enpassant_square = newSquare + 8

        # if white moved a pawn two squares
        if movedPiece == self.BLACK_PAWN and abs(newSquare - oldSquare) == 16 and newSquare in self.BLACK_DOUBLE_ENPASSANT_SQUARES:
            if newArray[newSquare - 1] == self.WHITE_PAWN or newArray[newSquare + 1] == self.WHITE_PAWN:
                _enpassant_square = newSquare - 8
        elif newSquare == self.BLACK_LEFT_ENPASSANT_SQUARE:
            if newArray[newSquare + 1] == self.WHITE_PAWN:
                _enpassant_square = newSquare - 8
        elif newSquare == self.BLACK_RIGHT_ENPASSANT_SQUARE:
            if newArray[newSquare - 1] == self.WHITE_PAWN:
                _enpassant_square = newSquare - 8


        newBoard = BoardRep(newArray, not self.whitemove, _whitecastle, _blackcastle, _enpassant_square,_is_promotion, _is_capture)
        newBoard.confirmedlegal = _confirmedlegal
        return newBoard

    def squareHasEnemyPiece(self, square):
        return self.isEnemyPiece(self.array[square])

    def isEnemyPiece(self, piece):
        if self.whitemove:
            return piece in self.BLACK_PIECES
        else:
            return piece in self.WHITE_PIECES

    def squareHasEnemyKing(self, square):
        return self.isEnemyKing(self.array[square])

    def isEnemyKing(self, piece):
        if self.whitemove:
            return piece == self.BLACK_KING
        else:
            return piece == self.WHITE_KING

    def getEnemyKingSquare(self):

        if self.king_square is not None:
            return self.king_square

        if self.whitemove:
            king_square =  self.array.index(self.BLACK_KING)
        else:
            king_square = self.array.index(self.WHITE_KING)

        self.king_square = king_square
        return king_square


    def getPseudoLegalPawnMoves(self, square):

        result = []
        if self.whitemove:
            factor = -1
            starting_squares = self.WHITE_PAWN_START
        else:
            factor = 1
            starting_squares = self.BLACK_PAWN_START

        #if can move one square forward
        new_square = self.MAILBOX[self.TO_MAILBOX[square] + factor * 10]
        if  self.array[new_square] == self.EMPTY:
            #Todo: all the below code ir repeated for forward move, and each diagonal move -> put it in a function
            if new_square in self.WHITE_PAWN_PROMOTION:
                for piece in [self.WHITE_BISHOP, self.WHITE_KNIGHT, self.WHITE_ROOK, self.WHITE_QUEEN]:
                    result.append([self.getBoard(square, new_square, piece), [square, new_square]])
            elif new_square in self.BLACK_PAWN_PROMOTION:
                for piece in [self.BLACK_BISHOP, self.BLACK_KNIGHT, self.BLACK_ROOK, self.BLACK_QUEEN]:
                    result.append([self.getBoard(square, new_square, piece), [square, new_square]])
            else:
                result.append([self.getBoard(square, new_square), [square, new_square]])

            #check if can move two squares forward
            new_square = self.MAILBOX[self.TO_MAILBOX[square] + factor * 20]
            if self.array[new_square] == self.EMPTY and square in starting_squares:
                result.append([self.getBoard(square, new_square), [square, new_square]])

        #if can move diagonally
        new_square = self.MAILBOX[self.TO_MAILBOX[square] + factor * 9]
        if new_square != -1 and (self.squareHasEnemyPiece(new_square) or new_square == self.enpassant_square):
            if new_square in self.WHITE_PAWN_PROMOTION:
                for piece in [self.WHITE_BISHOP, self.WHITE_KNIGHT, self.WHITE_ROOK, self.WHITE_QUEEN]:
                    result.append([self.getBoard(square, new_square, piece), [square, new_square]])
            elif new_square in self.BLACK_PAWN_PROMOTION:
                for piece in [self.BLACK_BISHOP, self.BLACK_KNIGHT, self.BLACK_ROOK, self.BLACK_QUEEN]:
                    result.append([self.getBoard(square, new_square, piece), [square, new_square]])
            else:
                result.append([self.getBoard(square, new_square), [square, new_square]])

        new_square = self.MAILBOX[self.TO_MAILBOX[square] + factor * 11]
        if new_square != -1 and (self.squareHasEnemyPiece(new_square) or new_square == self.enpassant_square):
            if new_square in self.WHITE_PAWN_PROMOTION:
                for piece in [self.WHITE_BISHOP, self.WHITE_KNIGHT, self.WHITE_ROOK, self.WHITE_QUEEN]:
                    result.append([self.getBoard(square, new_square, piece), [square, new_square]])
            elif new_square in self.BLACK_PAWN_PROMOTION:
                for piece in [self.BLACK_BISHOP, self.BLACK_KNIGHT, self.BLACK_ROOK, self.BLACK_QUEEN]:
                    result.append([self.getBoard(square, new_square, piece), [square, new_square]])
            else:
                result.append([self.getBoard(square, new_square), [square, new_square]])

        return result


    def hasPseudoLegalPawnCaptures(self, square):
        king_square = self.getEnemyKingSquare()

        if self.whitemove and king_square // 8 - square // 8 != -1:
                return False
        if not self.whitemove and  king_square // 8 - square //8 != 1:
                return False

        if self.whitemove:
            factor = -1
        else:
            factor = 1

        #if can move diagonally
        new_square = self.MAILBOX[self.TO_MAILBOX[square] + factor * 9]
        if new_square != -1 and self.squareHasEnemyKing(new_square):
            return True
        new_square = self.MAILBOX[self.TO_MAILBOX[square] + factor * 11]
        if new_square != -1 and self.squareHasEnemyKing(new_square):
            return True

        return False

    def getPseudoLegalRBQMoves(self, square, offsets):
        result = []
        for offset in offsets:
            for i in range(1,8):
                new_square = self.MAILBOX[self.TO_MAILBOX[square] + offset*i]
                if new_square != -1 and self.array[new_square] == self.EMPTY:
                    result.append([self.getBoard(square, new_square),[square, new_square]])
                elif new_square != -1 and self.squareHasEnemyPiece(new_square):
                    result.append([self.getBoard(square, new_square), [square, new_square]])
                    break
                else:
                    break

        return result

    def hasPseudoLegalRBQCaptures(self, square, offsets):
        for offset in offsets:
            for i in range(1,8):
                new_square = self.MAILBOX[self.TO_MAILBOX[square] + offset*i]
                if new_square != -1 and self.squareHasEnemyKing(new_square):
                    return True
                elif new_square != -1 and self.squareHasEnemyPiece(new_square):
                    break
                elif not (new_square != -1 and self.array[new_square] == self.EMPTY):
                    break

        return False

    def getPseudoLegalKingMoves(self, square):
        result = []
        for offset in self.KING_OFFSETS:
            new_square = self.MAILBOX[self.TO_MAILBOX[square] + offset]
            if new_square != -1 and self.array[new_square] == self.EMPTY:
                result.append([self.getBoard(square, new_square), [square, new_square]])
            elif new_square != -1 and self.squareHasEnemyPiece(new_square):
                result.append([self.getBoard(square, new_square), [square, new_square]])

        # Check for castling
        if (self.whitemove and self.whitecastle in [self.KS_CASTLE, self.BOTH_CASTLE]) or\
            (not self.whitemove and self.blackcastle in [self.KS_CASTLE, self.BOTH_CASTLE]):
            potential_castling_board = self.canKingSideCastle(square)
            if potential_castling_board is not None:
                result.append([potential_castling_board, [square, self.WHITE_KING_KS_CASTLE if self.whitemove else self.BLACK_KING_KS_CASTLE]])

        if (self.whitemove and self.whitecastle in [self.QS_CASTLE, self.BOTH_CASTLE]) or\
            (not self.whitemove and self.blackcastle in [self.QS_CASTLE, self.BOTH_CASTLE]):
            potential_castling_board = self.canQueenSideCastle(square)
            if potential_castling_board is not None:
                result.append([potential_castling_board, [square, self.WHITE_KING_QS_CASTLE if self.whitemove else self.BLACK_KING_QS_CASTLE]])

        return result

    # TODO: save check status in board rep so it only has to be calculated once per board
    # TODO: don't need to pass square to this function
    def canKingSideCastle(self, square):

        if self.whitemove:
            passthru_square = 61
            end_square = self.WHITE_KING_KS_CASTLE
        else:
            passthru_square = 5
            end_square = self.BLACK_KING_KS_CASTLE

        if BoardRep.isInCheck(self):
            return None

        if self.array[end_square] != self.EMPTY or self.array[passthru_square] != self.EMPTY:
            return None

        if BoardRep.isInCheckOtherPlayer(self.getBoard(square, passthru_square)):
            return None

        potential_castling_board = self.getBoard(square, end_square)
        if BoardRep.isInCheckOtherPlayer(potential_castling_board):
            return None

        return potential_castling_board

    # TODO: combine KS and QS castling functions
    def canQueenSideCastle(self, square):

        if self.whitemove:
            passthru_squares = [57,58, 59]
            end_square = self.WHITE_KING_QS_CASTLE
        else:
            passthru_squares = [1,2,3]
            end_square = self.BLACK_KING_QS_CASTLE

        if BoardRep.isInCheck(self):
            return None

        if self.array[end_square] != self.EMPTY:
            return None

        if self.array[passthru_squares[0]] != self.EMPTY or self.array[passthru_squares[1]] != self.EMPTY or self.array[passthru_squares[2]] != self.EMPTY:
            return None

        if BoardRep.isInCheckOtherPlayer(self.getBoard(square, passthru_squares[1])):
            return None

        if BoardRep.isInCheckOtherPlayer(self.getBoard(square, passthru_squares[2])):
            return None


        potential_castling_board = self.getBoard(square, end_square)
        if BoardRep.isInCheckOtherPlayer(potential_castling_board):
            return None

        return potential_castling_board

    def hasPseudoLegalKingCaptures(self, square):
        for offset in self.KING_OFFSETS:
            new_square = self.MAILBOX[self.TO_MAILBOX[square] + offset]
            if new_square != -1 and self.squareHasEnemyKing(new_square):
                return True

        return False

    def getPseudoLegalKnightMoves(self, square):
        result = []
        for offset in self.KNIGHT_OFFSETS:
            new_square = self.MAILBOX[self.TO_MAILBOX[square] + offset]
            if new_square != -1 and self.array[new_square] == self.EMPTY:
                result.append([self.getBoard(square, new_square), [square, new_square]])
            elif new_square != -1 and self.squareHasEnemyPiece(new_square):
                result.append([self.getBoard(square, new_square), [square, new_square]])

        return result

    def hasPseudoLegalKnightCaptures(self, square):
        for offset in self.KNIGHT_OFFSETS:
            new_square = self.MAILBOX[self.TO_MAILBOX[square] + offset]
            if new_square != -1 and self.squareHasEnemyKing(new_square):
                return True

        return False

    def getPseudoLegalRookMoves(self, square):
        return self.getPseudoLegalRBQMoves(square, self.ROOK_OFFSETS)

    def getPseudoLegalBishopMoves(self, square):
        return self.getPseudoLegalRBQMoves(square, self.BISHOP_OFFSETS)

    def getPseudoLegalQueenMoves(self, square):
        return self.getPseudoLegalRBQMoves(square, self.QUEEN_OFFSETS)

    def hasPseudoLegalRookCaptures(self, square):
        king_square = self.getEnemyKingSquare()

        if square // 8 != king_square // 8 and square % 8 != king_square % 8:
            return None

        return self.hasPseudoLegalRBQCaptures(square, self.ROOK_OFFSETS)

    def hasPseudoLegalBishopCaptures(self, square):

        king_square = self.getEnemyKingSquare()

        if king_square in self.LIGHT_SQUARES:
            if square not in self.LIGHT_SQUARES:
                return False
        elif square not in self.DARK_SQUARES:
            return False

        return self.hasPseudoLegalRBQCaptures(square, self.BISHOP_OFFSETS)

    def hasPseudoLegalQueenCaptures(self, square):

        king_square = self.getEnemyKingSquare()

        if king_square // 8 != square // 8 and king_square % 8 != square % 8:
            if king_square in self.LIGHT_SQUARES and square not in self.LIGHT_SQUARES:
                return False
            if king_square not in self.LIGHT_SQUARES and square in self.LIGHT_SQUARES:
                return False

        return self.hasPseudoLegalRBQCaptures(square, self.QUEEN_OFFSETS)

    #write test cases
    def getPseudoLegalMoves(self):
        start_time = time.time()
        BoardRep.numgetpseudo += 1
        result = []
        for squareNumber in range(0,64):
            piece = self.array[squareNumber]
            if piece in self.getCurrentSidePieces():
                if piece == self.WHITE_PAWN or piece == self.BLACK_PAWN:
                    moves = self.getPseudoLegalPawnMoves(squareNumber)
                    if moves is not None:
                        result.extend(moves)
                elif piece == self.WHITE_ROOK or piece == self.BLACK_ROOK:
                    moves = self.getPseudoLegalRookMoves(squareNumber)
                    if moves is not None:
                        result.extend(moves)
                elif piece == self.WHITE_BISHOP or piece == self.BLACK_BISHOP:
                    moves = self. getPseudoLegalBishopMoves(squareNumber)
                    if moves is not None:
                        result.extend(moves)
                elif piece == self.WHITE_QUEEN or piece == self.BLACK_QUEEN:
                    moves = self. getPseudoLegalQueenMoves(squareNumber)
                    if moves is not None:
                        result.extend(moves)
                elif piece == self.WHITE_KING or piece == self.BLACK_KING:
                    moves = self.getPseudoLegalKingMoves(squareNumber)
                    if moves is not None:
                        result.extend(moves)
                elif piece == self.WHITE_KNIGHT or piece == self.BLACK_KNIGHT:
                    moves = self.getPseudoLegalKnightMoves(squareNumber)
                    if moves is not None:
                        result.extend(moves)
        BoardRep.getpseudolegaltime += time.time() - start_time
        return result


    #TODO: Try sorting pieces by how close they are to the king?
    def hasPseudoLegalCaptures(self):
        start_time = time.time()
        BoardRep.numgetpseudocaptures += 1
        result = []
        for squareNumber in range(0,64):
            piece = self.array[squareNumber]
            if piece in self.getCurrentSidePieces():
                if piece == self.WHITE_PAWN or piece == self.BLACK_PAWN:
                    if self.hasPseudoLegalPawnCaptures(squareNumber):
                        return True
                elif piece == self.WHITE_ROOK or piece == self.BLACK_ROOK:
                    if self.hasPseudoLegalRookCaptures(squareNumber):
                        return True
                elif piece == self.WHITE_BISHOP or piece == self.BLACK_BISHOP:
                    if self. hasPseudoLegalBishopCaptures(squareNumber):
                        return True
                elif piece == self.WHITE_QUEEN or piece == self.BLACK_QUEEN:
                    if self. hasPseudoLegalQueenCaptures(squareNumber):
                        return True
                elif piece == self.WHITE_KNIGHT or piece == self.BLACK_KNIGHT:
                    if self.hasPseudoLegalKnightCaptures(squareNumber):
                        return True
                elif piece == self.WHITE_KING or piece == self.BLACK_KING:
                    if self.hasPseudoLegalKingCaptures(squareNumber):
                        return True

        BoardRep.getpseudocapturestime += time.time() - start_time
        return False


    def getLegalMoves(self):
        start_time = time.time()
        BoardRep.numgetlegal += 1
        if self.legalmoves is not None:
            BoardRep.getlegalmovestime += time.time() - start_time
            return self.legalmoves

        pseudo_legal_moves = self.getPseudoLegalMoves()
        legal_moves = []

        for move in pseudo_legal_moves:
            if move[:][0].confirmedlegal:
                legal_moves.append(move)
            elif not BoardRep.isInCheckOtherPlayer(move[:][0]):
                legal_moves.append(move)

        self.legalmoves = legal_moves
        BoardRep.getlegalmovestime += time.time() - start_time
        return legal_moves

