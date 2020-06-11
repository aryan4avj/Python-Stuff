#include<stdio.h>
int main()
{
	//your code here
	int n1,n2,n3,n4,i,j,k,sum=0;
    scanf("%d %d",&n1,&n2);
    
    int mat1[n1][n2];
    for(i=0;i<n1;i++)
    {
        for(j=0;j<n2;j++)
        {
            scanf("%d ",&mat1[i][j]);
        }
        printf("\n");
    }
    
    scanf("%d %d",&n3,&n4);
    int mat2[n3][n4],mat3[n2][n3];
    
   
    for(i=0;i<n3;i++)
    {
        for(j=0;j<n4;j++)
        {
            mat3[i][j]=0;
        }
        
    }
    
    if(n2!=n3)
    {
        printf("\n -1");
        
    }
    else
    {
         for(i=0;i<n3;i++)
    {
        for(j=0;j<n4;j++)
        {
            scanf("%d ",&mat2[i][j]);
        }
            printf("\n"); 
    }
    
        
        for (i=0;i<n1;i++) 
        {
        for (j=0;j<n4;j++) 
        {
            for (k=0;k<n3; k++) 
            {
                sum += mat1[i][k] * mat2[k][j];
            }
            mat3[i][j]=sum;
            sum=0;
        }
            
    }

    
    }
    
    
    for(i=0;i<n1;i++)
    {
        for(j=0;j<n4;j++)
        {
            printf("%d ",mat3[i][j]);
        }
        printf("\n");
    }
    return 0;
}
