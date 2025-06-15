#include <stdio.h>


int main (){
	// fgets string function
	char ztring[20];
	printf("str: ");
	fgets(ztring, sizeof(ztring), stdin);
	printf("%s", ztring);

	char stringg[20];
	int num;
	printf("str: ");
	scanf("%[^\n]s", stringg);  // scanf only gets one word at a time. Ex.: "^someword[space][scanf throws anything from now on away]"
	printf("num: ");
	scanf("%d", &num); 
	// "^" = not. So, "^\n" = everything that is not a new line.
	// & = tell the eddress of the var so that the func can change the content of it.
	// in the first scanf, the & is not used because the %s needs a var of type char * (pointer to a char type variable) and 
	// when you do only the var name it points to the var[0] that is  a char * 
	// scanf("%[^\n]s", &stringg); = take everything i give until a new line, and put inside stringg

	printf("%s\n", stringg);
	printf("%d\n", num);

	char cchar;
	int num2;
	printf("num & char: ");
	scanf("%d %c", &num2, &cchar); 
	printf("%d\n", num2);
	printf("%c\n", cchar);
	return 0;
}
