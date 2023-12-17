#Sadece Bunları Değiştirin
user = "admin"
password = "12345"

#Bunları Değiştirmeniz Önerilmez
while True:
    kullanici = input("Kullanici adinizi giriniz: ")
    parola = input("Şifrenizi giriniz: ")
    if kullanici == user and parola == password:
        print("Hoşgeldiniz, Admin")
        break
    elif kullanici == user and parola != password:
        print("Şifreniz yanliş ❌\n")
    elif kullanici != user and parola == password:
        print("Kullanici adiniz yanliş ❌\n")
    else:
        print("Kullanici adi ve şifre hatali ❌\n")