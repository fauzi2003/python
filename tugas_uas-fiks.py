def f(x):
    return x**3 + 2*x - 5

def bisection_method(a, b, e):
    if f(a) * f(b) >= 0:
        print("Tidak ada akar pada selang ini.")
        return None
    
    print("="*135)
    print(f"{'Iterasi':<10} {'|'} {'a':<10} {'|'} {'b':<10} {'|'} {'c':<10} {'|'} {'f(a)':<10} {'|'} {'f(c)':<10} {'|'} {'pengecekan':<26} {'|'} {'Selang':<10} {'|'} {'Galat':<10} \n") 

    iterasi = 0
    while (b - a) >= e:
        iterasi += 1
        c = (a + b) / 2
        f_a = f(a)
        f_c = f(c)
        pengecekan = f_a * f_c

        print("="*135)
        print(f"{iterasi:<10} {'|'} {a:<10.4f} {'|'} {b:<10.4f} {'|'} {c:<10.4f} {'|'} {f_a:<10.4f} {'|'} {f_c:<10.4f} {'|'} {pengecekan:<25}", end=" ")

        if f_c == 0:
            print("Akar tepat ditemukan.")
            return c
        elif f_a * f_c < 0:
            b = c
            print(f" {'|'} {'[a, c]':<10}" , end=" ")
        else:
            a = c
            print(f" {'|'} {'[c, b]':<10}" , end=" ")

        print(f"{'|'}{b - a:>5}")
        
    return (a + b) / 2

print("-"*135, "|")
print ("Tentukan solusi nyata dari persamaan nonlinier berikut: x^3 + 2x - 5 = 0, kerjakan dengan menggunakan metode tertutup (biseksi)")
print("-"*135, "|")
a = float(input("Masukkan nilai Awal a: "))
b = float(input("Masukkan nilai Awal b: "))
e = float(input("Masukkan nilai Galat: "))
print("-"*135, "|")
print("\n\n")
print("tabel penyelesaian menggunakan metode biseksi")

akar = bisection_method(a, b, e)
print("="*135)
if akar:
    print(f"Akar yang ditemukan adalah {akar}.")
    print("="*135)
else:
    print("Tidak ditemukan akar dalam selang yang diberikan.")
    print("="*135)
