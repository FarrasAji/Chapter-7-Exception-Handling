try :
    namafile = input ("Silahkan masukkan alamat file Anda : ")
    bukafile = open (namafile, "r")
    kondisi = True
    bukafile = open(namafile, "a")
    
    while (kondisi == True):
        isi_file = input ("Data yang mau ditambahkan :")
        bukafile.write(isi_file)
        bukafile.write("\n")
        
        konfirmasi = input ("Mau lagi? (y/n) :")
        if (konfirmasi != 'y'):
            kondisi = False
            bukafile = open (namafile, "r")
            print ("Tampilan dari file tersebut \n")
            print(bukafile.read())
            bukafile.close()
except (PermissionError):
    print ("\n Periksa kembali alamat file yang Anda masukkan")
except (FileNotFoundError):
    print ("\n File tidak ditemukan \n Periksa kembali alamat file anda")
