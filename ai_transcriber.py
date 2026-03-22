import whisper

# 1. Modeli Yükle
# 'base' hızlıdır, 'large' daha doğrudur ama güçlü GPU ister.
# Model bilgisayarına indirilir ve lokal çalışır.
model = whisper.load_model("base")

# 2. MP3 Dosyasını İşle
# Whisper, arka planda ffmpeg kullanarak mp3'ü işler ve spektrograma çevirir.
result = model.transcribe("kayit.mp3")

# 3. Sonucu Yazdır
print(f"Tespit Edilen Dil: {result['language']}")
print("-" * 30)
print(result["text"])

# İstersen sonucu bir dosyaya kaydet
with open("desifre.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])