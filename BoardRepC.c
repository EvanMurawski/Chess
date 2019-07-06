
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <wchar.h>
#include <locale.h>


struct BoardRep {
    uint64_t whitepawns, whitebishops, whiteknights, whiterooks, whitequeens, whitekings;
    uint64_t blackpawns, blackbishops, blackknights, blackrooks, blackqueens, blackkings;
    bool blackqueenside, whitequeenside, blackkingside, whitekingside, whitemove;
};

void printBoardString(struct BoardRep brep) {
	setlocale(LC_CTYPE, "");
	wchar_t whitepawn = 0x2659;
	wchar_t blackpawn = 0x265F;
	wchar_t whitebishop = 0x2657;
	wchar_t blackbishop = 0x265D;
	wchar_t whiteknight = 0x2658;
	wchar_t blackknight = 0x265E;
	wchar_t whiterook = 0x2656;
	wchar_t blackrook = 0x265C;
	wchar_t whitequeen = 0x2655;
	wchar_t blackqueen = 0x265B;
	wchar_t whiteking = 0x2654;
	wchar_t blackking = 0x265A;
	
	int count = 0;

	for(int i = 0; i< 64; i++) {
		uint64_t one = 0x1ULL;
		uint64_t square = one << (63-i);

		if (count == 8){
			printf("\n");
			count = 0;
		}

		if ((brep.whitepawns & square) > 0) {
			printf("%lc", blackpawn);
			printf(" ");
		}
		else if ((brep.blackpawns & square) > 0) {
			printf("%lc", whitepawn);
			printf(" ");
		}
		else if ((brep.whitebishops & square) > 0) {
			printf("%lc", blackbishop);
			printf(" ");
		}
		else if ((brep.blackbishops & square) > 0) {
			printf("%lc", whitebishop);
			printf(" ");
		}
		else if ((brep.whiteknights & square) > 0) {
			printf("%lc", blackknight);
			printf(" ");
		}
		else if ((brep.blackknights & square) > 0) {
			printf("%lc", whiteknight);
			printf(" ");
		}
		else if ((brep.whiterooks & square) > 0) {
			printf("%lc", blackrook);
			printf(" ");
		}
		else if ((brep.blackrooks & square) > 0) {
			printf("%lc", whiterook);
			printf(" ");
		}
		else if ((brep.whitequeens & square) > 0) {
			printf("%lc", blackqueen);
			printf(" ");
		}
		else if ((brep.blackqueens & square) > 0) {
			printf("%lc", whitequeen);
			printf(" ");
		}
		else if ((brep.whitekings & square) > 0) {
			printf("%lc", blackking);
			printf(" ");
		}
		else if ((brep.blackkings & square) > 0) {
			printf("%lc", whiteking);
			printf(" ");
		}
		else {
			printf(". ");
		}

		count++;
	}
	printf("\n");

}

struct BoardRep getInitialBoard() {
	struct BoardRep brep;
	brep.whitepawns = 	0x000000000000FF00ULL;
    brep.blackpawns = 	0x00FF000000000000ULL;
    brep.whitebishops = 0x0000000000000024ULL;
    brep.blackbishops = 0x2400000000000000ULL;
    brep.whiteknights = 0x0000000000000042ULL;
    brep.blackknights = 0x4200000000000000ULL;
    brep.whiterooks = 	0x0000000000000081ULL;
    brep.blackrooks = 	0x8100000000000000ULL;
    brep.whitequeens = 	0x0000000000000010ULL;
    brep.blackqueens = 	0x1000000000000000ULL;
    brep.whitekings = 	0x0000000000000008ULL;
    brep.blackkings = 	0x0800000000000000ULL;
    brep.blackqueenside = true;
    brep.blackkingside = true;
    brep.whitequeenside = true;
    brep.whitekingside = true;
    brep.whitemove = true;

    return brep;
}


int main () {
    struct BoardRep mybrep = getInitialBoard();

    printf("Hello world.");
    printf("%lx", mybrep.whitepawns);

    printf("\n\n");

    char myboardstring[] = "0000000000000000000000000000000000000000000000000000000000000000";

    printf("%s", myboardstring);
    printf("\n\n");

    printBoardString(mybrep);

}

