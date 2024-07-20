def hesap_makinesi():
    print("Hesap Makinesi")
    print("İşlemler:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    
    # Kullanıcıdan işlemi ve sayıları al
    işlem = input("Lütfen yapmak istediğiniz işlemi seçin (1/2/3/4): ")
    sayı1 = float(input("Birinci sayıyı girin: "))
    sayı2 = float(input("İkinci sayıyı girin: "))
    
    if işlem == '1':
        sonuç = sayı1 + sayı2
        print(f"{sayı1} + {sayı2} = {sonuç}")
    elif işlem == '2':
        sonuç = sayı1 - sayı2
        print(f"{sayı1} - {sayı2} = {sonuç}")
    elif işlem == '3':
        sonuç = sayı1 * sayı2
        print(f"{sayı1} * {sayı2} = {sonuç}")
    elif işlem == '4':
        if sayı2 != 0:
            sonuç = sayı1 / sayı2
            print(f"{sayı1} / {sayı2} = {sonuç}")
        else:
            print("Bir sayıyı sıfıra bölemezsiniz!")
    else:
        print("Geçersiz işlem seçimi!")

# Hesap makinesini çalıştır
hesap_makinesi()