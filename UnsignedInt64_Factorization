// BigNumberFactorization.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"
#include <time.h>
#include <windows.h>



void process_2(unsigned long long int &number, unsigned long long int divs[], unsigned long long int &div_n)
{
	while (number % 2 == 0)
	{
		number = number / 2;
		divs[div_n] = 2;
		div_n++;
	}
		


}

unsigned long long int number_sum(unsigned long long int is_3_div)
{
	int sum = 0;
	while (is_3_div != 0)
	{
		sum = sum + is_3_div % 10;
		is_3_div = is_3_div / 10;
	}

	if (sum > 10)
		return number_sum(sum);
	else
		return sum;
}
void process_3(unsigned long long int &number, unsigned long long int divs[], unsigned long long int &div_n)
{
	while (number_sum(number) % 3 == 0)
	{
		number = number / 3;
		divs[div_n] = 3;
		div_n++;
	}



}

void process_5(unsigned long long int &number, unsigned long long int divs[], unsigned long long int &div_n)
{
	while (number % 5 == 0)
	{
		number = number / 5;
		divs[div_n] = 5;
		div_n++;
	}



}

void rest_factors(unsigned long long int &number, unsigned long long int divs[], unsigned long long int &div_n)
{

	for (unsigned long long int i = 7; i <= sqrt(number); i = i + 2)
	{
		if (number % i == 0)
		{
			number = number / i;
			divs[div_n] = i;
			div_n++;
			rest_factors(number, divs, div_n);
		}
	}

}

int main()
{


	unsigned long long int big_number, factors[100], num_div=0;
	printf("Enter number: ");

	scanf_s("%I64u", &big_number);
	printf("Number is:    %I64u\n", big_number);

	DWORD dw1 = GetTickCount();

	process_2(big_number, factors, num_div);
	process_3(big_number, factors, num_div);
	process_5(big_number, factors, num_div);
	

	if (big_number > 1)
	{
		rest_factors(big_number, factors, num_div);
		if (big_number != 1)
		{
			factors[num_div] = big_number;
			num_div++;
		}


	}

	printf("Biggest factor is: %I64u\n", factors[num_div-1]);

	printf("Number of factors: %I64u\nDivisors: ", num_div);
	for (unsigned long long int i = 0; i < num_div; i++)
	{
		printf("%I64u ",factors[num_div - i - 1]);
	}
	printf("\n");

	DWORD dw2 = GetTickCount();

	printf("Time difference is %lu milliSeconds\nStart: %lu\nEnd: %lu\n", dw2 - dw1, dw2, dw1);

    return 0;
}

