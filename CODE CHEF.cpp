#include<stdio.h>
int main()
{
	int t;
	scanf("%d", &t);
	for(int i=0;i<t;i++)
	{
		int a,b,c,x,y;
		int ans =0;
		scanf("%d %d %d %d %d", &a,&b,&c,&x,&y);
		for(int i=0;i<a;i++)
		{
			if (b+i == x && c+a-i == y)
			{
				ans++;
			}
			if (b+i == y && c+a-i == x)
			{
				ans++;
			}
			if (b+a-i == x && c+i == y)
			{
				ans++;
			}
			if (b+a-i == y && c+i == x)
			{
				ans++;
			}
		}
		for(int i=0;i<b;i++)
		{
			if (a+i == x && c+b-i == y)
			{
				ans++;
			}
			if (a+i == y && c+b-i == x)
			{
				ans++;
			}
			if (a+b-i == x && c+i == y)
			{
				ans++;
			}
			if (a+b-i == y && c+i == x)
			{
				ans++;
			}
		}
		for(int i=0;i<c;i++)
		{
			if (a+i == x && b+c-i == y)
			{
				ans++;
			}
			if (a+i == y && b+c-i == x)
			{
				ans++;
			}
			if (a+c-i == x && b+i == y)
			{
				ans++;
			}
			if (a+c-i == y && b+i == x)
			{
				ans++;
			}
		}
		if (ans>0)
		{
			printf("YES");
		}HIII
		else
		{
			printf("NO");
		}
	}
}
