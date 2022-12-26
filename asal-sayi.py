def Asal (sayi):
    adet=0
    for i in range(2,sayi+1):
        if sayi%i==0:
            adet+=1
    if adet==1:
        print (sayi, " asal sayıdır.")
    else:
        print (sayi," asal sayı değildir.")
 
sayi=int(input("sayi giriniz:"))
Asal(sayi)
