# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L_UMc-rQZXGkLG71OKLptjtXTrrNpsDA
"""

def kasallik_tashxisi(alomat):
  if alomat=="bosh og'riq":
    return "trimol, kyupen "
  elif alomat=="qorin og'riq":
     return "smetik,espomizan"
  elif alomat=="tish og'riq":
    return "brufen, zumm-25, odeston "
  elif alomat=="bel og'rig'i":
    return "deklofenak, menovazin, sariq gel dalgit"
  elif alomat=="tamoq og'riq":
    return "septoleto total"
  elif alomat=="yelka og'rig'i":
    return "snepar aktiv gel"
  elif alomat=="ko'z og'rig'i":
    return "taflotan"
  elif alomat=="bo'yin og'rig'i":
    return "loreal"
  elif alomat=="oyoq og'rig'i":
    return "Genel"
  elif alomat=="yo'tal":
    return "Kombizid"
  else:
     return "Noaniq kasallik, shifokorga murojaat qiling"
alomat=input("Alomatni kiriting")
natija=kasallik_tashxisi(alomat)
print(natija)

def mevalar_tarjimasi(meva):
  if meva=="olma":
    return "apple"
  elif meva=="shaftoli":
    return "pear"
  elif meva=="nok":
    return "peach"
  elif meva=="uzum":
    return "grap"
  elif meva=="banan":
    return "banana"
  elif meva=="xurmo":
    return "dates"
  else:
    return "noaniq meva"
meva=input("Mevani kiriting: ")
tarjima=mevalar_tarjimasi(meva)
print(tarjima)