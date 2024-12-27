#include <stdio.h>

int main (){
	int i = 0;

	// while
	while (i < 10){ // ends at nine
		printf("%d ", i);
		i++;
	}

	printf("\n\n");
	i = 0;

	// while with the thing in the test
	while (i++ < 10){ // ends at ten
		printf("%d ", i);
	}

	printf("\n\n");
	i = 0;

	// do while loop

	do {
		printf("%d ", i);	// this will run
		i++;				// this will run
	} while ( i < 10 ); // if this is true, this will run again

	printf("\n\n");
	i = 0;

	while (i < 10){
		if ( i == 3){
			break;
		}
		printf("%d ", i);
		i++;
	}

	printf("\n\n");
	i = 0;

	while (i < 10){
		i++; // this have to be here. else, an infinite loop is created
		if ( i == 3){
			continue;
		}
		printf("%d ", i);
	}

	return 0;
}

