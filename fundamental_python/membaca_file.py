import requests
url="https://storage.googleapis.com/dqlab-dataset/hello.txt"
response=requests.get(url)

#cetak kode status response
print(response)

#cetak isi response menggunakan iter_lines()
print("\n>> Cetak isi file hello.txt menggunakan method response.iter_lines():")
for baris in response.iter_lines():
    print(baris)


# Cetak isi file hello.txt menggunakan atribut response.text
print("\n>> Cetak isi file hello.txt menggunakan atribut response.text:")
print(response.text)