# README: Tutorial Penggunaan Script Pengiriman Token $CARV di Base Network

## NOTE !!!
Program ini hanya bekerja jika drainer kalian tidak ngedrain native coin (ETH BASE) nya, program ini dibuat agar bisa adu cepat saat drainer mencoba claim alokasi carv kalian


## Pendahuluan
Script ini bertujuan untuk memonitor saldo token $CARV di sebuah wallet Ethereum dan mengirimkannya secara otomatis ke wallet penerima. Script ini menggunakan teknologi Web3 dan layanan Infura untuk terhubung dengan jaringan blockchain Base.

Panduan ini dirancang untuk membantu pengguna dengan sedikit atau tanpa pengalaman di bidang IT.

---

## Langkah-Langkah

### 1. Pastikan Anda Telah Menginstal Python

Python adalah bahasa pemrograman yang dibutuhkan untuk menjalankan script ini. Ikuti langkah berikut untuk menginstal Python:

1. Buka [situs Python](https://www.python.org/downloads/).
2. Klik tombol **Download** yang sesuai dengan sistem operasi Anda (Windows, Mac, atau Linux).
3. Setelah terunduh, buka file installer tersebut dan **centang kotak** yang bertuliskan "Add Python to PATH".
4. Klik **Install Now** dan tunggu hingga selesai.

### 2. Instal Program Pendukung (Library Python)

Setelah Python terinstal, Anda perlu menginstal program pendukung (library) agar script dapat berjalan. Ikuti langkah-langkah ini:

1. Buka **Command Prompt** (di Windows, ketik *cmd* di kotak pencarian).
2. Ketik perintah berikut untuk menginstal library yang dibutuhkan:

    ```bash
    pip install web3 python-dotenv eth-account
    ```

3. Tekan **Enter** dan tunggu hingga proses instalasi selesai.

### 3. Siapkan File Konfigurasi

Anda perlu membuat file konfigurasi `.env` yang berisi informasi rahasia seperti kunci privat (private key) dari wallet Ethereum Anda. Ikuti langkah-langkah ini:

1. Buka **Notepad** (atau aplikasi teks lainnya).
2. Copy dan paste teks berikut ke Notepad:

    ```bash
    PRIVATE_KEY='masukkan_private_key_anda_di_sini'
    RECIPIENT_WALLET='masukkan_alamat_wallet_penerima_di_sini'
    INFURA_URL='masukkan_infura_rpc_url_anda_di_sini'
    ```

3. Gantilah nilai `PRIVATE_KEY`, `RECIPIENT_WALLET`, dan `INFURA_URL` dengan informasi yang sesuai:
   - **PRIVATE_KEY**: Kunci privat dari wallet Ethereum Anda (jangan pernah membagikan kunci privat ini kepada orang lain).
   - **RECIPIENT_WALLET**: Masukkan alamat wallet penerima yang akan menerima token $CARV.
   - **INFURA_URL**: Masukkan URL RPC dari Infura yang Anda dapatkan setelah membuat akun di [Infura.io](https://infura.io/).
4. Simpan file ini dengan nama `.env` di folder yang sama dengan file `carv.py`.

### 4. Ubah Address Token $CARV dalam Kode

Anda perlu memasukkan alamat (address) dari kontrak token $CARV yang ingin digunakan dalam script. Ikuti langkah ini:

1. Buka file `carv.py` dengan editor teks (seperti Notepad).
2. Cari baris berikut di kode:

    ```python
    degen_token_address = Web3.to_checksum_address('ISI ADDRESS CARV DISINI')
    ```

3. Gantilah `'ISI ADDRESS CARV DISINI'` dengan alamat kontrak token $CARV yang sebenarnya. Pastikan Anda mendapatkan alamat kontrak yang benar dari sumber yang terpercaya.
4. Simpan perubahan pada file `carv.py`.

### 5. Menjalankan Script `carv.py`

1. Buat file bernama `run.bat` di folder yang sama dengan `carv.py`. Caranya:
   - Buka **Notepad** dan salin teks berikut:

     ```batch
     @echo off
     FOR /L %%i IN (1,1,3) DO (
         echo Running carv.py - Iteration %%i
         python carv.py
     )
     pause
     ```

   - Simpan file tersebut dengan nama **run.bat**.
2. Untuk menjalankan script ini sebanyak 3 kali, klik dua kali file **run.bat**.
3. Jendela Command Prompt akan terbuka dan menampilkan proses dari script yang sedang dijalankan. Jika ada saldo token $CARV di wallet, script akan mengirimkannya ke alamat penerima.

---

## Troubleshooting (Jika Terjadi Masalah)

### 1. **Error: "Connection failed to the Base network"**
   - Pastikan URL RPC yang Anda masukkan dalam file `.env` benar.
   - Periksa koneksi internet Anda.

### 2. **Error: "Error sending transaction"**
   - Pastikan Anda memiliki cukup saldo ETH di wallet untuk membayar biaya gas.

---

Dengan mengikuti langkah-langkah di atas, Anda sekarang dapat menjalankan script untuk mengirim token $CARV secara otomatis dari wallet Anda!
