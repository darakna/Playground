#include<iostream>
#include<fstream>
using namespace std;

/*in.txt
5 5
1 2 3 4 21
5 6 7 8 31
9 10 11 12 41
51 61 71 81 91
101 102 103 104 105
*/

void selectedRead(int linii, int coloane, const int **p) {
	for (int c = 0, l = 0; c + l <= linii + coloane - 2; c<coloane - 1 ? c++ : l++) {
		int copyC = c;
		int copyL = l;
		while (copyC >= 0 && copyL <= linii - 1) {
			cout << p[copyL][copyC] << ' ';
			copyC--;
			copyL++;
		}
	}
}

void main()
{
	int m,n,mat[20][20];
	ifstream myReadFile;
 myReadFile.open("in.txt");
 myReadFile>>m>>n;
 for(int i=0;i<m;i++)
 {
	 for(int j=0;j<n;j++)
	 {
		 myReadFile>>mat[i][j];
	 }
 }
 for(int i=0;i<m;i++)
 {
	 for(int j=0;j<n;j++)
	 {
		 cout<<mat[i][j]<<" ";
	 }
	 cout<<endl; 
 }
 int sign=0;
 cout << endl << endl;
 //selectedRead( m, n,*mat);

 for (int c = 0, l = 0; c + l <= m + n - 2; c<m - 1 ? c++ : l++) {
	 int copyC = c;
	 int copyL = l;
	 while (copyC >= 0 && copyL <= n - 1) {
		 cout << mat[copyL][copyC] << ' ';
		 copyC--;
		 copyL++;
	 }
	 cout << endl;
 }

 myReadFile.close();


}
