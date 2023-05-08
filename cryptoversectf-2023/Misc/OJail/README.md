# OJail

## Description

Heard people like OCaml, unfortunately Plaid CTF didn't put one. Here's a simple one for you to learn its syntax.

## Solution

```bash
let files = Sys.readdir ".";;
# val files : string array = [|"secret"; "Dockerfile"; "flag.txt"; "build.sh"|]]
let channel = open_in "flag.txt";;
# val channel : in_channel = <abstr>
while true do
  let line = input_line channel in
  print_endline line
done;;
# The real flag is not here...
# Exception: End_of_file.

let files = Sys.readdir "./secret";;
# val files : string array = [|"flag-1d573e0faa99.json"|]
let channel = open_in "./secret/flag-1d573e0faa99.json";;
# val channel : in_channel = <abstr>
while true do
  let line = input_line channel in
  print_endline line
done;;
# {
#     "message": "Flag is here. OCaml syntax is easy, right?",
#     "flag": "cvctf{J41L3d_OOOO-C4mL@@}"
# }
# Exception: End_of_file.
```