#include<stdio.h>
int main()
{
    int n,i,limit,sum=0;
    printf("enter the limit");
    scanf("%d",&limit);
        for(i=0;i<=limit;i++)
        {
            for(i=1;i<=n/2;i++)
            {
                if(n%i==0)
                {
                   sum=sum+i;
                }
                if(n==sum)
                printf("perfect number");
            }
            
            
            
        }
}