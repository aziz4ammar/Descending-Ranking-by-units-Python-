def saisir ():
    global n
    test=False
    while test==False:
        n=int(input("n="))
        test=(n%2!=0)and(3<=n<=21)
def remplir (t,n):
    for i in range (n):
        test=False
        while test==False:
            t[i]=int(input("t["+str(i)+"]="))
            test=(10<=t[i]<=99)and(t[i]%10!=t[i]//10)
def tribulles(t,n):
    test=False
    while test==False:
        echange=False
        for i in range (n-1):
            if(t[i]%10<t[i+1]%10):
                aux=t[i]
                t[i]=t[i+1]
                t[i+1]=aux
                echange=True
        n-=1
        test=(echange==False)or(n==1)
def afficher(t,n):
    for i in range(n):
        print(t[i],end="|")
#p.p
import numpy as np
saisir()
t=np.array([int()]*n)
remplir(t,n)
tribulles(t,n)
afficher(t,n)
