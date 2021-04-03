#Membuat program grading nilai
print('Selamat Datang di Program Konversi Nilai')
print('Sebelum Memasuki program, Mohon isi Form Dibawah Ini')
print()
a = str(input('Nama Lengkap:'))
b = str(input('Nama Panggilan:'))
c = str(input('NIM'))
d = int(input('Masukkan Nilai Untuk Dikonversi:'))
print()
if d < 60:
    print('Halo,' + ' '+b+'! ' +'Nilai anda setelah dikonversi adalah'+' E' )
elif d <= 64:
    print('Halo,' + ' '+b+'! ' +'Nilai anda setelah dikonversi adalah'+' C' )
elif d <= 69:
    print('Halo,' + ' '+b+'! ' +'Nilai anda setelah dikonversi adalah'+' C+' )
elif d <= 74:
    print('Halo,' + ' '+b+'! ' +'Nilai anda setelah dikonversi adalah'+' B' )
elif d <= 79:
    print('Halo,' + ' '+b+'! ' +'Nilai anda setelah dikonversi adalah'+' B+' )
elif d <= 84:
    print('Halo,' + ' '+b+'! ' +'Nilai anda setelah dikonversi adalah'+' A-' )
elif d <= 100:
    print('Halo,' + ' '+b+'! ' +'Nilai anda setelah dikonversi adalah'+' A' )
else:
    print('Data Yang Anda Masukkan Salah')