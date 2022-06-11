class karyawan:
    nama_perusahaan="INKAOSKU"
    upah_lembur=500000

    def __init__ (self,nama,usia, pendapatan):
        self.nama=nama
        self.usia=usia
        self.pendapatan=pendapatan

    # def show(self):
    #     print("Hai {}".format(
    #         self.nama
    #     ))
    def show(self):
         print("Nama: {} \nUsia: {} \nGaji {}".format(
             self.nama,
             self.usia,
             self.pendapatan
         ))

adi=karyawan("Adi",25,3000000)

adi.show()

