#include <stdio.h>

int main() {

	//string array
	char *users[] ={"user1", "user2", "user3"};
	
	//for loop to print each user in their own line
	for (int i=0; i<3; i++){
		printf("%s\n", users[i]);
	}


	int a=2;
	int b=2;
	int c=a+b;
	printf("C says: hello world\n");
	printf("%d +%d = %d\n", a,b,c);

	return 0;
}
