//To print reverse of a string
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char isAlphabet(char x)
{
    return ((x >= 'A' && x <= 'Z') || (x >= 'a' && x <= 'z'));
}
 
void reverse(char str[])
{
    int r = strlen(str) - 1, l = 0;
    while (l < r) {
        if (!isAlphabet(str[l]))
            l++;
        else if (!isAlphabet(str[r]))
            r--;
        else {
            char temp = str[l];
            str[l] = str[r];
            str[r] = temp;
            l++;
            r--;
        }
    }
}
int main()
{
	char s[50];
	gets(s);
	reverse(s);
	printf("%s",s);
}
