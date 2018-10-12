## Botngaji.py - AYO NGAJI BOT V.1.0 [ 20-3-2018 , 20:33]
# Coded by Asterix88
# -*- UTF-8 -*-
##
import sys
from time import sleep



def banner():
	print """\033[1;32m
             ##               
            #  #              
            #  #  #  #   ##   
            ####  #  #  #  #  
            #  #   # #  #  #  
            #  #    #    ##   
                   #          
                          #    #    
                                    
      ###    ###   ###    #   ##    
      #  #  #  #  #  #    #    #    
      #  #   ##   # ##    #    #    
      #  #  #      # #  # #   ###   BOT
             ###         #          

           Dibuat dengan penuh <3
   Buatlah Handphone mu lebih bermanfaat^^
                      
    
"""
def tanya():
	ask = raw_input("\033[0mAssalamualaikum , siapa nama kamu? : ")
	print "\nSelamat datang " + ask +"\nsilahkan kamu pilih , pilihan berikut: "




def menu():
	print "\n1] Asmaul Husna"
	print "2] Doa-doa"
	print "3] Pengamalan Rutin"
	print "\n"
	print " Materi lainnya akan ada pada update\n selanjutnya, insyaallah"
	print "\n"
	print "99] Keluar"
	
def main():
	try:
		pilih = input("\033[1;32mMasukan nomor pilihan kamu\033[0m: ")
		if pilih == 1:
			print """\033[1;32m1. Yaa allahulladzi Laa illa ha ila anta\n2. Yaa Rohmanu\n3. Yaa Rohimu"""
			print "4. Yaa Maliku\n5. Yaa Kuddusu\n6. Yaa Salaamu"
			print "7. Yaa Mu'minu\n8. Yaa Muhaiminu\n9. Yaa Azizu\n10. Yaa Jabbaru"
			sleep(1)
			print "\n11. Yaa Mutakabbiru 16. Yaa Kohharu"
			print "12. Yaa Khooliqu 17. Yaa Wahhabu"
			print "13. Yaa Baariu\t 18. Yaa Rozzaqu"
			print "14. Yaa Mussiwru 19. Yaa Fattakhu"
			print "15. Yaa Ghoffaru 20. Yaa Alimu"
			sleep(1)
			print "\n21. Yaa Kobidu\t 26. Yaa Mudzilu"
			print "22. Yaa Baasitu\t 27. Yaa Samiiu"
			print "23. Yaa Khofidu\t  28. Yaa Basiiru"
			print "24. Yaa Roofiu\t 29. Yaa Khakamu"
			print "25. Yaa Mu'izzu\t 30. Yaa Adlu"
			sleep(1)
			print "\n31. Yaa Latiifu\t 36. Yaa Saykurru"
			print "32. Yaa Khobiiru 37. Yaa Aliyyu"
			print "33. Yaa Khaliimu 38. Yaa Kabiiru"
			print "34. Yaa Adiimu\t 39. Yaa Khafidzu"
			print "35. Yaa Ghofuuru 40. Yaa Muqiitu"
			sleep(1)
			print "\n41. Yaa Khasibu\t 46. Yaa Waasiu"
			print "42. Yaa Jaliilu\t 47. Yaa Khakiimu"
			print "43. Yaa Kariimu\t 48. Yaa Waduudu"
			print "44. Yaa Roqiibu\t 49. Yaa Majiidu"
			print "45. Yaa Mujiibu\t 50. Yaa Baitsu"
			sleep(1)
			print "\n51. Yaa Syahiidu 56. Yaa Waliyyu"
			print "52. Yaa Khaqqu\t 57. Yaa Kahmiidu"
			print "53. Yaa Wakiilu\t 58. Yaa Mukhsi"
			print "54. Yaa Qowiyyu\t 59. Yaa Mubdiu"
			print "55. Yaa Matiinu\t 60. Yaa Muiidu"
			sleep(1)
			print "\n61. Yaa Mukhyi\t 66. Yaa Majiidu"
			print "62. Yaa Mumiitu\t 67. Yaa Wakhidu"
			print "63. Yaa Khayyu\t 68. Yaa Somadu"
			print "64. Yaa Qoyyumu\t 69. Yaa Qodiiru"
			print "65. Yaa Waajidu\t 70. Yaa Muqtadiru"
			sleep(1)
			print "\n71. Yaa Muqoddimu 76. Yaa Baatinu"
			print "72. Yaa Muakhkhiru 77. Yaa Waali"
			print "73. Yaa Awwalu\t 78. Yaa Muta'ali"
			print "74. Yaa Aakhiru\t 79. Yaa Barru"
			print "75. Yaa Dhohiru\t 80. Yaa Tawwaabu"
			sleep(1)
			print "\n81. Yaa Muntaqimu\t86. Yaa Muqsitu"
			print "82. Yaa Afuwwu\t\t87. Yaa Jaamiu"
			print "83. Yaa Rouufu\t\t88. Yaa Goniyyu"
			print "84. Yaa Malikalmulki\t89. Yaa Mughni"
			print "85.Yaa Dzal Jalali Walikrom 90. Yaa Maaniu"
			sleep(1)
			print "\n91. Yaa Dhooru\t 96. Yaa Baaqi"
			print "92. Yaa Naafiu\t 97. Yaa Waaritsu"
			print "93. Yaa Nuurr\t 98. Yaa Rosyidu"
			print "94. Yaa Haadi\t 99.Yaa Sobuuru"
			print "95. Yaa Badiiu"
			
			sleep(0.5)
			print "\n[00] Kembali"
			print "[99] Keluar"
			choice = input("ayngji_>\033[0m")
			if choice == 00:
				menu()
				main()
			
			elif choice == "99":
				sys.exit()
				
		if pilih == 2:
			print "\033[1;33m\nDOA-DOA"
			print "\n"
			sleep(1)
			print "\033[1;31m[1] Doa Agar Terhindar dari Munafik"
			print "\n Allohuma inni audzubika minannifaki\n wasuil akhlaki wadoifil arzako\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[2] Doa Barokah"
			print "\n Allohuma baarik lanaa fiima a'toitana"
			print " Allohumma baaarik lanaa fiima rozaqtana\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[3] Ismaul A'dhom"
			print "\n Allohumma inni as aluka bianni\n bianni ashadu annaka antallahu\n laa ila ha illa antal akhadussomadu\n Alladzi lam yalid walam yulad\n walam yakullahu kufuwwan akhad\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[4] Doa Kumpulan Nabi Muhammad SAW"
			print "\n Allohumma inni as aluka min khoirima\n sa alaka minhu nabiyyuka muhammad\n wa audzubika min syarimas ta ada bika\n minhu nabiyyuka muhammad\n wa antal musta 'anu wa 'alaikal balagh\n wala khaula wala kuwwata illa billah"
			print "\n Insyaallah akan ditambah lagi pada update selanjutya :D\033[0m"
			
			sleep(0.3)
			print "\n[00] Kembali"
			print "[99] Keluar"
			choice=input("ayngji_>")
			if choice == 00:
				menu()
				main()
				
			elif choice == "99":
				sys.exit()
		if pilih == 3:
			print " \nPENGAMALAN RUTIN "
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 1 [-]"
			print "\n"
			print " Laa ilaha illallahu wakhdahu laa\n syariikalahu\n lahul mulku walahul khamdu\n wahuwa \'ala kulli syai\'in qodiir"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 2 [-]"
			print "\n"
			print " Subkhanallahi wabikhamdihi\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 3 [-]"
			print "\n"
			print " Subkhanallahi wabikhamdihi\n Subkhanallahil \'adhiim\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 4 [-]"
			print"\n"
			print " Laa ilaha illallahu wallahu akbar\n walaa khaula walaa kuwwata illa billah\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 5 [-]"
			print "\n"
			print " Astaghfirullahalladzi laa ilaha illa\n huwalkhayyul qoyyum wa atuubu ilaih\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pegamlan Rutin 6 [-]"
			print "\n"
			print " Rodhiitu billahi robba wabil islamidina\n wabi muhammadin sollalluhu 'alaihi\n wasallam rosula\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 7 [-]"
			print "\n"
			print "Subhana kalloumma wabi hamdika\n asyhadualla ilaha illa anta\n asytaghfiruka wa atubu ilaik\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 8 [-]"
			print "\n"
			print " Robbighfirlii watub \'allaya innaka\n anta tawwabur rohiim\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 9 [-]"
			print "\n"
			print " Bismillahi ladzi la yadurru ma\'asmihi\n syaiun fil ardi wala fissamaai\n wahuwas sami\'ul \'alim\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 10 [-]"
			print "\n"
			print " Allahumma anta robbi la ilaha illa anta\n kholaqtani wa ana \'abduka\n wa ana \'ala \'ahdika wawa\'dika mastato\'tu\n \'audzubika min syarima sona\'tu wa abu\'u \n ilaika\n bini\'matika \'alayya wa a'tarifu bidzunubi\n faghfirli dzunubi innahu la yaghfiru\n dzunuba illa anta\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 11 [-]"
			print "\n"
			print " Laa ilaha illallahu robbul 'aliyyul haliim\n Laa ilaha illallahu rabbul \'arsyil \'adhiim\n Laa ilaha illallahu robbus samawaati\n walard\n warabbul \'arsyil kariim\033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 12 [-]"
			print "\n"
			print " Subhanallah 100x \n Alhamdulillah 100x \n Laa ilaha illallah 100x \n Allahu akbar 100x \033[0m"
			print "\n"
			sleep(1)
			print "\033[1;31m[-] Pengamalan Rutin 13 [-]"
			print "\n"
			print " Alhamdulillahilladzi \'afanii mimmab\n talaaka bihi wafadholani \'ala katsiirin\n mimman kholaqo tafdhilaa\033[0m"
			
			sleep(0.2)
			print "\n[00] Kembali"
			print "[99] Keluar"
			
			choice=input("ayngji_>")
			if choice == 00:
				menu()
				main()
			elif choice == "99":
				sys.exit()
				
	
		
		
		
		
		
		
		if pilih == "99":
			sys.exit()
			
			
			
            
			
		
			
	except:
		print "something wrong"
		menu()
		main()
banner()
tanya()
menu()
main()
		
			