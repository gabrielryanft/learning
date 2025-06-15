#include <stdio.h>

int main(){
	float f_num = 1.123456;

	printf("%f\n", f_num);
	printf("%.0f\n", f_num);
	printf("%.1f\n", f_num);
	printf("%.2f\n", f_num);
	printf("%.3f\n", f_num);
	printf("%.4f\n", f_num); // decimals start to jump one digit around here.
	printf("%.5f\n", f_num);
	printf("%.6f\n\n", f_num);

	/*
	1.123456
	1
	1.1
	1.12
	1.123
	1.1235
	1.12346
	1.123456
	*/

	float five  = 1.555555;
	float m_five= 1.666666;
	float lm_five= 1.500001;
	float l_five= 1.444444;
	float ll_five= 1.400009;

	printf("%.0f\n", five  );
	printf("%.0f\n", m_five);
	printf("%.0f\n", lm_five);
	printf("%.0f\n", l_five);
	printf("%.0f\n", ll_five);

	/*
	2
	2
	2
	1
	1
	*/

	return 0;
}

