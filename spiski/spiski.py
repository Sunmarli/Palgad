
from Oma_moodul import *

while True:
    print("0-loe failist\n1-andmete lisamine\n2-salvestame failisse\n3-Kustuta\n 4-Maksimaalne palk\n5-Minimaalne\n6 Sorteerimine\n7 Samapalk\n8 Nimijargi otsing\n9Suurem/vaiksem kui xxx\n10 Top3\n11 Keskmine palk\n 12 Tulumalk\n 13 Sort by Name\n 14 Lower than average remove")
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
    elif v==6:
        print("Kasvavalt")
        sorteeriminekasv(palgad,inimesed)
        print("Kahanevalt")
        sorteeriminekah(palgad,inimesed)
    elif v==7:
        print(samapalk(palgad,inimesed))
    elif v==8:
        search(palgad,inimesed)
    elif v==9:
        m=int(input("Suurem kui XX vajuta 1\nVaiksem kui XX vajuta 2\n"))
        if m==1:
            suuremkui(palgad,inimesed)
        if m==2:
            vaiksemkui(palgad,inimesed)
    elif v==10:
        top3(palgad,inimesed)
    elif v==11:
        keskmine(palgad,inimesed)
    elif v==12:
        tulumaks(palgad,inimesed)
    elif v==13:
        sortbyname(palgad,inimesed)
    elif v==14:
        deleteloweravg(palgad,inimesed)