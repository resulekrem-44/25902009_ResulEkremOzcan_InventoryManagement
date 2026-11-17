# -*- coding: utf-8 -*-
import os
import math
from PIL import Image, ImageDraw, ImageFont

def draw_stylish_arrow(draw, start, end, color='#2563eb', width=3, arrow_len=14):
    x0, y0 = start
    x1, y1 = end
    
    # Başlangıç noktasına şık bir hedef daire/nokta koy
    draw.ellipse([x0-4, y0-4, x0+4, y0+4], fill=color, outline='#ffffff', width=1)
    
    # Çizgi
    draw.line([start, end], fill=color, width=width)
    
    # Ok Başı
    angle = math.atan2(y1 - y0, x1 - x0)
    angle1 = angle + math.pi - math.pi / 5.5
    angle2 = angle + math.pi + math.pi / 5.5
    
    p1 = (x1 + arrow_len * math.cos(angle1), y1 + arrow_len * math.sin(angle1))
    p2 = (x1 + arrow_len * math.cos(angle2), y1 + arrow_len * math.sin(angle2))
    draw.polygon([end, p1, p2], fill=color)

def draw_badge_card(draw, rect, badge_num, title, lines, color_theme, font_num, font_title, font_body):
    x, y, w, h = rect
    bg = color_theme['bg']
    border = color_theme['border']
    primary = color_theme['primary']
    text_color = color_theme['text']
    
    # Gölge efekti
    draw.rounded_rectangle([x+3, y+3, x+w+3, y+h+3], radius=10, fill='#e2e8f0')
    # Ana Kart
    draw.rounded_rectangle([x, y, x+w, y+h], radius=10, fill=bg, outline=border, width=2)
    
    # Rozet (Numara Çemberi)
    bx, by, br = x + 24, y + 24, 14
    draw.ellipse([bx-br, by-br, bx+br, by+br], fill=primary)
    
    # Rozet Numarası (Merkezleme)
    draw.text((bx-5, by-8), str(badge_num), fill='#ffffff', font=font_num)
    
    # Başlık
    draw.text((x + 48, y + 14), title, fill=primary, font=font_title)
    
    # Açıklama Metinleri
    cur_y = y + 42
    for line in lines:
        draw.text((x + 16, cur_y), line, fill=text_color, font=font_body)
        cur_y += 18

base_shots = r"C:\Users\ahmet\OneDrive\Desktop\.NET PROJE ÖDEVİ\25902009_ResulEkremOzcan_InventoryManagement\Screenshots"
out_dir = r"C:\Users\ahmet\OneDrive\Desktop\.NET PROJE ÖDEVİ\25902009_ResulEkremOzcan_InventoryManagement\03_Report\Gorseller"
os.makedirs(out_dir, exist_ok=True)

# Fontlar
try:
    f_header = ImageFont.truetype("arialbd.ttf", 20)
    f_sub = ImageFont.truetype("arial.ttf", 13)
    f_num = ImageFont.truetype("arialbd.ttf", 13)
    f_title = ImageFont.truetype("arialbd.ttf", 13)
    f_body = ImageFont.truetype("arial.ttf", 11)
except:
    f_header = ImageFont.load_default()
    f_sub = ImageFont.load_default()
    f_num = ImageFont.load_default()
    f_title = ImageFont.load_default()
    f_body = ImageFont.load_default()

themes = {
    'blue':   {'bg': '#f8faff', 'border': '#3b82f6', 'primary': '#1d4ed8', 'text': '#1e293b'},
    'green':  {'bg': '#f6fdf8', 'border': '#22c55e', 'primary': '#15803d', 'text': '#1e293b'},
    'red':    {'bg': '#fef7f7', 'border': '#ef4444', 'primary': '#b91c1c', 'text': '#1e293b'},
    'purple': {'bg': '#faf6ff', 'border': '#a855f7', 'primary': '#7e22ce', 'text': '#1e293b'},
    'amber':  {'bg': '#fffbf0', 'border': '#f59e0b', 'primary': '#b45309', 'text': '#1e293b'}
}

# =========================================================================
# GÖRSEL 1: ANA EKRAN KULLANIM & KONTROL REHBERİ
# =========================================================================
img1_raw = Image.open(os.path.join(base_shots, "01_AnaEkran_GenelGörünüm.png"))
w_raw, h_raw = img1_raw.size
canvas1 = Image.new('RGB', (w_raw + 480, h_raw + 100), color='#f1f5f9')
d1 = ImageDraw.Draw(canvas1)

# Üst Başlık Şeridi
d1.rectangle([0, 0, canvas1.width, 60], fill='#0f172a')
d1.text((30, 12), "STOK YÖNETİM SİSTEMİ • ANA EKRAN BİLEŞENLERİ VE KONTROL REHBERİ", fill='#ffffff', font=f_header)
d1.text((30, 36), "Resul Ekrem ÖZCAN - 25902009 | BGT331 .NET Programlama - I", fill='#94a3b8', font=f_sub)

