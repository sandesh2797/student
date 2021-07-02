#include<stdio.h>
void main()
{
int i,sum=0,n;

printf("enter the first number");
scanf("%d",&n);
for(i=1; i<=n; i++)
{
sum=sum+i;

}
printf("the sum of  %d is %d ",sum);
}
