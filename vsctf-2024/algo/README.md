## baby-game

Very simple challenge: check the manhattan distance between two points. If the distance is odd, first player wins, otherwise second player wins.

This can be proved by induction. Let the distance `d = |x1 - x2| + |y1 - y2|`.

If `d = 1`, the first player can move to the other player's point and win.

If `d = 2`, there are 2 possibilities: on corners of 2x2 grid, or on a straight line with distance 2.

For the first scenario, if the first player moves closer to the second player, `d` becomes 1 hence he loses. So he has to move away from the second player. The second player can follow/copy the first player's moves. Eventually the first player will be forced to the corner and lose.

For the second scenario it's very similar, proof is left as an exercise to the reader.

Because the parity doesn't change after 2 moves, the first player will always win if `d` is odd.

```cpp
#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, a, b, c, d;
    cin >> n >> a >> b >> c >> d;
    if ((a - b + c - d) % 2 == 1) printf("Caring Koala");
    else printf("Red Panda");
    return 0;
}
```

## baby-game-revisited

This challenge is harder than the previous version. However, we know second player can move 1 or 2 steps - which means **he can change the parity at his will**. So the first player can never win unless `d = 1` at the beginning.

To code it, we use dynamic programming. Define a 6d array `dp[x1][y1][x2][y2][u][depth]` where `x1, y1` is the first player's position, `x2, y2` is the second player's position (defined array size is `n`), `u` is the current player (0 for first, 1 for second), and `depth` is the current depth of the recursion. `depth` can be `3*n` since in worst case they cannot move more than that steps.

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 31;
const int INF = 1e9;

int dx[] = {1, 0, -1, 0, 2, 0, -2, 0};
int dy[] = {0, 1, 0, -1, 0, 2, 0, -2};
int f[2][91][N][N][N][N];

int n, a, b, c, d;

int dfs(int x, int y, int a, int b, int c, int d) {
    if (y > 3 * n) return INF;
    if (a == c && b == d) return x ? INF : 0;
    if (f[x][y][a][b][c][d]) return f[x][y][a][b][c][d];

    int ans = 0, xx, yy;
    if (x) {
        ans = INF;
        for (int i = 0; i < 8; ++i) {
            xx = c + dx[i];
            yy = d + dy[i];
            if (xx >= 1 && xx <= n && yy >= 1 && yy <= n)
                ans = min(ans, dfs(0, y + 1, a, b, xx, yy));
        }
    } else {
        for (int i = 0; i < 4; ++i) {
            xx = a + dx[i];
            yy = b + dy[i];
            if (xx >= 1 && xx <= n && yy >= 1 && yy <= n)
                ans = max(ans, dfs(1, y + 1, xx, yy, c, d));
        }
    }

    f[x][y][a][b][c][d] = ++ans;
    return ans;
}

int main() {
    cin >> n >> a >> b >> c >> d;
    if (abs(a - c) + abs(b - d) == 1) {
        cout << "Caring Koala 1" << endl;
        return 0;
    }
    cout << "Red Panda " << dfs(0, 0, a, b, c, d) << endl;
    return 0;
}
```

## quickmaffs-permutation-puzzle

Another DP problem. Code is self-explanatory.

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 1e4 + 10;
const int MOD = 1e9 + 7;

int main() {
    int n;
    cin >> n;
    
    vector<vector<int>> dp(N, vector<int>(N, 0)), sum(N, vector<int>(N, 0));
    
    dp[1][1] = sum[1][1] = 1;

    for (int i = 2; i <= n; ++i) {
        for (int j = 1; j <= i; ++j) {
            if (i % 2 == 0) {
                dp[i][j] = (sum[i-1][i-1] - sum[i-1][j-1] + MOD) % MOD;
            } else {
                dp[i][j] = sum[i-1][j-1];
            }
            sum[i][j] = (sum[i][j-1] + dp[i][j]) % MOD;
        }
    }

    cout << sum[n][n] << endl;
    return 0;
}
```
