#include <stdio.h>
#include <ctype.h> // (tolower & toupper) + (islower & isupper)
#define LEN_INPUT 10

int main(void) {
    char s1[LEN_INPUT];
    int idx=0;
    scanf("%s", s1);
    while (s1[idx]){
        if (isupper(s1[idx]))
        {
            s1[idx] = tolower(s1[idx]);
        }
            
        else if (islower(s1[idx]))
        {
            s1[idx] = toupper(s1[idx]);
        }
        
        idx++;
    }
    printf("%s", s1);

    return 0;
}