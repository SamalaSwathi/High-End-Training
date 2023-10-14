//To print lonely integers in an array
#include<stdio.h>
int main()
{
	int n;
	scanf("%d",&n);
	int i=0,a[n],res=0;
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(i=0;i<n;i++)
	res=res^a[i];
	printf("%d",res);
}
