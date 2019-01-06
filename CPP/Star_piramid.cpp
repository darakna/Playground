#include<iostream>
using namespace std;
void main()
{
	int row_number=0;
	cout <<"Row number is:";cin>>row_number;
	for(int row=1;row<=row_number;row++)
	{
		for(int column=1;column<(row_number*2);column++)
		{
			if((column>(row_number-row))&&(column<(row_number+row)))
			{
				cout<<"*";
			}
			else
			{
				cout<<" ";
			}
		
		}
		cout<<endl;
	}
}
