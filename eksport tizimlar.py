# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DimrE30frYW9qHqtNUtQ0rvTFWXD25cx
"""

def kasallik_tashxisi(belgi):
  if belgi == "Istima":
    return "Parasetamol iching"
  elif belgi == " Bosh og'rig'i ":
    return "Trimol"
  elif belgi == " Tish og'rig'i ":
    return "Senepar"
  elif belgi =="Shamollash":
    return "Tallon xot"
  elif belgi =="Bo'gim og'rig'i":
    return "Zefam"
  elif belgi =="Tomog' og'rig'i ":
   return "Fratsilin"
  elif belgi =="Ko'z og'rig'i":
   return "Lutax"
  elif belgi =="Tumov":
    return "Renoksin"
  elif belgi =="Oshqazon og'rig'i":
   return "Mezim"
  elif belgi =="Alergiya":
   return "Diazalin"
  else:
    return "Shifokorga murojat qiling"
belgi = input ("Kasallik belgisini kiriting")
natija=kasallik_tashxisi(belgi)
print (natija)

def Supper_car (belgi):
  if belgi == "Buggati chiron":
    return "Tezlik"
  elif belgi == "BMW":
    return " Drift"
  elif belgi == "Mercedes":
    return " Comford "
  elif belgi =="Rolls Royce":
    return " Obro' "
  elif belgi =="Lambargini":
    return "Tashqi dizayn"
  elif belgi =="Maclarn ":
   return "Chiroyli ko'rinish"
  elif belgi =="Nissan GTR":
   return "Kuchli mator"
  elif belgi =="Supra":
    return " Balan ovoz "
  elif belgi =="Tesla":
   return " Kuchli  elektra divigatel "
  elif belgi =="Gelik":
   return " Qulay haydash "
  else:
    return "Bu turda malumot yo'q"
belgi = input ("Supper_car")
natija=Supper_car(belgi)
print (natija)