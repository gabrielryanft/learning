#include <stdio.h>

int main(){
	int i; // you have to define this outside
	for (i = 0 ; i < 10 ; i++){ // 0 - 9
		printf("%d\n", i);
	}

	printf("\n\n");
	for (i = 0; i < 10 ; i++){ // runs only once, 
		printf("pipipi %d\n", i);
		for (i = 0; i < 10 ; i++){ // because this, turns i into 9
			printf("oioi %d\n", i);
		} // i gets out here, 9
	} // i++ = 10, i is not less than 10

	printf("\n\n");
	for (i = 0; i < 10 && i % 2 == 0; i++)
	// OBVIOUSLY, the loop will run only if the condition is true.
	// that is why it only prints 0 and ends.
	// when i = 1, i % 2 == 0 returns false, and it ends
	{
		printf("%d\n", i);
	}

	printf("\n\n");
	for (i = 0; i <= 10 ; i++)
	{
		if (i % 2 == 0){
			printf("%d\n", i);
		}
	}

	printf("\n\n");
	// You can use break in here too.
	for (i = 0; i<10; i++)
	{
	  if ( i == 2) { break; } 
		printf("%d\n", i);
	}


	printf("\n\n");
	for (i = 0; i<10; i++)
	{
		printf("index: ");
	  if ( i == 2) { continue; } 
		printf("%d\n", i);
	}
	return 0;
}
