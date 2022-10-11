#include <iostream>
#include <vector>
#include <string>
#define MAX 10000000
using namespace std;

const string welcome =
    "    ______           __             __  __                              \n"
    "   / ____/________ _/ /_____  _____/ /_/ /_  ___  ____  ___  _____      \n"
    "  / __/ / ___/ __ `/ __/ __ \\/ ___/ __/ __ \\/ _ \\/ __ \\/ _ \\/ ___/ \n"
    " / /___/ /  / /_/ / /_/ /_/ (__  ) /_/ / / /  __/ / / /  __(__  )       \n"
    "/_____/_/   \\__,_/\\__/\\____/____/\\__/_/ /_/\\___/_/ /_/\\___/____/  \n";

const string special = "!#$^&*{}[]?<>_";

vector<int> spf;

void sieve(int n) {
    spf.resize(n+1);
    for (int i = 2; i <= n; ++i) {
        spf[i] = i;
    }
    for (int i = 2; i * i <= n; ++i) {
        if (spf[i] != i) continue; // skip if `i` is not a prime number
        for (int j = i * i; j <= n; j += i) {
            if (spf[j] == j) {
                spf[j] = i;
            }
        }
    }
}

vector<int> getFact(int n) {
    vector<int> factors;
    while (n > 1) {
        factors.push_back(spf[n]);
        n /= spf[n];
    }
    return factors;
}

inline bool isU(char c) {
    return (c >= 'A' and c <= 'Z');
}

inline bool isL(char c) {
    return (c >= 'a' and c <= 'z');
}

inline bool isN(char c) {
    return (c >= '0' and c <= '9');
}

inline bool isA(char c) {
    return isU(c) or isL(c);
}

inline bool isSp(char c) {
    return special.find(c) != string::npos;
}

inline bool isValid(char c) {
    return isA(c) or isSp(c) or isN(c);
}

bool check(vector<int>& nums, const int chance, const int n) {
    for (auto i = 0; i < n; ++i) {
        // Do some division..
        nums[i] /= chance;
    }
    for (auto i = 0; i < n; i++) {
        const auto& res = getFact(nums[i]);
        switch (i) {
            case 0 :
                if (res.size() != 2 || res[0] != 5 || res[1] != 5 * res[0] - 2) return false;
                break;
            case 1 :
                if (res != vector<int>{7, 7}) return false;
                break;
            case 2 :
                if (res.size() != 2 || res[0] != 3 || res[1] != 17) return false;
                break;
            case 3 :
                if (res != vector<int>{2, 43}) return false;
                break;
            case 4 :
                if (res != vector<int>{3, 17}) return false;
                break;
            case 5 :
                if (res.size() != 2 || res[0] * res[1] != 95) return false;
                break;
            case 6 :
                if (res != vector<int>{2, 2, 2, 2, 3}) return false;
                break;
            case 7 :
                if (res.size() != 3 || res[0] != 2 || res[1] != 3 || res[2] + 1 != res[0]*res[1]*res[1]) return false;
                break;
            case 8 :
                if (res != vector<int>{5, 19}) return false;
                break;
            case 9 :
                if (res.size() != 3 || res[2] != 19 || res[0] != res[1]) return false;
                break;
            case 10 :
                if (res.size() != 2 || res[0] != res[1] || res[1] != 7) return false;
                break;
            case 11 :
                if (res != vector<int>{2, 3, 17}) return false;
                break;
            case 12 :
                if (res != vector<int>{3, 17}) return false;
                break;
            case 13 :
                if (res != vector<int>{3, 11}) return false;
                break;
            default:
                return false;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cout << welcome << endl;
    cout << "You have 10 chances to guess the flag!" << endl;
    sieve(MAX);
    int chance = 10;

    while (chance--) {
        cout << "Input your guess: " << endl;
        string input;
        cin >> input;
        if (input.length() != 14) {
            cout << "Huh, you even got the length wrong..." << endl;
            continue;
        }

        bool valid = true;
        for (const auto& c : input) {
            if (!isValid(c)) {
                valid = false;
                break;
            }
        }

        if (!valid) {
            cout << "Sorry, your input is invalid." << endl;
            continue;
        }

        int n = input.length();
        vector<int> numbers;
        for (const auto& c : input) {
            numbers.push_back(chance * int(c));
        }

        if (check(numbers, chance, n)) {
            cout << "Yay, you found the flag!" << endl;
            return 0;
        } else {
            cout << "Nah, try again!" << endl;
        }
    }

    cout << "You failed all 10 attempts, good luck next time!" << endl;
    return 0;
}