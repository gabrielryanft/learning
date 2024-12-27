#import <stdio.h>
#import <stdbool.h>

int main () {
	int day = 0;

	switch (day) {
		case 0: 
			printf("sunday");
		// if day = 0, because this case does not have a break, it keeps going
		// so it prints ...
		case 1: 
			printf("monday"); // ... this line ...
			break; // abd then breaks 
		case 2: 
			printf("tuesday");
			break;
		case 3: 
			printf("wednesday");
			break;
		case 4: 
			printf("thursday");
			break;
		case 5: 
			printf("friday");
			break;
		case 6: 
			printf("saturday");
			break;
		case 7: 
			printf("sunday");
			break;
		default:
			printf("this day does not seem to exist");
			//does not need a break
	}

	return 0;
}
