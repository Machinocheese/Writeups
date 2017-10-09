#include <stdio.h>
#include <stdlib.h>

//gcc -m32 -fno-pic -no-pie -mpreferred-stack-boundary=2 lvl3.c -o lvl3

int main()
{
	char name[32];
	puts("Welcome to the No Security Aggregate");
	puts("Please sign in with your name.");
	puts("You tricked us last time with that planted pointer...we won't get fooled again.");
	gets(name);
	puts("Please take a seat, we'll be with you at some point this week.");
	return 0;
}
