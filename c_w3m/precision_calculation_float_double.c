#include <stdio.h>

int main ()
{
	float seven = 1.1234567;
	double fifteen = 1.123456789123456;

	float op1 = seven * fifteen;
	double op2 = seven * fifteen;

	printf("%f\n", op1);
	printf("%lf\n\n", op2);

	float opp1 = seven * 10;
	double opp2 = fifteen * 10;

	printf("%f\n", opp1);
	printf("%lf\n\n", opp2);

	double oppp2 = fifteen * 1.999999;
	float oppp1 = seven * 1.999999;

	printf("%f\n", oppp1);
	printf("%lf\n\n", oppp2);


	// I probably did something wrong, because there is no difference in the results
	// output
	/*
	1.262155
	1.262155

	11.234568
	11.234568

	2.246912
	2.246912
	*/

	return 0;
}


