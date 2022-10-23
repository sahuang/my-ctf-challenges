#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <cuda_runtime.h>
#include "calc.h"
#include "dev_array.h"
#include <math.h>

using namespace std;

int main()
{
    // Perform matrix multiplication C = A*B
    // where A, B and C are NxN matrices
    int N = 4;
    int SIZE = N * N;

    // Allocate memory on the host
    vector<float> h_A(SIZE);
    vector<float> h_B(SIZE);
    vector<float> h_C(SIZE);

    // Read flag
    string flag;
    cout << "Enter flag: ";
    cin >> flag;
    if (flag.length() != SIZE) {
        exit(1);
    }

    // Initialize matrices on the host
    int curr = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            h_A[i * N + j] = flag[curr];
            h_B[i * N + j] = curr++;
        }
    }

    h_B[0]++;
    h_B[3]+=2;
    h_B[5] += 2;
    h_B[6] += 3;
    h_B[10] += 1;
    h_B[14] += 5;

    // Allocate memory on the device
    dev_array<float> d_A(SIZE);
    dev_array<float> d_B(SIZE);
    dev_array<float> d_C(SIZE);

    d_A.set(&h_A[0], SIZE);
    d_B.set(&h_B[0], SIZE);

    matrixMultiplication(d_A.getData(), d_B.getData(), d_C.getData(), N);
    cudaDeviceSynchronize();

    d_C.get(&h_C[0], SIZE);
    cudaDeviceSynchronize();

    vector<vector<int>> res{ 
        {2755,3324,4553,4150},
        {2534,3087,4271,3863},
        {1828,2145,2903,2739},
        {2436,2830,3926,3490} };

    // cvctf{CuD4_B@@M}
    for (int ROW = 0; ROW < N; ROW++) {
        for (int COL = 0; COL < N; COL++) {
            if ((int)h_C[ROW * N + COL] != res[ROW][COL]) exit(1);
        }
    }

    cout << "Congratulations!\n";

    return 0;
}