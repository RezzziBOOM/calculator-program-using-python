def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol"
    return a/ b

def kalkulator():
    print("""
================================================
             PROGRAM KALKULATOR SEDERHANA 
                    REZZI BOOM
================================================
Kode |            PILIHAN  OPERASI         |
-------------------------------------------------
1.              Tambah        (  +  )
2.              Kurang        (  -  )
3.              Kali          (  *  )
4.              Bagi          (  /  )
=================================================
    """)

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan not in ['1', '2', '3', '4']:
        print("Pilihan tidak valid.")
        return

    angka1 = None
    angka2 = None
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Masukkan harus berupa angka.")
        return

    if pilihan == '1':
        print(f"{angka1:.2f} + {angka2:.2f} =", tambah(angka1, angka2))
    elif pilihan == '2':
        print(f"{angka1:.2f} - {angka2:.2f} =", kurang(angka1, angka2))
    elif pilihan == '3':
        print(f"{angka1:.2f} * {angka2:.2f} =", kali(angka1, angka2))
    elif pilihan == '4':
        print(f"{angka1:.2f} / {angka2:.2f} =", bagi(angka1, angka2))

while True:
    kalkulator()

    ulangi = input("Apakah Anda ingin mengulangi perhitungan? (y/n): ")
    if ulangi.lower() != 'y':
        print("Terima kasih telah mengunnakan caculator ini.")
        print("================== REZZI BOOM ==============.")
        break
