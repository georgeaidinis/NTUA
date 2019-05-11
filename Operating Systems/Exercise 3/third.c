#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <stdbool.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char ** argv){
        int Ppid = getpid();
        int status;
        int N = atoi(argv[1]);
        int K = atoi(argv[2]);
        int i,j;
        long long int result = 0;

        if(N<1 || N>10){
            printf("Wrong Input\n");
            exit(0);
        }
        // children array
        //pid_t *childpid = malloc(N * sizeof(pid_t));
        pid_t childpid[10];

        for(i=0; i<N; i++){
            childpid[i]=-2;
        }

        // pipe array
        int arr[10][2];
        //int **arr = (int **)malloc(N+1 * sizeof(int *));
        for (i=0; i<N+1; i++){
            //arr[i] = (int *)malloc(2 * sizeof(int));
            pipe(arr[i]); //0 on success, -1 on error.
        }


        for(i=0; i<N; i++){
            childpid[i]=fork();
            if(childpid[i]==0){
                j=i;
                for(int k=0; k<N; k++){
                	//close every read end apart from the one we're in
                    if(k!=i){
                        close(arr[k][0]);
                        //printf("Close read end %d for child %d\n",k,i);
                    }
                    //close every write end apart from the one that's next of us, and the one that's first.
                    if(k!=i+1){
                    	//this is the first write pipe:
                        if((j==N-1 && k==0)){
                        }
                        //this is every other:
                        else{
                            close(arr[k][1]);
                            //printf("Close write end %d for child %d\n",k,i);
                        }
                    }
                }
                break;
            }
            else{
            	//needs more code but ok
                continue;
            }
        }
        //printf("j is: %d, \n",j);
        for(i=0; i<N; i++){
            if(childpid[i]==0){
                while(true){
                	//if something has been written, that's not the -1 we wrote at the beginning:
                    if(read(arr[i][0],&result,sizeof(result))!=-1){
                    	//if we've reached the result, it means that K calculations have been made, and thus this is the last calc:
                        if(j==K){
                            printf("Last Child (%d) Wrote at pipe %d the result is %lld\n",i,N,result);
                            write(arr[N][1],&result,sizeof(result));//Behaves like FIFO
                            //sleep(1);
                            exit(0); //exit so that parent can continue
                        }
                        result = result * (j+1);
                        //if it ever comes back to this child, the j must have made +N calculations:
                        j=j+N;
                        write(arr[(i+1)%N][1],&result,sizeof(result));
                        printf("Child %d Wrote at pipe %d the result is %lld\n\n",i,(i+1)%N,result);
                        //if we are beyond K calculations, we have to close everything so that parent can read and finish.
                        if(j>K){
                            close(arr[(i+1)%N][1]);
                            close(arr[i][0]);
                            close(arr[N][0]);
                            close(arr[N][1]);
                            exit(0);
                        }
                    }
                }
            }
        }
        //if we are in the parent process:
        if(getpid()==Ppid){
            result = 1;
            //all childs are still waiting for something to be written to their pipes.
            for(i=0; i<N; i++){
            	//close the read end for every pipe for parent proc:
                close(arr[i][0]);
            }
            //write to the first pipe:
            write(arr[0][1],&result,sizeof(result));
            for(i=0; i<N; i++){
            	//close all writing pipes:
                close(arr[i][1]);
                }
                //wait for every kid:
                for(int i = 0; i<N ; i++){
                    wait(&status);
                }
                //read the last pipe for the result:
                read(arr[N][0],&result,sizeof(result));
                printf("Result = %lld \n",result);
                return(0);
            }
        }
