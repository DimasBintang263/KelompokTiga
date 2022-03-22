class Kalkulator:
    def __1init__(self, x, y ):
        self.A = x
        self.B = y
        print("A ="+str(x)+", B ="+str(y))

    def tambah(self):
        self.hasil = self.A + self.B
        print("A + B = "+str(self.hasil))

    def kurang(self):
        self.hasil = self.A - self.B
        print("A - B = "+str(self.hasil))

    def kali(self):
        self.hasil = self.A * self.B
        print("A X B = "+str(self.hasil))

    def bagi(self):
        if self.B==0:
            print("Pembagian dengan Nol")
        else:
            self.hasil=self.A/self.B
            print("A / B = "+str(self.hasil))

ans=True
while ans:
    print ("="*50)
    print ("Menu Operasi\n1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Keluar")
    ans=input("Operasi Apa yang akan dilakukan? ")
    print ("="*50)
    if ans=="1":
        ob1 = int(input("Masukan Angka 1 "))
        ob2 = int(input("Masukan Angka 2 "))
        Object1 = Kalkulator(ob1,ob2)
        Object1.tambah()
        print("\nOperasi selesai")
    elif ans=="2":
        ob1 = int(input("Masukan Angka 1 "))
        ob2 = int(input("Masukan Angka 2 "))
        Object1 = Kalkulator(ob1,ob2)
        Object1.kurang()
        print("\nOperasi selesai")
    elif ans=="3":
        ob1 = int(input("Masukan Angka 1 "))
        ob2 = int(input("Masukan Angka 2 "))
        Object1 = Kalkulator(ob1,ob2)
        Object1.kali()
        print("\nOperasi selesai")
    elif ans=="4":
        ob1 = int(input("Masukan Angka 1 "))
        ob2 = int(input("Masukan Angka 2 "))
        Object1 = Kalkulator(ob1,ob2)
        Object1.bagi()
        print("\nOperasi selesai")
    elif ans=="5":
        print ("Terimakasi^^\nAnggota Kelompok:\n1. Dicka\n2. Dimas\n3. Fatih\n4. Kenny")
        break
    elif ans !="":
        print("\n Tidak Valid coba lagi!")