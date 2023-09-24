#include <random>
#include <vector>
#include <iostream>
#include <fstream>

#include <faiss/IndexFlat.h>
#include <faiss/IndexIVFFlat.h>

using idx_t = faiss::Index::idx_t;
using namespace std;

float get_rand() {
    return (float) rand() / (float) RAND_MAX;
}

void print_flag() {
    ifstream f("./flag.txt");
    if (!f) {
        cout << "[!] Flag file not found. Please contact admin if this happens on server." << endl;
        return;
    }
    string line;
    while (getline(f, line)) {
        cout << line << endl;
    }
    f.close();
}

int main() {
    try {
        const int d = 128;     // dimension
        const int nb = 100000; // database size
        const int nq = 10;     // number of queries
        const int nlist = 100; // buckets
        const int k = 3;       // saved top k
        const int nprobe = 10; // number of buckets to search

        // random seed based on current time
        srand(time(0));

        cout << "[+] Adding vectors to the database..." << endl;

        float* xb = new float[d * nb];

        for (int i = 0; i < nb; i++) {
            for (int j = 0; j < d; j++)
                xb[d * i + j] = get_rand();
            xb[d * i] += i / 1000.;
        }

        faiss::IndexFlatL2 quantizer(d); // the other index
        faiss::IndexIVFFlat index(&quantizer, d, nlist);

        index.train(nb, xb);
        index.add(nb, xb);

        cout << "[!] Vectors added to the database." << endl;
        cout << "[+] Querying..." << endl;

        float* xq = new float[d * nq];
        for (int i = 0; i < nq; i++) {
            for (int j = 0; j < d; j++)
                xq[d * i + j] = get_rand();
            xq[d * i] += i / 1000.;
        }

        idx_t n1, n2, n3; // 3 nearest neighbors
        {
            idx_t* I = new idx_t[k * nq];
            float* D = new float[k * nq];

            index.search(nq, xq, k, D, I);

            // printf("I=\n");
            // for (int i = 0; i < nq; i++) {
            //     for (int j = 0; j < k; j++)
            //         printf("%5zd ", I[i * k + j]);
            //     printf("\n");
            // }

            for (int i = 0; i < nq; i++) {
                cout << "Query " << i+1 << " - nearest neighbour indices:" << endl;
                cout << "> ";
                cin >> n1 >> n2 >> n3;
                if (n1 != I[i * k] || n2 != I[i * k + 1] || n3 != I[i * k + 2]) {
                    cout << "[!] Wrong! Exiting..." << endl;
                    return 1;
                }
            }

            delete[] I;
            delete[] D;
        }

        cout << "[!] Querying done." << endl;
        cout << "[+] Flag: " << endl;
        print_flag();

        delete[] xb;
        delete[] xq;
        return 0;
    } catch (const std::exception& e) {
        cout << "[!] Exception occurred, exiting..." << endl;
        return 1;
    }
}