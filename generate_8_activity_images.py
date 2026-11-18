# -*- coding: utf-8 -*-
import os
import math
from PIL import Image, ImageDraw, ImageFont

def draw_pointer_arrow(draw, start, end, color='#2563eb', width=3, arrow_len=14):
    x0, y0 = start
    x1, y1 = end
    
    # Başlangıç noktasına şık beyaz kenarlıklı daire
    draw.ellipse([x0-4, y0-4, x0+4, y0+4], fill=color, outline='#ffffff', width=2)
    # Çizgi
    draw.line([start, end], fill=color, width=width)
    
    # Ok Başı
    angle = math.atan2(y1 - y0, x1 - x0)
    angle1 = angle + math.pi - math.pi / 5.5
    angle2 = angle + math.pi + math.pi / 5.5
    
    p1 = (x1 + arrow_len * math.cos(angle1), y1 + arrow_len * math.sin(angle1))
    p2 = (x1 + arrow_len * math.cos(angle2), y1 + arrow_len * math.sin(angle2))
    draw.polygon([end, p1, p2], fill=color)

def draw_card(draw, rect, badge_num, title, lines, theme, font_num, font_title, font_body):
    x, y, w, h = rect
    bg = theme['bg']
    border = theme['border']
    primary = theme['primary']
    text_color = theme['text']
    
    # Yumuşak gölge
    draw.rounded_rectangle([x+3, y+3, x+w+3, y+h+3], radius=10, fill='#e2e8f0')
    # Ana Kart
    draw.rounded_rectangle([x, y, x+w, y+h], radius=10, fill=bg, outline=border, width=2)
    
    # Rozet (Badge) Dairesi
    bx, by, br = x + 24, y + 24, 14
    draw.ellipse([bx-br, by-br, bx+br, by+br], fill=primary)
    draw.text((bx-5, by-8), str(badge_num), fill='#ffffff', font=font_num)
    
    # Başlık
    draw.text((x + 48, y + 14), title, fill=primary, font=font_title)
    
    # Satırlar
    cur_y = y + 42
    for line in lines:
        draw.text((x + 16, cur_y), line, fill=text_color, font=font_body)
        cur_y += 18

desktop = os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop')
proj_dir = os.path.join(desktop, '.NET PROJE ÖDEVİ', '25902009_ResulEkremOzcan_InventoryManagement')
raw_dir = os.path.join(proj_dir, 'Screenshots_Raw')
out_dir = os.path.join(proj_dir, '03_Report', 'Gorseller')
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
# AKTİVİTE 1: ANA EKRAN VE GENEL YÖNETİM
# =========================================================================
raw1 = Image.open(os.path.join(raw_dir, "01_AnaEkran.png"))
w1, h1 = raw1.size
c1 = Image.new('RGB', (w1 + 480, h1 + 100), color='#f1f5f9')
d1 = ImageDraw.Draw(c1)
d1.rectangle([0, 0, c1.width, 60], fill='#0f172a')
d1.text((30, 12), "AKTİVİTE 1: ANA EKRAN, CANLI DASHBOARD VE YÖNETİM MERKEZİ", fill='#ffffff', font=f_header)
d1.text((30, 36), "Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009) • .NET Programlama - I", fill='#94a3b8', font=f_sub)
c1.paste(raw1, (30, 80))

cx = w1 + 50
draw_card(d1, (cx, 80, 430, 95), 1, "CANLI DASHBOARD KARTLARI", [
    "• Toplam Urun, Toplam Stok, Kritik Urun ve Envanter Degeri.",
    "• Sabit degil; generic List<Urun> uzerinde LINQ Count() ve",
    "  Sum(u => u.ToplamDegerHesapla()) ile canli hesaplanir."
], themes['blue'], f_num, f_title, f_body)
draw_pointer_arrow(d1, (450, 195), (cx, 125), color='#1d4ed8')

draw_card(d1, (cx, 195, 430, 95), 2, "FILTRELEME VE ARAMA PANELİ", [
    "• Urun adi/koduna gore harf yazildikca canli arama yapilir.",
    "• Kategori acilir kutusu ile Elektronik, Gida ve Giyim suzulur.",
    "• 'Filtreleri Temizle' butonu ile aninda ilk duruma donulur."
], themes['green'], f_num, f_title, f_body)
draw_pointer_arrow(d1, (400, 260), (cx, 240), color='#15803d')

