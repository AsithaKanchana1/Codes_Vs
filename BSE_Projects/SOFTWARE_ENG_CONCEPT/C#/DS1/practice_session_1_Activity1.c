Question No: 1
#include <stdio.h>

int main() {
   
    int age = 21;
       
    printf("Sandaruwan");
    printf("\nAge: %d", age);

    return 0;
}


Question No:2
#include <stdio.h>

int main()
{
    int fnumber;
    printf("what are the 5 most favourite numbers (provide it without space)? ");
    scanf("%d\n" , &fnumber);
    printf("value : %d\n ", fnumber);
    printf("after value : %d\n ", ++fnumber);
    fnumber--;
    printf("after value : %d ", --fnumber);
    return 0;
}


Question No:3
#include <stdio.h>

int main() {
    //s number=S23010526 
    int total = 2+3+0+1+0+1+6+7;    
    
    int userInput;
    printf("Enter an integer value: ");
    scanf("%d", &userInput);

    if (userInput >= total) {
        printf("The value you entered is greater than or equal to the total value\n");
    } else {
        printf("The value you entered is less than the total value\n");
    }

    return 0;
}