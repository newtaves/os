// Write a program to calculate sum of n numbers using Pthreads. 


#include <iostream>
#include <pthread.h>
using namespace std;

int sum1 = 0;   // Sum computed by thread 1
int sum2 = 0;   // Sum computed by thread 2
int *arr;       // Input array
int sizeArr;    // Size of the array

// Thread function
void* runner(void *arg) {
    int id = *(int*)arg;

    if (id == 0) {
        // Thread 1: sum first half
        for (int j = 0; j < sizeArr / 2; j++)
            sum1 += arr[j];

        cout << "Sum computed by thread 1: " << sum1 << endl;
    } 
    else {
        // Thread 2: sum second half
        for (int j = sizeArr / 2; j < sizeArr; j++)
            sum2 += arr[j];

        cout << "Sum computed by thread 2: " << sum2 << endl;
    }

    return NULL;
}

// Input function
void input() {
    cout << "Enter Size of the array: ";
    cin >> sizeArr;

    arr = new int[sizeArr];

    cout << "Enter Array Elements:\n";
    for (int i = 0; i < sizeArr; i++) {
        cout << "arr[" << i << "]: ";
        cin >> arr[i];
    }
}

int main() {
    pthread_t t1, t2;
    int tNum1 = 0, tNum2 = 1;

    input();

    // Creating two threads
    pthread_create(&t1, NULL, runner, &tNum1);
    pthread_create(&t2, NULL, runner, &tNum2);

    // Waiting for threads to complete
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    cout << "\nFinal Sum = " << sum1 + sum2 << endl;

    return 0;
}
