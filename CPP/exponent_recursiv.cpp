// Exp_recursiv.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
using namespace std;
float pwr(float a, float b)
{
	//cout << a << " " << b << endl;
	if (b == 0) return 1;
	else if (b < 0) return 1/a*(pwr(a, b + 1));
	else return a*(pwr(a, b - 1));

	//to be implemented 0< exponent < 1
}
void main()
{
	float baza, exponent;
	cout << "Baza este:"; cin >> baza;
	cout << "Exponentul este:"; cin >> exponent;
	cout << baza << " la puterea " << exponent << " este " << pwr(baza, exponent) << endl;
}
