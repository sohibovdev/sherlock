#!/usr/bin/env python3
import asyncio
import aiohttp
import os
import sys
from colorama import Fore, Style, init

# Ranglarni faollashtirish
init(autoreset=True)

BANNER = f"""
{Fore.CYAN}███████╗██╗  ██╗███████╗██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
{Fore.CYAN}██╔════╝██║  ██║██╔════╝██╔══██╗██║     ██╔═══██╗██╔════╝██║  ██║
{Fore.CYAN}███████╗███████║█████╗  ██████╔╝██║     ██║   ██║██║     ███████║
{Fore.CYAN}╚════██║██╔══██║██╔══╝  ██╔══██╗██║     ██║   ██║██║     ██╔══██║
{Fore.CYAN}███████║██║  ██║███████╗██║  ██║███████╗╚██████╔╝╚██████╗██║  ██║
{Fore.CYAN}╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
{Fore.GREEN}       [+] Real Sherlock OSINT - Fast Username Search v2.0 [+]
{Fore.YELLOW}                [*] NO ROOT REQUIRED - High Speed [*]
"""

# Haqiqiy Sherlock ma'lumotlar bazasining asosiy qismi (Xalqaro va mashhur saytlar)
SITES = {
    "GitHub": "https://github.com{}",
    "Instagram": "https://instagram.com{}",
    "Reddit": "https://reddit.com{}",
    "TikTok": "https://tiktok.com@{}",
    "Pinterest": "https://pinterest.com{}",
    "Steam": "https://steamcommunity.com{}",
    "SoundCloud": "https://soundcloud.com{}",
    "Medium": "https://medium.com@{}",
    "Vimeo": "https://vimeo.com{}",
    "Twitch": "https://twitch.tv{}",
    "Telegram": "https://t.me{}",
    "Twitter/X": "https://x.com{}",
    "GitLab": "https://gitlab.com{}",
    "DockerHub": "https://docker.com{}",
    "Spotify": "https://spotify.com{}",
    "Discourse": "https://discourse.org{}",
    "Patreon": "https://patreon.com{}",
    "DailyMotion": "https://dailymotion.com{}",
    "Behance": "https://behance.net{}",
    "DeviantArt": "https://deviantart.com{}"
}

async def check_site(session, platform, url_template, username, results):
    url = url_template.format(username)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    
    try:
        async with session.get(url, headers=headers, timeout=6, allow_redirects=True) as response:
            # Ba'zi saytlar 200 qaytaradi, lekin profil yo'qligini matnda ko'rsatadi
            content = await response.text()
            
            # Instagram yoki Twitter xatoliklarini to'g'ri aniqlash uchun tekshiruvlar
            if response.status == 200 and "not found" not in content.lower() and "page not found" not in content.lower():
                print(f"{Fore.GREEN}[+] {platform}: Topildi! -> {url}")
                results.append(f"{platform}: {url}")
            else:
                # Profil mavjud bo'lmaganda ko'pincha 404 yoki redirect bo'ladi
                pass
    except Exception:
        # Ulanish xatoliklarini o'tkazib yuboramiz (Tezlikni tushirmaslik uchun)
        pass

async def main_search():
    os.system("clear")
    print(BANNER)
    
    username = input(f"{Fore.CYAN}Qidiriladigan foydalanuvchi nomini (username) kiriting: {Fore.WHITE}").strip()
    if not username:
        print(f"{Fore.RED}[-] Username kiritilmadi.")
        return

    print(f"\n{Fore.YELLOW}[*] '{username}' bo'yicha {len(SITES)} ta sayt parallel skaner qilinmoqda...\n")
    
    results = []
    
    # Barcha so'rovlarni bitta sessiyada parallel yuborish
    async with aiohttp.ClientSession() as session:
        tasks = [check_site(session, platform, url, username, results) for platform, url in SITES.items()]
        await asyncio.gather(*tasks)

    print(f"\n{Fore.CYAN}{'='*50}")
    print(f"{Fore.GREEN}[=] Qidiruv yakunlandi. Jami topilgan haqiqiy profillar: {len(results)}")
    print(f"{Fore.CYAN}{'='*50}")

    # Natijalarni faylga yozish
    if results:
        file_name = f"{username}_report.txt"
        with open(file_name, "w") as f:
            f.write(f"Sherlock OSINT Report for: {username}\n")
            f.write("="*40 + "\n")
            for res in results:
                f.write(res + "\n")
        print(f"{Fore.YELLOW}[*] Hisobot '{file_name}' fayliga muvaffaqiyatli saqlandi.")

if __name__ == "__main__":
    try:
        asyncio.run(main_search())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[-] Dastur to'xtatildi.")
