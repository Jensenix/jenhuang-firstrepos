class MemberPerpustakaan:
    def __init__(self):
        self.members = []
    
    def tampilkan_member(self):
        print("\n=== DAFTAR MEMBER PERPUSTAKAAN ===")
        print("="*70)
        print(f"{'NIM':<15} {'Nama Lengkap':<20} {'Jurusan':<20} {'No HP':<15}")
        print("="*70)
        for member in self.members:
            print(f"{member['nim']:<15} {member['nama']:<20} {member['jurusan']:<20} {member['no_hp']:<15}")
        print("="*70)
    
    def tambah_member(self):
        print("\n=== TAMBAH MEMBER BARU ===")
        while True:
            try:
                jumlah = int(input("Masukkan jumlah member yang akan ditambahkan (minimal 10): "))
                if jumlah < 10:
                    print("Minimal 10 member harus ditambahkan!")
                    continue
                break
            except ValueError:
                print("Masukkan angka yang valid!")
        
        for i in range(jumlah):
            print(f"\nMember ke-{i+1}")
            nim = input("NIM: ")
            nama = input("Nama Lengkap: ")
            jurusan = input("Jurusan: ")
            no_hp = input("No HP: ")
            
            self.members.append({
                'nim': nim,
                'nama': nama,
                'jurusan': jurusan,
                'no_hp': no_hp
            })
        
        print(f"\n{jumlah} member berhasil ditambahkan!")
    
    def cari_member(self):
        print("\n=== CARI MEMBER ===")
        nim = input("Masukkan NIM yang dicari: ")
        
        found = None
        for member in self.members:
            if member['nim'] == nim:
                found = member
                break
        
        if found:
            print("\nMember ditemukan:")
            print("="*50)
            print(f"{'NIM':<15} {'Nama Lengkap':<20} {'Jurusan':<20} {'No HP':<15}")
            print("="*50)
            print(f"{found['nim']:<15} {found['nama']:<20} {found['jurusan']:<20} {found['no_hp']:<15}")
            print("="*50)
        else:
            print(f"Member dengan NIM {nim} tidak ditemukan.")
    
    def ubah_member(self):
        print("\n=== UBAH DATA MEMBER ===")
        nim = input("Masukkan NIM member yang akan diubah: ")
        nama = input("Masukkan Nama Lengkap member yang akan diubah: ")
        
        found = None
        index = -1
        for i, member in enumerate(self.members):
            if member['nim'] == nim and member['nama'].lower() == nama.lower():
                found = member
                index = i
                break
        
        if found:
            print("\nData member saat ini:")
            print(f"NIM: {found['nim']}")
            print(f"Nama Lengkap: {found['nama']}")
            print(f"Jurusan: {found['jurusan']}")
            print(f"No HP: {found['no_hp']}")
            
            print("\nMasukkan data baru:")
            new_nim = input("NIM (kosongkan jika tidak diubah): ") or found['nim']
            new_nama = input("Nama Lengkap (kosongkan jika tidak diubah): ") or found['nama']
            new_jurusan = input("Jurusan (kosongkan jika tidak diubah): ") or found['jurusan']
            new_no_hp = input("No HP (kosongkan jika tidak diubah): ") or found['no_hp']
            
            self.members[index] = {
                'nim': new_nim,
                'nama': new_nama,
                'jurusan': new_jurusan,
                'no_hp': new_no_hp
            }
            
            print("\nData member berhasil diubah!")
        else:
            print(f"Member dengan NIM {nim} dan Nama {nama} tidak ditemukan.")
    
    def merge_sort(self, arr, key='nim', ascending=True):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            
            self.merge_sort(left, key, ascending)
            self.merge_sort(right, key, ascending)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                left_val = left[i][key].lower() if isinstance(left[i][key], str) else left[i][key]
                right_val = right[j][key].lower() if isinstance(right[j][key], str) else right[j][key]
                
                if ascending:
                    condition = left_val <= right_val
                else:
                    condition = left_val >= right_val
                
                if condition:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
    
    def urutkan_member(self):
        print("\n=== URUTKAN MEMBER ===")
        print("1. Berdasarkan NIM (Ascending)")
        print("2. Berdasarkan NIM (Descending)")
        print("3. Berdasarkan Nama (Ascending)")
        print("4. Berdasarkan Nama (Descending)")
        
        pilihan = input("Pilih metode pengurutan (1-4): ")
        
        if pilihan == '1':
            self.merge_sort(self.members, 'nim', True)
            print("\nMember berhasil diurutkan berdasarkan NIM (Ascending)")
        elif pilihan == '2':
            self.merge_sort(self.members, 'nim', False)
            print("\nMember berhasil diurutkan berdasarkan NIM (Descending)")
        elif pilihan == '3':
            self.merge_sort(self.members, 'nama', True)
            print("\nMember berhasil diurutkan berdasarkan Nama (Ascending)")
        elif pilihan == '4':
            self.merge_sort(self.members, 'nama', False)
            print("\nMember berhasil diurutkan berdasarkan Nama (Descending)")
        else:
            print("Pilihan tidak valid!")
    
    def main(self):
        print("=== PROGRAM MANAJEMEN MEMBER PERPUSTAKAAN ===")
        
        self.members = [
            {'nim': '123456', 'nama': 'Budi Santoso', 'jurusan': 'Teknik Informatika', 'no_hp': '08123456789'},
            {'nim': '234567', 'nama': 'Ani Wijaya', 'jurusan': 'Sistem Informasi', 'no_hp': '08234567890'},
            {'nim': '345678', 'nama': 'Citra Dewi', 'jurusan': 'Manajemen', 'no_hp': '08345678901'},
        ]
        
        while True:
            print("\nMenu Utama:")
            print("1. Tampilkan Member Pustaka")
            print("2. Tambah Member Pustaka")
            print("3. Cari Member")
            print("4. Ubah Member")
            print("5. Urutkan Member")
            print("6. Keluar")
            
            pilihan = input("Pilih menu (1-6): ")
            
            if pilihan == '1':
                self.tampilkan_member()
            elif pilihan == '2':
                self.tambah_member()
            elif pilihan == '3':
                self.cari_member()
            elif pilihan == '4':
                self.ubah_member()
            elif pilihan == '5':
                self.urutkan_member()
            elif pilihan == '6':
                print("Terima kasih telah menggunakan program ini!")
                break
            else:
                print("Pilihan tidak valid!")

if __name__ == "__main__":
    program = MemberPerpustakaan()
    program.main()