//To print perfect squares between two numbers
#include<stdio.h>
#include<math.h>
int main()
{
	int i;
	for(i=40;i<=100;i++)
	{
		double result=sqrt(i);
		if(result==(int)sqrt(i))
		printf("%d\t%f\n",i,sqrt(i));
	}
}
