#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>
#include <time.h>
void signalhandler(int Signal){
	/*if ( Signal == SIGCONT)
		printf("I handled a cont\n");
	if ( Signal == SIGUSR1)
		printf("I handled a usr1\n");*/
	return;
}
void timestamp() {
  time_t t;
  time(&t);
  printf("the time is %s", ctime(&t));
}

int main(int argc, char **argv){
	printf("=============================================================================================\n");
	int status;
	int order [5];
	for(int i = 1; i<argc; i++){
		order[i-1] = atoi(argv[i]);
	}
	pid_t F = getpid();
	pid_t C;
	int children_pid [5];
	for (int i=0; i<5; i++){
		C = fork();
		if(C<0) printf("oops!");
		else if (C>0) 
			children_pid[i] = C;
		else {
			signal(SIGCONT, signalhandler);
			if(i==4) 
				kill(getppid(), SIGUSR1);
			pause();
			int counter = 1;
			//printf("I got here\n");
			for(;;){
				printf("Child%d, process ID %d, is executed (%d)\n", i+1, getpid(), counter);
				sleep(1);
				counter++;
				if (counter>15)
					break;
			}
			exit(0);
		}
	}
	signal(SIGUSR1, signalhandler);
	pause();
	/*for (int i=0; i<5; i++){
		printf("    %d   ",i+1);
	}
	printf("\n");
	for (int i=0; i<5; i++){
		printf("    %d   ",order[i]);
	}

	printf("\n");
	for (int i=0; i<5; i++){
		printf("%d   ",children_pid[i]);
	}
	printf("\n");
	for (int i=0; i<5; i++){
		printf("%d   ",children_pid[order[i]-1]);
	}
	printf("\n");
	printf("F: %d\n", F);
	for (int i=0; i<5; i++){
		printf("C%d has pid %d \n",i+1,children_pid[i]);
	}*/
	//timestamp();
	for(int i=0; i<4; i++){
		for(int j=0; j<5; j++){
			kill(children_pid[order[j]-1], SIGCONT);
			sleep(3);
			kill(children_pid[order[j]-1], SIGSTOP);
		}
	}
	//timestamp();
	for(int j=0; j<5; j++){
		kill(children_pid[order[j]-1], SIGTERM);
	}
	exit(0);
}





