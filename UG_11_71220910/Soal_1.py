print("====================")
print("Operasi Matematika")
print("1. Jumlah   [+]")
print("2. Kurang   [+]")
print("3. Kali     [+]")
print("4. Bagi     [+]")
print("====================")
pilihan = input("Pilih operasi (1/2/3/4): ")
print("====================")
bilangan_pertama = eval(input("Masukkan bilangan pertama : "))
bilangan_kedua = eval(input("Masukkan bilangan kedua : "))
def penjumlahan():
    jumlah = bilangan_pertama+bilangan_kedua
    return jumlah
def pengurangan():
    kurang = bilangan_pertama-bilangan_kedua
    return kurang
def perkalian():
    kali = bilangan_pertama*bilangan_kedua
    return kali
def pembagian():
    bagi = bilangan_pertama/bilangan_kedua

if pilihan == "1":
    print ("Hasil operasi dari ",bilangan_pertama, "+",bilangan_kedua,"=",penjumlahan())
elif pilihan == "2":
    print ("Hasil operasi dari ",bilangan_pertama, "-",bilangan_kedua,"=",pengurangan())
elif pilihan == "3":
    print ("Hasil operasi dari ",bilangan_pertama, "*",bilangan_kedua,"=",perkalian())
elif pilihan == "4":
    print ("Hasil operasi dari ",bilangan_pertama, "/",bilangan_kedua,"=",pembagian())
