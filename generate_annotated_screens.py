# -*- coding: utf-8 -*-
import os
import math
from PIL import Image, ImageDraw, ImageFont

def draw_arrow(draw, start, end, color='#dc2626', width=4, arrow_size=16):
    x0, y0 = start
    x1, y1 = end
    draw.line([start, end], fill=color, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    
    # Ok başının iki kanadı
    angle1 = angle + math.pi - math.pi / 6
    angle2 = angle + math.pi + math.pi / 6
    
    p1 = (x1 + arrow_size * math.cos(angle1), y1 + arrow_size * math.sin(angle1))
    p2 = (x1 + arrow_size * math.cos(angle2), y1 + arrow_size * math.sin(angle2))
    
    draw.polygon([end, p1, p2], fill=color)

def draw_callout(draw, rect, text, subtext, color_theme, font_title, font_body):
    x, y, w, h = rect
    bg_color = color_theme['bg']
    border_color = color_theme['border']
    title_color = color_theme['title']
    body_color = color_theme['body']
    
    # Arka plan ve kenarlık
    draw.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=bg_color, outline=border_color, width=2)
    
    # Başlık
    draw.text((x + 10, y + 8), text, fill=title_color, font=font_title)
    # Açıklama
    draw.text((x + 10, y + 28), subtext, fill=body_color, font=font_body)

base_shots = r"C:\Users\ahmet\.gemini\antigravity\scratch\25902009_ResulEkremOzcan_InventoryManagement\Screenshots"
out_dir = r"C:\Users\ahmet\.gemini\antigravity\scratch\25902009_ResulEkremOzcan_InventoryManagement\Okli_Gorseller"
os.makedirs(out_dir, exist_ok=True)

# Font ayarları
try:
    font_bold_lg = ImageFont.truetype("arialbd.ttf", 15)
    font_bold = ImageFont.truetype("arialbd.ttf", 13)
    font_regular = ImageFont.truetype("arial.ttf", 11)
    font_header = ImageFont.truetype("arialbd.ttf", 18)
except:
    font_bold_lg = ImageFont.load_default()
    font_bold = ImageFont.load_default()
    font_regular = ImageFont.load_default()
    font_header = ImageFont.load_default()

themes = {
    'blue': {'bg': '#eff6ff', 'border': '#3b82f6', 'title': '#1d4ed8', 'body': '#1e293b'},
    'red': {'bg': '#fef2f2', 'border': '#ef4444', 'title': '#b91c1c', 'body': '#1e293b'},
    'green': {'bg': '#f0fdf4', 'border': '#22c55e', 'title': '#15803d', 'body': '#1e293b'},
    'purple': {'bg': '#faf5ff', 'border': '#a855f7', 'title': '#7e22ce', 'body': '#1e293b'},
    'orange': {'bg': '#fff7ed', 'border': '#f97316', 'title': '#c2410c', 'body': '#1e293b'}
}

# =========================================================================
# 1. GÖRSEL: ANA EKRAN VE GENEL GÖRÜNÜM (OKLARLA İŞLEV ANLATIMI)
# =========================================================================
img1_raw = Image.open(os.path.join(base_shots, "01_AnaEkran_GenelGörünüm.png"))
canvas1 = Image.new('RGB', (1600, 780), color='#f8fafc')
canvas1.paste(img1_raw, (20, 40))
d1 = ImageDraw.Draw(canvas1)

d1.text((20, 10), "EKRAN 1: STOK YÖNETİM SİSTEMİ ANA EKRAN KONTROLLERİ VE KOMUTLARI", fill='#0f172a', font=font_header)

# Sağ taraftaki Callout'lar ve ekran üzerine işaretleme
# Ok 1: Dashboard
draw_arrow(d1, (1140, 100), (450, 140), color='#2563eb', width=3)
draw_callout(d1, (1140, 70, 430, 65), "1. CANLI DASHBOARD (ÖZET KARTLARI)", 
             "Toplam urun, stok adedi, kritik stoktaki urunler ve mali deger.\nSabit degildir; generic List<Urun> uzerinden dinamik hesaplanir.", 
             themes['blue'], font_bold, font_regular)

