#include<stdio.h>
main()
{
int n,i,sum=0;
printf("enter the number");
scanf("%d",&n);
for(i=0;i<=n;i++)
{
sum=sum+i;
}
printf("sum of %d is %d",n,sum);
}
