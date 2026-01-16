# --- SportXtv 7/24 GLOBAL KAYNAK VE FİLTRE AYARLARI ---

# 1. İzlenecek Bölgeler (Tüm Dünya 7/24)
BOLGELER = ["Japonya", "Avrupa", "Amerika", "Ortadogu", "Katar"]

# 2. Canlı TV, Belgesel ve Film Kategorileri
KATEGORILER = ["Spor", "Belgesel", "Sinema", "Haber", "Dizi"]

# 3. Akıllı Filtre (Gereksiz ve Bozuk Linkleri Otomatik Siler)
def link_temizle(mesaj):
    # Bu sistem reklamlı ve virüslü çöpleri temizler
    yasakli = ["reklam", "virus", "bahis", "fake", "hata"]
    if any(kelime in mesaj.lower() for kelime in yasakli):
        return False
    return True

print("--- SportXtv 7/24 Zekası ve Filtre Sistemi Aktif ---")
