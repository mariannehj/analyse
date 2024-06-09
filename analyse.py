#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:57:33 2024

@author: kandidatnummer
"""
 
#importerer nødvendige biblioteker
#importerer nødvendige biblioteker
import csv 
import numpy as np
import matplotlib.pyplot as plt

filnavn = "tidsbruk_aktiviteter.csv"

underkategorier = []
hovedkategorier = []
tid_kvinner_underkategori = []
tid_kvinner_hovedkategori = []
tid_menn_underkategori = []
tid_menn_hovedkategori = []
tid_alle_underkategori = []
tid_alle_hovedkategori = []

def omgjoring(tid):
    timer, minutter = tid.split(".")
    tid = int(timer)*60 + int(minutter)
    return tid

with open(filnavn, encoding="ISO8859-1") as fil:
    innhold = csv.reader(fil, delimiter = ";")
    beskrivelse = next(innhold) # Hopper over første rad, da den bare inneholder beskrivelse
    tom_linje = next(innhold) # Hopper over den tomme raden
    overskrifter = next(innhold) # Hopper over linjen med overskrifter
    
    for i in range(3):
        next(innhold)
        
    for rad in innhold:
        
        #print(rad)
        tid = rad[2]
        kjønn = rad[1]
        
        if rad[0][0] == "-":
            if rad[0] not in underkategorier: 
                underkategorier.append(rad[0])
                
            if kjønn == "Kvinner" and tid not in tid_kvinner_underkategori:
                tid_kvinner_underkategori.append(omgjoring(tid))
                
            elif kjønn =="Menn" and tid not in tid_menn_underkategori: 
                tid = tid
                omgjoring(tid)
                tid_menn_underkategori.append(omgjoring(tid))
                
            else: 
                if tid not in tid_alle_underkategori: 
                    tid = tid
                    tid_alle_underkategori.append(omgjoring(tid))
        else: 
            if rad[0] not in hovedkategorier: 
                hovedkategorier.append(rad[0])
                
            if kjønn == "Kvinner" and tid not in tid_kvinner_hovedkategori: 
                tid = tid
                omgjoring(tid)
                tid_kvinner_hovedkategori.append(omgjoring(tid))
                
            elif kjønn =="Menn" and tid not in tid_menn_hovedkategori: 
                tid = tid
                tid_menn_hovedkategori.append(omgjoring(tid))
                
            else: 
                if tid not in tid_alle_hovedkategori: 
                    tid = tid
                    tid_alle_hovedkategori.append(omgjoring(tid))
                    
#fungerer ikke enda, må få sortert den
    def mest_popis(kategori, tider):
        kategorier_og_tider = []
        for i in range(len(kategori)):
            kategorier_og_tider.append([kategori[i], tider[i]])
        return kategorier_og_tider
#            if kategorier_og_tider[i][1] > storst:
#                kategorier_og_tider[i]
    
#hovedkategorier                  
x = np.arange(len(hovedkategorier))
#bredde på stolpene
width = 0.4
#Plotting av stolpene for menn og kvinner 
stolper_menn = plt.bar(x-width/2, tid_menn_hovedkategori, width, label="Menn", color ="skyblue")
stolper_kvinner = plt.bar(x+width/2, tid_kvinner_hovedkategori, width, label="Kvinner", color="orange")
plt.title("tid på ulike aktiviteter i løpet av en gjennomsnittlig dag")
plt.ylabel("minutter")
plt.xlabel("hovedkategorier")
plt.legend()
plt.grid(axis="y")
plt.xticks(x,hovedkategorier)
#plt.bar(hovedkategorier, tid_alle_hovedkategori, alpha = 0.8) (gjør den gjennomsiktig)
plt.gcf().autofmt_xdate()
plt.show()

"""
#underkategorier 
x = np.arange(len(underkategorier))
#bredde på stolpene
width = 0.4
#plotting av stolpene for menn og kvinner 
stolper_menn = plt.barh(x-width/2, tid_menn_underkategori, width, label="Menn", color="skyblue")
stolper_kvinner = plt.barh(x+width/2, tid_kvinner_underkategori, width, label="Kvinner", color="pink")
plt.title("tid på ulike aktiviteter i løpet av en gjennomsnittlig dag")
plt.ylabel("minutter")
plt.xlabel("kategorierer")
plt.legend()
plt.grid(axis="x")
plt.subplots_adjust(top=1.5)
plt.yticks(x, underkategorier)
plt.show()

x = np.arange(len(hovedkategorier))
#bredde på stolpene
width = 0.5
plt.title("tid på ulike aktiviteter i løpet av en gjennomsnittlig dag")
plt.barh(hovedkategorier, tid_alle_hovedkategori, width, color = "orange")
plt.xlabel("minutter")
plt.ylabel("hovedkategorier")
plt.grid(axis="y")
plt.yticks(x,hovedkategorier)
plt.show()
"""

"""
# Beregne totaltiden brukt av kvinner på hovedkategorier
total_tid_kvinner_hovedkategorier = sum(tid_kvinner_hovedkategori)
 
# Beregne andel av hver hovedkategori
andel_tid_kvinner_hovedkategori = [tid / total_tid_kvinner_hovedkategorier * 100 for tid in tid_kvinner_hovedkategori]
 
# Plotting av sektordiagram
plt.figure(figsize=(8, 8))
plt.pie(andel_tid_kvinner_hovedkategori, labels=hovedkategorier, autopct='%1.1f%%', startangle=140)
plt.title('tiden til kvinner på hver hovedkategori', pad=30)
plt.axis('equal')  # Gjør at sektordiagrammet er sirkulært
plt.show()

"""