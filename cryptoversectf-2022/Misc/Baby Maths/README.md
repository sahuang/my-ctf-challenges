# Baby Maths

## Description

They claimed "any preschooler can solve this Maths quiz". I doubt so.

Please round the answer you got to 5 decimal places. The flag is `cvctf{answer}`. (e.g. `cvctf{1.00000}`)

[Link](https://drive.google.com/file/d/1ufuPbjdi2x_EeQCZulm6_eHoFu-7Ag3i/view)

## Solution

Here is a brief walk through. (`v` means vector)

- From `vAO=vAB+4vAC` and the fact that `vAO=vAB+vBO`, we can get `vBO=4vAC`. This also implies `BO` is parallel to `AC`.
- Let `∠BCA=α`, `AC=x`, then `∠OBC=∠OCB=α`, `OA=OB=OC=4x`, `∠OAC=∠AOB=2α`. Since `OA=OB` we know `∠OAB=90°-α`.
- Solve triangle `OAC`, we can get the value of `α` using cosine law.
- `sin(∠BAC)=sin(90°+α)=cos(α)` is the answer.

Flag: `cvctf{0.75000}`