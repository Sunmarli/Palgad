from functools import reduce
from re import I

def loe_failist(file:str)->list:
    fail=open(file,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def lisamine(mas:list,file:str):
    f=open(file,'w',encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()

def element_listisse(p:list,i:list):
    n=int(input("Mitu inimesi lisame?"))
    for j in range (n):
        nimi=input("Nimi: ")
        i.append(nimi)
        palk=input("palk: ")
        p.append(palk)
    return p,i

def kustuta(nimi:str,p:list,i:list):
    n=i.count(nimi)
    pos=0
    for j in range(n):
        ind=i.index(nimi,pos)
        pos=ind
        i.remove(nimi)
        p.pop(ind)
    return p,i
def str_to_int(mas:list)->list:
    for m in mas:
        ind=mas.index(m)
        mas.pop(mas.index(m))
        m=int(m)
        mas.insert(m,ind)     
    return mas

def maximumpalk(p:list,i:list):
    p=list(map(int,p))
    max_palk=max(p)
    n=p.count(max_palk)
    pos=0
    print(f"Maksimaalne palk: {max_palk}")
    for j in range(n):    
        ind=p.index(max_palk,pos)   
        nimi=i[ind]
        print(f"{nimi}-l on maksimaalne palk")
        pos=ind+1
def miinimum(p:list,i:list):
    p=list(map(int,p))
    min_palk=min(p)
    n=p.count(min_palk)
    pos=0
    print(f"Minimaalne palk {min_palk}")
    for j in range(n):    
        ind=p.index(min_palk,pos)   
        nimi=i[ind]
        print(f"{nimi}-l on mnimaalne palk")
        pos=ind+1