draw_card(d1, (cx, 310, 430, 105), 3, "KRITIK STOK GORSEL UYARISI", [
    "• Kritik stok sinirinin altindaki urunler acik kirmizi arka",
    "  plan rengi ile boyanarak satinalma uyarisi verilir.",
    "• Onay kutusu secildiginde sadece kritik urunler süzülür."
], themes['red'], f_num, f_title, f_body)
draw_pointer_arrow(d1, (500, 370), (cx, 360), color='#b91c1c')

draw_card(d1, (cx, 435, 430, 105), 4, "POLIMORFIK DETAY KOLONU (OOP)", [
    "• DetayBilgisiGetir() soyut metodunun dinamik cagrisidir.",
    "• Elektronikte Marka/Garanti, Gidada STT/Soguk Zincir,",
    "  Giyimde Beden/Kumas bilgisi ayni kolonda listelenir."
], themes['purple'], f_num, f_title, f_body)
draw_pointer_arrow(d1, (w1 - 120, 380), (cx, 485), color='#7e22ce')

draw_card(d1, (cx, 560, 430, 95), 5, "CRUD ISLEM BUTONLARI", [
    "• Yeni Urun Ekle: FormUrunEkleGuncelle ekranini acar.",
    "• Urun Duzenle / Sil: Secili kaydi gunceller veya kaldirir.",
    "• Mukerrer/ayni kod eklenmesi sistem tarafindan engellenir."
], themes['amber'], f_num, f_title, f_body)
draw_pointer_arrow(d1, (200, h1 + 40), (cx, 605), color='#b45309')

draw_card(d1, (cx, 675, 430, 105), 6, "STOK GIRIS (+) VE CIKIS (-) ISLEMLERI", [
    "• Secili urune kontrollu stok artisi veya azilisi yapilir.",
    "• Miktara 0, 000 veya negatif deger girilmesi engellenir.",
    "• Yetersiz bakiye kilidiyle eksi stok riski kesin olarak onlenir."
], themes['green'], f_num, f_title, f_body)
draw_pointer_arrow(d1, (w1 - 120, h1 + 40), (cx, 725), color='#15803d')

c1.save(os.path.join(out_dir, "01_AnaEkran_Rehberi.png"))

# =========================================================================
# AKTİVİTE 2: CANLI ARAMA VE SÜZME
# =========================================================================
raw2 = Image.open(os.path.join(raw_dir, "02_AramaFiltre.png"))
c2 = Image.new('RGB', (w1 + 480, h1 + 100), color='#f1f5f9')
d2 = ImageDraw.Draw(c2)
d2.rectangle([0, 0, c2.width, 60], fill='#0f172a')
d2.text((30, 12), "AKTİVİTE 2: DİNAMİK ARAMA VE ANLIK ENVANTER SÜZME", fill='#ffffff', font=f_header)
d2.text((30, 36), "txtArama_TextChanged • Harf Yazıldıkça LINQ ile Anlık Filtreleme", fill='#94a3b8', font=f_sub)
c2.paste(raw2, (30, 80))

draw_card(d2, (cx, 160, 430, 110), 1, "CANLI METİN ARAMA (TextChanged)", [
    "• txtArama kutusuna 'Fare' yazildigi anda olay tetiklenir.",
    "• UrunAdi.Contains() veya UrunKodu.Contains() kurali calisir.",
    "• Kullanici butona basmadan tablo aninda süzülür."
], themes['blue'], f_num, f_title, f_body)
draw_pointer_arrow(d2, (250, 260), (cx, 215), color='#1d4ed8')

draw_card(d2, (cx, 310, 430, 110), 2, "ANLIK TABLO VE KAYIT GÖSTERİMİ", [
    "• Sadece aranan kelimeyle eslesen 'ELK-102 Kablosuz Optik",
    "  Fare' kaydi listelenir; diger urunler filtrelenir.",
    "• Veriler bellek icinde (In-Memory) yuksek hizla islenir."
], themes['green'], f_num, f_title, f_body)
draw_pointer_arrow(d2, (450, 370), (cx, 365), color='#15803d')

draw_card(d2, (cx, 460, 430, 110), 3, "FİLTRELERİ TEMİZLEME MEKANİZMASI", [
    "• 'Filtreleri Temizle' butonuna basildiginda arama metni",
    "  temizlenir, kategori 'Tümü' yapilir ve tum liste geri gelir."
], themes['amber'], f_num, f_title, f_body)
draw_pointer_arrow(d2, (w1 - 180, 260), (cx, 515), color='#b45309')

