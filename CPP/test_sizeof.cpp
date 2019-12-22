// AoCD20.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include<iostream>
#include<string>
#include<cstdint>


int main()
{
	std::cout << "Test " << std::endl;
	std::cout << "SizeOf( int ) " << sizeof( int ) <<std::endl;
	std::cout << "SizeOf( long ) " << sizeof(long) << std::endl;
	std::cout << "SizeOf( char ) " << sizeof(char) << std::endl;
	std::cout << "SizeOf( string ) " << sizeof(std::string) << std::endl;
	std::cout << "SizeOf( long int ) " << sizeof(long int) << std::endl;
	std::cout << "SizeOf( unsigned long int ) " << sizeof(unsigned long int) << std::endl;
	std::cout << "SizeOf( unsigned long int8_t ) " << sizeof(int8_t) << std::endl;
	std::cout << "SizeOf( unsigned long int16_t ) " << sizeof(int16_t) << std::endl;
	std::cout << "SizeOf( unsigned long int32_t ) " << sizeof(int32_t) << std::endl;
	std::cout << "SizeOf( unsigned long int64_t ) " << sizeof(int64_t) << std::endl;
    return 0;
}
