"""
Minerva - Asisten AI dengan kemampuan kontrol perangkat dan TTS
Author: Aditya pratama
Date: 2026-08-29
"""

import os
import subprocess
import psutil
import pyautogui
import sys
from datetime import datetime
from pathlib import Path

# Import Google Gemini API - gunakan yang lama karena lebih stabil
import google.generativeai as genai

# Text-to-Speech (opsional)
try:
    import pyttsx3
    TTS_AVAILABLE = True
except Exception:
    TTS_AVAILABLE = False


class DeviceController:
    """Kelas untuk mengontrol perangkat lokal"""

    @staticmethod
    def open_application(app_name):
        """Membuka aplikasi berdasarkan nama"""
        apps = {
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'browser': ['cmd', '/c', 'start', 'chrome'],
            'chrome': ['cmd', '/c', 'start', 'chrome'],
            'edge': ['cmd', '/c', 'start', 'msedge'],
            'explorer': 'explorer.exe',
            'cmd': 'cmd.exe',
            'steam': ['cmd', '/c', 'start', 'steam://open/main'],
            'vscode': ['cmd', '/c', 'start', 'code'],
            'spotify': ['cmd', '/c', 'start', 'spotify'],
            'discord': ['cmd', '/c', 'start', 'discord'],
            'captain tsubasa': ['cmd', '/c', 'start', 'steam://rungameid/1163550'],
            'tsubasa': ['cmd', '/c', 'start', 'steam://rungameid/1163550']
        }

        app_name = app_name.lower()
        if app_name in apps:
            try:
                cmd = apps[app_name]
                if isinstance(cmd, list):
                    subprocess.Popen(cmd, shell=True)
                else:
                    subprocess.Popen(cmd)
                return f"✓ Aplikasi {app_name} berhasil dibuka"
            except Exception as e:
                return f"✗ Gagal membuka {app_name}: {str(e)}"
        else:
            return f"✗ Aplikasi {app_name} tidak dikenali. Tersedia: {', '.join(apps.keys())}"

    @staticmethod
    def take_screenshot():
        """Mengambil screenshot dan menyimpannya"""
        try:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = screenshots_dir / f"screenshot_{timestamp}.png"

            screenshot = pyautogui.screenshot()
            screenshot.save(filename)

            return f"✓ Screenshot disimpan: {filename}"
        except Exception as e:
            return f"✗ Gagal mengambil screenshot: {str(e)}"

    @staticmethod
    def get_system_info():
        """Mendapatkan informasi sistem"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

            info = f"""