# Ekranı Yapıştır
canvas1.paste(img1_raw, (30, 80))

# Sağdaki Dialog/Açıklama Kartları
cx = w_raw + 50
draw_badge_card(d1, (cx, 80, 430, 95), 1, "CANLI DASHBOARD KARTLARI", [
    "• Toplam Urun, Toplam Stok, Kritik Stok ve Envanter Tutari.",
    "• Sabit sayi degildir; generic List<Urun> uzerinden dinamik",
    "  formuller ve LINQ sorgulari ile her islemde guncellenir."
], themes['blue'], f_num, f_title, f_body)
draw_stylish_arrow(d1, (450, 195), (cx, 125), color='#1d4ed8', width=3)

draw_badge_card(d1, (cx, 195, 430, 95), 2, "CANLI ARAMA & KATEGORI FILTRESI", [
    "• txtArama ile ad veya kod yazildikca liste aninda suzulur.",
    "• ComboBox ile Elektronik, Gida ve Giyim kategorilerine gore",
    "  tek tikla filtreleme yapilir. Filtreleri Temizle ile sifirlanir."
], themes['green'], f_num, f_title, f_body)
draw_stylish_arrow(d1, (400, 260), (cx, 240), color='#15803d', width=3)

draw_badge_card(d1, (cx, 310, 430, 105), 3, "KRITIK STOK FILTRESI & RENK VURGUSU", [
    "• Kritik stok sinirinin altindaki urunler tabloda acik kirmizi",
    "  renkle boyanarak yoneticiye acil tedarik uyarisi verir.",
    "• Onay kutusu secildiginde sadece kritik urunler listelenir."
], themes['red'], f_num, f_title, f_body)
draw_stylish_arrow(d1, (500, 370), (cx, 360), color='#b91c1c', width=3)

draw_badge_card(d1, (cx, 435, 430, 105), 4, "POLIMORFIK DETAY SUTUNU (OOP)", [
    "• DetayBilgisiGetir() soyut metodunun polimorfik cagrisidir.",
    "• Elektronik icin 'Marka & Garanti', Gida icin 'STT & Soguk",
    "  Zincir', Giyim icin 'Beden & Kumas' bilgisi dinamik gosterilir."
], themes['purple'], f_num, f_title, f_body)
draw_stylish_arrow(d1, (w_raw - 120, 380), (cx, 485), color='#7e22ce', width=3)

draw_badge_card(d1, (cx, 560, 430, 95), 5, "URUN YONETIMI BUTONLARI (CRUD)", [
    "• Yeni Urun Ekle: FormUrunEkleGuncelle diyalogunu acar.",
    "• Urun Duzenle & Urun Sil: Secili kaydi gunceller veya siler.",
    "• Mukerrer kod kontrolu ile ayni kodun eklenmesi engellenir."
], themes['amber'], f_num, f_title, f_body)
draw_stylish_arrow(d1, (200, h_raw + 40), (cx, 605), color='#b45309', width=3)

draw_badge_card(d1, (cx, 675, 430, 105), 6, "STOK GIRIS (+) VE CIKIS (-) ISLEMLERI", [
    "• Secili urunun stogunu kontrollu artirir veya guvenle dusurur.",
    "• Miktar 0, 000 veya negatif girilemez; aciklama zorunludur.",
    "• Yetersiz bakiye kilidiyle eksi stok riski kesin olarak engellenir."
], themes['green'], f_num, f_title, f_body)
draw_stylish_arrow(d1, (w_raw - 120, h_raw + 40), (cx, 725), color='#15803d', width=3)

canvas1.save(os.path.join(out_dir, "01_AnaEkran_Rehberi.png"))

# =========================================================================
# GÖRSEL 2: YENİ ÜRÜN EKLEME / GÜNCELLEME DİYALOG REHBERİ
# =========================================================================
img2_raw = Image.open(os.path.join(base_shots, "02_YeniUrun_EklemeEkrani.png"))
w2_raw, h2_raw = img2_raw.size
canvas2 = Image.new('RGB', (w2_raw + 520, h2_raw + 100), color='#f1f5f9')
d2 = ImageDraw.Draw(canvas2)

d2.rectangle([0, 0, canvas2.width, 60], fill='#0f172a')
d2.text((30, 12), "ÜRÜN EKLEME VE DOĞRULAMA (VALIDATION) REHBERİ", fill='#ffffff', font=f_header)
d2.text((30, 36), "FormUrunEkleGuncelle • Kapsülleme ve Veri Bütünlüğü Doğrulamaları", fill='#94a3b8', font=f_sub)

canvas2.paste(img2_raw, (30, 80))

