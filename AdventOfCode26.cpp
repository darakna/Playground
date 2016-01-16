// AoC25.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<cstdint> // for int64_t


int main()
{
	int64_t start = 20151125, multiply = 252533, divisor = 33554393, next = 0, lines = 2947, columns = 3029, ord = 0;

	ord = ((lines + columns-2)*(lines + columns-1))/2 + columns-1;
	next = start;
	for (int64_t i = 1; i <= ord; i++)
	{
		next = next * multiply;
		next = next % divisor;

	}
	std::cout << next << std::endl;

    return 0;
}

