#include <iostream>
int cal(int arr[], int size){
    int sum = 0;
    for (int i=0; i<size; ++i) {
        if (arr[i]%2!=0){
            sum+=arr[i];
        }
    }
    return sum;
}
int main(int argc, char *argv[]){
    int arr[]{1,2,3,4,5};
    int size = sizeof(arr)/sizeof(arr[0]);
    std::cout<<"odd sum = "<<cal(arr,size)<<"\n";
}