#include <stdio.h>
int arr[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
int sumColumn[3] = {0,0,0};
int main(){
for (int i = 0; i < 3; i++){
    int sumRow = 0;
    for (int j = 0; j < 3; j++){
        printf("%d\t", arr[i][j]);
        sumRow = sumRow + arr[i][j];
        sumColumn[j] = sumColumn[j] + arr[i][j];
    }
    printf("| %d\n", sumRow);
}
printf("--------------------\n");
for (int j = 0; j < 3; j++){
    printf("%d\t", sumColumn[j]);
}
return 0;
}
