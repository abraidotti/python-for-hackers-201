#include "pch.h"
#include<stdio.h>

extern "C"
{
    _declspec(dllexport) void hello()
    {
        puts("hello from the dll");
    }
    _declspec(dllexport) int length(char* input)
    {
        return strlen(input)
    }
    _declspec(dllexport) int add(int a, int b)
    {
        return a + b;
    }
    _declspec(dllexport) void add_p(int* a, int* b, int* result)
    {
        *result = *a + *b;
    }
}
