# Membuat program untuk menyapa pengunjung hotel
print("""MOHON MASUKKAN INFORMASI YANG DIMINTA DI BAWAH INI

""")
a = input('Mohon masukkan Nama depan anda:')
b = input('Mohon masukkan Nama belakang anda :')
c = input('Jenis Kelamin:(Pria/Wanita):')
if c == 'Pria':
    print('Selamat Datang' + ' ' + 'Tuan' + ' ' + a)
elif c == 'Wanita':
    print('Selamat Datang' + ' ' + 'Nyonya' + ' ' + a)
else:
    print('Data yang anda masukkan tidak valid')