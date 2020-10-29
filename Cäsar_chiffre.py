abc=[chr(x)for x in range(65,91)]
chiffre=list(abc)
def rotate_list(liste,n):
    if n<1: return
    if n>26: n=n%26
    for i in range(n):
        liste.insert(0,liste.pop())
    return liste
klartext=input("Geben sie einen String ein: ")
try:
    verschiebung=int(input('Geben sie die Verschiebung an: '))
except:
    print('Falsche Eingabe')
words=klartext.split(' ')
chipher=rotate_list(chiffre,verschiebung)
print(chipher)
codetext=[]
for word in words:
    word=word.upper()
    code=''
    for l in word:
        code+=chipher[abc.index(l)]
    codetext.append(code)
print(' '.join(codetext))