# Ok 2: Arama ve Filtre
draw_arrow(d1, (1140, 190), (320, 205), color='#059669', width=3)
draw_callout(d1, (1140, 160, 430, 65), "2. CANLI ARAMA & KATEGORI FILTRESI", 
             "txtArama_TextChanged ile anlik urun adi/kodu aramasi yapilir.\nComboBox ile Elektronik, Gida ve Giyim filtrelemesi saglanir.", 
             themes['green'], font_bold, font_regular)

# Ok 3: Kritik Stok Kutusu & Tablo Vurgusu
draw_arrow(d1, (1140, 280), (660, 205), color='#dc2626', width=3)
draw_arrow(d1, (1140, 310), (450, 290), color='#dc2626', width=3)
draw_callout(d1, (1140, 250, 430, 75), "3. KRITIK STOK FILTRESI VE RENKLI VURGU", 
             "chkKritikFiltre tiklandiginda sadece kritik seviyedekiler listelenir.\nTabloda kritik seviyenin altindaki urunler kirmizi arka planla\nvurgulanarak satinalma uyarisi verilir.", 
             themes['red'], font_bold, font_regular)

# Ok 4: Polymorphic Detay Sütunu
draw_arrow(d1, (1140, 400), (950, 310), color='#7e22ce', width=3)
draw_callout(d1, (1140, 360, 430, 80), "4. POLIMORFIK DETAY SUTUNU (OOP)", 
             "DetayBilgisiGetir() soyut (abstract) metodunun sonucudur.\nElektronik urunde 'Marka/Garanti', Gidada 'STT/Soguk Zincir',\nGiyimde 'Beden/Kumas' dinamik olarak tablodan gosterilir.", 
             themes['purple'], font_bold, font_regular)

# Ok 5: CRUD Butonları
draw_arrow(d1, (1140, 520), (220, 725), color='#ea580c', width=3)
draw_callout(d1, (1140, 480, 430, 75), "5. URUN YONETIMI BUTONLARI (CRUD)", 
             "+ Yeni Urun Ekle: Dialog formunu acarak polimorfik urun ekler.\nUrun Duzenle / Urun Sil: Secili kaydi gunceller veya bellekten kaldirir.\nAyni urun kodunun tekrar eklenmesi engellenir.", 
             themes['orange'], font_bold, font_regular)

# Ok 6: Stok Giriş & Çıkış Butonları
draw_arrow(d1, (1140, 640), (870, 725), color='#16a34a', width=3)
draw_callout(d1, (1140, 600, 430, 75), "6. STOK GIRIS (+) VE STOK CIKIS (-) ISLEMLERI", 
             "Secilen urunun stogunu artirir veya guvenli sekilde dusurur.\n0'dan buyuk olma ve yetersiz stok bakiye kontrolleri yapilarak\nnegatif stok olusmasi kesin olarak engellenir.", 
             themes['green'], font_bold, font_regular)

canvas1.save(os.path.join(out_dir, "01_Oklu_AnaEkran_Rehberi.png"))

# =========================================================================
# 2. GÖRSEL: YENİ ÜRÜN EKLEME EKRANI (OKLARLA İŞLEV ANLATIMI)
# =========================================================================
img2_raw = Image.open(os.path.join(base_shots, "02_YeniUrun_EklemeEkrani.png"))
canvas2 = Image.new('RGB', (1050, 600), color='#f8fafc')
canvas2.paste(img2_raw, (30, 40))
d2 = ImageDraw.Draw(canvas2)

d2.text((30, 10), "EKRAN 2: YENİ ÜRÜN EKLEME FORMU VE DOĞRULAMA (VALIDATION) KOMUTLARI", fill='#0f172a', font=font_header)

