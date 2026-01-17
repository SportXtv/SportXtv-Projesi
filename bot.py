import asyncio
from telethon import TelegramClient, events

# --- 2. PROJE: SportXtv APK (DÜNYA ÇAPINDA) ---
# Rusya sunucu altyapısı - APK destek botu.

# --- AYARLAR (Sarsılmaz Kısımlar) ---
api_id = '21820427'
api_hash = '8900600a9446d3e18507851e50882352'
bot_token = '8550515825:AAExuPyUH_ZMGzowjWWvzWA7o1-7IdH4L1U'
MY_ID = 7225508611

# Botu Başlat
client = TelegramClient('SportXtv_Oturum', api_id, api_hash).start(bot_token=bot_token)

# --- DESTEK MESAJI YAKALAYICI ---
@client.on(events.NewMessage)
async def destek_mesajlari(event):
    if event.is_private:
        sender = await event.get_sender()
        mesaj = f"🏟️ **SportXtv - Yeni Destek Mesajı**\n👤: {sender.first_name}\n💬: {event.text}"
        await client.send_message(MY_ID, mesaj)
        await event.reply("SportXtv ekibine ulaştınız. En kısa sürede döneceğiz.")

async def main():
    print("--- SportXtv SİSTEMİ ŞU AN AKTİF VE DİNLİYOR ---")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
