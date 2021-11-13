print("Python Hesap  Makinesi ")
print("İşlemler;")
print("Toplama için 1 butonuna basın")
print("Çıkarma için 2 butonuna basın")
print("Çarpma  için 3 butonuna basın")
print("Bölme için 4 butonuna basın")

islem = input("İşlem seçiniz: ")

if islem == "1":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 + sayi2)
elif islem == "2":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 - sayi2)
elif islem == "3":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 * sayi2)
elif islem == "4":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 / sayi2)
else:
    print("geçersiz işlem girdiniz...")
