#include<iostream>
#include<fstream>
using namespace std;

/* continut fisier in.txt:
11 22
1 5 8 4 3 6 8 9 7 10 5
*/
int sum=0;
void sort(int *v,int nr)
{
	int i=1;
	while(i<nr)
	{
		if(v[i]>v[i+1])
		{

			int tmp=v[i+1];
			v[i+1]=v[i];
			v[i]=tmp;
			i=1;
		}
		i++;
	}
}
int reparatie(int *v, int nr_tevi,int distanta)
{
	if(nr_tevi&&(v[nr_tevi]==distanta))
		{
			cout<<v[nr_tevi]<<" ";
			sum+=v[nr_tevi];
	}
	else if(nr_tevi&&(distanta>v[nr_tevi]))
		{
			reparatie(v,nr_tevi-1,distanta-v[nr_tevi]);
			cout<<v[nr_tevi]<<" ";
			sum+=v[nr_tevi];
	}
	else if(nr_tevi)reparatie(v,nr_tevi-1,distanta);
	else return 0;
}

void main()
{
	int m,n,tevi[100],ir=0;
	ifstream myReadFile;
 myReadFile.open("in.txt");
 myReadFile>>m>>n;//m = nr tevi, n = lungimea de reparat
 cout<<"Nr de tevi este "<<m<<endl<<"Tevile sunt: ";
 for(int i=1;i<=m;i++)
 {
	 
		 myReadFile>>tevi[i];
 }
 sort(tevi,m);
 for(int i=1;i<=m;i++)
 {
	 
		 myReadFile>>tevi[i];
		 cout<<tevi[i]<<" ";
 }
 cout<<endl<<"Distanta de reparat este "<<n<<" si poate fi reparata cu:"<<endl;
 reparatie(tevi,m,n);
 if(sum==n)cout<<endl<<"Reparatie completa"<<endl;
 else cout<<endl<<"Reparatie incompleta! Distanta reparata "<<sum<<endl;
 
 myReadFile.close();
}
