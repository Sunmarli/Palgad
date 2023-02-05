from collections import Counter
import heapq
from math import *
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

def sorteeriminekasv(p:list,inim:list):
    p=list(map(int,p))
    arg_sort = sorted(range(len(p)), key=lambda i: p[i])
    
    print([p[i] for i in arg_sort])
    print([inim[i] for i in arg_sort])


def sorteeriminekah(p:list,inim:list):
    p=list(map(int,p))
    #p=(sorted(p, reverse=True))
    arg_sort = sorted(range(len(p)), key=lambda i: p[i],reverse=True)
    print([p[i] for i in arg_sort])
    print([inim[i] for i in arg_sort]) 

def samapalk(p:list,inim:list):
    p=list(map(int,p))
    #samad= [a: p.count(a) for a in set(p) if p.count(a) > 1]
    nimi=[]
    for a in p:
        n=p.count(a)
        pos=0
        if p.count(a)>1: 
            for t in range (n):   
                ind=p.index(a,pos)
                nim=inim[ind]
                nimi.append(nim)
                pos=ind+1
    print(f"----------{p.count(a)}")
    print(f"---------{nimi}-l")

def search(p:list,inim:list):
    n=str(input("Keda otsime?\n "))
    s=inim.count(n)
    pos=0
    for i in inim:
        if i==n:
            ind=inim.index(i,pos)
            pos=ind+1
            print("Tema palk - ", p[ind])

def suuremkui(p:list,inim:list):
    n=int(input("Suurem kui ---> "))
    p=list(map(int,p))
    pos=0
    for i in p:
        if n<=i:
            ind=p.index(i,pos)
            pos=ind+1
            print(f"Suurem kui {n} on --------- {inim[ind]}")

def vaiksemkui(p:list,inim:list):
    n=int(input("Vaiksem kui ---> "))
    p=list(map(int,p))
    pos=0
    for i in p:
        if n>=i:
            ind=p.index(i,pos)
            pos=ind+1
            print(f"Vaiksem kui {n} on -------- {inim[ind]}")

def top3(p:list,inim:list):
    p=list(map(int,p))
    print("Top3 Suurt palka -- ",sorted(zip(p, inim), reverse=True)[:3])
    #print(heapq.nlargest(3, zip(p, inim)))
    print("Top3 Vaiksemat palka -- ",sorted(zip(p, inim), reverse=False)[:3])

def keskmine(p:list,inim:list):
    p=list(map(int,p))
    avg = round(sum(p) / len(p))
    print("Keskmine palk on---", avg)
    #vah=avg-avg*0.2
    #vah2=avg+avg*0.2
    pos=0
    for i in p:
        if avg-avg*0.05 <i< avg+avg*0.05:
            ind=p.index(i,pos)
            pos=ind+1
            print(f"Enam vahem keskmine palk on {p[ind]} {inim[ind]}-l") 

def tulumaks(p:list,inim:list):
    katte=[]
    p=list(map(int,p))
    for i in p:
        if i<654:
            puh=i
            katte.append(puh)
        elif 654 <=i <=1200:
            puh=654+(i-654)*0.8
            katte.append(puh)
        elif  1200<=i<2100:
            vaba=654-654/900*(i-1200)
            puh=vaba+(i-vaba)*0.8
            katte.append(puh)
        elif i>=2100:
            puh=round(i*0.8)
            katte.append(puh) 
    tulemus=list(zip(katte,inim))
    #print("Tulumaksuvaba \n",katte) 
    print(tulemus)
    
def sortbyname(p:list,inim:list): 
    
    arg_sort = sorted(range(len(inim)), key=lambda i: inim[i])
    
    print([p[i] for i in arg_sort])
    print([inim[i] for i in arg_sort]) 

def deleteloweravg(p:list,inim:list):
    p=list(map(int,p))
    avg = round(sum(p) / len(p))
    #pos=0
    for i in p:
        if i<=avg:
            ind=p.index(i)
            p.remove(i)
            inim.pop(ind)

    print(p,inim)
