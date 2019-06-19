class BoardRep:

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
    WHITE_PAWN_START = [48, 49, 50, 51, 52, 53, 54, 55]
    BLACK_PAWN_START = [8,  9, 10, 11, 12, 13, 14, 15]

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

    def __init__(self, array=None, whitemove=None, whitecastle=None, blackcastle=None):

        self.whitecastle = self.BOTH_CASTLE
        self.blackcastle = self.BOTH_CASTLE
        self.whitemove = True

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

    @staticmethod
    def numbersToAlg(move_squares):
        return BoardRep.NUMBER_TO_ALG[move_squares[0]] + BoardRep.NUMBER_TO_ALG[move_squares[1]]

    #Returns true if the player to move is in check
    @staticmethod
    def isInCheck(board):
        flip_move_board = BoardRep(board.array, not board.whitemove, board.whitecastle, board.blackcastle)
        next_boards = flip_move_board.getPseudoLegalMoves()
        if board.whitemove:
            player_king = BoardRep.WHITE_KING
        else:
            player_king = BoardRep.BLACK_KING

        found_check = False
        for next_board in next_boards:
            if player_king not in next_board[:][0].array:
                found_check = True

        return found_check

    #returns true if the player who moved previously is in check (i.e. illegal move)
    @staticmethod
    def isInCheckOtherPlayer(board):
        next_boards = board.getPseudoLegalMoves()
        if board.whitemove:
            player_king = BoardRep.BLACK_KING
        else:
            player_king = BoardRep.WHITE_KING

        found_check = False
        for next_board in next_boards:
            if player_king not in next_board[:][0].array:
                found_check = True

        return found_check

    def print(self):
        line = ""
        for i in range(0,64):
            line += self.STRING_DICT[self.array[i]] + " "
            if (i + 1) % 8 == 0:
                print(line)
                line = ""

    def getCurrentSidePieces(self):
        if self.whitemove:
            return self.WHITE_PIECES
        else:
            return self.BLACK_PIECES

    #TODO check if move is castling, check for queen promotion
    def getBoard(self, oldSquare, newSquare):
        newArray = self.array[:]
        movedPiece = newArray[oldSquare]
        newArray[oldSquare] = self.EMPTY
        newArray[newSquare] = movedPiece
        newBoard = BoardRep(newArray, not self.whitemove, self.whitecastle, self.blackcastle)
        return newBoard

    def squareHasEnemyPiece(self, square):
        return self.isEnemyPiece(self.array[square])

    def isEnemyPiece(self, piece):
        if self.whitemove:
            return piece in self.BLACK_PIECES
        else:
            return piece in self.WHITE_PIECES



    #TODO fix for black moves, add en passant
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
            result.append([self.getBoard(square, new_square), [square, new_square]])

            #check if can move two squares forward
            new_square = self.MAILBOX[self.TO_MAILBOX[square] + factor * 20]
            if self.array[new_square] == self.EMPTY and square in starting_squares:
                result.append([self.getBoard(square, new_square), [square, new_square]])

        #if can move diagonally
        new_square = self.MAILBOX[self.TO_MAILBOX[square] + factor * 9]
        if new_square != -1 and self.squareHasEnemyPiece(new_square):
            result.append([self.getBoard(square, new_square), [square, new_square]])
        new_square = self.MAILBOX[self.TO_MAILBOX[square] + factor * 11]
        if new_square != -1 and self.squareHasEnemyPiece(new_square):
            result.append([self.getBoard(square, new_square), [square, new_square]])

        return result


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

    def getPseudoLegalKingMoves(self, square):
        result = []
        for offset in self.KING_OFFSETS:
            new_square = self.MAILBOX[self.TO_MAILBOX[square] + offset]
            if new_square != -1 and self.array[new_square] == self.EMPTY:
                result.append([self.getBoard(square, new_square), [square, new_square]])
            elif new_square != -1 and self.squareHasEnemyPiece(new_square):
                result.append([self.getBoard(square, new_square), [square, new_square]])

        return result

    def getPseudoLegalKnightMoves(self, square):
        result = []
        for offset in self.KNIGHT_OFFSETS:
            new_square = self.MAILBOX[self.TO_MAILBOX[square] + offset]
            if new_square != -1 and self.array[new_square] == self.EMPTY:
                result.append([self.getBoard(square, new_square), [square, new_square]])
            elif new_square != -1 and self.squareHasEnemyPiece(new_square):
                result.append([self.getBoard(square, new_square), [square, new_square]])

        return result


    def getPseudoLegalRookMoves(self, square):
        return self.getPseudoLegalRBQMoves(square, self.ROOK_OFFSETS)

    def getPseudoLegalBishopMoves(self, square):
        return self.getPseudoLegalRBQMoves(square, self.BISHOP_OFFSETS)

    def getPseudoLegalQueenMoves(self, square):
        return self.getPseudoLegalRBQMoves(square, self.QUEEN_OFFSETS)

    #write test cases
    def getPseudoLegalMoves(self):
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

        return result

    def getLegalMoves(self):
        pseudo_legal_moves = self.getPseudoLegalMoves()
        legal_moves = []

        for move in pseudo_legal_moves:
            if not BoardRep.isInCheckOtherPlayer(move[:][0]):
                legal_moves.append(move)

        return legal_moves

