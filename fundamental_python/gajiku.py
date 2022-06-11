keuangan={
    'pengeluaran': [2,2.5,2.25,2.5,3.2,2.5,3.5,4.3],
    'pemasukan': [7.8,7.5,9,7.6,7.2,7.5,7.10,7.5]
}

total_pengeluaran=0
total_pemasukan=0
for biaya in keuangan['pengeluaran']:
    total_pengeluaran=total_pengeluaran+biaya
for biaya in keuangan['pemasukan']:
    total_pemasukan=total_pemasukan+biaya

rata2_pemasukan=total_pengeluaran/len(keuangan['pengeluaran'])


rata=len(keuangan['pengeluaran'])

print(rata)

print(rata2_pemasukan)