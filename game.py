from random import randint

print("Tas, kagit, makas oyununa hosgeldiniz.")
print("Tas, kagit, makas uclusunden birini secin, Taş:1, Kağıt:2, Makas:3 \nSeçtiğiniz obje için numarayı girip enter tuşuna basmanız yeterli")

user_choice = int(input("Seçiminizi yapın: "))

if user_choice == 1:
    print("Taşı seçtiniz.")
elif user_choice ==2:
    print("Kağıtı seçtiniz.")
elif user_choice ==3:
    print("Makası seçtiniz.")
elif user_choice < 1 or user_choice > 3:
    print("Lütfen geçerli bir seçim giriniz.")

msg = "-" * 30

print(msg)

print("Sıra bilgisayarda.")

print(msg)

computer_choice = randint(1,3)

if computer_choice == 1:
    print("Bilgisayarın seçimi: Taş")
elif computer_choice == 2:
    print("Bilgisayarın seçimi: Kağıt")
elif computer_choice == 3:
    print("Bilgisayarın seçimi: Makas")

print(msg)

def game_result():
    if computer_choice == user_choice:
        print("Maç sonucu berabere.")
    elif computer_choice == 1 and user_choice == 2:
        print("Siz kazandınız.")
    elif computer_choice == 1 and user_choice == 3:
        print("Bilgisayar kazandı.")
    elif computer_choice == 2 and user_choice == 1:
        print("Bilgisayar kazandı.")
    elif computer_choice == 2 and user_choice == 3:
        print("Siz kazandınız.")
    elif computer_choice == 3 and user_choice == 1:
        print("Siz kazandınız.")
    elif computer_choice == 3 and user_choice == 2:
        print("Bilgisayar kazandı.")

game_result()

print(msg)

print("Oyun sona erdi.")


