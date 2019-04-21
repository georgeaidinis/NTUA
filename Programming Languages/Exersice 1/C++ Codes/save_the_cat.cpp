#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <stack>

using namespace std;

class coord {
public:
    int x;
    int y;
    int t;

    coord(int a,int b,int c){
        x=a;
        y=b;
        t=c;
    }

    int get_x(){
        return x;
    }

    int get_y(){
        return y;
    }

    int get_t(){
        return t;
    }
};

int cats=1;

string Answer (char board[1001][1001], int ti, int tj, int si, int sj){
    string answer ;
    string key;
        while(!(ti==si && tj==sj)){
            if (board[ti][tj] >= 'a' && board[ti][tj] <= 'z'){
                board[ti][tj] = board[ti][tj] + 'A' - 'a';
            }
            key=string(1,board[ti][tj]);
            if (tj==-1){
                return " ";
            }
            if(board[ti][tj] == 'D'){
                ti--;
            }
            else if(board[ti][tj] == 'U'){
                ti++;
            }
            else if(board[ti][tj] == 'R'){
                tj--;
            }
            else if(board[ti][tj] == 'L'){
                tj++;
            }
            answer = answer + key;
        }
    //cout << answer << " a" << endl;
    reverse(answer.begin(),answer.end());
    return answer;
}

bool is_cat(char a){
    if (a == 'A' || a == 'L' || a == 'R' || a == 'U' || a == 'D')
        return true;
    return false;
}

bool were_cat(char a){
    if (a == 'a' || a == 'l' || a == 'r' || a == 'u' || a == 'd')
        return true;
    return false;
}

bool is_water(char a){
    if ( a == 'W' || a == 'l' || a == 'r' || a == 'u' || a == 'd' || a == 'a')
        return true;
    return false;
}

char conflict(char a, char b){
    if(a>b)
        return a;
    return b;
}

void min_pos(int result [2], char board[1001][1001], int M, int N){
    for (int i=0; i<M; i++){
        for (int j=0; j<N; j++){
            if(is_cat(board[i][j]) && i<result[0]) {
                result[0] = i;
                result[1] = j;
            }
            if(is_cat(board[i][j]) && i==result[0] && j<result[1])
                result[1] = j;
        }
    }
}

void Min_pos(int result [2], char board[1001][1001],int timed[1001][1001], int M, int N,int T){
    for (int i=0; i<M; i++){
        for (int j=0; j<N; j++){
            if(were_cat(board[i][j]) && i<result[0] && timed[i][j]==T-2) {
                result[0] = i;
                result[1] = j;
            }
            if(were_cat(board[i][j]) && i==result[0] && j<result[1] && timed[i][j]==T-2)
                result[1] = j;
        }
    }
}

bool update_cat (char board[1001][1001],int timed[1001][1001],int bs[2] ,int I,int J,int T,int N,int M,stack <coord> &c){
    bool cat=false;
    if(J!=0){
        if(board[I][J-1] == '.' ){
            board[I][J-1] = 'L';
            timed[I][J-1] = T;
            c.push(coord(I,J-1,T));
            cats++;
            bs[0]++;
            cat = true;
        }
        else if(is_cat(board[I][J-1])){
            if (timed[I][J-1] == T){
                board[I][J-1] = conflict(board[I][J-1],'L');
            }
        }
    }
    if(J!=N-1){
        if(board[I][J+1] == '.'){
            board[I][J+1] = 'R';
            timed[I][J+1] = T;
            c.push(coord(I,J+1,T));
            cats++;
            bs[0]++;
            cat = true;
        }
        else if(is_cat(board[I][J+1])){
            if (timed[I][J+1] == T){
                board[I][J+1] = conflict(board[I][J+1],'R');
            }
        }
    }
    if(I!=0){
        if(board[I-1][J] == '.'){
            board[I-1][J] = 'U';
            timed[I-1][J] = T;
            c.push(coord(I-1,J,T));
            cats++;
            bs[0]++;
            cat = true;
        }
        else if(is_cat(board[I-1][J])){
            if (timed[I-1][J] == T){
                board[I-1][J] = conflict(board[I-1][J],'U');
            }
        }
    }
    if(I!=M-1){
        if(board[I+1][J] == '.'){
            board[I+1][J] = 'D';
            timed[I+1][J] = T;
            c.push(coord(I+1,J,T));
            cats++;
            bs[0]++;
            cat = true;
        }
        else if(is_cat(board[I+1][J])){
            if (timed[I+1][J] == T){
                board[I+1][J] = conflict(board[I+1][J],'D');
            }
        }
    }
    return cat;
}

