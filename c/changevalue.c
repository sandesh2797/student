#include<stdio.h>

void main()
{
    const int a=10;
    int *p;
    p=&a;

    printf("value of a is %d",a);

    *p=20;

    printf("now value of a is %d",*p) ;
}