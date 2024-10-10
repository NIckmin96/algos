#include <stdio.h>
#define LEN_INPUT 11

int main(void) {
    int idx=0;
    char s1[LEN_INPUT];
    scanf("%s", &s1);
    while (s1[idx])
    {
        printf("%c \n", s1[idx]); // 문자열 하나 출력할때는 %c로!!
        idx++;
    }

    return 0;
}
