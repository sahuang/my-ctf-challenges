# Solution

## Setup

`passCheck.c` is compiled by Emscripten to `passCheck.js` and `passCheck.wasm`. Command: `emcc passCheck.c -o passCheck.js -s EXPORTED_FUNCTIONS="['_checker']" -s EXPORTED_RUNTIME_METHODS=ccall,cwrap -s EXPORT_ES6=1 -s MODULARIZE=1 -s ALLOW_MEMORY_GROWTH=1`.

As we can see from source code, we need to rotate the number locks to the correct position to unlock the locker. `checker` functions is what we need to understand.

## Initial Analysis

Here's the check logic:

```js
const password_checker = mod.cwrap('checker', 'boolean', ['string', 'string', 'number']);
let queryString = new URLSearchParams(window.location.href.split('?').length > 1 ? window.location.href.split('?')[1] : 'placeholder');
let params = Array.from(queryString.entries());

if (params.length > 5 && params[0][0] == "r3v3r53" &&
    password_checker(comboArray.join(""), params[0][1], comboArray.length)) {
  // Render the flag
  console.log("Your flag is: cvctf{" + comboArray.join("") + params[0][1] + "}");
}
```

We are expected to provide a URL which has more than 5 parameters, and the first parameter has key `r3v3r53`. Then, the `checker` function will be called with locker password and parameter value.

## WASM Analysis

We can decompile `passCheck.wasm` with `wabt`. I used `wasm-decompile.exe` and the result is in C-like syntax. Depending on your tool, the output might be different.

`export function checker(a:int, b:int, c:int):int` This is the main function we need to understand. At the start, a loop is called from index 0 to 8. Essentially, input hex string is converted to a number array from 0 to 15.

Then, we can see many statements like `if (..) goto ..;`, which is to check if the condition is satisfied, else checker will return false. We need to go through all checks and get the correct input. The process takes some work, I will skip the details but you can compare the decompiled code with the original C code.

In the end, we can get the final password: `b203d77e`, and URL input: `@Tm`. Feeding password to the website with url `https://safe-locker-2-51057538e91e.surge.sh/?r3v3r53=@Tm&a=1&b=1&c=1&d=1&e=1` gives a "FLAGGED" output.

Console shows the flag: `cvctf{b203d77e@Tm}`.