draw_arrow(d2, (500, 100), (320, 100), color='#dc2626', width=3)
draw_callout(d2, (500, 70, 520, 60), "1. URUN KODU VE BENZERSIZLIK KONTROLU", 
             "Bos birakilamaz kontrolu yapilir (string.IsNullOrWhiteSpace).\nSistemde onceden kayitli bir kod girilirse kayit engellenir.", 
             themes['red'], font_bold, font_regular)

draw_arrow(d2, (500, 175), (320, 170), color='#2563eb', width=3)
draw_callout(d2, (500, 145, 520, 65), "2. KATEGORI SECIMI (DINAMIK OOP ENJEKSIYONU)", 
             "Secilen kategoriye gore (Elektronik, Gida, Giyim) alt paneller\ndinamik acilir ve ilgili somut sinif (Derived Class) new'lenir.", 
             themes['blue'], font_bold, font_regular)

draw_arrow(d2, (500, 255), (320, 240), color='#059669', width=3)
draw_callout(d2, (500, 225, 520, 65), "3. KAPSULLEME & NEGATIF DEGER KORUMASI", 
             "Birim Fiyat ve Stok Miktari alanlari NumericUpDown ile korunur.\nOOP set bloklarindaki 'if (value < 0)' ile negatif veri engellenir.", 
             themes['green'], font_bold, font_regular)

draw_arrow(d2, (500, 345), (320, 335), color='#7e22ce', width=3)
draw_callout(d2, (500, 310, 520, 65), "4. KATEGORIYE OZGU EK ALANLAR (KALITIM)", 
             "Elektronik icin Marka & Garanti, Gida icin Son Tuketim Tarihi,\nGiyim icin Beden ve Kumas ozellikleri kalitilan sinifta toplanir.", 
             themes['purple'], font_bold, font_regular)

draw_arrow(d2, (500, 465), (280, 455), color='#ea580c', width=3)
draw_callout(d2, (500, 435, 520, 65), "5. DOGRULAMA VE KAYIT ISLEMI (btnKaydet_Click)", 
             "Try-catch bloklariyla veriler denetlenir; basariliysa StokYonetici'ye\neksiksiz aktarilir ve islem logu olusturulur.", 
             themes['orange'], font_bold, font_regular)

canvas2.save(os.path.join(out_dir, "02_Oklu_UrunEkleme_Rehberi.png"))

# =========================================================================
# 3. GÖRSEL: STOK GİRİŞ VE ÇIKIŞ İŞLEMLERİ (OKLARLA İŞLEV ANLATIMI)
# =========================================================================
img3_raw = Image.open(os.path.join(base_shots, "03_StokGiris_Ekrani.png"))
img4_raw = Image.open(os.path.join(base_shots, "04_StokCikis_Ekrani.png"))

canvas3 = Image.new('RGB', (1200, 680), color='#f8fafc')
canvas3.paste(img3_raw, (40, 50))
canvas3.paste(img4_raw, (40, 380))
d3 = ImageDraw.Draw(canvas3)

d3.text((40, 15), "EKRAN 3: STOK GİRİŞ (+) VE STOK ÇIKIŞ (-) GÜVENLİK KOMUTLARI", fill='#0f172a', font=font_header)

draw_arrow(d3, (500, 110), (320, 120), color='#16a34a', width=3)
draw_callout(d3, (500, 80, 660, 65), "1. STOK GIRISI (+) MIKTAR DOGRULAMASI", 
             "Girilecek miktar mutlaka 0'dan buyuk olmalidir (miktar > 0).\nOnaylandiginda urunun mevcut stogu artirilir ve IslemKaydi olusur.", 
             themes['green'], font_bold, font_regular)

draw_arrow(d3, (500, 220), (320, 215), color='#2563eb', width=3)
draw_callout(d3, (500, 190, 660, 65), "2. ISLEM ACIKLAMASI VE DENETIM IZI", 
             "Tedarikci, fatura no veya sevkiyat bilgisi serbest metin olarak girilir.\nTum hareketler tarih/saat damgasiyla gecmise kaydedilir.", 
             themes['blue'], font_bold, font_regular)

