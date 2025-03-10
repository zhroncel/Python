import math

pi=3.14
def secim():
	print("Geometrik Hesaplama Programı")
	hesaplama_sayisi = 0
	while True:
		print("\nHangi şekil için hesaplama yapmak istersiniz?\n")
		print("1.Kare\n2.Daire\n3.Dikdörtgen\n4.Küre\n5.Çıkış")
		secim =int(input("Secim yapiniz (1/2/3/4/5):"))

		if secim>=1 and secim<=5:
			if secim==1:
				kenar=float(input("Karenin kenar uzunlugunu girin:"))
				if kenar <= 0:
					print("pozitif bir deger girin")
					continue
				kare_alan= kenar*kenar
				kare_cevre= kenar*4
				print(f"Karenin alani:{kare_alan}")
				print(f"Karenin cevresi:{kare_cevre}")

			elif secim==2:
				r=float(input("Dairenin yaricapini girin:"))
				if r <= 0:
					print("pozitif bir deger girin")
					continue
				daire_alan=pi*r*r    
				daire_cevre=2*pi*r    
				print(f"Dairenin alani:{daire_alan}")    
				print(f"Dairenin cevresi:{daire_cevre}")

			elif secim==3:
				kkenar=float(input("Dikdortgenin kisa kenar uzunlugunu girin:"))
				ukenar=float(input("Dikdortgenin uzun kenar uzunlugunu girin:"))
				if kkenar <= 0 or ukenar <= 0:
					print("pozitif degerler girin")
					continue
				dikdortgen_alan= kkenar*ukenar
				dikdortgen_cevre= 2*kkenar + 2*ukenar
				print(f"Dikdortgenin alani:{dikdortgen_alan}")
				print(f"Dikdortgenin cevresi:{dikdortgen_cevre}")
        
			elif secim==4:
				r=float(input("Kurenin yaricapini girin:"))
				if r <= 0:
					print("pozitif deger girin")
					continue
				kure_yAlan=4*pi*r*r 
				kure_hacim=(4%3)*pi*r*r*r
				print(f"Kurenin yuzey alani:{kure_yAlan}")
				print(f"Kurenin hacim:{kure_hacim}")
        
			else:
				print("Programdan cıkılıyor.Hoscakalın!")
				break
        
		else:
			print("Lütfen belirtilen aralikta bir sayi girin(1-5)")
			continue
      
		hesaplama_sayisi+=1
	print(f"hesaplama sayisi:{hesaplama_sayisi}")
secim()