# Boost Game

## Description

Can you pass the `boost` game?

## Solution

I have been using [boost C++ library](https://www.boost.org/) for a long time as part of my work, so I decided to make a challenge about it.

Reversing it is quite standard, you can solve statically by loading in IDA and check the decompiled code. Afterall, the challenge is about fixed RNG generator.

Source code:

```cpp
#include <iostream>
#include <fstream>
#include <ctime>
#include <vector>
#include <map>
#include <string>
#include <stdio.h>
#include <stdlib.h>

#include <boost/range/irange.hpp>
#include <boost/random/linear_congruential.hpp>
#include <boost/random/uniform_int.hpp>
#include <boost/random/uniform_real.hpp>
#include <boost/random/variate_generator.hpp>
#include <boost/generator_iterator.hpp>

using namespace std;
typedef boost::minstd_rand base_generator_type;

constexpr int MODDER = 1333337;

vector<int> span(base_generator_type& generator)
{
    typedef boost::uniform_int<> distribution_type;
    typedef boost::variate_generator<base_generator_type&, distribution_type> gen_type;
    gen_type custom(generator, distribution_type(1, 114514));

    boost::generator_iterator<gen_type> gene(&custom);
    vector<int> res(1337, 0);
    for (int i = 0; i < 1337; i++) {
        res[i] = *gene++;
    }
    return res;
}

int getResult(const vector<int>& v, int s) {
    int curr = 0;
    for (int i : boost::irange(s, 1337, 7)) {
        curr += v[i];
        curr %= MODDER;
    }
    return curr;
}

int main()
{
    base_generator_type generator(42);
    generator.seed(static_cast<unsigned int>(0));
    const auto& res = span(generator);

    int inp;
    string flag = "";
    for (auto i : boost::irange(1, 100, 20)) {
        cout << getResult(res, i) << endl;
        cin >> inp;
        if (inp != getResult(res, i)) return 1;
        flag += to_string(getResult(res, i));
    }

    cout << "Congrats, flag is: cvctf{" << flag << "}" << endl;
    return 0;
}
```

Get flag:

```
> .\Challenge.exe
232665
1332123
7300
1060456
1282900
Congrats, flag is: cvctf{2326651332123730010604561282900}
```