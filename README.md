# M6L2 Image Generation Discord Bot

Bu proje, Discord üzerinde çalışan ve kullanıcıdan aldığı metin prompt'u ile bir görsel oluşturan basit bir bot şablonudur.

## Özellikler
- Discord komut sistemiyle çalışır
- `!generate_image <prompt>` komutu ile görsel üretir
- Oluşturulan görseli Discord mesajı olarak gönderir

## Dosya Yapısı
- `bot.py` : Discord botunun ana dosyası
- `logic.py` : Görsel indirme ve token bilgisi için yardımcı mantık
- `index.html` : Örnek HTML sayfası

## Örnek:
![ornek](/ornek.png)

## Kurulum
1. Gerekli paketleri yükleyin:
   ```bash
   pip install discord.py requests
   ```

2. [logic.py](logic.py) dosyasındaki `TOKEN` değerini kendi Discord bot token'ınızla değiştirin.

3. Botu başlatın:
   ```bash
   python bot.py
   ```

## Kullanım
Bot çalıştıktan sonra Discord sunucusunda şu komutu kullanabilirsiniz:

```text
!generate_image bir kedi
```

Bu komut, ilgili prompt için görsel oluşturur ve Discord mesajı olarak gönderir.

## Not
- Token bilgilerinizi asla paylaşmayın.
- Botunuzun Discord Developer Portal üzerinden gerekli izinleri aktif ettiğinizden emin olun.
