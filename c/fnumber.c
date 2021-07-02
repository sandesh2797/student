/* find factor for the given number */

#include<stdio.h>
main()
{
int n,i,f=1;
printf("enter the number");
scanf("%d",&n);
for(i=0;i<=n/2;i++)
{
if(n%i==0)
{
++f;
}
printf("count %d",f);
}
}
