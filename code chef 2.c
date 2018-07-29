#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int n,m;
		scanf("%d %d", &n,&m);
		int a[n][m];
		for (int i=0;i<n;i++)
		{
			int in[m];
			scanf("%s",&in);
			for( int j=0;j<m;j++)
			{
				a[n][m]= in[m];
			}
		}
		char op[100];
		scanf("%s",&op);
		int opl;
		opl = strlen ( op );
		for(int i=0;i<opl;i++)
		{
			if (op[i]=='D' || op[i]=='d')
			{
				int s;
				for(int i=0;i<m;i++)
				{
					for (int i=0;i<n;i++)
					{
						if(a[n][m] == 1)
						s++;
					}
					for(int i =n-1;s>0;i--)
					{
						a[i][m]= 1;
						s--;
					}
					for(int i =0;i<n-s;i++)
					{
						a[i][m]=0;
					}
				}
			}
			if (op[i]=='U' || op[i]=='u')
			{
				int s;
				for(int i=0;i<m;i++)
				{
					for (int i=0;i<n;i++)
					{
						if(a[n][m] == 1)
						s++;
					}
					for(int i = 0;i<s;i++)
					{
						a[i][m]= 1;
					}
					for(int i =s;i<n;i++)
					{
						a[i][m]=0;
					}
				}
			}
			if (op[i]=='L' || op[i]=='l')
			{
				int s;
				for(int i=0;i<n;i++)
				{
					for (int i=0;i<m;i++)
					{
						if(a[n][m] == 1)
						s++;
					}
					for(int i =0;i<s;i++)
					{
						a[n][i]=1;
					}
					for(int i =s;i<n;i++)
					{
						a[n][i]=0;
					}
				}
			}
			if (op[i]=='R' || op[i]=='r')
			{
				int s;
				for(int i=0;i<n;i++)
				{
					for (int i=0;i<m;i++)
					{
						if(a[n][m] == 1)
						s++;
					}
					for(int i =m-1;s>0;i--)
					{
						a[n][i]=1;
						s--;
					}
					for(int i =0;i<n-s;i++)
					{
						a[n][i]=0;
					}
				}
			}
			
		} 
		for (int i=0;i<n;i++)
		{
			for(int i =0;i<m;i++)
			{
				printf("%d",a[n][m]);
			}
		}
	}
}

