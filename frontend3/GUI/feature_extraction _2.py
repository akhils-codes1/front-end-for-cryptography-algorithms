from base64 import b64decode

def split_into_bytes(s):
    #s = bitstring
    res = []
    j = 0
    while(j<len(s)):
        try:
            res+=[s[j:j+8]]
        except IndexError:
            res+=[s[j:].zfill(8)]
        j = j+8
    return res

def feature_vector():
    f = open("ciphertext.txt","r")
    f = f.read()
    if(f[-1]=='\n'):
       f = f[:-1]
    f = f.encode('utf-8')
    f = b64decode(f)
    s = f.hex()
    a = [hex(i)[-1] for i in range(16)]
    c = [bin(i)[2:].zfill(4) for i in range(16)]
    d = {}
    for i in range(16):
        d[a[i]] = c[i]
    for i in d:
        s = s.replace(i,d[i])
    b = split_into_bytes(s)
    c = {}
    for i in range(8):
        c[i] = split_into_bytes("".join([j[i] for j in b]))
    dict256 = {}
    for i in range(256):
        dict256[bin(i)[2:].zfill(8)]=i
    x = {}
    for i in range(8):
        x[i] = [0]*256
    for i in c:
        for j in c[i]:
            x[i][dict256[j]]=1
    y = {}
    for i in range(8):
        y[i] = [str(j) for j in x[i]]
        y[i] = "".join(y[i])
    y = y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7]
    print("temp = ",y)
    return y
