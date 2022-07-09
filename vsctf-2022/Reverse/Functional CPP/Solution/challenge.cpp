// g++ -O0 -std=c++14 challenge.cpp -o challenge

#include <iostream>
#include <algorithm>
#include <functional>
#include <random>
#include <time.h>
#include <vector>

using namespace std;

static unsigned long int next_int = 1;
const int arr_size = 58;
const vector<int> secret = {222, 60, 161, 197, 220, 78, 169, 208, 54, 64, 121, 82, 191, 57, 161, 196, 7, 214, 166, 117, 93, 67, 83, 225, 47, 121, 233, 160, 187, 50, 3, 165, 77, 17, 241, 118, 123, 21, 198, 43, 168, 252, 221, 54, 125, 166, 85, 197, 95, 98, 200, 150, 222, 44, 54, 20, 147, 70};

int rand(void) {
    next_int = next_int * 1103515245 + 12345;
    return (unsigned int)(next_int/65536) % 32768;
}

void srand(unsigned int seed)
{
    next_int = seed;
}

int main() {
    vector<int> input(arr_size + 3, 0);

    // generate 3 random bytes
    srand(12345);
    for (auto i = 0; i < 65537; ++i) {
        auto tmp = rand() % 256;
    }
    for (auto i = 0; i < 3; ++i) {
        input[i] = rand() % 256;
    }

    string flag;
    cout << "Your flag is either at https://www.youtube.com/watch?v=dQw4w9WgXcQ, or here: ";
    cin >> flag;

    // vsctf{1_b37_y0u_w1LL_n3v3r_u53_Func710n4L_C++_1n_ur_L1F3?}
    if (flag.length() != 58) {
        cout << "Sorry not here." << endl;
        return 0;
    }

    auto c_xor = [](int a) -> auto {
        return[a](int b) -> auto {
            return (a ^ b);
        };
    };

    auto c_addition = [](char a) -> auto {
        return[a](char b) -> auto {
            return (char)a + b;
        };
    };

    auto c_modulus = [](char a) -> auto {
        return[a](int b) -> char {
            return a % b;
        };
    };

    for (auto i = 3; i < input.size(); ++i) {
        unsigned char c = 0;
        c = c_addition(c_addition(c_addition(c)(input[i-3]))(input[i-2]))(input[i-1]);
        c = c_modulus(c)(256);
        input[i] = (int) c;
    }

    // Some functional CPP transform
    vector<int> input2(arr_size + 3, 0);
    vector<int> input3(arr_size + 3, 0);

    transform(input.begin(), input.end(), input2.begin(),
    [](int w) -> int{ return w + 3; });
    transform(input2.begin(), input2.end(), input3.begin(),
    [&](int w) -> int{ return c_xor(w)(7); });

    // XOR result
    for (auto i = 3; i < input3.size(); ++i) {
        if (((int)(flag[i-3]) ^ input3[i]) != secret[i-3]) {
            cout << "Sorry not here." << endl;
            return 0;
        }
    }

    cout << "You got it." << endl;
    return 0;
}