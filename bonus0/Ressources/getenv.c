#include <stdlib.h>
#include <stdio.h>

int main(int ac, char **argv)
{
	if (ac > 1)
		printf("address for %s is: %p (%s)\n", argv[1], getenv(argv[1]), getenv(argv[1]));
}
