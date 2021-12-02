#include <stdio.h> 

#define GET getchar()

int readInp(char *val, int *num)
{
	if((*val = GET) == EOF)
		return 0;

	while(GET != ' ');
	scanf("%d", num);
	GET;
	return 1;
}

int main()
{
	int n = 0;
	int ai = 0;
	int r[4] = { 0, 0, 0, 0 };
	char c;
	while(readInp(&c, &n))
	{
		switch(c)
		{
			case 'f':
				r[0] += n;
				r[2] += n;
				r[3] += ai * n;
				break;
			case 'u':
				r[1] -= n;
				ai -= n;
				break;
			default:
				ai += n;
				r[1] += n;
		}
	}
	printf("%d\n%d",r[0] * r[1], r[2] * r[3]);
	return 0;
}