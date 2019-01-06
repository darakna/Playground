#include<iostream>
using namespace std;
void main()
{
	int a[100]={2,3,5,8,5,3,7,4},b[100]={9,5,6,8,3,1,1},c[100];
	int na=0,nb=0,nc=0;
	while(a[na])
		{
			na++;
	cout<<a[na-1]<<" ";
	}
	cout<<endl<<na<<endl;
	while(b[nb])
		{
			nb++;
			cout<<b[nb-1]<<" ";
	}
	cout<<endl<<nb<<endl;
	if(na<nb)
	{
		int tmp=na;
		na=nb;
		nb=tmp;
	}
	else if((na==nb)&&(a[0]+b[0]>9))
	{
		for(int i=0;i<=na;i++)
		{
			a[na-i+1]=a[na-i];
			b[na-i+1]=b[na-i];
		}
		a[0]=0;
		b[0]=0;
		na++;
		nb++;
	}
	while(nb>0)
	{
			na--;
			nb--;
		if(a[na]+b[nb]>9)
		{
			a[na-1]++;
			c[na]=(a[na]+b[nb])%10;
		}
		else 
			c[na]=a[na]+b[nb];
		
	}
	while(na>=0)
		{
			c[na]=a[na];
			na--;
	}
	while(a[na+1])
	{
		na++;
		cout<<c[na]<<" ";
		
	}
	cout<<endl;
}
