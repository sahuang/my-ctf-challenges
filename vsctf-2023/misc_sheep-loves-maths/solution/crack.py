from zipfile import ZipFile
import itertools, binascii

def permutations_with_replacement(szDic, k):
    result = []
    for i in itertools.product(szDic, repeat = k):
        result.append(''.join(i))
    return result

def multiCrack(iSize,lCrcs):
    dic = '''abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!-@_{}'''
    dResult = {}
    mydic = permutations_with_replacement(dic,iSize)
    for i in mydic:
        txt = "".join(i)
        crc = binascii.crc32(txt.encode())
        if str(crc) in lCrcs:
            print(hex(crc)+" "+txt)
            dResult[str(crc)] = txt
    return dResult

def crack(lFilesCRC):
    lResult = []
    iSizes = set([int(i.split('|')[1]) for i in lFilesCRC])
    for iSize in iSizes:
        lCrcs = [i.split('|')[2] for i in lFilesCRC if i.split('|')[1]==str(iSize)]
        dTMP = multiCrack(iSize,lCrcs)
        for k,v in dTMP.items():
            for i in lFilesCRC:
                if i.find(k)>0:
                    lResult.append(i+" "+v)
    return lResult

if __name__ == "__main__":
    myzip = ZipFile(r"Sheep loves Maths.zip")
    fInfos = myzip.filelist
    lFilesCRC = []
    for i in range(len(fInfos)):
        fInfo = fInfos[i]
        if fInfo.file_size < 5:
            lFilesCRC.append(fInfo.filename + '|' + str(fInfo.file_size) + '|' + str(fInfo.CRC))
    print(lFilesCRC)
    print(sorted(crack(lFilesCRC)))