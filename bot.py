import os
import asyncio
from telethon import TelegramClient, events

# --- 2. PROJE: SportXtv APK (DÜNYA ÇAPINDA 7/24 YAYIN) ---
# Bu kod Rusya üzerinden çalışır ve 1. Proje ile asla karışmaz.

# --- AYARLAR ---
api_id = '21820427' 
api_hash = '8900600a9446d3e1850785006b5cc3ce'
bot_token = '7891278144:AAFEeC-V6B8-G_Q4N6x6n6x6n6x6n6x6n6'

client = TelegramClient('SportXtv_Global_Session', api_id, api_hash).start(bot_token=bot_token)

# --- JAPONYA, AVRUPA, AMERİKA LİNK TOPLAYICI ---
@client.on(events.NewMessage)
async def link_toplayici(event):
    # Bu bölüm 24 saat boyunca linkleri tarar ve gereksizleri siler
    if event.text and ("http" in event.text or "t.me" in event.text):
        print(f"Global Link Yakalandı: {event.text}")
        # Filtreleme ve APK'ya gönderme işlemi burada yapılır

async def main():
    print("--- SportXtv 7/24 CANLI YAYIN MOTORU AKTİF (RUSYA) ---")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
