a = int(input("Masukkan Bilangan Pertama  : "))
b = int(input("Masukkan Bilangan Kedua    : "))
c = int(input("Masukkan Bilangan Ketiga   : "))

if a < b :
print ("Urutan Bilangan :%s"  % a,b,c)
if a > b :
print ("Urutan Bilangan : %s" % b,a,c)
if a < c < b:
    print("Urutan Bilangan : %s" % a,c,b)
if b < c < a:
print("Urutan Bilangan : %s" % b,c,a)
if c < b:
print("Urutan Bilangan : %s" % c,a,b)
if c < b < a:
print("Urutan Bilangan : %s" % c,b,a)