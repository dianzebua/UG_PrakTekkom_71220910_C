print("Pemeriksa Kelipatan 9")
bilangan = int(input("Masukkan kelipatan 9 yang ingin diperiksa : "))
def kelipatan_sembilan():
    jawab =(bilangan%9)
    return jawab

if kelipatan_sembilan()==0:
    print("BENAR")
else :
    print("SALAH")
