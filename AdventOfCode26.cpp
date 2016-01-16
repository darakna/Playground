// AoC25.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<cstdint> // for int64_t
#include <algorithm> // for std::find
#include <iterator> // for std::begin, std::end

void temp()
{
	for (int64_t i = 0; i <= 6; i++)
	{
		for (int64_t j = 0; j <= i; j++)
		{
			std::cout << "next" << " ";
			//next++;
		}
		std::cout << std::endl;
	}
}
int64_t find_position(int64_t *array, int64_t size_arr, int64_t value)
{
	std::cout << "In ";
	for (int64_t i = 0; i < size_arr; i++)
	{
		if (array[i] == value)return i;
	}
	return -1;
}
int main()
{
	int64_t start = 20151125, multiply = 252533, divisor = 33554393, next = 0, lines, columns;
	int64_t pos = 0;
	int64_t* numbers = new int64_t[33554394];
	memset(numbers, 0, 33554394*sizeof(int64_t));
	numbers[0] = 20151125;
	for (int64_t i = 1; i < divisor; i++)
	{
		next = numbers[i - 1];
		next = next * multiply;
		next = next % divisor;
		pos = find_position(numbers, i, next);
		if(pos!= -1)std::cout << pos << std::endl;
		numbers[i] = next;
	}


    return 0;
}

