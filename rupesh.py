def p(b):
    p = ord(b)
    if (p>=65 and p<=90):
        value = p-65
    elif (p>=97 and p<=122):
        value = p-97+26
    elif (p>=48 and p<=57):
        value = p-48+52
    elif p == 43:
        value = 62
    elif p == 47:
        value = 63
    return value

def n(k):
    return '{0:06b}'.format(k)

def m(s):
    r = ''
    for i in s:
        r += n(p(i))
    return r

def r(s):
    a = []
    for i in s:
        a.append(p(i))
    return a

def g(b):
    a = []
    for i in range(len(b)):
        if(i%8==7):
            p = b[i-7:i+1]
            a.append(int(p,2))
    return a

def t(a):
    v = ''
    for i in a:
        v += chr(i)
    return v

def fi(c):
    k = ord(c)
    return '{0:08b}'.format(k)

def gi(d):
    r = ''
    for i in d:
        r += fi(i)
    return r

def mi(v):
    a = []
    for i in range(len(v)):
        if(i%6==5):
            p = v[i-5:i+1]
            a.append(int(p,2))
    return a

def pi(b):
    if(b>=0 and b<=25):
        v = b+65
    elif(b>=26 and b<=51):
        v = b-26+97
    elif(b>=52 and b<=61):
        v = b-52+48
    elif(b==62):
        v = 43
    elif(b==63):
        v = 47
    return chr(v)

def qi(a):
    v = ''
    for i in a:
        v += pi(i)
    return v

print qi(mi(gi('madras')))

print t(g(m('Y3Jvc3MgdGhpcyBpbnRlcm5zaGlwIGdyYXBoIGFsZ29yaXRobXMgYmxhY2sgYnVjayB0aGlydGVlbiBzdW1tZXIw')))
