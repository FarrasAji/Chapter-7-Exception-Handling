print ("-----------------------------")
print ("  PROGRAM HITUNG RATA-RATA  ")
print ("-----------------------------\n")

kondisi = True
sum = 0
awal = 0

while (kondisi == True):
    try:
        bil = int (input("Masukkan bilangan bulat : "))
        sum = sum + bil
        awal += 1
        
        konfirmasi = input ("Lagi (y/n) ? : ")
        if konfirmasi != 'y' :
            kondisi = False
            print ("\nRata-rata adalah ", sum/awal)
    except (ValueError):
        print ('Bukan bilangan bulat')
