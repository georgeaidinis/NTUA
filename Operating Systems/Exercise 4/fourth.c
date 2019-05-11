#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <stdbool.h>
#include <sys/types.h>
#include <sys/wait.h>

void critical_section(int i,pid_t child_ID,int pipe0[],int pipe1[],int pipe2[]){
	int j,x;
	int cont = 1;
	int stop = 0;
	while(true){
		read(pipe0[0],&x, sizeof(stop));
		if(x>0){
			write(pipe0[1],&stop,sizeof(stop));
			printf("\n");
			for (j=1; j<6; j++){
				printf("Child %d, pID: %d, executes a Critical section, for the %d time.\n",i+1, child_ID, j);
			}
			printf("\n");
			//read(pipe0[0],&x, sizeof(stop));
			write(pipe0[1],&cont,sizeof(stop));
			return;
		}
		write(pipe0[1],&x,sizeof(stop));
	}
}
void non_critical_section(int i,pid_t child_ID,int pipe0[],int pipe1[],int pipe2[],int times){
	int x;
	int cont = 1;
	if (times==0)
		return;
	read(pipe0[0],&x, sizeof(cont));
	if(x>0){
		printf("Child %d, pID: %d, executes a Non - Critical section, for the %d time.\n",i+1, child_ID, 8-times);
		write(pipe0[1],&x,sizeof(cont));
		non_critical_section(i,child_ID,pipe0,pipe1,pipe2,times-1);
	}
	else{
		write(pipe0[1],&x,sizeof(cont));
		non_critical_section(i,child_ID,pipe0,pipe1,pipe2,times);
	}

	/*while(true){
		read(pipe0[0],&x, sizeof(cont));
		if(x>0){
			while(j<8){
				if (x>0){
					printf("Child %d, pID: %d, executes a Non - Critical section, for the %d time.\n",i+1, child_ID, j);
					write(pipe0[1],&cont,sizeof(stop));
					j++;
					if(j<=8){
						read(pipe0[0],&x, sizeof(stop));
					}
				}
				else {
					write(pipe0[1],&stop,sizeof(stop));
					continue;
				}
			}
			return;
		}
		else {
			write(pipe0[1],&stop,sizeof(stop));
			continue;
		}
	}*/
}
int main (int argc, char ** argv){
	int i,x, status;
	int cont = 1;
	pid_t Child_ID[3];
	int pipe0[2], pipe1[2], pipe2[2];
	if (pipe(pipe0) == -1)
   		printf("Error on pipe creation\n"); //0 on success, -1 on error.
	if (pipe(pipe1) == -1)
   		printf("Error on pipe creation\n"); //0 on success, -1 on error.
   	if (pipe(pipe2) == -1)
   		printf("Error on pipe creation\n"); //0 on success, -1 on error.
   	write(pipe0[1],&cont,sizeof(cont));
	for(i=0;i<3;i++){
		x = fork();
		if (x>0){
			Child_ID[i] = x;
		}
		else if (x==0 && i==0){
			pid_t child1 = getpid();
	    	critical_section(0,child1,pipe0,pipe1,pipe2);
	    	non_critical_section(0,child1,pipe0,pipe1,pipe2,7);
	    	non_critical_section(0,child1,pipe0,pipe1,pipe2,7);
	    	critical_section(0,child1,pipe0,pipe1,pipe2);
	    	non_critical_section(0,child1,pipe0,pipe1,pipe2,7);
	    	critical_section(0,child1,pipe0,pipe1,pipe2);
    		exit(0);
			break;
		}
		else if (x==0 && i==1){
			pid_t child2 =  getpid();
			non_critical_section(1,child2,pipe0,pipe1,pipe2,7);
	     	critical_section(1,child2,pipe0,pipe1,pipe2);
	     	non_critical_section(1,child2,pipe0,pipe1,pipe2,7);
	     	critical_section(1,child2,pipe0,pipe1,pipe2);
	     	non_critical_section(1,child2,pipe0,pipe1,pipe2,7);
	     	critical_section(1,child2,pipe0,pipe1,pipe2);
			exit(0);
			break;
		}
		else if (x==0 && i==2){
			pid_t child3 = getpid();
	     	critical_section(2,child3,pipe0,pipe1,pipe2);
	     	non_critical_section(2,child3,pipe0,pipe1,pipe2,7);
	     	critical_section(2,child3,pipe0,pipe1,pipe2);
	     	non_critical_section(2,child3,pipe0,pipe1,pipe2,7);
	     	critical_section(2,child3,pipe0,pipe1,pipe2);
	     	non_critical_section(2,child3,pipe0,pipe1,pipe2,7);
			exit(0);
			break;
		}
		else printf("Error on fork!\n");
	}
	
	wait(&status);
	wait(&status);
	wait(&status);

	printf("###################################################\n");
	for(i=0;i<3;i++){
    	printf("Child %d, has pID: %d\n",i+1, Child_ID[i]);
    }
    exit(0);
}