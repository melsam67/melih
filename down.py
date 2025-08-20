import yt_dlp
import os

def download_video(url, platform):
    # Platforma göre kaydedilecek klasörü ayarlayalım
    folder = "downloads/youtube" if platform == "youtube" else "downloads/tiktok"
    
    # İndirme ayarları
    ydl_opts = {
        "format": "mp4",
        "outtmpl": f"{folder}/%(title)s.%(ext)s"  # Başlığa göre isim veriyor
    }

    # İndir
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    print("\n✅ Video indirildi!")
    print("📂 Kaydedilen dosya:", os.path.abspath(filename))


def main():
    print("🎥 Video Downloader Menü")
    print("1 - TikTok")
    print("2 - YouTube Shorts")
    
    secim = input("Seçiminizi yapın (1/2): ")

    if secim == "1":
        url = input("👉 TikTok linkini gir: ")
        download_video(url, "tiktok")
    elif secim == "2":
        url = input("👉 YouTube Shorts linkini gir: ")
        download_video(url, "youtube")
    else:
        print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    main()
