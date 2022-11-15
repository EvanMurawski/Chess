import csv

def getPieceFactors():
    with open('../data/test.csv') as csvfile:

        piece_type = 0
        piece_values = [[0 for square in range(64)] for piece in range(13)]
        this_piece_value = []

        reader = csv.reader(csvfile)

        for row in reader:

            if row[0] == "start":
                continue

            if row[1] == "PIECE_NUM":
                if len(this_piece_value) == 64:
                    piece_type = int(row[0])
                    piece_values[piece_type] = this_piece_value
                    this_piece_value = []
                else:
                    raise Exception("Malformed CSV file for piece factors")
            else:
                this_piece_value += [float(i) for i in row]

    return piece_values