c2.save(os.path.join(out_dir, "02_AramaFiltre_Rehberi.png"))

# =========================================================================
# AKTİVİTE 3: KRİTİK STOK FİLTRESİ
# =========================================================================
raw3 = Image.open(os.path.join(raw_dir, "03_KritikStok.png"))
c3 = Image.new('RGB', (w1 + 480, h1 + 100), color='#f1f5f9')
d3 = ImageDraw.Draw(c3)
d3.rectangle([0, 0, c3.width, 60], fill='#0f172a')
d3.text((30, 12), "AKTİVİTE 3: KRİTİK STOKTAKİ ÜRÜNLERİN GÖRSEL TESPİTİ", fill='#ffffff', font=f_header)
d3.text((30, 36), "chkKritikFiltre_CheckedChanged • Stok <= KritikSeviye Koşulu ve Kırmızı Vurgu", fill='#94a3b8', font=f_sub)
c3.paste(raw3, (30, 80))

draw_card(d3, (cx, 160, 430, 110), 1, "KRİTİK STOK FİLTRESİ KUTUSU", [
    "• 'Sadece Kritik Stok Seviyesindekiler' onay kutusu secilince",
    "  Urun.KritikStoktaMi (StokMiktari <= KritikStokSeviyesi)",
    "  ozelligi 'true' olan tum kayitlar aninda izole edilir."
], themes['red'], f_num, f_title, f_body)
draw_pointer_arrow(d3, (650, 260), (cx, 215), color='#b91c1c')

draw_card(d3, (cx, 310, 430, 110), 2, "GÖRSEL RENKLİ UYARI MEKANİZMASI", [
    "• Kritik stoktaki urunler acik kirmizi arka plan ve koyu",
    "  kirmizi yazi rengi ile boyanir.",
    "• Depo yoneticisinin acil siparis ihtiyacini aninda gormesini saglar."
], themes['red'], f_num, f_title, f_body)
draw_pointer_arrow(d3, (450, 370), (cx, 365), color='#b91c1c')

draw_card(d3, (cx, 460, 430, 110), 3, "DASHBOARD SAYACI İLE TAM UYUM", [
    "• Tablodaki filtrelenen 3 kritik urun, Dashboard'daki",
    "  'KRİTİK STOKTAKİ ÜRÜNLER: 3' degeri ile birebir eslesir."
], themes['blue'], f_num, f_title, f_body)
draw_pointer_arrow(d3, (700, 195), (cx, 515), color='#1d4ed8')

c3.save(os.path.join(out_dir, "03_KritikStok_Rehberi.png"))

# =========================================================================
# AKTİVİTE 4: DENETİM İZİ VE HAREKET GEÇMİŞİ
# =========================================================================
raw4 = Image.open(os.path.join(raw_dir, "04_DenetimIzi.png"))
c4 = Image.new('RGB', (w1 + 480, h1 + 100), color='#f1f5f9')
d4 = ImageDraw.Draw(c4)
d4.rectangle([0, 0, c4.width, 60], fill='#0f172a')
d4.text((30, 12), "AKTİVİTE 4: STOK HAREKETLERİ GEÇMİŞİ VE DENETİM İZİ (AUDIT LOG)", fill='#ffffff', font=f_header)
d4.text((30, 36), "IslemKaydi • Sisteme Yapılan Tüm İşlemlerin Zaman Damgasıyla Takibi", fill='#94a3b8', font=f_sub)
c4.paste(raw4, (30, 80))

draw_card(d4, (cx, 120, 430, 95), 1, "KESİN ZAMAN DAMGASI (DateTime.Now)", [
    "• Yapilan tum ekleme, guncelleme, silme ve stok islemleri",
    "  saniyesine kadar tarih/saat damgasiyla kayit altina alinir.",
    "• Tabloda en son gerceklesen hareket en ustte listelenir."
], themes['blue'], f_num, f_title, f_body)
draw_pointer_arrow(d4, (120, 340), (cx, 165), color='#1d4ed8')

draw_card(d4, (cx, 250, 430, 95), 2, "TİP GÜVENLİ İŞLEM TÜRLERİ (ENUM)", [
    "• IslemTuru enum yapisi (UrunEkleme, UrunGuncelleme,",
    "  UrunSilme, StokGiris, StokCikis) ile tip guvenli takip saglanir."
], themes['purple'], f_num, f_title, f_body)
draw_pointer_arrow(d4, (240, 340), (cx, 295), color='#7e22ce')

