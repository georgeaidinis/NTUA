#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv){
    //fstream  afile;
    //afile.open(argv[1], ios::in );
    int N, K, sum = 0, i, j, ans;
    ifstream infile;
    infile.open(argv[1]);
    infile >> N >> K ;
    int *Arr = new int[N];
    int *check = new int[N];
    for(i=0; i<N; i++){
        infile >> Arr[i];
        check[i]=0;
    }
    i=0; j=0; ans=N+1;
    while(true){
        while(sum<K && j<N){
            if(check[Arr[j]]==0){
                sum++;
            }
            check[Arr[j]]++;
            j++;
        }
        while(sum==K && j<=N){
            if (j-i <= ans){
                ans = j - i;
            }
            if(check[Arr[i]] == 1){
                sum--;
            }
            check[Arr[i]]--;
            i++;
        }
        if(j==N){
            break;
        }
    }
    if(ans == N+1){
        cout << 0 << endl;
        exit(0);
    }
    cout << ans << endl;
    exit(0);
}