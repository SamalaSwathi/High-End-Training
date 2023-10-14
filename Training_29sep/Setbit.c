#include<stdio.h>
int main()
{
	int a,count=0;
	scanf("%d",&a);
	/*while(a>0)
	{
		if(a&1)
		count++;
		a=a>>1;
	}*/
	while(a)
	{
		count++;
		a=a&(a-1);
	}
	printf("Count setbits :%d ",count);
}
