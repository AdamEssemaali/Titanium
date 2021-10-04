#include <stdio.h>
#include <iostream>


void tiWriteLine(const char* text)
{
    printf("%s\n", text);
}

void tiWrite(const char* text)
{
    printf(text);
}

char* tiReadLine()
{
    char* final;
    printf("\n");
    std::cin >> final;
    return final;
}

