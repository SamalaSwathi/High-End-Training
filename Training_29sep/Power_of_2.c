//To check whether a number is power of 2 or not
#include<stdio.h>
int main()
{
	int n,count=0;
	scanf("%d",&n);
	while(n)
	{
		count++;
		n=n&(n-1);
	}
	if(count==1)
	printf("Yes");
	else
	printf("No");
}
