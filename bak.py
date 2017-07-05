# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#-- Projenin adi    : backup
#-------------------------------------------------------------------------------
#-- Dosyanin adi    : bak.py
#-- Yazar           : electrocoder  <https://electrocoder.wordpress.com>
#-- Sirket          : 
#-- Tarih           : 2012-06-21
#-- Guncelleme T.   : 2015-08-22
#					  2016-09-20
#-- Test platform   : Ubuntu 12.04 LTS, Windows XP, Mac OS 10.10.4
#-- Python version  : Python 2.7.3, Python 3
#-------------------------------------------------------------------------------
#-- Sorumluluk      : Klasor yedekleme
#-------------------------------------------------------------------------------
#-- Copyright (c) 2012 - 2016
#-------------------------------------------------------------------------------
#-- Degisiklikler   :
#-- Tarih          Version  Yazar          Sorumluluk
#-- 2012-06-21     1.0      electrocoder   Baslangic
#-- 2016-09-20     1.1      electrocoder   Python 3 uyumluluk
#-------------------------------------------------------------------------------

from __future__ import print_function
import shutil, datetime, sys

help_read = """\nBu script proje gelistiren yazilimcilerin,
belirli zaman araliklari ile backup almasi amaciyla gelistirilmistir.
Yedegi alinacak klasorun adi parametre olarak verildiginde
<klasor_adi.yil.ay.gun.saat.dakika> olarak zip dosyasi olusturulur.
Yedegi alinan klasorun tum alt klasor ve dosyalari yedeklenir.
Hata ve yardim bildirimi icin = https://electrocoder.wordpress.com adresini kullaniniz.
Kullanimi = <bak.py [klasor_adi] [help]>
"""
def main():
	if sys.argv[1] == "help":
	    print(help_read)
	    sys.exit
	else:
	    print(sys.argv[1] + " arsivleniyor...")
	    i=datetime.datetime.now()

	    if len(str(i.day))==1:
	        day = "0" + str(i.day)
	    else:
	        day = str(i.day)

	    if len(str(i.month))==1:
	        month = "0" + str(i.month)
	    else:
	        month = str(i.month)

	    if len(str(i.hour))==1:
	        hour = "0" + str(i.hour)
	    else:
	        hour = str(i.hour)

	    if len(str(i.minute))==1:
	        minute = "0" + str(i.minute)
	    else:
	        minute = str(i.minute)

	    date_time = str(i.year) + "." + (month) + "." + (day) + "." + (hour) + "." + (minute)
	    try:
	        shutil.make_archive(sys.argv[1] + "." + date_time, "zip", sys.argv[1])
	        print("dosya " + sys.argv[1] + "." + date_time + " ismi ile arsivlendi")
	    except:
	        print("sorun olustu. dosya arsivlenemedi. lutfen https://electrocoder.wordpress.com adresinden hata bildirimi yapiniz.")

if __name__ == "__main__":
    main()
