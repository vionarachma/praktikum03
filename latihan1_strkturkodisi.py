def main():
    print('======================================')
    print('   Viona Rachma Haji Sahbrina (312110373)')
    print(' Program Menentukan Bilangan Terbesar')
    print('======================================')
    a = int(input("Masukan bilangan pertama   : "))
    b = int(input("Masukan bilangan kedua     : "))
 
    if a > b:
        maks = a
    else:
        maks = b
    print('Nilai Terbesar adalah      : %d' % maks)
 
if __name__ == '__main__':
    main()