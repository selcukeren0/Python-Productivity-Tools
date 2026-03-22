import yt_dlp
import sys

def download_youtube_video(url):
    """
    Belirtilen URL'deki videoyu en yüksek kalitede indirir ve MP4 olarak birleştirir.
    """
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'postprocessors': [
            {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'},
            {'key': 'FFmpegMetadata'}
        ]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"İndirme başlatılıyor: {url}")
            ydl.download([url])
            print("İşlem başarıyla tamamlandı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    # URL'yi ister terminalden al, ister input olarak sor
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        video_url = input("İndirmek istediğiniz YouTube URL'sini girin: ")
    
    download_youtube_video(video_url)
