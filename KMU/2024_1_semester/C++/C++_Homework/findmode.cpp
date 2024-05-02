#include <iostream>

int findFrequency(const int arr[], int length, int an) {
    int count = 0;
    for (int i = 0 ; i <length ; ++i) {
        if (arr[i] == an) {
            ++count;
        }
    }
    return count;
}

int findMode(const int arr[], int length, int maxFrequency){
    int mode = arr[0];
    maxFrequency = findFrequency(arr, length, mode);

    for (int i = 1; i <length; ++i) {
        int frequency = findFrequency(arr,length, arr[i]);
        if (frequency > maxFrequency) {
            maxFrequency = frequency;
            mode = arr[i];
        }
    }
    return mode;
}

int main() {
    int numbers[] = {1,2,3,3,3,4,4};
    int length = sizeof(numbers) / sizeof (numbers[0]);
    int maxFrequency;
    int mode = findMode(numbers,length,maxFrequency);

    std::cout << "The mode is" << mode << "and it appears" << maxFrequency << "times /n";
}