draw_card(d4, (cx, 380, 430, 95), 3, "ÜRÜN VE MİKTAR BİLGİSİ", [
    "• Hangi urun kodunda kac adet degisiklik oldugu seffafca",
    "  sunulur. Stok tutarsizliklari aninda tespit edilir."
], themes['green'], f_num, f_title, f_body)
draw_pointer_arrow(d4, (550, 340), (cx, 425), color='#15803d')

draw_card(d4, (cx, 510, 430, 95), 4, "DENETİM AÇIKLAMALARI VE NOTLAR", [
    "• Kullanicinin islem aninda girdigi tedarikci veya musteri",
    "  notlari saklanir; boylece tam izlenebilirlik saglanir."
], themes['amber'], f_num, f_title, f_body)
draw_pointer_arrow(d4, (850, 340), (cx, 555), color='#b45309')

c4.save(os.path.join(out_dir, "04_DenetimIzi_Rehberi.png"))

# =========================================================================
# AKTİVİTE 5: YENİ ÜRÜN EKLEME (ELEKTRONİK)
# =========================================================================
raw5 = Image.open(os.path.join(raw_dir, "05_UrunEkle_Elektronik.png"))
w5, h5 = raw5.size
c5 = Image.new('RGB', (w5 + 520, h5 + 100), color='#f1f5f9')
d5 = ImageDraw.Draw(c5)
d5.rectangle([0, 0, c5.width, 60], fill='#0f172a')
d5.text((30, 12), "AKTİVİTE 5: YENİ ÜRÜN EKLEME VE DOĞRULAMA (VALIDATION)", fill='#ffffff', font=f_header)
d5.text((30, 36), "FormUrunEkleGuncelle • Kapsülleme, Özel Karakter Engeli ve 0 TL Fiyat Koruması", fill='#94a3b8', font=f_sub)
c5.paste(raw5, (30, 80))

cx5 = w5 + 50
draw_card(d5, (cx5, 90, 480, 85), 1, "BENZERSİZ ÜRÜN KODU KONTROLÜ", [
    "• string.IsNullOrWhiteSpace ve en az 2 karakter kurali.",
    "• @, #, $, %, & gibi yabanci karakterler kesinlikle engellenir.",
    "• Sistemde onceden kayitli olan bir kodun tekrar eklenmesi onlenir."
], themes['red'], f_num, f_title, f_body)
draw_pointer_arrow(d5, (340, 140), (cx5, 130), color='#b91c1c')

draw_card(d5, (cx5, 195, 480, 85), 2, "DİNAMİK KATEGORİ SEÇİMİ (KALITIM)", [
    "• Kategori acilir kutusundan secim yapildiginda alt paneller",
    "  dinamik olarak degisir ve ilgili alt sinif somutlastirilir."
], themes['blue'], f_num, f_title, f_body)
draw_pointer_arrow(d5, (340, 215), (cx5, 235), color='#1d4ed8')

draw_card(d5, (cx5, 300, 480, 85), 3, "KAPSÜLLEME: 0 TL VE NEGATİF FİYAT ENGELİ", [
    "• NumericUpDown kontrolu ile sayisal sinirlar belirlenir.",
    "• Urun.cs set blogundaki 'fiyat <= 0' kontrolu ile bedelsiz",
    "  veya negatif fiyatli urun eklenmesi engellenir."
], themes['green'], f_num, f_title, f_body)
draw_pointer_arrow(d5, (340, 255), (cx5, 340), color='#15803d')

draw_card(d5, (cx5, 405, 480, 85), 4, "ELEKTRONİK ALANLARI (Marka / Garanti)", [
    "• ElektronikUrun sinifina ozgu Marka ve Garanti Suresi alanlari",
    "  regex kurallariyla dogrulanarak guvenle alinir."
], themes['purple'], f_num, f_title, f_body)
draw_pointer_arrow(d5, (340, 390), (cx5, 445), color='#7e22ce')

draw_card(d5, (cx5, 510, 480, 80), 5, "KAYIT VE DOĞRULAMA (btnKaydet_Click)", [
    "• Try-Catch bloklari altinda somut nesne uretilir,",
    "  StokYonetici listesine eklenir ve islem logu yazilir."
], themes['amber'], f_num, f_title, f_body)
draw_pointer_arrow(d5, (260, h5 + 20), (cx5, 550), color='#b45309')