void update_water (char board[1001][1001],int timed[1001][1001],int bs[2] , int I,int J,int T,int N,int M,stack <coord> &w){
    if(J!=0){
        if(board[I][J-1] == '.' || is_cat(board[I][J-1])){
            if(is_cat(board[I][J-1])){
                cats--;
                bs[0]--;
                bs[1]++;
                board[I][J-1] = board[I][J-1] + 'a' - 'A';
                timed[I][J-1] = T;
            }
            else{
                bs[1]++;
                board[I][J-1] = 'W';
                timed[I][J-1] = T;
            }
            w.push(coord(I,J-1,T));
        }
    }
    if(J!=N-1){
        if(board[I][J+1] == '.' || is_cat(board[I][J+1])){
            if(is_cat(board[I][J+1])){
                cats--;
                bs[0]--;
                bs[1]++;
                board[I][J+1] = board[I][J+1] + 'a' - 'A';
                timed[I][J+1] = T;
            }
            else{
                bs[1]++;
                board[I][J+1] = 'W';
                timed[I][J+1] = T;
            }
            w.push(coord(I,J+1,T));
        }
    }
    if(I!=0){
        if(board[I-1][J] == '.' || is_cat(board[I-1][J])) {
            if(is_cat(board[I-1][J])){
                cats--;
                bs[0]--;
                bs[1]++;
                board[I-1][J] = board[I-1][J] + 'a' - 'A';
                timed[I-1][J] = T;
            }
            else{
                bs[1]++;
                board[I-1][J] = 'W';
                timed[I-1][J] = T;
            }
            w.push(coord(I-1,J,T));
        }
    }
    if(I!=M-1){
        if(board[I+1][J] == '.' || is_cat(board[I+1][J])) {
            if(is_cat(board[I+1][J])){
                cats--;
                bs[0]--;
                bs[1]++;
                board[I+1][J] = board[I+1][J] + 'a' - 'A';
                timed[I+1][J] = T;
            }
            else{
                bs[1]++;
                board[I+1][J] = 'W';
                timed[I+1][J] = T;
            }
            w.push(coord(I+1,J,T));
        }
    }
}

int main(int argc, char** argv){
    ifstream infile;
    infile.open(argv[1]);
    char Board[1001][1001];
    int Timed[1001][1001];
    int Miinimum_positions[2] = {1001,1001};
    stack <coord> c1,c2,w1,w2;
    int Bs[2] = {0};
    int prev[2]= {0};
    bool play = true;
    bool check = true;
    bool Stop = true;
    int N = 0 , M = 0, i = 0, j = 0, time = 1, Si=0, Sj=0;
    char a;
    while(infile.get(a)){
        if (a == ' '){
            continue;
        }
        else if(a == '\n'){
            check = false;
            M++;
            j=0;
            i++;
            continue;
        }
        else {
            Board[i][j] = a;
            Timed[i][j] = 0;
            if(a == 'W'){
                Bs[1]++;
                prev[1]++;
                w1.push(coord(i,j,0));
            }
            if(a == 'A'){
                Bs[0]++;
                Si=i;
                Sj=j;
                c1.push(coord(i,j,0));
            }
            j++;
            if(check){
                    N++;
            }
        }
    }
    /*
    for(int i=0; i<M; i++){
        for (int j=0; j<N; j++){
            cout << Board[i][j] << ' ';
        }
        cout << endl;
    }*/
    infile.close();
    while(true){
        coord temp(-1,-1,-1);
        bool A;
        if((time+1)%2==0){
            while(!c1.empty()){
                temp = c1.top();
                c1.pop();
                A = update_cat(Board,Timed,Bs,temp.get_x(),temp.get_y(),time,N,M,c2);
                if(A){
                    Stop = false;
                }
            }
            while(!w1.empty()){
                temp = w1.top();
                w1.pop();
                update_water(Board,Timed,Bs,temp.get_x(),temp.get_y(),time,N,M,w2);
            }
        }
        else{
            while(!c2.empty()){
                temp = c2.top();
                c2.pop();
                A = update_cat(Board,Timed,Bs,temp.get_x(),temp.get_y(),time,N,M,c1);
                if(A){
                    Stop = false;
                }
            }
            while(!w2.empty()){
                temp = w2.top();
                w2.pop();
                update_water(Board,Timed,Bs,temp.get_x(),temp.get_y(),time,N,M,w1);
            }
        }
        time++;
        if(!play){
            break;
        }
        /*for(int i=0; i<M; i++){
            for (int j=0; j<N; j++){
                cout << Board[i][j] << ' ';
            }
            cout << endl;
        }
        cout << endl;
        */
        if(c1.empty() && c2.empty() && (prev[1]==Bs[1] || cats==0)){
            play = false;
            continue;
        }
        else if(Stop &&  prev[0]==Bs[0] ){
            play = false;
            continue;
        }
        else{
            prev[0]=Bs[0];
            prev[1]=Bs[1];
        }

    }
    if(Bs[0]!=0){
        min_pos(Miinimum_positions, Board, M, N);
        cout << "infinity" << endl;
        if(Miinimum_positions[0]==Si && Miinimum_positions[1]==Sj){
            cout << "stay" << endl;
        }
        else{
            cout << Answer(Board,Miinimum_positions[0],Miinimum_positions[1],Si,Sj) << endl;
        }
    }
    else{
        Min_pos(Miinimum_positions, Board,Timed, M, N,time);
        cout << time-3 << endl;
        cout << Answer(Board,Miinimum_positions[0],Miinimum_positions[1],Si,Sj) << endl;
    }
    return(0);
}