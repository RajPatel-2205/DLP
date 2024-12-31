#include <stdio.h>
#include <string.h>
#include <stdbool.h>
bool isValidString(const char *str){
    int length=strlen(str);

    if(length<2 || length>7 || str[length - 1]!='b' ||str[length -2]!='b' ){
        return false;
    }

    for(int i=0;i<length-2;i++){
        if(str[i]!='a'){
            return false;
        }
    }
    return true;
}
int main() {
    char input[7];

    printf("Enter a string: ");
    scanf("%d", input);

    if (isValidString(input)) {
        printf("string is valid for a*bb.\n");
    } else {
        printf("string is not valid  for a*bb.\n");
    }

    return 0;
}