c5.save(os.path.join(out_dir, "05_UrunEkle_Elektronik_Rehberi.png"))

# =========================================================================
# AKTİVİTE 6: ÜRÜN BİLGİSİ GÜNCELLEME
# =========================================================================
raw6 = Image.open(os.path.join(raw_dir, "06_UrunDuzenle.png"))
c6 = Image.new('RGB', (w5 + 520, h5 + 100), color='#f1f5f9')
d6 = ImageDraw.Draw(c6)
d6.rectangle([0, 0, c6.width, 60], fill='#0f172a')
d6.text((30, 12), "AKTİVİTE 6: ÜRÜN BİLGİLERİNİ GÜNCELLEME VE VERİ KORUMA", fill='#ffffff', font=f_header)
d6.text((30, 36), "FormUrunEkleGuncelle • Ürün Kodu ve Kategori Değiştirilemez (Read-Only) Koruması", fill='#94a3b8', font=f_sub)
c6.paste(raw6, (30, 80))

draw_card(d6, (cx5, 100, 480, 95), 1, "ÜRÜN KODU KORUMASI (READ-ONLY)", [
    "• Var olan urun duzenlenirken UrunKodu 'ReadOnly = true'",
    "  olarak kilitlenir; sistemdeki kimlik bilgisi bozulamaz."
], themes['red'], f_num, f_title, f_body)
draw_pointer_arrow(d6, (340, 140), (cx5, 145), color='#b91c1c')

draw_card(d6, (cx5, 230, 480, 95), 2, "GÜNCELLENEBİLİR ALANLAR", [
    "• Urun Adi, Birim Fiyat, Kritik Stok Seviyesi ve kategoriye",
    "  ozgu marka/garanti bilgileri kontrollu olarak degistirilir."
], themes['blue'], f_num, f_title, f_body)
draw_pointer_arrow(d6, (340, 220), (cx5, 275), color='#1d4ed8')

draw_card(d6, (cx5, 360, 480, 95), 3, "STOK DEĞİŞİMİ ENGELLİ (KORUMA)", [
    "• Guncelleme formunda stok adedi 'Enabled = false' yapilir.",
    "• Stok miktari bu ekrandan rastgele degistirilemez;",
    "  mutlaka denetimli 'Stok Giris/Cikis' pencereleri kullanilmalidir."
], themes['amber'], f_num, f_title, f_body)
draw_pointer_arrow(d6, (340, 290), (cx5, 405), color='#b45309')

draw_card(d6, (cx5, 490, 480, 95), 4, "GÜNCELLEME LOGU OLUŞTURMA", [
    "• 'Guncelle' butonuna basildiginda degisiklik uygulanir",
    "  ve Denetim İzi sekmesine 'UrunGuncelleme' kaydi duser."
], themes['green'], f_num, f_title, f_body)
draw_pointer_arrow(d6, (260, h5 + 20), (cx5, 535), color='#15803d')

c6.save(os.path.join(out_dir, "06_UrunDuzenle_Rehberi.png"))

# =========================================================================
# AKTİVİTE 7: STOK GİRİŞİ (+)
# =========================================================================
raw7 = Image.open(os.path.join(raw_dir, "07_StokGiris.png"))
w7, h7 = raw7.size
c7 = Image.new('RGB', (w7 + 550, h7 + 100), color='#f1f5f9')
d7 = ImageDraw.Draw(c7)
d7.rectangle([0, 0, c7.width, 60], fill='#0f172a')
d7.text((30, 12), "AKTİVİTE 7: STOK GİRİŞ İŞLEMİ (+) VE 0 / 000 MİKTAR ENGELİ", fill='#ffffff', font=f_header)
d7.text((30, 36), "FormStokIslem • Pozitif Miktar Doğrulaması ve Tedarikçi Notu Girişi", fill='#94a3b8', font=f_sub)
c7.paste(raw7, (30, 80))

cx7 = w7 + 50
draw_card(d7, (cx7, 85, 500, 95), 1, "SEÇİLEN ÜRÜN BİLGİ PANELİ", [
    "• Ana ekranda secilen urunun kodu, adi, kategorisi ve",
    "  o anki mevcut stok adedi salt okunur olarak hatirlatilir."
], themes['blue'], f_num, f_title, f_body)
draw_pointer_arrow(d7, (280, 150), (cx7, 130), color='#1d4ed8')

