dics = {'a':'£',
        'b':'*',
        'c':'%',
        'd':'&',
        'e':'>',
        'f':'<',
        'g':'!',
        'h':')',
        'i':'"',
        'j':'(',
        'k':'@',
        'l':'a',
        'm':'b',
        'n':'c',
        'o':'d',
        'p':'e',
        'q':'f',
        'r':'g',
        's':'h',
        't':'i',
        'u':'j',
        'v':'k',
        'w':'l',
        'x':'m',
        'y':'n',
        'z':'o'}

while True:
    message = input("enter message ")
    encrypt = ""
    for m in message.strip():
        encrypt +=dics[m]
    print (encrypt)

