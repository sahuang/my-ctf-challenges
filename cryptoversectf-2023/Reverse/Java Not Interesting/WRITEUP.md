# Solution

This is a simple Kotlin APK built with Android Studio. As title suggests, JNI is used to call native C code. Upon opening the APK in decompiler, we can see the following code:

```java
/* JADX INFO: Access modifiers changed from: private */
public static final void onCreate$lambda$0(HelloJni this$0, ActivityHelloJniBinding binding, View it) {
    Intrinsics.checkNotNullParameter(this$0, "this$0");
    Intrinsics.checkNotNullParameter(binding, "$binding");
    if (this$0.checkValid(binding.flag.getText().toString())) {
        binding.valid.setText("Correct!");
    } else {
        binding.valid.setText(binding.flag.getText().toString());
    }
}

static {
    System.loadLibrary("hello-jni");
}
```

As such, we need to reverse the logics in `hello-jni.so` lib and find the flag. We can open it in IDA decompiler and search this `checkValid` function.

```c
__int64 __fastcall Java_com_example_hellojni_HelloJni_checkValid(__int64 a1, __int64 a2, __int64 a3)
{
  int *v3; // rax
  int v5; // [rsp+Ch] [rbp-A4h]
  int v6; // [rsp+10h] [rbp-A0h]
  int j; // [rsp+14h] [rbp-9Ch]
  int i; // [rsp+18h] [rbp-98h]
  __int64 v9; // [rsp+30h] [rbp-80h]
  unsigned __int8 v10; // [rsp+57h] [rbp-59h]
  char v11[24]; // [rsp+58h] [rbp-58h] BYREF
  char v12[24]; // [rsp+70h] [rbp-40h] BYREF
  char v13[31]; // [rsp+88h] [rbp-28h] BYREF
  char v14; // [rsp+A7h] [rbp-9h] BYREF
  unsigned __int64 v15; // [rsp+A8h] [rbp-8h]

  v15 = __readfsqword(0x28u);
  if ( !a3 )
    return 0;
  v9 = _JNIEnv::GetStringUTFChars(a1, a3, &v14);
  std::string::basic_string<decltype(nullptr)>(v13, v9);
  if ( sub_21F10(v13) == 38 )
  {
    std::vector<int>::vector(v12, 31LL);
    for ( i = 0; i < 31; ++i )
    {
      v6 = (int)sub_21FB0(2LL, (unsigned int)(i % 16)) % 37 % 31;
      *(_DWORD *)sub_21FE0(v12, i) = v6;
    }
    std::string::basic_string<decltype(nullptr)>(v11, "acefghiklmnABCDGHXYZ012389_-?!~");
    for ( j = 6; j < 37; ++j )
    {
      v5 = *(char *)sub_22000(v13, j);
      v3 = (int *)sub_21FE0(v12, 7 * j % 31);
      if ( v5 != *(char *)sub_22000(v11, *v3) )
      {
        v10 = 0;
        goto LABEL_14;
      }
    }
    v10 = 1;
LABEL_14:
    std::string::~string(v11);
    sub_22030(v12);
  }
  else
  {
    v10 = 0;
  }
  std::string::~string(v13);
  return v10;
}
```

Code is not stripped. We can see that input string has a length of 38. Because it is a flag checker (as shown on APK UI by inputting text for flag check), we know it is in format `cvctf{}`. `sub_21FB0` is math power. We essentially compare middle part of flag against some constants. Write a simple python script to solve it:

```py
v12 = [i for i in range(31)]
for i in range(31):
    v12[i] = (2 ** (i % 16)) % 37 % 31
s = "acefghiklmnABCDGHXYZ012389_-?!~"
flag = "cvctf{"
for i in range(6, 37):
    flag += s[v12[7 * i % 31]]
flag += "}"
print(flag)
```

This gives `cvctf{Cgaef3-Gc_l9gacX~-GHCl9efcX~c_H}`. Feed it into the UI, it shows Correct as expected.