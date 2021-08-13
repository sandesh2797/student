#include<stdio.h>

void main()
{
    int a,b,temp,*p,*q;
    p=&a;
    q=&b;

    printf("enter the two number ");
    scanf("%d%d",&a,&b);
    printf("before swap %d %d",a,b);
    
    temp=*q;
    *q=*p;
    *p=temp;

printf("after swaping %d%d",*p,*q);
}