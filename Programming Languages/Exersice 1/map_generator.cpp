#include <iostream>
#include <fstream> 
#include <string>
#include <stdlib.h>

using namespace std;

int main(void){
	string name;
	string filetype = ".txt";
	cout << "Please give a name to the map" << endl;
	cin >> name;
	std::ofstream outfile (name+filetype);
	int M, N;
	cout << "Please give dimensions of map, M,N" << endl;
	cin >> M >> N;
	char Board[M][N];
	cout << "A '.txt' file will be created in the same directory." << endl;
	cout << M << "  " << N << endl;
	int a_x, a_y;
	a_x = rand()%M;
	a_y = rand()%N;
	cout<< a_x << ',' << a_y << endl;
	int value;
	for(int i = 0; i < M; i++){
		for(int j = 0; j<N; j++){
			if (i == a_x && j == a_y){
				Board[i][j] = 'A';
				cout << Board[i][j] << ' ';
				continue;
			}
			else {
				value = rand()%100 +1;
				if (value<=2)
					Board[i][j] = 'W';
				else if(value>2 && value<75)
					Board[i][j] = '.';
				else
					Board[i][j] = 'X';
			}
			cout << Board[i][j] << ' ';
		}
		cout << endl;
	}
	ofstream myfile; 
	myfile.open (name+filetype);
	for(int i = 0; i < M; i++){
		for(int j = 0; j<N; j++){
			myfile << Board[i][j] << ' ';
		}
		myfile << endl;
	}
	myfile.close();
}