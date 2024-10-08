# README: Tutorial Penggunaan Script Pengiriman Token $CARV di Base Network

## Pendahuluan
Script ini bertujuan untuk memonitor saldo token $CARV di sebuah wallet dan mengirimkannya secara otomatis ke wallet penerima menggunakan Web3 dan Infura. Tutorial ini disusun agar mudah dipahami oleh pengguna awam.

## Prasyarat

### 1. Software yang Dibutuhkan
- **Python 3.7+**: Pastikan Python telah terpasang di komputer Anda. [Download Python di sini](https://www.python.org/downloads/).
- **Pip**: Manajer paket Python untuk menginstal library yang dibutuhkan.
- **Infura Account**: Dapatkan akses ke Infura dan buat proyek baru untuk mendapatkan URL RPC jaringan Base. [Daftar di Infura](https://infura.io/).
- **Wallet Ethereum**: Anda membutuhkan private key dari wallet Ethereum Anda dan alamat wallet penerima.

### 2. Library Python yang Diperlukan
Jalankan perintah berikut di terminal untuk menginstal library yang diperlukan:

```bash
pip install web3 python-dotenv eth-account
```

### 3. Buat File `.env`
Buat file bernama `.env` di folder yang sama dengan script `carv.py`, dan tambahkan informasi berikut:

```bash
PRIVATE_KEY='masukkan_private_key_anda_di_sini'
RECIPIENT_WALLET='masukkan_alamat_wallet_penerima_di_sini'
INFURA_URL='masukkan_infura_rpc_url_anda_di_sini'
```

- **PRIVATE_KEY**: Masukkan private key dari wallet pengirim (pastikan ini bersifat rahasia).
- **RECIPIENT_WALLET**: Masukkan alamat wallet penerima yang akan menerima token.
- **INFURA_URL**: Masukkan URL RPC dari proyek Infura Anda yang terhubung ke jaringan Base.

### 4. Jalankan Script
Untuk menjalankan script `carv.py`, buka terminal atau command prompt di direktori tempat Anda menyimpan file, lalu jalankan perintah berikut:

```bash
python carv.py
```

Script ini akan terus berjalan dan memonitor saldo token $CARV di wallet Anda. Jika saldo ditemukan, token tersebut akan dikirim secara otomatis ke wallet penerima.

### 5. Troubleshooting
- **Connection failed to the Base network**: Pastikan URL RPC yang Anda masukkan di `.env` benar dan Anda memiliki koneksi internet yang baik.
- **Error sending transaction**: Cek saldo wallet Anda untuk memastikan Anda memiliki cukup ETH untuk membayar gas fee.