cx2 = w2_raw + 50
draw_badge_card(d2, (cx2, 90, 480, 85), 1, "BENZERSIZ URUN KODU VE UZUNLUK KONTROLU", [
    "• string.IsNullOrWhiteSpace kontrolu ile bos birakilamaz.",
    "• En az 2 karakter olmali ve @, #, $, % gibi ozel karakterler",
    "  kesinlikle engellenir. Mukerrer/ayni kod eklenemez."
], themes['red'], f_num, f_title, f_body)
draw_stylish_arrow(d2, (340, 140), (cx2, 130), color='#b91c1c', width=3)

draw_badge_card(d2, (cx2, 195, 480, 85), 2, "KATEGORI SECIMI VE DINAMIK KALITIM PANELİ", [
    "• Kategori secildiginde alt panel dinamik olarak degisir.",
    "• Elektronik ise Marka/Garanti, Gida ise STT/Soguk Zincir,",
    "  Giyim ise Beden/Kumas panel kontrolleri gorunur hale gelir."
], themes['blue'], f_num, f_title, f_body)
draw_stylish_arrow(d2, (340, 215), (cx2, 235), color='#1d4ed8', width=3)

draw_badge_card(d2, (cx2, 300, 480, 85), 3, "KAPSULLEME: 0 TL VE NEGATIF FIYAT KORUMASI", [
    "• NumericUpDown kontrolu ile yalnizca sayisal giris yapilir.",
    "• Urun.cs kapsulleme katmaninda fiyat <= 0 ise sistem hata",
    "  firlatir; bedelsiz veya eksi fiyatli urun eklenemez."
], themes['green'], f_num, f_title, f_body)
draw_stylish_arrow(d2, (340, 255), (cx2, 340), color='#15803d', width=3)

draw_badge_card(d2, (cx2, 405, 480, 85), 4, "POLIMORFIK ALANLAR VE GUCLU VALIDASYON", [
    "• Marka, Beden ve Kumas alanlarina zararli ozel karakterlerin",
    "  girisi regex filtreleri ile engellenerek veri guvenligi saglanir."
], themes['purple'], f_num, f_title, f_body)
draw_stylish_arrow(d2, (340, 390), (cx2, 445), color='#7e22ce', width=3)

draw_badge_card(d2, (cx2, 510, 480, 80), 5, "KAYDET VE DOGRULAMA (btnKaydet_Click)", [
    "• Try-Catch bloklari altinda somut alt sinif (Derived Class)",
    "  new'lenerek StokYonetici listesine guvenle dahil edilir."
], themes['amber'], f_num, f_title, f_body)
draw_stylish_arrow(d2, (260, h2_raw + 20), (cx2, 550), color='#b45309', width=3)

canvas2.save(os.path.join(out_dir, "02_UrunEkleme_Rehberi.png"))

# =========================================================================
# GÖRSEL 3: STOK GİRİŞ VE ÇIKIŞ GÜVENLİK DİYALOGLARI
# =========================================================================
img3_raw = Image.open(os.path.join(base_shots, "03_StokGiris_Ekrani.png"))
img4_raw = Image.open(os.path.join(base_shots, "04_StokCikis_Ekrani.png"))

w3_raw, h3_raw = img3_raw.size
canvas3 = Image.new('RGB', (w3_raw + 550, h3_raw * 2 + 130), color='#f1f5f9')
d3 = ImageDraw.Draw(canvas3)

d3.rectangle([0, 0, canvas3.width, 60], fill='#0f172a')
d3.text((30, 12), "STOK HAREKETLERİ • GİRİŞ (+) VE ÇIKIŞ (-) GÜVENLİK DİYALOGLARI", fill='#ffffff', font=f_header)
d3.text((30, 36), "FormStokIslem • 0, 000 Engeli, Yetersiz Bakiye Kilidi ve Denetim İzi", fill='#94a3b8', font=f_sub)

canvas3.paste(img3_raw, (30, 80))
canvas3.paste(img4_raw, (30, 80 + h3_raw + 30))

cx3 = w3_raw + 50
draw_badge_card(d3, (cx3, 90, 500, 95), 1, "STOK GIRISI (+) VE 0 / 000 MIKTAR ENGELI", [
    "• Miktar alanina 0, 00, 000 veya gecersiz giris yapilmasi",
    "  int.TryParse ve <= 0 kontrolleri ile tamamen engellenmistir.",
    "• Girilen miktar kadar urun stogu dogrudan artirilir."
], themes['green'], f_num, f_title, f_body)
draw_stylish_arrow(d3, (280, 205), (cx3, 135), color='#15803d', width=3)

