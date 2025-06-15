#include <stdio.h>
#include <string.h>

int main (){
	char oi[10] = "oi"; // have to be in double quotes
	//      10 -> if you give it a value, it will have that value
	// the string being that long or not
	printf("%d\n", strlen(oi)); // so strlen(oi) -> 2
	printf("%d\n", sizeof(oi)); // so sizeof(oi) -> 10

	printf("\n\n");
	printf("%s\n", oi);

	int size_oi = sizeof(oi); // 3

	printf("%d\n", size_oi);
	printf("%d\n", strlen(oi)); // 2// can only be used if string.h is influded

	// making strings the hard way:
	char sthw[] = {'a', 'n', 't', 'i', 's', 'o', 'c', 'i', 'a', 'l', '\0'};
	// put the \0 to identify the end of the str
	printf("%s\n", sthw);

	char sthw_incomplete[] = {'a', 'n', 't', 'i', 's', '\0', 'o', 'c', 'i', 'a', 'l'};
	printf("%s\n", sthw_incomplete);
	printf("%d\n", strlen(sthw)); // 10
	printf("%d\n", strlen(sthw_incomplete)); // 5, because the str ends first

	char especial_chars[] = "this \"is\' \\ things."; // have to escape the quotes and backslashes
	char escape_sequences[] = "new line: \\n;\ntuple: \t; et citera "; // especial chars

	// MERGING STRINGS
	char str1[20] = "Hello, "; // for the strings to be able to merge, the first one have to be bigger or equal of the resulting string
	char str2[] = "World";

	printf("str 1 before cat: %s\n", str1);
	printf("str 2 before cat: %s\n", str2);

	strcat(str1, str2);

	printf("after cat, str1: %s\n", str1);

	printf("\n\n");
	//COPY STRINGS

	char first_one[20] = "copy this";
	char copy_one[20];

	printf("first_one before copy: %s\n", first_one);
	printf("copy_one before copy: %s\n", copy_one);

	strcpy(copy_one, first_one);

	printf("after copy, copy_one: %s\n", copy_one);

	printf("\n\n");
	// COMPARE STRINGS

	char equal1[] = "oi";
	char equal2[] = "oi";
	char not_equal[] = "op";

	printf("%d\n", strcmp(equal1, equal2)); // 0 = equal 
	printf("%d\n", strcmp(equal1, not_equal)); // some other number = not equal 

	return 0;
}
