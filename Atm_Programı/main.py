
print("************************\nKULLANICI GİRİŞİ\n"
      "************************")

sys_kullanici_adi = "ismail"
sys_parola = "12345"

giris_hakkı = 3

while True:
      kullanici_adi = input("Kullanıcı adını giriniz:")
      parola = input("Parola giriniz:")

      if(parola == sys_parola and kullanici_adi == sys_kullanici_adi):
            print("Sisteme başarıyla giriş yapıldı...")
            break
      elif (parola != sys_parola and kullanici_adi == sys_kullanici_adi):
            print("Parola hatalı...")
            giris_hakkı-=1
      elif(parola == sys_parola and kullanici_adi != sys_kullanici_adi):
            print("Kullanıcı adı hatalı...")
            giris_hakkı-=1
      else:
            print("Kullanıcı adı ve parola hatalı...")
            giris_hakkı-=1

      if(giris_hakkı == 0):
            print("Giriş hakkınız bitmiştir...")
            break




print("****************\nİSMBANK'A HOŞ GELDİNİZ\n****************")
print("****İşlemler****\n1.Para Yatırma\n2.Para Çekme\n3.Bakiye Sorgulama")
print("Çıkış için q'ya basınız\n****************")

bakiye = 5000 #Bakiye 5 bin olsun

while True:
    islem = input("Yapacağınız işlemi giriniz: ")

    if islem == "q":
        print("Tekrar Bekleriz...")
        break

    elif islem =="1":
        yatirilacak_tutar =int(input("Yatırılacak tutarı giriniz:"))
        bakiye += yatirilacak_tutar
        print("Bakiyeniz {} Tl".format(bakiye))


    elif islem == "2":
        cekilen_tutar =int(input("Çekmek istediğiniz tutarı giriniz:"))
        if(cekilen_tutar > bakiye):
            print(" Yetersiz bakiye...")
            continue

        else :
            bakiye -= cekilen_tutar
        print("Bakiyeniz {} Tl".format(bakiye))

    elif islem == "3":
        print("Bakiyeniz {} TL".format(bakiye))

    else:
        print("Geçersiz işlem...")

