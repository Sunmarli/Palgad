
from Oma_moodul import *

while True:
    print("0-loe failist\n1-andmete lisamine\n2-salvestame failisse\n3-Kustuta\n 4-Maksimaalne palk\n5-Minimaalne  ")
    v=int(input())
    if v==0:
        palgad=[]
        inimesed=[]
        palgad=loe_failist("palgadefail.txt")
        inimesed=loe_failist("inimesed.txt")
        print(palgad)
        print(inimesed)
    elif v==1:
        palgad, inimesed=element_listisse(palgad,inimesed)
        print(palgad)
        print(inimesed)
    elif v==2:
        lisamine(palgad,"palgadefail.txt")
        lisamine(inimesed,"inimesed.txt")
    elif v==3:
        palgad,inimesed =kustuta(input("Keda kustutada? "),palgad,inimesed)
    elif v==4:
        maximumpalk(palgad,inimesed)
    elif v==5:
        miinimum(palgad,inimesed)