#include<stdio.h>
main()
{
int n,count=1,i;
printf("enter the number");
scanf("%d",&n);
for(i=1;i<=n/2;i++)
{
if(n%i==0)
{
count ++;
}
}
if(count==2)
printf("it is prime number");
else
printf("not prime number");
}
