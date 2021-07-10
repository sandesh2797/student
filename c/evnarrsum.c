#include<stdio.h>
int main()
{
    int a[6]={12,44,47,55,2,3};
    int sum=0,i;
    for(i=0;i<6;i++)
    {
        if(i%2==0)
        sum=sum+a[i];
    }
    printf("the addition is = %d",sum);
}