draw_badge_card(d3, (cx3, 205, 500, 95), 2, "ZORUNLU ACIKLAMA VE OZEL KARAKTER FILTRESI", [
    "• Tedarikci, fatura no veya sevk bilgisi girilmesi zorunludur.",
    "• Aciklamaya @, #, $, <, > gibi yabanci karakterler girilemez;",
    "  denetim izi kayitlarinin temiz kalmasi saglanir."
], themes['blue'], f_num, f_title, f_body)
draw_stylish_arrow(d3, (280, 245), (cx3, 250), color='#1d4ed8', width=3)

draw_badge_card(d3, (cx3, 440, 500, 105), 3, "STOK CIKISI (-) VE YETERSIZ BAKIYE KILIDI", [
    "• Mevcut stoktan (ornegin 12 adetten) daha fazla cikis yapilamaz!",
    "• numMiktar.Maximum degeri urunun eldeki stoguna sinirlanir.",
    "• if (miktar > StokMiktari) kontrolu ile eksiye dusus imkansizdir."
], themes['red'], f_num, f_title, f_body)
draw_stylish_arrow(d3, (280, 440 + h3_raw - 120), (cx3, 490), color='#b91c1c', width=3)

draw_badge_card(d3, (cx3, 565, 500, 95), 4, "ANLIK DUSUM VE ISLEM KAYDI OLUSTURMA", [
    "• Urun.StokCikis(miktar) metodu basariyla tamamlandiginda",
    "  stok aninda duser ve denetim sekmesine IslemKaydi yazilir.",
    "• Ana ekrandaki Dashboard sayilari aninda guncellenir."
], themes['amber'], f_num, f_title, f_body)
draw_stylish_arrow(d3, (220, 440 + h3_raw - 20), (cx3, 610), color='#b45309', width=3)

canvas3.save(os.path.join(out_dir, "03_StokHareketleri_Rehberi.png"))

# =========================================================================
# GÖRSEL 4: STOK DENETİM İZİ (AUDIT LOG) REHBERİ
# =========================================================================
img6_raw = Image.open(os.path.join(base_shots, "06_StokHareketleriGecmisi.png"))
w6_raw, h6_raw = img6_raw.size
canvas4 = Image.new('RGB', (w6_raw + 480, h6_raw + 100), color='#f1f5f9')
d4 = ImageDraw.Draw(canvas4)

d4.rectangle([0, 0, canvas4.width, 60], fill='#0f172a')
d4.text((30, 12), "STOK HAREKETLERİ GEÇMİŞİ VE DENETİM İZİ (AUDIT LOG) REHBERİ", fill='#ffffff', font=f_header)
d4.text((30, 36), "IslemKaydi • Yapılan Her İşlemin Tarih, Saat, Tür ve Miktar Takibi", fill='#94a3b8', font=f_sub)

canvas4.paste(img6_raw, (30, 80))

cx4 = w6_raw + 50
draw_badge_card(d4, (cx4, 120, 430, 95), 1, "KESIN ZAMAN DAMGASI (DateTime.Now)", [
    "• Yapilan tum ekleme, guncelleme, silme ve stok islemleri",
    "  saniyesine kadar tarih/saat damgasiyla kayit altina alinir.",
    "• Tabloda en son gerceklesen islem en ustte listelenir."
], themes['blue'], f_num, f_title, f_body)
draw_stylish_arrow(d4, (120, 260), (cx4, 165), color='#1d4ed8', width=3)

draw_badge_card(d4, (cx4, 250, 430, 95), 2, "TIP GUVENLI ISLEM TURLERI (ENUM)", [
    "• IslemTuru enum yapisi (UrunEkleme, UrunGuncelleme,",
    "  UrunSilme, StokGiris, StokCikis) sayesinde veriler tip",
    "  guvenli olarak saklanir ve yonetilir."
], themes['purple'], f_num, f_title, f_body)
draw_stylish_arrow(d4, (240, 260), (cx4, 295), color='#7e22ce', width=3)

draw_badge_card(d4, (cx4, 380, 430, 95), 3, "URUN VE MIKTAR DETAYLARI", [
    "• Hangi urun kodunda kac adet degisiklik oldugu seffafca",
    "  sunulur. Stok tutarsizliklari kolaylikla takip edilebilir."
], themes['green'], f_num, f_title, f_body)
draw_stylish_arrow(d4, (550, 260), (cx4, 425), color='#15803d', width=3)

draw_badge_card(d4, (cx4, 510, 430, 95), 4, "DENETIM ACIKLAMALARI VE SUREC TAKIBI", [
    "• Kullanicinin islem aninda girdigi tedarikci, musteri veya",
    "  sistem aciklamalari raporlanir; tam denetim izi saglanir."
], themes['amber'], f_num, f_title, f_body)
draw_stylish_arrow(d4, (850, 260), (cx4, 555), color='#b45309', width=3)

canvas4.save(os.path.join(out_dir, "04_DenetimIzi_Rehberi.png"))

print("Tum yeni nesil diyalog kartli rehber gorselleri basariyla uretildi!")
