#include <stdio.h>

int main (){

	int nums[4] = {10, 20, 30, 40};

	int i;
	for (i=0;i < (sizeof(nums) / sizeof(nums[0]));i++){
		printf("addr of %d: %p\n", nums[i], &nums[i]);
		// the values printed are distant by a value of four, bacause the data(ints) have the size of four
		// addr of 1: 0x7ffeb8b7a630 0 
		// addr of 2: 0x7ffeb8b7a634 4
		// addr of 3: 0x7ffeb8b7a638 8
		// addr of 4: 0x7ffeb8b7a63c c (c = 12 in hex)
	}

	// in arrays, the mem addr of the arr ( as a whole) is the same as tha first element
	printf("(arr.: %p) == (first el.: %p) -> %d\n", nums, &nums[0], nums == &nums[0]); // true = 1

	// get the first element with arr mem addr
	printf("%d\n", *nums);
	// Get the second element
	printf("%d\n", *( nums + 1 ) ); // 0B + 4B = 4B = 2nd position 
	//                                       |
	//                                     ( 1 integer = 4 Bytes )
	// Get the third element
	printf("%d\n", *( nums + sizeof("a") ) ); // 0B + 8B = 8B = 3rd position
	//                                                 |
	//                                               ( 1 char (i.e. "a") = 8 Bytes )
	return 0;
}
