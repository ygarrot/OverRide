#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	if (argc > 1)
		printf("%s = %p\n", argv[1], getenv(argv[1]));
}