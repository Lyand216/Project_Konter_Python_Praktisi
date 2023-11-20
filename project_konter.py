import os

data_provider = ["Indosat", "XL", "Tri", "LiveOn"]
data_saldo_indosat=[10000, 25000, 50000, 100000]
data_saldo_xl=[25000,30000, 50000, 100000]
data_saldo_tri=[10000, 25000,30000, 50000, 100000]
data_saldo_liveOn = [65000, 120000, 250000]

def header_menu():
    print("-"*40)
    print("SELAMAT DATANG DI BINTANG TIMUR CELL".center(40))
    print("-"*40)
    print("Silahkan pilih provider dibawah ini:")
    for index, provider in enumerate(data_provider):
        print(f"{index+1}. {provider}")
    print("-"*40)

def perhitungan_indosat(bayar, saldo):
    if saldo == "1":
        sisa = bayar - data_saldo_indosat[0]
        return  sisa
    elif saldo == "2":
        sisa = bayar - data_saldo_indosat[1]
        return sisa
    elif saldo == "3":
        sisa = bayar - data_saldo_indosat[2]
        return sisa
    elif saldo == "4":
        sisa = bayar - data_saldo_indosat[3]
        return sisa
    else:
        return "Saldo tidak valid"
    
def perhitungan_xl(bayar, saldo):
    if saldo == "1":
        sisa = bayar - data_saldo_xl[0]
        return  sisa
    elif saldo == "2":
        sisa = bayar - data_saldo_xl[1]
        return sisa
    elif saldo == "3":
        sisa = bayar - data_saldo_xl[2]
        return sisa
    elif saldo == "4":
        sisa = bayar - data_saldo_xl[3]
        return sisa
    else:
        return "Saldo tidak valid"
    
def perhitungan_tri(bayar, saldo):
    if saldo == "1":
        sisa = bayar - data_saldo_tri[0]
        return  sisa
    elif saldo == "2":
        sisa = bayar - data_saldo_tri[1]
        return sisa
    elif saldo == "3":
        sisa = bayar - data_saldo_tri[2]
        return sisa
    elif saldo == "4":
        sisa = bayar - data_saldo_tri[3]
        return sisa
    elif saldo == "5":
        sisa = bayar - data_saldo_tri[4]
        return sisa
    else:
        return "Saldo tidak valid"
    
def perhitungan_liveon(bayar, saldo):
    if saldo == "1":
        sisa = bayar - data_saldo_liveOn[0]
        return  sisa
    elif saldo == "2":
        sisa = bayar - data_saldo_liveOn[1]
        return sisa
    elif saldo == "3":
        
        return bayar - data_saldo_liveOn[2]
    else:
        return "Saldo tidak valid"
    
def header_output():
    print("-"*40)
    print("BINTANG TIMUR CELL".center(40))
    print("- Lampung Timur -".center(40))
    print("-"*40)
    
while True:
    os.system("cls")
    header_menu()
    pilih_provider = input("Pilih provider : ")
    print("-"*40)

    if pilih_provider == '1':
        provider = "INDOSAT"
        print(provider)
        # menampilkan pilihan saldo
        for index, n in enumerate(data_saldo_indosat):
            print(f"{index+1}. {n}")
        print("-"*40)   
        # input dari user
        saldo = input("Pilih saldo : ")
        no_hp = input("Masukkan nomor HP : ")
        jumlah_bayar = int(input("Masukkan jumlah bayar : "))
        
        # pemanggilan funsi untuk memproses pembelian
        sisa = perhitungan_indosat(jumlah_bayar,saldo)
        
    elif pilih_provider == '2':
        provider = "XL"
        print(provider)
        # menampilkan pilihan saldo
        for index, n in enumerate(data_saldo_xl):
            print(f"{index+1}. {n}")
        print("-"*40)    
        # input dari user
        saldo = input("Pilih saldo : ")
        no_hp = input("Masukkan nomor HP : ")
        jumlah_bayar = int(input("Masukkan jumlah bayar : "))
        
        # pemanggilan funsi untuk memproses pembelian
        sisa = perhitungan_xl(jumlah_bayar,saldo)
        
    elif pilih_provider == '3':
        provider = "TRI"
        print(provider)
        # menampilkan pilihan saldo
        for index, n in enumerate(data_saldo_tri):
            print(f"{index+1}. {n}")
        print("-"*40)    
        # input dari user
        saldo = input("Pilih saldo : ")
        no_hp = input("Masukkan nomor HP : ")
        jumlah_bayar = int(input("Masukkan jumlah bayar : "))
        
        # pemanggilan funsi untuk memproses pembelian
        sisa = perhitungan_tri(jumlah_bayar,saldo)
        
    elif pilih_provider == '4':
        provider = "LIVE ON"
        print(provider)
        # menampilkan pilihan saldo
        for index, n in enumerate(data_saldo_liveOn):
            print(f"{index+1}. {n}")
        print("-"*40)
            
        # input dari user
        saldo = input("Pilih saldo : ")
        no_hp = input("Masukkan nomor HP : ")
        jumlah_bayar = int(input("Masukkan jumlah bayar : "))
        # pemanggilan funsi untuk memproses pembelian
        sisa = perhitungan_liveon(jumlah_bayar,saldo)

    else:
        print("Pilihan tidak valid")
        continue
    # output
        
    header_output()
    print("Provider\t\t:",provider)
    print("Nomor HP\t\t:",no_hp)
    print(f"Jumlah bayar\t\t: Rp.{jumlah_bayar}")
    print(f"Sisa bayar\t\t: Rp.{sisa}")
    print("-"*40)
    print("TERIMAKASIH".center(40))
    print("-"*40)
        
    stop = input("Mau beli lagi ? (y/n) : ")
    if stop == "n" or stop == "N":
        break