//Fibonacci
#include<stdio.h>
long long int fibonacci(long long int n)
{
	if(n==0)
	return 0;
	else if(n==1)
	return 1;
	else
	return fibonacci(n-1)+fibonacci(n-2);
}
int main()
{
	long long int n,i;
	scanf("%lld",&n);
	for(i=0;i<n;i++)
	{
		printf("%lld ",fibonacci(i));
	}
}
