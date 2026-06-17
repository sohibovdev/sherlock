# Sherlock OSINT - Fast Username Finder 🔍

Ushbu loyiha kiberxavfsizlik va OSINT (ochiq manbalar orqali qidiruv) yo'nalishida nishon shaxsning foydalanuvchi nomi (username) orqali uning turli ijtimoiy tarmoqlardagi profillarini soniyalar ichida aniqlash uchun yaratilgan. 

Dastur `asyncio` va `aiohttp` kutubxonalari yordamida barcha saytlarga parallel (bir vaqtning o'zida) so'rov yuboradi. Shu sababli juda yuqori tezlikda ishlaydi.

> ⚠️ **MUHIM:** Ushbu dasturni ishga tushirish uchun **ROOT huquqi talab qilinmaydi**. Termux va Linux tizimlarida xavfsiz ishlaydi.

## ✨ Xususiyatlari
- ⚡ **Asinxron Tezlik:** Barcha veb-saytlar bir vaqtda skaner qilinadi (kutish vaqti deyarli yo'q).
- 📊 **Keng Baza:** Dunyoning eng ommabop 20 dan ortiq ijtimoiy tarmoqlari integratsiya qilingan (Telegram, GitHub, Instagram, TikTok, Reddit va h.k.).
- 💾 **Avtomatik Hisobot:** Topilgan barcha profillar havolalari yakunda avtomatik ravishda `[username]_report.txt` fayliga saqlanadi.
- 🎨 **Vizual Dizayn:** Terminal interfeysi rangli va tushunarli tartibda chiqarilgan.

## 🛠️ O'rnatish va Talablar

Dastur to'g'ri ishlashi uchun Python 3 va uning tashqi kutubxonalari bo'lishi shart.

### 1. Kerakli paketlarni o'rnatish:
* **Linux (Ubuntu/Kali):**
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip git -y
  ```
* **Termux:**
  ```bash
  pkg update
  pkg install python git -y
  ```

### 2. Loyihani yuklab olish va kutubxonalarni o'rnatish:
```bash
git clone https://github.com[repozitoriya-nomi].git
cd [repozitoriya-nomi]
pip install -r requirements.txt
```
*(Eslatma: `[repozitoriya-nomi]` o'rniga GitHub'dagi loyihangiz nomini yozing).*

## 🚀 Ishga tushirish
Dasturni oddiy foydalanuvchi huquqi bilan ishga tushiring:
```bash
python3 sherlock.py
```

## 📝 Ishlash jarayonidan namuna
1. Dastur ishga tushgach, maqsadli foydalanuvchi nomini kiritasiz.
2. Dastur parallel ravishda bazadagi saytlarni tekshiradi va topilganlarini yashil rangda `[+]` belgisi bilan chiqaradi.
3. Yakunda jami topilgan natijalar soni ko'rsatiladi va hisobot fayli yaratiladi.
4. 