draw_arrow(d3, (500, 440), (320, 450), color='#dc2626', width=3)
draw_callout(d3, (500, 410, 660, 75), "3. STOK CIKISI (-) YETERSIZ STOK VE BAKIYE KORUMASI", 
             "Mevcut stoktan (ornegin 12 adetten) daha fazla cikis yapilmasina izin verilmez!\nNumericUpDown.Maximum degeri dinamik olarak urunun mevcut stoguna sinirlanir.\nBoylece eksi/negatif stok riski %100 engellenir.", 
             themes['red'], font_bold, font_regular)

draw_arrow(d3, (500, 560), (280, 600), color='#dc2626', width=3)
draw_callout(d3, (500, 530, 660, 65), "4. STOK DUSURME ONAYI (btnOnayla_Click)", 
             "Urun.StokCikis(miktar) metodu tetiklenir. Basarili cikis sonrasi ana ekrandaki\ntoplam stok ve dashboard istatistikleri aninda guncellenir.", 
             themes['red'], font_bold, font_regular)

canvas3.save(os.path.join(out_dir, "03_Oklu_StokHareketleri_Rehberi.png"))

# =========================================================================
# 4. GÖRSEL: DENETİM İZİ VE İŞLEM GEÇMİŞİ (OKLARLA İŞLEV ANLATIMI)
# =========================================================================
img6_raw = Image.open(os.path.join(base_shots, "06_StokHareketleriGecmisi.png"))
canvas4 = Image.new('RGB', (1600, 780), color='#f8fafc')
canvas4.paste(img6_raw, (20, 40))
d4 = ImageDraw.Draw(canvas4)

d4.text((20, 10), "EKRAN 4: STOK HAREKETLERİ GEÇMİŞİ VE DENETİM İZİ (AUDIT LOG)", fill='#0f172a', font=font_header)

draw_arrow(d4, (1140, 120), (280, 205), color='#2563eb', width=3)
draw_callout(d4, (1140, 80, 430, 70), "1. OTOMATIK TARIH VE ZAMAN DAMGASI", 
             "IslemKaydi olusturuldugu anda DateTime.Now ile sistem saati\nsaniyesine kadar kaydedilir ve siralama en guncelden baslar.", 
             themes['blue'], font_bold, font_regular)

draw_arrow(d4, (1140, 260), (320, 270), color='#7e22ce', width=3)
draw_callout(d4, (1140, 220, 430, 75), "2. ISLEM TURU (ENUM ISLEMTURU)", 
             "UrunEkleme, UrunGuncelleme, UrunSilme, StokGiris ve StokCikis\nislem turleri C# Enum yapisi ile tip guvenli olarak saklanir.", 
             themes['purple'], font_bold, font_regular)

draw_arrow(d4, (1140, 400), (620, 310), color='#059669', width=3)
draw_callout(d4, (1140, 360, 430, 75), "3. ISLEM MIKTARI VE URUN DETAYI", 
             "Hangi urunden kac adet girildigi veya dusuldugu kayit altina alinir.\nHerhangi bir veri kaybi veya karisiklik yasanmaz.", 
             themes['green'], font_bold, font_regular)

draw_arrow(d4, (1140, 540), (820, 310), color='#ea580c', width=3)
draw_callout(d4, (1140, 500, 430, 75), "4. ACIKLAMA VE NOT BILGISI", 
             "Kullanicinin islem yaparken girdigi notlar (Tedarikci, Musteri satisi vb.)\ndenetim amacli goruntulenir.", 
             themes['orange'], font_bold, font_regular)

canvas4.save(os.path.join(out_dir, "04_Oklu_DenetimIzi_Rehberi.png"))

print("Tum oklu gorseller basariyla uretildi!")
