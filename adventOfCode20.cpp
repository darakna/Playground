// AoCD20.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
#include<cstdint>

int main()
{
	int64_t present = 36000000;
	int64_t curent_pres = 0;
	int64_t found = 0;
	while (found == 0)
	{
		for (int64_t casa = 1; casa <= present; casa++)
		{
			curent_pres = 0;
			for (int64_t ren = 1; ren <= casa; ren++)
			{
				if (casa % ren == 0)
				{

					curent_pres = curent_pres + ren * 10;
					if (curent_pres == present)
					{
						std::cout << casa << std::endl;
						break;
					}
				}
			}
			std::cout << "House " << casa << " got " << curent_pres << " presents." << std::endl;

		}

	}
	
    return 0;
}