draw_card(d7, (cx7, 195, 500, 105), 2, "0, 00, 000 VE GEÇERSİZ MİKTAR KORUMASI", [
    "• Klavyeden miktar kutusuna '0', '00', '000' yazilmasi",
    "  int.TryParse ve <= 0 kontrolleri ile tamamen engellenmistir.",
    "• Sistem kullanicidan mutlaka en az 1 adet girmesini ister."
], themes['red'], f_num, f_title, f_body)
draw_pointer_arrow(d7, (280, 205), (cx7, 245), color='#b91c1c')

draw_card(d7, (cx7, 315, 500, 95), 3, "ZORUNLU AÇIKLAMA VE GÜVENLİK FİLTRESİ", [
    "• Tedarikci, fatura no veya irsaliye bilgisi yazilmalidir.",
    "• Aciklama alanina zararli kod veya karakter girilemez."
], themes['green'], f_num, f_title, f_body)
draw_pointer_arrow(d7, (280, 245), (cx7, 360), color='#15803d')

draw_card(d7, (cx7, 425, 500, 85), 4, "STOK EKLE ONAYI (btnOnayla_Click)", [
    "• Onaylandiginda urunun stogu artar, Dashboard yenilenir",
    "  ve denetim kayitlarina 'StokGiris' hareketi eklenir."
], themes['amber'], f_num, f_title, f_body)
draw_pointer_arrow(d7, (220, h7 + 25), (cx7, 465), color='#b45309')

c7.save(os.path.join(out_dir, "07_StokGiris_Rehberi.png"))

# =========================================================================
# AKTİVİTE 8: STOK ÇIKIŞI (-)
# =========================================================================
raw8 = Image.open(os.path.join(raw_dir, "08_StokCikis.png"))
c8 = Image.new('RGB', (w7 + 550, h7 + 100), color='#f1f5f9')
d8 = ImageDraw.Draw(c8)
d8.rectangle([0, 0, c8.width, 60], fill='#0f172a')
d8.text((30, 12), "AKTİVİTE 8: STOK ÇIKIŞ İŞLEMİ (-) VE YETERSİZ BAKİYE KİLİDİ", fill='#ffffff', font=f_header)
d8.text((30, 36), "FormStokIslem • Negatif Stok Engeli ve Satış/Sevkiyat Düşümü", fill='#94a3b8', font=f_sub)
c8.paste(raw8, (30, 80))

draw_card(d8, (cx7, 85, 500, 95), 1, "GÜVENLİ ÇIKIŞ ÜRÜN GÖSTERGESİ", [
    "• Stok cikisi yapilacak urun adi ve eldeki stok goruntulenir.",
    "• Stok miktari 0 olan urunden cikis yapilmasina izin verilmez."
], themes['blue'], f_num, f_title, f_body)
draw_pointer_arrow(d8, (280, 150), (cx7, 130), color='#1d4ed8')

draw_card(d8, (cx7, 195, 500, 105), 2, "YETERSİZ BAKİYE VE AŞIM KİLİDİ", [
    "• Eldeki stoktan (ornegin 12 adetten) fazla cikis yapilamaz!",
    "• numMiktar.Maximum degeri anlik stok adedine kilitlenir.",
    "• Kod düzeyinde de 'miktar > StokMiktari' kontrolu yapilir."
], themes['red'], f_num, f_title, f_body)
draw_pointer_arrow(d8, (280, 205), (cx7, 245), color='#b91c1c')

draw_card(d8, (cx7, 315, 500, 95), 3, "SATIŞ / SEVKİYAT NOTU GİRİŞİ", [
    "• Cikisin hangi musteriye veya siparise ait oldugu not edilir.",
    "• Bos gecilmesi engellenerek tam izlenebilirlik saglanir."
], themes['green'], f_num, f_title, f_body)
draw_pointer_arrow(d8, (280, 245), (cx7, 360), color='#15803d')

draw_card(d8, (cx7, 425, 500, 85), 4, "STOK DÜŞ ONAYI (btnOnayla_Click)", [
    "• Urun.StokCikis(miktar) metodu calisir, stok guvenle duser,",
    "  ve Denetim İzi sekmesine 'StokCikis' kaydi duser."
], themes['amber'], f_num, f_title, f_body)
draw_pointer_arrow(d8, (220, h7 + 25), (cx7, 465), color='#b45309')

c8.save(os.path.join(out_dir, "08_StokCikis_Rehberi.png"))

print("Tum 8 aktivite gorseli sifirdan net ve ferah duzende basariyla uretildi!")
