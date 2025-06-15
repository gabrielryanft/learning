#include <stdio.h>

int main (){
	int arrayNums[] = {10, 20, 40, 70, 100};
	/*printf("%d", arrayNums);*/

	int n = sizeof(arrayNums) / sizeof(arrayNums[0]);
	//       size of arr in     size of first element
	//        bytes  (if         in bytes
	// there is 2 int, the      with this you can determine the size of the 
	//  size is 2 * 4 = 8)       element in the array, int, char ... if the 
	//                       items are int, all of them will have the size of
	//         !------- 4 bytes, char: 1 byte  ...
	// Ex: x * 4  = 20
	// so: x = 40 / 4 -> x = 5 -> five is the length of the array
	// 


	printf("%lu\n\n", sizeof(int));
	int i;
	for ( i = 0 ; i < n ; i++ ){
	printf("%d\n", arrayNums[i]);
	}

	int arr_w4[4]; // creates a arr with 4 items

	// multidimensional arrays:

	printf("\n\n");

	int twoD[2][3] = {{1, 2, 3}, {4, 5, 6}}; // you have to specify the size
	// [2] = the main list have 2 items : { x, x } of k size
	// [3] = the two inner ones, have 3 of length
	//                   x or i     y or j
	// 1 2 3 
	// 4 5 6  matrix = 2 x 3
	printf("%d\n", twoD[0][2]);

	int n2d_parent = sizeof(twoD) / sizeof(twoD[0]);
	int n2d_child = sizeof(twoD[0]) / sizeof(twoD[0][0]);

	printf("%d\n", n2d_parent);
	printf("%d\n", n2d_child);

	int j;
	for (i = 0 ; i < n2d_parent ; i++){
	for (j = 0 ; j < n2d_child ; j++){
			printf("%d\n", twoD[i][j]);
	}
	}

	return 0;
}
