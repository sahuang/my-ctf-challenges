## Solution

### Easier way

Checking IDA decomp, we can see the final flag is checked char by char:

```cpp
  for ( k = 0; ; ++k )
  {
    v17 = k;
    if ( v17 >= std::vector<int>::size(v35) )
      break;
    v18 = *(char *)std::string::operator[](v37, k);
    v19 = *(_DWORD *)std::vector<int>::operator[](v35, k) ^ v18;
    if ( v19 != *(_DWORD *)std::vector<int>::operator[](&secret, k) )
    {
      v20 = std::operator<<<std::char_traits<char>>(&std::cout, "Sorry.");
      std::ostream::operator<<(v20, &std::endl<char,std::char_traits<char>>);
      exit(0);
    }
  }
```

We can patch the `ptrace` check and then hook here and get the values. In fact we have `flag[i] ^ v35[i] = secret[i]` and since we would know `v35` and `secret` we then calculate `flag = secret ^ v35`.

### Harder way

Statically analyse the `v35` generation logics, which involves a lot of modular arithmetics and lambda functions. Check source code for details.

### Flag

`vsctf{fUnC710N4L_0p_w_Competitive_Prog_TEMPLATES?}`