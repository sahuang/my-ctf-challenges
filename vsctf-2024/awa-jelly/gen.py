flag = "J3lly_0oooosHii11i_awawawawaawa!"
shuf = "1o1i_awlaw_aowsay3wa0awa!iJlooHi" # input flag should give this output
awaflag = open("awawa.txt", "w")

# lookup table containing the AwaSCII coding
lookup = "AWawJELYHOSIUMjelyhosiumPCNTpcntBDFGRbdfgr0123456789 .,!'()~_/;\n"

# never forget the leading awa
ans = "awa"

def print_string(flag, submerge=None):
    if submerge is not None:
        submerge += [0] * (len(flag) - len(submerge))
    flag = flag[::-1]
    output = ""
    for u in range(len(flag)):
        c = flag[u]
        awascii_code = lookup.index(c)
        binary_awascii = format(awascii_code if awascii_code < 32 else (awascii_code - 31), '#010b')[5:]

        awascii = binary_awascii.replace("0", " awa").replace("1", "wa")
        awascii = " awa awawa awawa awa awa awa" + awascii

        if awascii_code > 31:
            binary_awascii_2 = format(31, '#010b')[5:]
            added_awascii = binary_awascii_2.replace("0", " awa").replace("1", "wa")
            added_awascii = " awa awawa awawa awa awa awa" + added_awascii
            awascii += added_awascii + " awawa awawawa"
        
        output += awascii
        if submerge is not None:
            output += submerge_bottom(submerge[u])
    output += " awa awa awa awawa" * len(flag)
    return output

def read(): return " awa awa awawawa"
def pop(): return " awa awawawawa"
def count(): return " awawawawawa"
def print_and_pop(): return " awa awa awawa awa" + " awa awawawawa"
def submerge_bottom(awascii_code):
    binary_awascii = format(awascii_code, '#010b')[5:]
    return " awa awawawa awa" + binary_awascii.replace("0", " awa").replace("1", "wa")


ans += read() + pop() # read flag and store in abyss
merges = [2,3,4,1,6,5,3,10,20,22,25,3,0,0] * 2 + [0, 16, 26, 31]
for i in merges:
    ans += submerge_bottom(i)
ans += " awa awa awa awawa" * len(flag)
awaflag.write(ans)