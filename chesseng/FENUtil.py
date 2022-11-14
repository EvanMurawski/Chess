from chesseng.BoardRep import BoardRep

class FENUtil:

    WHITE_PAWN = "P"
    WHITE_KNIGHT = "N"
    WHITE_BISHOP = "B"
    WHITE_ROOK = "R"
    WHITE_QUEEN = "Q"
    WHITE_KING = "K"
    BLACK_PAWN = "p"
    BLACK_KNIGHT = "n"
    BLACK_BISHOP = "b"
    BLACK_ROOK = "r"
    BLACK_QUEEN = "q"
    BLACK_KING = "k"

    FEN_TO_BOARD_DICT = {BLACK_PAWN: BoardRep.BLACK_PAWN, BLACK_KNIGHT: BoardRep.BLACK_KNIGHT, BLACK_BISHOP: BoardRep.BLACK_BISHOP, BLACK_ROOK: BoardRep.BLACK_ROOK, BLACK_QUEEN: BoardRep.BLACK_QUEEN,
                        BLACK_KING: BoardRep.BLACK_KING, WHITE_PAWN: BoardRep.WHITE_PAWN, WHITE_KNIGHT: BoardRep.WHITE_KNIGHT, WHITE_BISHOP: BoardRep.WHITE_BISHOP, WHITE_ROOK: BoardRep.WHITE_ROOK,
                        WHITE_QUEEN: BoardRep.WHITE_QUEEN, WHITE_KING: BoardRep.WHITE_KING}

    ALG_TO_NUM_DICT = {v: k for k, v in BoardRep.NUMBER_TO_ALG.items()}

    @staticmethod
    def fenToArray(fen):
        new_array = []

        split_text = FENUtil.splitFen(fen)

        for i in range(0,8):
            for char in split_text[i]:
                if char.isdigit():
                    num_empty = int(char)
                    for j in range(0,num_empty):
                        new_array.append(BoardRep.EMPTY)
                else:
                    new_array.append(FENUtil.FEN_TO_BOARD_DICT[char])
        return new_array


    @staticmethod
    def splitFen(fen):
        split_text = []
        for item in fen.split("/"):
            split_text.extend(item.split(" "))
        return split_text

    @staticmethod
    def getWhiteMove(fen):
        split_text = FENUtil.splitFen(fen)

        return split_text[8] == "w"

    @staticmethod
    def getCastling(fen):
        split_text = FENUtil.splitFen(fen)
        castle_string = split_text[9]

        white_castling = BoardRep.NO_CASTLE
        black_castling = BoardRep.NO_CASTLE

        if castle_string == "-":
            return white_castling, black_castling

        else:
            if "K" in castle_string:
                white_castling += BoardRep.KS_CASTLE
            if "Q" in castle_string:
                white_castling += BoardRep.QS_CASTLE
            if "k" in castle_string:
                black_castling += BoardRep.KS_CASTLE
            if "q" in castle_string:
                black_castling += BoardRep.QS_CASTLE

        return white_castling, black_castling

    @staticmethod
    def getEnPassant(fen):
        split_text = FENUtil.splitFen(fen)
        enpassant_string = split_text[10]

        if enpassant_string == "-":
            return None
        else:
            return FENUtil.ALG_TO_NUM_DICT[enpassant_string]

    @staticmethod
    def fenToBoard(fen):
        return BoardRep(FENUtil.fenToArray(fen), FENUtil.getWhiteMove(fen), FENUtil.getCastling(fen)[0], FENUtil.getCastling(fen)[1], FENUtil.getEnPassant(fen))