#include <stdio.h>

int main (){
	char one = 65;
	char two = 66;
	char tree = 67;
	char four = 68;
	char pipe = 124;
	char tilde = 126;
	
	printf("%c\n", one);
	printf("%c\n", two);
	printf("%c\n", tree);
	printf("%c\n", four);
	printf("%c\n", pipe);
	printf("%c\n", tilde);

	// To store strings
	char text[] = "Hello, world!";
	printf("%s\n", text);	// %s to print str

	char this[] = "";
	printf("%c\n", this);
	/*No matter what you put inside the "this"*/
	/*it will return some random ascii character*/
	/*(i think)*/

	return 0;
}
