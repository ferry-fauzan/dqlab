from codecs import namereplace_errors


class Karyawan:
    perusahaan="PAKO GROUP"
    insentif_lembur=500000

    def __init__(self,name,usia,pendapatan):
        self.nama=name
        self.usia=usia
        self.gaji=pendapatan

    def lembur(self):
        self.gaji_lembur= self.gaji+self.insentif_lembur

    def total_pendapatan(self):
        return self.gaji_lembur


aksara=Karyawan('Aksara',20,5000000)
aksara.lembur()
print("Gaji Aksara : ", aksara.total_pendapatan())