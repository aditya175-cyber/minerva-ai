# 🤖 Panduan AI Assistant - Windows OS

## 📋 Daftar Isi
1. [Persyaratan Sistem](#persyaratan-sistem)
2. [Instalasi Library](#instalasi-library)
3. [Mendapatkan API Key](#mendapatkan-api-key)
4. [Cara Menjalankan](#cara-menjalankan)
5. [Fitur-Fitur](#fitur-fitur)
6. [Troubleshooting](#troubleshooting)

---

## 🖥️ Persyaratan Sistem

- **OS**: Windows 10/11
- **Python**: 3.8 atau lebih baru
- **Mikrofon**: Diperlukan untuk fitur speech recognition
- **Speaker**: Diperlukan untuk fitur text-to-speech
- **Koneksi Internet**: Diperlukan untuk API Gemini dan speech recognition

---

## 📦 Instalasi Library

### Langkah 1: Buka Terminal/Command Prompt
- Tekan `Win + R`, ketik `cmd`, lalu Enter
- Atau buka VS Code dan buka terminal dengan `Ctrl + ~`

### Langkah 2: Navigate ke Folder Project
```bash
cd D:\coding\claude
```

### Langkah 3: Install PyAudio (Khusus Windows)
PyAudio memerlukan instalasi khusus di Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

**Jika gagal**, download wheel file manual:
1. Kunjungi: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
2. Download file sesuai Python version Anda (misal: `PyAudio-0.2.14-cp311-cp311-win_amd64.whl` untuk Python 3.11)
3. Install dengan:
```bash
pip install PyAudio-0.2.14-cp311-cp311-win_amd64.whl
```

### Langkah 4: Install Library Lainnya
```bash
pip install -r requirements.txt
```

### Langkah 5: Verifikasi Instalasi
```bash
pip list
```

Pastikan semua library terinstall:
- ✓ google-generativeai
- ✓ psutil
- ✓ pyautogui
- ✓ Pillow
- ✓ SpeechRecognition
- ✓ pyttsx3
- ✓ pyaudio

---

## 🔑 Mendapatkan API Key

### Google Gemini API (GRATIS)

1. **Buka Google AI Studio**
   - Kunjungi: https://makersuite.google.com/app/apikey
   - Atau: https://aistudio.google.com/app/apikey

2. **Login dengan Akun Google**
   - Gunakan akun Gmail Anda

3. **Create API Key**
   - Klik tombol "**Create API Key**"
   - Pilih project atau buat project baru
   - Copy API Key yang muncul

4. **Simpan API Key** (Pilih salah satu cara):

   **Cara A: Menggunakan Environment Variable (Direkomendasikan)**
   ```bash
   # Buka PowerShell sebagai Administrator
   setx GEMINI_API_KEY "your-api-key-here"
   ```
   Setelah itu, **restart terminal/VS Code** agar environment variable aktif.

   **Cara B: Masukkan Manual Saat Program Dijalankan**
   - Program akan meminta API key saat pertama kali dijalankan

**⚠️ PENTING**: 
- Jangan share API key Anda ke orang lain
- Jangan commit API key ke GitHub
- Gemini API gratis memiliki limit: 60 requests/menit

---

## ▶️ Cara Menjalankan

### Opsi 1: Menjalankan di Terminal/CMD

```bash
# Navigate ke folder project
cd D:\coding\claude

# Jalankan program
python ai_assistant.py
```

### Opsi 2: Menjalankan di VS Code

1. Buka folder `D:\coding\claude` di VS Code
2. Buka file `ai_assistant.py`
3. Tekan `F5` atau klik "Run" > "Run Without Debugging"
4. Atau klik tombol ▶️ di kanan atas

### Opsi 3: Menjalankan dengan Environment Variable

```bash
# Set API key terlebih dahulu
set GEMINI_API_KEY=your-api-key-here

# Jalankan program
python ai_assistant.py
```

---

## ✨ Fitur-Fitur

### 1️⃣ Mode Teks (Ketik Perintah)

**Perintah Kontrol Sistem:**
```
Buka notepad          → Membuka Notepad
Buka calculator       → Membuka Calculator
Buka browser          → Membuka Chrome/Edge
Buka chrome           → Membuka Chrome
Buka explorer         → Membuka File Explorer
Screenshot            → Mengambil screenshot
Info sistem           → Melihat CPU, RAM, Disk usage
```

**Percakapan Umum:**
```
Apa itu Python?
Jelaskan tentang AI
Buatkan puisi
Berapa 15 x 23?
```

**Keluar Program:**
```
exit
keluar
quit
```

### 2️⃣ Mode Suara (Voice Control)

**Cara Menggunakan:**
1. Pilih mode 2 saat program dimulai
2. Tunggu AI berkata "Mendengarkan..."
3. Bicara dengan jelas ke mikrofon
4. AI akan memproses dan menjawab dengan suara

**Contoh Perintah Suara:**
```
"Buka notepad"
"Ambil screenshot"
"Info sistem"
"Apa kabar?"
"Keluar"
```

**Tips Voice Recognition:**
- Bicara dengan jelas dan tidak terlalu cepat
- Pastikan mikrofon tidak terlalu jauh
- Kurangi noise di sekitar
- Gunakan bahasa Indonesia atau Inggris

---

## 🔧 Troubleshooting

### ❌ Problem: "No module named 'pyaudio'"

**Solusi:**
```bash
pip install pipwin
pipwin install pyaudio
```

Atau download wheel file manual dari https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

---

### ❌ Problem: "API Key invalid"

**Solusi:**
1. Pastikan API key sudah benar (copy-paste langsung dari Google AI Studio)
2. Cek apakah ada spasi di awal/akhir API key
3. Generate API key baru jika perlu

---

### ❌ Problem: "Microphone not working"

**Solusi:**
1. Cek pengaturan microphone di Windows:
   - Settings > Privacy > Microphone
   - Pastikan "Allow apps to access your microphone" ON
2. Test microphone di aplikasi lain (misal: Voice Recorder)
3. Jalankan program sebagai Administrator

---

### ❌ Problem: "Speech recognition error"

**Solusi:**
1. Pastikan koneksi internet stabil (Google Speech API memerlukan internet)
2. Bicara lebih jelas dan pelan
3. Kurangi noise di sekitar
4. Restart program

---

### ❌ Problem: "Rate limit exceeded" (Gemini API)

**Solusi:**
- Gemini API gratis memiliki limit 60 requests/menit
- Tunggu beberapa menit sebelum mencoba lagi
- Atau upgrade ke plan berbayar

---

## 📊 Struktur File

```
D:\coding\claude\
│
├── ai_assistant.py         # File program utama
├── requirements.txt        # Daftar library yang diperlukan
├── PANDUAN.md             # File panduan ini
│
└── screenshots/           # Folder untuk menyimpan screenshot (otomatis dibuat)
    ├── screenshot_20260829_141030.png
    └── screenshot_20260829_142315.png
```

---

## 🎯 Cara Mengembangkan Lebih Lanjut

### Menambah Aplikasi Baru

Edit bagian `apps` di class `DeviceController`:

```python
apps = {
    'notepad': 'notepad.exe',
    'calculator': 'calc.exe',
    # Tambahkan aplikasi baru di sini:
    'vscode': 'code',
    'spotify': 'spotify.exe',
    'discord': 'discord.exe',
}
```

### Menambah Perintah Sistem Baru

Tambahkan method baru di class `DeviceController`:

```python
@staticmethod
def shutdown_computer():
    """Mematikan komputer"""
    os.system("shutdown /s /t 60")  # Shutdown dalam 60 detik
    return "Komputer akan shutdown dalam 60 detik"
```

Lalu tambahkan kondisi di `process_command()`:

```python
elif 'shutdown' in command_lower:
    response = self.device.shutdown_computer()
    return response
```

---

## 📝 Tips Penggunaan

1. **Mode Teks** lebih akurat dan cepat untuk perintah spesifik
2. **Mode Suara** lebih praktis tapi memerlukan koneksi internet
3. Screenshot otomatis disimpan di folder `screenshots/`
4. Gunakan perintah "info sistem" untuk monitoring resource
5. AI dapat menjawab pertanyaan umum menggunakan Gemini

---

## ⚖️ Lisensi & Credit

- **Dibuat oleh**: Kiro AI
- **Tanggal**: 29 Agustus 2026
- **API**: Google Gemini API
- **License**: MIT (gunakan dan modifikasi sesuai kebutuhan)

---

## 📞 Support

Jika ada pertanyaan atau masalah, silakan:
1. Cek bagian Troubleshooting di atas
2. Baca dokumentasi library yang digunakan
3. Google error message yang muncul

---

**Selamat mencoba! 🚀**
