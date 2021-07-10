#include<stdio.h>
main()
{
int n,cube,sum=0,temp,r;
printf("enter the nuber");
scanf("%d",&n);
while(n>0)
{
r=n%10;
cube=r*r*r;
sum=sum+cube;
n=n%10;
}
n=temp;
if(n==sum)
printf("this is armstrong");
else
printf("not armstrong");

}
