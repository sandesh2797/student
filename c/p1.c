// swap two number using pointer

#include<stdio.h>
int main()
{
    int a,b,*p,*q,temp;
    p=&a;
    q=&b;
    printf("enter the two number");
    scanf("%d%d",&a,&b);
    printf("before swaping %d%d\n",a,b);
    temp=*p;
    *p=*q;
    *q=temp;
    printf("after swaping %d%d\n",*p,*q);
}