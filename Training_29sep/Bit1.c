//to check whether the ith bit is 1 or not
#include<stdio.h>
int main()
{
	int a=15,i=4;
	if(a&(1<<(i-1)))
	printf("Yes");
	else
	printf("No");
}