📊 Informasi Sistem:
━━━━━━━━━━━━━━━━━━━━━━━━━━
🖥️  CPU Usage: {cpu_percent}%
💾 RAM Usage: {memory.percent}% ({memory.used / (1024**3):.2f} GB / {memory.total / (1024**3):.2f} GB)
💿 Disk Usage: {disk.percent}% ({disk.used / (1024**3):.2f} GB / {disk.total / (1024**3):.2f} GB)
━━━━━━━━━━━━━━━━━━━━━━━━━━
            """
            return info.strip()
        except Exception as e:
            return f"✗ Gagal mendapatkan info sistem: {str(e)}"


class AIAssistant:
    """Kelas utama untuk Minerva"""

    def __init__(self, api_key):
        """Inisialisasi Minerva"""
        # Setup Google Gemini
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

        # Setup Text-to-Speech (opsional)
        self.tts_engine = None
        if TTS_AVAILABLE:
            try:
                self.tts_engine = pyttsx3.init()
                self.tts_engine.setProperty('rate', 175)
                self.tts_engine.setProperty('volume', 0.9)
            except Exception:
                pass

        # Device Controller
        self.device = DeviceController()

        print("✓ Minerva  siap digunakan!")

    def speak(self, text):
        """Mengubah teks menjadi suara (jika tersedia)"""
        print(f"\nMinerva: {text}")
        if self.tts_engine:
            try:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            except Exception:
                pass

    def process_command(self, command):
        """Memproses perintah dari user"""
        command_lower = command.lower()

        # Cek apakah perintah berhubungan dengan kontrol sistem
        if any(keyword in command_lower for keyword in ['buka', 'open', 'jalankan', 'launch']):
            # Ekstrak nama aplikasi
            for app in ['captain tsubasa', 'tsubasa', 'steam', 'notepad', 'calculator', 'browser', 'chrome', 'edge', 'explorer', 'cmd', 'vscode', 'spotify', 'discord']:
                if app in command_lower:
                    response = self.device.open_application(app)
                    return response

        elif any(keyword in command_lower for keyword in ['screenshot', 'tangkap layar', 'capture']):
            response = self.device.take_screenshot()
            return response

        elif any(keyword in command_lower for keyword in ['system info', 'info sistem', 'sistem', 'ram', 'cpu']):
            response = self.device.get_system_info()
            return response

        # Untuk semua input lainnya (termasuk sapaan), gunakan AI
        try:
            response = self.model.generate_content(command)
            # Cek apakah response berhasil
            if hasattr(response, 'text') and response.text:
                return response.text
            elif hasattr(response, 'parts'):
                # Alternatif cara akses response
                return ''.join(part.text for part in response.parts)
            else:
                return "✗ Momo tidak memberikan respons"
        except Exception as e:
            error_msg = str(e)
            # Berikan pesan error yang lebih informatif
            if "API key" in error_msg or "invalid" in error_msg.lower():
                return "✗ Error: API Key tidak valid. Periksa kembali API key Anda."
            elif "quota" in error_msg.lower():
                return "✗ Error: Kuota API habis. Periksa billing di Google AI Studio."
            elif "404" in error_msg:
                return "✗ Error: Model tidak ditemukan. Pastikan menggunakan model yang tersedia."
            else:
                return f"✗ Error AI: {error_msg}"

    def run_text_mode(self):
        """Menjalankan AI dalam mode teks"""
        print("\n" + "="*50)
        print("Minerva - MODE TEKS")
        print("="*50)
        print("Perintah yang tersedia:")
        print("  • Buka [aplikasi] - Membuka aplikasi")
        print("  • Screenshot - Mengambil tangkapan layar")
        print("  • Info sistem - Melihat informasi sistem")
        print("  • [pertanyaan] - Tanya Minerva apapun")
        print("  • 'exit' atau 'keluar' - Keluar dari program")
        print("="*50)

        while True:
            try:
                user_input = input("\n👤 Anda: ").strip()

                if not user_input:
                    continue

                if user_input.lower() in ['exit', 'keluar', 'quit']:
                    print("👋 Terima kasih! Sampai jumpa!")
                    break

                response = self.process_command(user_input)
                print(f"\nMomo: {response}")

            except KeyboardInterrupt:
                print("\n👋 Program dihentikan. Sampai jumpa!")
                break
            except EOFError:
                print("\n👋 Input selesai. Program dihentikan.")
                break


def main():
    """Fungsi utama"""
    print("""
███╗   ███╗  ██╗███╗   ██╗███████╗██████╗ ██╗   ██╗ █████╗ 
████╗ ████║  ██║████╗  ██║██╔════╝██╔══██╗██║   ██║██╔══██╗
██╔█  █ ██║  ██║██╔██╗ ██║█████╗  ██████╔╝██║   ██║███████╔╝
██║╚██╗ ██║  ██║██║╚██╗██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══██╗
██║     ██║  ██║██║ ╚████║███████╗██║  ██║ ╚████╔╝ ██║  ██║
╚═╝     ══╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝
    """)

    # Minta API Key (atau load dari environment variable)
    api_key = os.getenv('GEMINI_API_KEY')

    if not api_key:
        print("⚠️  API Key tidak ditemukan di environment variable GEMINI_API_KEY")
        print("Anda bisa set dengan: $env:GEMINI_API_KEY='your-api-key'")
        print("Atau masukkan langsung di bawah ini:\n")

        try:
            api_key = input("Masukkan Google Gemini API Key: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n✗ Program dibatalkan.")
            sys.exit(1)

    if not api_key:
        print("✗ API Key diperlukan untuk menjalankan program!")
        sys.exit(1)

    # Inisialisasi AI Assistant
    try:
        assistant = AIAssistant(api_key)
    except Exception as e:
        print(f"✗ Gagal inisialisasi Minerva: {e}")
        sys.exit(1)

    # Mode teks (default)
    print("\n📝 Menjalankan dalam Mode Teks")
    print("(Voice mode membutuhkan PyAudio yang belum terinstall)\n")

    assistant.run_text_mode()


if __name__ == "__main__":
    main()
