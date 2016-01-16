#include<iostream>
#include<string.h>
using namespace std;
void ver_sir(char tmp[])
{
	int tmp_len=strlen(tmp),p_inc=0,p_des=0,j=0,err=0;
	char tmp2[20];
	for(int i=0;i<tmp_len;i++)//verificare nr de paranteze inchise si deschise;copiere paranteze in sir nou
	{
		if((tmp[i]==40)||(tmp[i]==91)||(tmp[i]==123)){ p_inc++;tmp2[j]=tmp[i];j++;}
		else if((tmp[i]==41)||(tmp[i]==93)||(tmp[i]==125)){ p_des++;tmp2[j]=tmp[i];j++;}
		cout<<tmp[i];
	}
	cout<<endl;
	for(int i=0;i<j;i++)cout<<tmp2[i];cout<<endl;
	if(p_inc==p_des)cout<<"Nr de paranteze deschise este acelasi cu nr de paranteze inchise"<<endl;
	else cout<<"Nr de paranteze deschise nu este acelasi cu nr de paranteze inchise"<<endl;
	for(int i=0;i<j-1;i++)
	{
		if(j%2==1){err=1;cout<<"Numar inegal de paranteze"<<endl;/*break*/;}
		if((tmp2[i]==123)&&!((tmp2[i+1]==125)||(tmp2[i+1]==91)||(tmp2[i+1]==40))){err=1;cout<<"Paranteza incorecta dupa "<<tmp2[i]<<" este "<<tmp2[i+1]<<endl;/*break*/;}
		else if((tmp2[i]==91)&&!((tmp2[i+1]==93)||(tmp2[i+1]==40))){err=1;cout<<"Paranteza incorecta dupa "<<tmp2[i]<<" este "<<tmp2[i+1]<<endl;/*break*/;}
		else if((tmp2[i]==40)&&!(tmp2[i+1]==41)){err=1;cout<<"Paranteza incorecta dupa "<<tmp2[i]<<" este "<<tmp2[i+1]<<endl;/*break*/;}
		else if((tmp2[i]==125)&&!((tmp2[i+1]==123)||(tmp2[i+1]==91)||(tmp2[i+1]==40))){err=1;cout<<"Paranteza incorecta dupa "<<tmp2[i]<<" este "<<tmp2[i+1]<<endl;/*break*/;}
		else if((tmp2[i]==93)&&!((tmp2[i+1]==125)||(tmp2[i+1]==91)||(tmp2[i+1]==40))){err=1;cout<<"Paranteza incorecta dupa "<<tmp2[i]<<" este "<<tmp2[i+1]<<endl;/*break*/;}
		else if((tmp2[i]==41)&&(tmp2[i+1]==41)){err=1;cout<<"Paranteza incorecta dupa "<<tmp2[i]<<" este "<<tmp2[i+1]<<endl;/*break*/;}
	}
	if(err==1)cout<<"Expresia are parantezele gresite"<<endl<<endl;
	else cout<<"Expresia are parantezele corecte"<<endl<<endl;


}

void main()
{
	char a[]="{x+[3*(2-1)+(2-1)+5]*(3-2)+3}";//definire sir corect
	char b[]="{x+[3*(2-{3*2}+2-1]+5}+3[";//definire sir gresit
	ver_sir(a);
	ver_sir(b);
}
