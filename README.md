# Tugas 2 KKA Membuat Program

| | | |
|---|---|---|
| **Nama** | Farrel Satria Mukti |
| **NRP** | 5025251138 |
| **Kelas** | KKA (A) |

## A. Penjelasan Tugas
Pada tugas ini, saya diminta untuk menyelesaikan permasalahan Romania `(NRP Genap)` menggunakan program. Adapun ketentuan yang harus dipenuhi oleh program adalah:

1. Menggunakan `Python`.
2. Menggunakan algoritma `Greedy BFS` dan `A*`.
3. Program memiliki interface/antarmuka.
4. User dapat menginput sembarang kota asal dan sembarang kota tujuan pada program.
5. User dapat memilih algoritma yang ingin digunakan.
6. Program menampilkan rute dan cost hasil pencarian.

## B. Penjelasan Program

### 1. Penjelasan Struktur Project

```
kka-tugas2/
  |__ app.py
  |__ data.py
  |__ algorithm.py
  |__ requirements.txt
```

- `app.py` : Berisikan kode streamlit untuk menampilkan interface dari program.
- `data.py` : Berisikan data statis seperti koneksi antar kota dan koordinat kota (koordinat kota didapat dari repositori Stuart Russel yang merupakan penulis buku AIMA).
- `algorithm.py` : Berisikan kode algoritma Greedy BFS dan A*.
- `requirements.txt` : Berisikan library python yang dibutuhkan untuk menjalankan program ini.

***# Mengapa menggunakan koordinat kota?***

Program ini mengharuskan user dapat memilih kota asal dan kota tujuan, sedangkan untuk dapat menghitung SLD dari kota asal dan tujuan yang bebas, diperlukan koordinat dari masing-masing kotanya. Sehingga tabel SLD yang ada pada PPT 3 KKA tidak dapat digunakan karena tabel tersebut hanya menyimpan SLD dengan tujuan kota Bucharest.

## C. Cara Menjalankan Program

Program ini dapat diakses melalui dua cara:

### 1. Melalui Website yang Sudah Dideploy

**Link akses:** [isi link deploy Streamlit kamu di sini]

### 2. Menjalankan Secara Lokal

Jika ingin menjalankan program secara lokal di komputer sendiri, ikuti langkah-langkah berikut.

#### Prasyarat
Pastikan sudah terinstall di komputer:
- [Python](https://www.python.org/downloads/) (versi 3.9 atau lebih baru disarankan)
- [Git](https://git-scm.com/downloads)

#### Langkah-langkah

**1. Clone repository**

```bash
git clone [isi link repository kamu di sini]
cd kka-tugas2
```

**2. Buat virtual environment (opsional, tapi disarankan)**

Virtual environment digunakan agar library yang diinstall untuk project ini tidak bercampur dengan library Python lain di komputer.

```bash
python -m venv .venv
```

Aktifkan virtual environment:

- **Windows:**
```bash
  .venv\Scripts\activate
```
- **macOS / Linux:**
```bash
  source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Jalankan aplikasi**

```bash
streamlit run app.py
```

Setelah perintah di atas dijalankan, Streamlit akan otomatis membuka aplikasi di browser (biasanya di alamat `http://localhost:8501`). Jika tidak terbuka otomatis, salin alamat tersebut dan buka manual di browser.

**5. Menghentikan aplikasi**

Kembali ke terminal, tekan `Ctrl + C` untuk menghentikan server Streamlit.