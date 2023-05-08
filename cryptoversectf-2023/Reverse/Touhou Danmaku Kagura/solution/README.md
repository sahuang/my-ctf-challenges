# Writeup

We are provided with a Danmaku game where player will control Reimu to avoid the bullets - game will be over if Reimu collides with the bullets. Assuming you have really good STG skills, you will soon realize after many minutes the game is still going on without any flag being displayed. Well, this is a reverse engineering challenge so obviously you cannot get flag just by playing.

Checking strings, we see it is a python compiled exe. Therefore we can use the right Python version with `pyinstxtractor` to extract the source code.

```bash
PS > Python37-32\python.exe .\pyinstxtractor.py .\Main.exe
PS > .\uncompyle6.exe .\Main.exe_extracted\Main.pyc
```

This gives us the source code. Inspecting the code, we see a few places that can be hacked and skipped:

```py
while isGameRunning and time.time() - start <= 1800:
```

We change 1800 to 1 to skip the time limit.

```py
if isGameRunning:
```

We need to change `if` to `while` because otherwise we will directly exit the game. If we load the game again with this Python script, we see a bunch of binary bits being displayed after a few seconds. The bits will go out of screen. Checking the code, we see the bullet is either displaying 1 or 0 from:

```py
# Display "1"
dx += 62
bullet(dx, dy)
for _ in range(42):
    bulletsY[(-1)] += 1
    loadBullet(bulletsX[(-1)], bulletsY[(-1)])

# Display "0"
dx += 62
bullet(dx, dy)
for _ in range(30):
    bulletsX[(-1)] -= 1
    bulletsY[(-1)] += 1
    loadBullet(bulletsX[(-1)], bulletsY[(-1)])

for _ in range(30):
    bulletsX[(-1)] += 1
    bulletsY[(-1)] += 1
    loadBullet(bulletsX[(-1)], bulletsY[(-1)])

for _ in range(30):
    bulletsX[(-1)] += 1
    bulletsY[(-1)] -= 1
    loadBullet(bulletsX[(-1)], bulletsY[(-1)])

for _ in range(30):
    bulletsX[(-1)] -= 1
    bulletsY[(-1)] -= 1
    loadBullet(bulletsX[(-1)], bulletsY[(-1)])
```

So we can just statically count the occurrance of above logic in code. (Or, you can change coordinate and let all digits be displayed on screen and count them manually.)

The final binary string is `11000111110110110001111101001100110111101110100100110011100100110011011110101011110001100111111101`, or `cvctf{R3IMu<3}` when converting to ASCII every 7 bits.