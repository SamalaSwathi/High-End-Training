//print 1 if all elements in row or coloumn or digonal is 1
//print 1 if all elements in row or coloumn or digonal is 0
#include<stdio.h>
int main()
{
	int n,i,j,k=0,k1=0,count,count1;
	scanf("%d",&n);
	int a[n][n];
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		scanf("%d",&a[i][j]);
	}
	for(i=0;i<n;i++)
	{
		count=0,count1=0;
		for(j=0;j<n;j++)
		{
		    if(a[i][j]==1)
		    count++;
		    else if(a[i][j]==0)
		    count1++;
		    if(count==n)
		    k++;
		    else if(count1==n)
		    k1++;
		}
	}
	printf("1's horizontal count:%d\n",k);
	printf("0's horizontal count:%d\n",k1);
	k=0;k1=0;
	for(i=0;i<n;i++)
	{
		count=0,count1=0;
		for(j=0;j<n;j++)
		{
		    if(a[j][i]==1)
		    count++;
		    else if(a[j][i]==0)
		    count1++;
		    if(count==n)
		    k++;
		    else if(count1==n)
		    k1++;
		}
	}
	printf("1's vertical count:%d\n",k);
	printf("0's vertical count:%d\n",k1);
	
	k=0;k1=0;count=0,count1=0;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
		    if(i==j)
		    {
		    	if(a[i][j]==1)
		    	count++;
		    	else if(a[i][j]=0)
		    	count1++;
			}
			if(count==n)
			k++;
			else if(count1==n)
			k1++;
		}
	}
	printf("1's left diagonal count:%d\n",k);
	printf("0's left diagonal count:%d\n",k1);
	
	k=0;k1=0;count=0;count1=0;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			int r=i+j;
			int y=n-1;
		    if(r==y)
		    {
		    	if(a[i][j]==1)
		    	count++;
		    	else if(a[i][j]==0)
		    	count1++;
		    }
		}
	}
	if(count==n)
	k+=1;
	if(count1==n)
	k1+=1;
	printf("1's right diagonal count:%d\n",k);
	printf("0's right diagonal count:%d\n",k1);
}
