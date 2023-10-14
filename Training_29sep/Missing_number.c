//To print 1 missing number in an array
#include<stdio.h>
int main()
{
	int n,i=0,x=0;
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(i=0;i<=n;i++)
	x=x^i;
	for(i=0;i<n-1;i++)
	x=x^a[i];
	printf("%d",x);
}
