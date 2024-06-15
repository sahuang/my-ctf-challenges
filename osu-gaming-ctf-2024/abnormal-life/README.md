# Abnormal Life

Few people farm their own map as BP1. [I do](https://osu.ppy.sh/beatmapsets/748836#osu/1577478). That was played 6 years ago though.

Recently I retried the top difficulty and got a terrible score. At least it passed...But what happend to the life bar on the score screen?

Wrap the string in `osu{}`. Flag format is `osu{[A-Z0-9_]+}`.

## Solution

Life bar spells out flag but it is under screen because y coordinate is negative. We can parse `osr` file and move up to see the flag easily.

`osu{H1D3_UND3R}`