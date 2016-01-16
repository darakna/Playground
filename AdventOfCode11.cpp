// AoC11.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>

bool straight_letters(char word[9])
{
	for (int i = 0; i <= 5; i++)
	{
		if (((int)word[i] == int(word[i + 1] - 1)) && (int(word[i + 1]) == int(word[i + 2] - 1)))
			return true;
	}
	return false;
}
bool confusing_letters(char word[9])
{
	for (int i = 0; i <= 7; i++)
	{
		if ((int(word[i]) == int('i')) || (int(word[i]) == int('o')) || (int(word[i]) == int('l')))
		{
			return false;
		}
	}
	return true;

}
bool pair_letters(char word[9])
{
	int pairs = 0;
	for (int i = 0; i <= 6; i++)
	{
		if ((int)word[i] == int(word[i + 1]))
		{
			pairs++;
			i++;

		}
	}
	if (pairs >= 2) return true;
	else
		return false;
}

char* increment(char word[9], int position)
{
	if ((position == 0) && (word[0] == 'z'))
	{
		word[0] = 'a';
		return word;
	}
	else 
		if (word[position] == 'z')
		{
			word[position] = 'a';
			return increment(word, position - 1);
		}
		else
		{
			word[position]++;
			return word;
		}

}

char* process_w(char* word2)
{
	std::cout << "Test3" << std::endl;
	bool valid = false;
	std::cout << "Test4: " << word2<<std::endl;
	while (valid == false)
	{
		word2 = increment(word2, 7);
		//std::cout << "Test5: " << word2<<std::endl;
		if (straight_letters(word2) && (confusing_letters(word2)) && (pair_letters(word2)))
			valid = true;
		
	}
	
	return word2;
}


int main()
{
	std::cout << "Test1" << std::endl;
	char word2[9] = "hepxcrrq";
	std::cout << "Test2" << std::endl;
	


	word2[9] = *process_w(word2);
	std::cout << word2 << std::endl;

	word2[9] = *process_w(word2);
	std::cout << word2 << std::endl;

	
}

