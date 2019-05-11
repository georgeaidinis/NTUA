#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main(void){
	int i = 0;
	int status;
	//so far this is F, no child process has been created
	//this is the process ID of F:
	pid_t F_pID;
	F_pID = getpid();
	//we need to create the left branch of the tree, C1 C3 C4
	//			F
	//	       / \
	//	      /   \
	//	   ->C1   C2
	//	    /  \    \
	//	   /    \    \
	//	->C3  ->C4   C5
	

	//time to fork
	pid_t C1;
	C1 = fork();
	//if we have fork<0, that means something went wrong
	if (C1<0)
		printf("Error! \n");


	//if fork=0, that means that we are in the forked process, C1
	else if (C1==0)
	{
	// now we need to create the children of C1
	//first C3

		pid_t C3;
		C3 = fork();
	//if we have fork<0, that means something went wrong
		if (C3<0)
			printf("Error! \n");

	//if fork=0, that means that we are in the forked process, C3
	//we need to do the printings here
		else if (C3 == 0){
			for(i=0; i<10; i++){
				//printf("C3:		");
				printf("Process %d is executed, my father is %d \n", getpid(), getppid());
	//the process sleeps between prints, so that the prints have intervals of 1 sec.
				sleep(1);
			}
	//before we move on to C4, we need to kill process C3:
			exit(0);
		}


	//else, fork>0, that means that we are still in the original C1, and therefore we need to fork again for C4
		else {
			pid_t C4;
			C4 = fork();
	//if we have fork<0, that means something went wrong
			if (C4<0)
				printf("Error! \n");


	//if fork=0, that means that we are in the forked process, C4
	//we need to do the printings here
			if (C4 == 0){
				for(i=0; i<10; i++){
				//printf("C4:		");
					printf("Process %d is executed, my father is %d \n", getpid(), getppid());
	//the process sleeps between prints, so that the prints have intervals of 1 sec.
					sleep(1);
				}
	//before we move on to the prints for C1 and C2, we need to kill process C4:
				exit(0);
			}


	//prints for C1:
			for(i=0; i<10; i++){
				//printf("C1:		");
				printf("Process %d is executed, my father is %d \n", getpid(), getppid());
	//the process sleeps between prints, so that the prints have intervals of 1 sec.
				sleep(1);
			}
	
	
	//Before we kill process C1 we need to wait for the children processes C3, C4 to end, so that we get the right ppid
			wait(&status);
			wait(&status);
	//now we kill process C1:
			exit(0);
		}
	}


	//if fork>0 that means that we are still in the original F, and therefore we need to fork now for C2
	//we need to create the right branch of the tree, C2 C5
	//			F
	//	       / \
	//	      /   \
	//	     C1   C2<-
	//	    /  \    \
	//	   /    \    \
	//	  C3    C4   C5<-
	else {
		pid_t C2;
		C2 = fork();
	//if we have fork<0, that means something went wrong	
		if (C2<0)
			printf("Error! \n");
	
	//if fork=0, that means that we are in the forked process, C1
		else if (C2 == 0){


	// now we need to create the children of C2
	//That's only C5:
			pid_t C5;
			C5 = fork();

	//if we have fork<0, that means something went wrong	
			if (C5<0)
				printf("Error! \n");
	

	//if fork=0, that means that we are in the forked process, C5
	//we need to do the printings here
			else if (C5 == 0){
				for(i=0; i<10; i++){
				//printf("C5:		");
					printf("Process %d is executed, my father is %d \n", getpid(), getppid());
	//the process sleeps between prints, so that the prints have intervals of 1 sec.
					sleep(1);
				}
	//before we move on to the prints for C2, we need to kill process C5:
				exit(0);
			}
	//prints for C2:		
			for(i=0; i<10; i++){
				//printf("C2:		");
				printf("Process %d is executed, my father is %d \n", getpid(), getppid());
				sleep(1);
			}
	//Before we kill process C2 we need to wait for the children processes C5 to end, so that we get the right ppid
			wait(&status);
	//now we can kill c2:
			exit(0);
		}
	}
	//As before, we can't kill F before C1 and C2 are over. so we wait for them
	wait(&status);
	wait(&status);
	exit(0);
}