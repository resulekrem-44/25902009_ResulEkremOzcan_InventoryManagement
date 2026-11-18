# -*- coding: utf-8 -*-
"""
Generate 8 refined activity images with:
1. Semi-transparent highlighted bounding boxes on targeted UI regions.
2. Sleek numbered badges attached directly or cleanly alongside the highlights.
3. Clean, horizontal/orthogonal pointer arrows connecting the target to the numbered badge.
4. Elegant side-cards referencing the numbers with full explanations.
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont

def draw_transparent_box(base_img, rect, fill_rgba=(37, 99, 235, 45), outline_rgb=(37, 99, 235), outline_width=2, radius=6):
    """Draws a semi-transparent rounded rectangle over the base image with an outline."""
    x0, y0, x1, y1 = rect
    # Create an RGBA overlay
    overlay = Image.new('RGBA', base_img.size, (255, 255, 255, 0))
    odraw = ImageDraw.Draw(overlay)
    
    # Fill with alpha
    odraw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill_rgba, outline=outline_rgb + (220,), width=outline_width)
    
    # Composite over base_img
    if base_img.mode != 'RGBA':
        base_rgba = base_img.convert('RGBA')
        res = Image.alpha_composite(base_rgba, overlay)
        return res.convert('RGB')
    else:
        return Image.alpha_composite(base_img, overlay)

def draw_badge(draw, center, number, bg_color='#2563eb', text_color='#ffffff', radius=14, font=None):
    """Draws a sleek circular badge with a number."""
    cx, cy = center
    # Shadow
    draw.ellipse([cx-radius+1, cy-radius+1, cx+radius+1, cy-radius+1], fill='#cbd5e1')
    # Badge
    draw.ellipse([cx-radius, cy-radius, cx+radius, cy-radius], fill=bg_color, outline='#ffffff', width=2)
    # Number text centered
    # Approximate centering
    s = str(number)
    draw.text((cx - (4 if len(s)==1 else 7), cy - 8), s, fill=text_color, font=font)

def draw_nizami_arrow(draw, start, end, color='#2563eb', width=2, arrow_len=10):
    """Draws a clean, neat pointer arrow with start dot and arrowhead."""
    x0, y0 = start
    x1, y1 = end
    
    # Start dot
    draw.ellipse([x0-3, y0-3, x0+3, y0+3], fill=color, outline='#ffffff', width=1)
    
    # Line
    draw.line([start, end], fill=color, width=width)
    
    # Arrow head
    angle = math.atan2(y1 - y0, x1 - x0)
    angle1 = angle + math.pi - math.pi / 5.5
    angle2 = angle + math.pi + math.pi / 5.5
    
    p1 = (x1 + arrow_len * math.cos(angle1), y1 + arrow_len * math.sin(angle1))
    p2 = (x1 + arrow_len * math.cos(angle2), y1 + arrow_len * math.sin(angle2))
    draw.polygon([end, p1, p2], fill=color)

def draw_info_card(draw, rect, badge_num, title, lines, theme, font_num, font_title, font_body):
    """Draws a neat info card referencing the number."""
    x, y, w, h = rect
    bg = theme['bg']
    border = theme['border']
    primary = theme['primary']
    text_color = theme['text']
    
    # Soft shadow
    draw.rounded_rectangle([x+2, y+2, x+w+2, y+h+2], radius=8, fill='#e2e8f0')
    # Card Body
    draw.rounded_rectangle([x, y, x+w, y+h], radius=8, fill=bg, outline=border, width=1)
    
    # Left colored accent bar
    draw.rounded_rectangle([x, y, x+5, y+h], radius=2, fill=primary)
    
    # Number badge on card
    bx, by, br = x + 26, y + 22, 13
    draw.ellipse([bx-br, by-br, bx+br, by+br], fill=primary)
    s = str(badge_num)
    draw.text((bx - (4 if len(s)==1 else 6), by - 8), s, fill='#ffffff', font=font_num)
    
    # Title
    draw.text((x + 48, y + 13), title, fill=primary, font=font_title)
    
    # Text lines
    cur_y = y + 40
    for line in lines:
        draw.text((x + 16, cur_y), line, fill=text_color, font=font_body)
        cur_y += 18

desktop = os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop')
proj_dir = os.path.join(desktop, '.NET PROJE ÖDEVİ', '25902009_ResulEkremOzcan_InventoryManagement')
raw_dir = os.path.join(proj_dir, 'Screenshots_Raw')
out_dir = os.path.join(proj_dir, '03_Report', 'Gorseller')
os.makedirs(out_dir, exist_ok=True)

# Fonts
try:
    f_header = ImageFont.truetype("arialbd.ttf", 20)
    f_sub = ImageFont.truetype("arial.ttf", 13)
    f_num = ImageFont.truetype("arialbd.ttf", 12)
    f_title = ImageFont.truetype("arialbd.ttf", 13)
    f_body = ImageFont.truetype("arial.ttf", 11)
except:
    f_header = ImageFont.load_default()
    f_sub = ImageFont.load_default()
    f_num = ImageFont.load_default()
    f_title = ImageFont.load_default()
    f_body = ImageFont.load_default()

themes = {
    'blue':   {'bg': '#ffffff', 'border': '#3b82f6', 'primary': '#1d4ed8', 'text': '#1e293b', 'rgba': (29, 78, 216, 40), 'rgb': (29, 78, 216)},
    'green':  {'bg': '#ffffff', 'border': '#22c55e', 'primary': '#15803d', 'text': '#1e293b', 'rgba': (21, 128, 61, 40), 'rgb': (21, 128, 61)},
    'red':    {'bg': '#ffffff', 'border': '#ef4444', 'primary': '#b91c1c', 'text': '#1e293b', 'rgba': (185, 28, 28, 40), 'rgb': (185, 28, 28)},
    'purple': {'bg': '#ffffff', 'border': '#a855f7', 'primary': '#7e22ce', 'text': '#1e293b', 'rgba': (126, 34, 206, 40), 'rgb': (126, 34, 206)},
    'amber':  {'bg': '#ffffff', 'border': '#f59e0b', 'primary': '#b45309', 'text': '#1e293b', 'rgba': (180, 83, 9, 40), 'rgb': (180, 83, 9)}
}

def create_base_canvas(raw_img_path, title, subtitle):
    raw = Image.open(raw_img_path)
    w, h = raw.size
    canvas = Image.new('RGB', (w + 480, h + 100), color='#f8fafc')
    d = ImageDraw.Draw(canvas)
    
    # Header bar
    d.rectangle([0, 0, canvas.width, 60], fill='#0f172a')
    d.text((30, 12), title, fill='#ffffff', font=f_header)
    d.text((30, 36), subtitle, fill='#94a3b8', font=f_sub)
    
    # Paste raw screenshot at (30, 80)
    canvas.paste(raw, (30, 80))
    return canvas, raw, (30, 80)

# =========================================================================
# 1. AKTİVİTE 1: ANA EKRAN & DASHBOARD
# =========================================================================
print("Generating Activity 1...")
c1, raw1, (ox, oy) = create_base_canvas(
    os.path.join(raw_dir, "01_AnaEkran.png"),
    "AKTİVİTE 1: ANA EKRAN, CANLI DASHBOARD VE YÖNETİM MERKEZİ",
    "Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009) • Saydam Vurgu ve Numara Rehberi"
)

# UI Elements to highlight relative to raw screenshot:
# 1: Dashboard Cards: (12, 10) to (w-12, 105)
# 2: Search/Filter Panel: (12, 115) to (w-12, 185)
# 3: CRUD Buttons: (12, 490) to (380, 535)
# 4: Stock Buttons: (w-360, 490) to (w-15, 535)
w1, h1 = raw1.size
cx = w1 + 50

# Apply transparent highlights on canvas
c1 = draw_transparent_box(c1, [ox + 12, oy + 10, ox + w1 - 12, oy + 105], fill_rgba=themes['blue']['rgba'], outline_rgb=themes['blue']['rgb'])
c1 = draw_transparent_box(c1, [ox + 12, oy + 115, ox + w1 - 12, oy + 185], fill_rgba=themes['purple']['rgba'], outline_rgb=themes['purple']['rgb'])
c1 = draw_transparent_box(c1, [ox + 12, oy + 490, ox + 380, oy + 535], fill_rgba=themes['green']['rgba'], outline_rgb=themes['green']['rgb'])
c1 = draw_transparent_box(c1, [ox + w1 - 360, oy + 490, ox + w1 - 15, oy + 535], fill_rgba=themes['amber']['rgba'], outline_rgb=themes['amber']['rgb'])

d1 = ImageDraw.Draw(c1)

# Badge 1: on top-right of dashboard box
draw_badge(d1, (ox + w1 - 25, oy + 25), 1, bg_color=themes['blue']['primary'], font=f_num)
draw_nizami_arrow(d1, (ox + w1 - 10, oy + 25), (cx - 5, 125), color=themes['blue']['primary'])
draw_info_card(d1, (cx, 80, 430, 92), 1, "CANLI DASHBOARD KARTLARI", [
    "• Toplam Urun, Toplam Stok, Kritik Urun ve Envanter Degeri.",
    "• Sabit degil; generic List<Urun> uzerinde LINQ Count() ve",
    "  Sum(u => u.ToplamDegerHesapla()) ile anlik hesaplanir."
], themes['blue'], f_num, f_title, f_body)

# Badge 2: on top-right of filter box
draw_badge(d1, (ox + w1 - 25, oy + 130), 2, bg_color=themes['purple']['primary'], font=f_num)
draw_nizami_arrow(d1, (ox + w1 - 10, oy + 130), (cx - 5, 230), color=themes['purple']['primary'])
draw_info_card(d1, (cx, 185, 430, 92), 2, "FILTRELEME VE ARAMA PANELİ", [
    "• Urun adi/koduna gore harf yazildikca canli arama yapilir.",
    "• Kategori acilir kutusu ile Elektronik, Gida ve Giyim suzulur.",
    "• Kritik Stok secenegi ile azalan stoklar tek tikla listelenir."
], themes['purple'], f_num, f_title, f_body)

# Badge 3: on CRUD button panel
draw_badge(d1, (ox + 365, oy + 512), 3, bg_color=themes['green']['primary'], font=f_num)
draw_nizami_arrow(d1, (ox + 380, oy + 512), (cx - 5, 335), color=themes['green']['primary'])
draw_info_card(d1, (cx, 290, 430, 92), 3, "CRUD YÖNETİM BUTONLARI", [
    "• 'Yeni Urun Ekle': Polimorfik dinamik form acar.",
    "• 'Secili Urunu Duzenle': Secili urun verilerini yukler.",
    "• 'Urunu Sil': Silme oncesi kullanicidan teyit onay penceresi alir."
], themes['green'], f_num, f_title, f_body)

# Badge 4: on Stock button panel
draw_badge(d1, (ox + w1 - 25, oy + 512), 4, bg_color=themes['amber']['primary'], font=f_num)
draw_nizami_arrow(d1, (ox + w1 - 10, oy + 512), (cx - 5, 440), color=themes['amber']['primary'])
draw_info_card(d1, (cx, 395, 430, 92), 4, "HIZLI STOK GİRİŞ / ÇIKIŞ", [
    "• 'Stok Girisi Yap': Tedarikci kabul ve miktar artirma.",
    "• 'Stok Cikisi Yap': Musteri satis ve eksi bakiye kontrollu cikis.",
    "• Tum islemler IslemKaydi tablosuna otomatik loglanir."
], themes['amber'], f_num, f_title, f_body)

c1.save(os.path.join(out_dir, "01_AnaEkran_Rehberi.png"))


# =========================================================================
# 2. AKTİVİTE 2: ARAMA & FİLTRELEME
# =========================================================================
print("Generating Activity 2...")
c2, raw2, (ox, oy) = create_base_canvas(
    os.path.join(raw_dir, "02_AramaFiltre.png"),
    "AKTİVİTE 2: CANLI ARAMA VE KATEGORİ FİLTRELEME SİSTEMİ",
    "Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009) • Saydam Vurgu ve Numara Rehberi"
)
w2, h2 = raw2.size
cx2 = w2 + 50

# Highlight 1: Search Box [ox+12, oy+135, ox+240, oy+175]
# Highlight 2: Filtered Grid [ox+12, oy+195, ox+w2-12, oy+480]
# Highlight 3: Synced Dashboard [ox+12, oy+10, ox+w2-12, oy+105]
c2 = draw_transparent_box(c2, [ox + 12, oy + 130, ox + 260, oy + 175], fill_rgba=themes['blue']['rgba'], outline_rgb=themes['blue']['rgb'])
c2 = draw_transparent_box(c2, [ox + 12, oy + 195, ox + w2 - 12, oy + 480], fill_rgba=themes['purple']['rgba'], outline_rgb=themes['purple']['rgb'])
c2 = draw_transparent_box(c2, [ox + 12, oy + 10, ox + w2 - 12, oy + 105], fill_rgba=themes['amber']['rgba'], outline_rgb=themes['amber']['rgb'])

d2 = ImageDraw.Draw(c2)

draw_badge(d2, (ox + 245, oy + 152), 1, bg_color=themes['blue']['primary'], font=f_num)
draw_nizami_arrow(d2, (ox + 260, oy + 152), (cx2 - 5, 140), color=themes['blue']['primary'])
draw_info_card(d2, (cx2, 90, 430, 95), 1, "CANLI METİN ARAMA KUTUSU", [
    "• Arama kutusuna 'Fare' yazildigi an TextChanged olayi tetiklenir.",
    "• IndexOf(..., StringComparison.OrdinalIgnoreCase) kullanilarak",
    "  harf duyarsiz aninda arama yapilir."
], themes['blue'], f_num, f_title, f_body)

draw_badge(d2, (ox + w2 - 25, oy + 230), 2, bg_color=themes['purple']['primary'], font=f_num)
draw_nizami_arrow(d2, (ox + w2 - 10, oy + 230), (cx2 - 5, 255), color=themes['purple']['primary'])
draw_info_card(d2, (cx2, 205, 430, 95), 2, "FİLTRELENEN VERİ TABLOSU", [
    "• Sadece arama kriterine uyan (Kablosuz Optik Fare) listelenir.",
    "• Diger ilgisiz kategoriler ve urunler aninda gizlenir.",
    "• DataGridView BindingList ile bagli oldugundan titresimsizdir."
], themes['purple'], f_num, f_title, f_body)

draw_badge(d2, (ox + w2 - 25, oy + 35), 3, bg_color=themes['amber']['primary'], font=f_num)
draw_nizami_arrow(d2, (ox + w2 - 10, oy + 35), (cx2 - 5, 370), color=themes['amber']['primary'])
draw_info_card(d2, (cx2, 320, 430, 95), 3, "EŞ ZAMANLI KPI SENKRONİZASYONU", [
    "• Ust paneldeki istatistikler filtrelenen sonuclara gore",
    "  aninda guncellenerek depocuya dinamik bilgi saglar.",
    "• Bos arama yapildiginda tum liste 1 milisaniyede geri yuklenir."
], themes['amber'], f_num, f_title, f_body)

c2.save(os.path.join(out_dir, "02_AramaFiltre_Rehberi.png"))


# =========================================================================
# 3. AKTİVİTE 3: KRİTİK STOK UYARISI
# =========================================================================
print("Generating Activity 3...")
c3, raw3, (ox, oy) = create_base_canvas(
    os.path.join(raw_dir, "03_KritikStok.png"),
    "AKTİVİTE 3: KRİTİK STOK UYARI SİSTEMİ VE GÖRSEL VURGULAMA",
    "Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009) • Saydam Vurgu ve Numara Rehberi"
)
w3, h3 = raw3.size
cx3 = w3 + 50

# Highlight 1: Checkbox [ox+480, oy+135, ox+780, oy+175]
# Highlight 2: Red Highlighted Rows [ox+12, oy+220, ox+w3-12, oy+310]
# Highlight 3: Red Dashboard Card [ox+w3-240, oy+10, ox+w3-12, oy+105]
c3 = draw_transparent_box(c3, [ox + 470, oy + 135, ox + 760, oy + 175], fill_rgba=themes['blue']['rgba'], outline_rgb=themes['blue']['rgb'])
c3 = draw_transparent_box(c3, [ox + 12, oy + 220, ox + w3 - 12, oy + 310], fill_rgba=themes['red']['rgba'], outline_rgb=themes['red']['rgb'])
c3 = draw_transparent_box(c3, [ox + w3 - 240, oy + 10, ox + w3 - 12, oy + 105], fill_rgba=themes['red']['rgba'], outline_rgb=themes['red']['rgb'])

d3 = ImageDraw.Draw(c3)

draw_badge(d3, (ox + 745, oy + 155), 1, bg_color=themes['blue']['primary'], font=f_num)
draw_nizami_arrow(d3, (ox + 760, oy + 155), (cx3 - 5, 140), color=themes['blue']['primary'])
draw_info_card(d3, (cx3, 90, 430, 95), 1, "KRİTİK STOK FİLTRELEME", [
    "• 'Sadece Kritik Stok Seviyesindeki Urunleri Goster' onay kutusu.",
    "• LINQ u.KritikStoktaMi() metodu calistirilir.",
    "• StokMiktari <= KritikStokSeviyesi kuralina uyanlar suzulur."
], themes['blue'], f_num, f_title, f_body)

draw_badge(d3, (ox + w3 - 25, oy + 260), 2, bg_color=themes['red']['primary'], font=f_num)
draw_nizami_arrow(d3, (ox + w3 - 10, oy + 260), (cx3 - 5, 255), color=themes['red']['primary'])
draw_info_card(d3, (cx3, 205, 430, 95), 2, "KIRMIZI SATIR VURGULAMA (CELL PAINT)", [
    "• DataGridView_RowPrePaint olayinda kritik urunler kontrol edilir.",
    "• Kritik urun satirlarinin arka plani acik kirmizi (#FFD2D2),",
    "  yazi rengi ise koyu kirmizi yapilarak aninda dikkat ceker."
], themes['red'], f_num, f_title, f_body)

draw_badge(d3, (ox + w3 - 25, oy + 35), 3, bg_color=themes['red']['primary'], font=f_num)
draw_nizami_arrow(d3, (ox + w3 - 10, oy + 35), (cx3 - 5, 370), color=themes['red']['primary'])
draw_info_card(d3, (cx3, 320, 430, 95), 3, "DASHBOARD KRİTİK STOK UYARISI", [
    "• Ust paneldeki 'Kritik Stoktaki Urun' karti kirmizi renkle",
    "  depo sorumlusuna kritik esigi asan 2 urun oldugunu bildirir.",
    "• Boylece tukenmek uzere olan malzemeler onceden siparis edilir."
], themes['red'], f_num, f_title, f_body)

c3.save(os.path.join(out_dir, "03_KritikStok_Rehberi.png"))


# =========================================================================
# 4. AKTİVİTE 4: DENETİM İZİ (AUDIT LOG)
# =========================================================================
print("Generating Activity 4...")
c4, raw4, (ox, oy) = create_base_canvas(
    os.path.join(raw_dir, "04_DenetimIzi.png"),
    "AKTİVİTE 4: DENETİM İZİ VE HAREKET GEÇMİŞİ (AUDIT LOG)",
    "Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009) • Saydam Vurgu ve Numara Rehberi"
)
w4, h4 = raw4.size
cx4 = w4 + 50

# Highlight 1: Timestamp & Enum [ox+12, oy+140, ox+260, oy+480]
# Highlight 2: Before/After stock [ox+480, oy+140, ox+660, oy+480]
# Highlight 3: Mandatory Notes [ox+660, oy+140, ox+w4-12, oy+480]
c4 = draw_transparent_box(c4, [ox + 12, oy + 140, ox + 260, oy + 480], fill_rgba=themes['blue']['rgba'], outline_rgb=themes['blue']['rgb'])
c4 = draw_transparent_box(c4, [ox + 480, oy + 140, ox + 660, oy + 480], fill_rgba=themes['purple']['rgba'], outline_rgb=themes['purple']['rgb'])
c4 = draw_transparent_box(c4, [ox + 660, oy + 140, ox + w4 - 12, oy + 480], fill_rgba=themes['green']['rgba'], outline_rgb=themes['green']['rgb'])

d4 = ImageDraw.Draw(c4)

draw_badge(d4, (ox + 245, oy + 200), 1, bg_color=themes['blue']['primary'], font=f_num)
draw_nizami_arrow(d4, (ox + 260, oy + 200), (cx4 - 5, 140), color=themes['blue']['primary'])
draw_info_card(d4, (cx4, 90, 430, 95), 1, "ZAMAN DAMGASI VE İŞLEM TÜRÜ", [
    "• Her stok degisikligi DateTime.Now ile saniyesine kadar kaydedilir.",
    "• IslemTuru enum'i ile 'Giris', 'Cikis' veya 'Guncelleme' olarak",
    "  tip guvenli (type-safe) bicimde loglanir."
], themes['blue'], f_num, f_title, f_body)

draw_badge(d4, (ox + 645, oy + 250), 2, bg_color=themes['purple']['primary'], font=f_num)
draw_nizami_arrow(d4, (ox + 660, oy + 250), (cx4 - 5, 255), color=themes['purple']['primary'])
draw_info_card(d4, (cx4, 205, 430, 95), 2, "ÖNCEKİ VE SONRAKİ STOK TAKİBİ", [
    "• Islem anindaki baslangic stogu, hareket miktari ve nihai bakiye",
    "  matematiksel tutarlilikla saklanir.",
    "• Gecmise donuk denetimlerde stok uyusmazliklarini onler."
], themes['purple'], f_num, f_title, f_body)

draw_badge(d4, (ox + w4 - 25, oy + 300), 3, bg_color=themes['green']['primary'], font=f_num)
draw_nizami_arrow(d4, (ox + w4 - 10, oy + 300), (cx4 - 5, 370), color=themes['green']['primary'])
draw_info_card(d4, (cx4, 320, 430, 95), 3, "ZORUNLU İŞLEM AÇIKLAMALARI", [
    "• Depocunun girdigi irsaliye numaralari, fatura veya sevkiyat notu",
    "  aciklama kolonunda ayrintili olarak gosterilir.",
    "• Aciklama alani bos gecilemez, en az 3 karakter girilmelidir."
], themes['green'], f_num, f_title, f_body)

c4.save(os.path.join(out_dir, "04_DenetimIzi_Rehberi.png"))


# =========================================================================
# 5. AKTİVİTE 5: ÜRÜN EKLEME (ELEKTRONİK ÖRNEĞİ)
# =========================================================================
print("Generating Activity 5...")
c5, raw5, (ox, oy) = create_base_canvas(
    os.path.join(raw_dir, "05_UrunEkle_Elektronik.png"),
    "AKTİVİTE 5: KATEGORİYE ÖZEL DİNAMİK ÜRÜN EKLEME",
    "Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009) • Saydam Vurgu ve Numara Rehberi"
)
w5, h5 = raw5.size
cx5 = w5 + 50

# Highlight 1: Core Fields [ox+20, oy+50, ox+w5-20, oy+180]
# Highlight 2: Price Validation [ox+20, oy+180, ox+w5-20, oy+260]
# Highlight 3: Dynamic Category Panel [ox+20, oy+260, ox+w5-20, oy+380]
# Highlight 4: Save Button [ox+w5-180, oy+390, ox+w5-20, oy+440]
c5 = draw_transparent_box(c5, [ox + 15, oy + 45, ox + w5 - 15, oy + 175], fill_rgba=themes['blue']['rgba'], outline_rgb=themes['blue']['rgb'])
c5 = draw_transparent_box(c5, [ox + 15, oy + 175, ox + w5 - 15, oy + 250], fill_rgba=themes['purple']['rgba'], outline_rgb=themes['purple']['rgb'])
c5 = draw_transparent_box(c5, [ox + 15, oy + 250, ox + w5 - 15, oy + 370], fill_rgba=themes['amber']['rgba'], outline_rgb=themes['amber']['rgb'])
c5 = draw_transparent_box(c5, [ox + w5 - 180, oy + 380, ox + w5 - 15, oy + 430], fill_rgba=themes['green']['rgba'], outline_rgb=themes['green']['rgb'])

d5 = ImageDraw.Draw(c5)

draw_badge(d5, (ox + w5 - 30, oy + 70), 1, bg_color=themes['blue']['primary'], font=f_num)
draw_nizami_arrow(d5, (ox + w5 - 15, oy + 70), (cx5 - 5, 115), color=themes['blue']['primary'])
draw_info_card(d5, (cx5, 70, 430, 85), 1, "ZORUNLU TEMEL ALANLAR", [
    "• Urun Kodu (benzersiz), Urun Adi, Baslangic Stogu ve Kritik Esik.",
    "• Urun adinda zararli karakterler regex ile guvenli engellenir."
], themes['blue'], f_num, f_title, f_body)

draw_badge(d5, (ox + w5 - 30, oy + 195), 2, bg_color=themes['purple']['primary'], font=f_num)
draw_nizami_arrow(d5, (ox + w5 - 15, oy + 195), (cx5 - 5, 195), color=themes['purple']['primary'])
draw_info_card(d5, (cx5, 160, 430, 85), 2, "0 TL VE MANTIKSIZ DEĞER KORUMASI", [
    "• Birim Fiyat <= 0 veya Kritik Stok < 0 girildiginde engellenir.",
    "• Kurus hanesi virgullu/noktali decimal hassasiyetle kontrol edilir."
], themes['purple'], f_num, f_title, f_body)

draw_badge(d5, (ox + w5 - 30, oy + 280), 3, bg_color=themes['amber']['primary'], font=f_num)
draw_nizami_arrow(d5, (ox + w5 - 15, oy + 280), (cx5 - 5, 280), color=themes['amber']['primary'])
draw_info_card(d5, (cx5, 250, 430, 85), 3, "KATEGORİYE ÖZEL DİNAMİK ALANLAR", [
    "• Kategori 'Elektronik' iken Garanti Suresi (Ay) ve Voltaj (V) acilir.",
    "• 'Gida' secilirse SKT/Sicaklik; 'Giyim' secilirse Beden/Kumas gelir."
], themes['amber'], f_num, f_title, f_body)

draw_badge(d5, (ox + w5 - 30, oy + 400), 4, bg_color=themes['green']['primary'], font=f_num)
draw_nizami_arrow(d5, (ox + w5 - 15, oy + 400), (cx5 - 5, 370), color=themes['green']['primary'])
draw_info_card(d5, (cx5, 340, 430, 85), 4, "KAYIT VE VALİDASYON KONTROLÜ", [
    "• Mukerrer urun kodu varsa sistem kaydi engeller ve uyarir.",
    "• Islem basarili olunca ana ekran tablosu ve KPI kartlari yenilenir."
], themes['green'], f_num, f_title, f_body)

c5.save(os.path.join(out_dir, "05_UrunEkle_Elektronik_Rehberi.png"))


# =========================================================================
# 6. AKTİVİTE 6: ÜRÜN DÜZENLEME
# =========================================================================
print("Generating Activity 6...")
c6, raw6, (ox, oy) = create_base_canvas(
    os.path.join(raw_dir, "06_UrunDuzenle.png"),
    "AKTİVİTE 6: MEVCUT ÜRÜN BİLGİLERİNİ GÜNCELLEME EKRANI",
    "Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009) • Saydam Vurgu ve Numara Rehberi"
)
w6, h6 = raw6.size
cx6 = w6 + 50

# Highlight 1: ReadOnly Product Code [ox+15, oy+45, ox+w6-15, oy+95]
# Highlight 2: Locked Stock Field [ox+15, oy+140, ox+w6-15, oy+185]
# Highlight 3: Editable Price & Tech Fields [ox+15, oy+185, ox+w6-15, oy+370]
c6 = draw_transparent_box(c6, [ox + 15, oy + 45, ox + w6 - 15, oy + 95], fill_rgba=themes['red']['rgba'], outline_rgb=themes['red']['rgb'])
c6 = draw_transparent_box(c6, [ox + 15, oy + 140, ox + w6 - 15, oy + 185], fill_rgba=themes['purple']['rgba'], outline_rgb=themes['purple']['rgb'])
c6 = draw_transparent_box(c6, [ox + 15, oy + 185, ox + w6 - 15, oy + 370], fill_rgba=themes['blue']['rgba'], outline_rgb=themes['blue']['rgb'])

d6 = ImageDraw.Draw(c6)

draw_badge(d6, (ox + w6 - 30, oy + 65), 1, bg_color=themes['red']['primary'], font=f_num)
draw_nizami_arrow(d6, (ox + w6 - 15, oy + 65), (cx6 - 5, 140), color=themes['red']['primary'])
draw_info_card(d6, (cx6, 90, 430, 95), 1, "SALT OKUNUR (READ-ONLY) ÜRÜN KODU", [
    "• Veri butunlugunu korumak icin benzersiz urun kodu kilitlidir.",
    "• txtUrunKodu.ReadOnly = true yapilarak kodun degistirilmesi",
    "  ve iliskili loglarin kopmasi engellenir."
], themes['red'], f_num, f_title, f_body)

draw_badge(d6, (ox + w6 - 30, oy + 160), 2, bg_color=themes['purple']['primary'], font=f_num)
draw_nizami_arrow(d6, (ox + w6 - 15, oy + 160), (cx6 - 5, 255), color=themes['purple']['primary'])
draw_info_card(d6, (cx6, 205, 430, 95), 2, "KİLİTLİ BAŞLANGIÇ STOĞU", [
    "• Mevcut stok miktari urun duzenleme ekranindan elle degistirilemez.",
    "• Stok hareketleri yalnizca resmi 'Stok Girisi' ve 'Stok Cikisi'",
    "  fisleri uzerinden kontrollu sekilde yapilabilir."
], themes['purple'], f_num, f_title, f_body)

draw_badge(d6, (ox + w6 - 30, oy + 260), 3, bg_color=themes['blue']['primary'], font=f_num)
draw_nizami_arrow(d6, (ox + w6 - 15, oy + 260), (cx6 - 5, 370), color=themes['blue']['primary'])
draw_info_card(d6, (cx6, 320, 430, 95), 3, "FİYAT VE TEKNİK BİLGİ GÜNCELLEME", [
    "• Birim fiyat, kritik stok seviyesi, garanti suresi ve voltaj",
    "  gibi ozellikler serbestce guncellenebilir.",
    "• 'Guncelle' basildiginda IslemKaydi'na log birakilir."
], themes['blue'], f_num, f_title, f_body)

c6.save(os.path.join(out_dir, "06_UrunDuzenle_Rehberi.png"))


# =========================================================================
# 7. AKTİVİTE 7: STOK GİRİŞİ
# =========================================================================
print("Generating Activity 7...")
c7, raw7, (ox, oy) = create_base_canvas(
    os.path.join(raw_dir, "07_StokGiris.png"),
    "AKTİVİTE 7: GÜVENLİ STOK GİRİŞİ İŞLEMİ",
    "Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009) • Saydam Vurgu ve Numara Rehberi"
)
w7, h7 = raw7.size
cx7 = w7 + 50

# Highlight 1: Product Info Card [ox+15, oy+40, ox+w7-15, oy+140]
# Highlight 2: Quantity Input [ox+15, oy+145, ox+w7-15, oy+215]
# Highlight 3: Note Box [ox+15, oy+220, ox+w7-15, oy+310]
c7 = draw_transparent_box(c7, [ox + 15, oy + 40, ox + w7 - 15, oy + 140], fill_rgba=themes['blue']['rgba'], outline_rgb=themes['blue']['rgb'])
c7 = draw_transparent_box(c7, [ox + 15, oy + 145, ox + w7 - 15, oy + 215], fill_rgba=themes['purple']['rgba'], outline_rgb=themes['purple']['rgb'])
c7 = draw_transparent_box(c7, [ox + 15, oy + 220, ox + w7 - 15, oy + 310], fill_rgba=themes['green']['rgba'], outline_rgb=themes['green']['rgb'])

d7 = ImageDraw.Draw(c7)

draw_badge(d7, (ox + w7 - 30, oy + 70), 1, bg_color=themes['blue']['primary'], font=f_num)
draw_nizami_arrow(d7, (ox + w7 - 15, oy + 70), (cx7 - 5, 140), color=themes['blue']['primary'])
draw_info_card(d7, (cx7, 90, 430, 95), 1, "ÜRÜN VE MEVCUT STOK BİLGİSİ", [
    "• Islem yapilacak urunun kodu, adi ve depodaki guncel adedi",
    "  bilgi panelinde salt okunur olarak sunulur.",
    "• Yanlis urune stok girisi yapilmasi engellenir."
], themes['blue'], f_num, f_title, f_body)

draw_badge(d7, (ox + w7 - 30, oy + 175), 2, bg_color=themes['purple']['primary'], font=f_num)
draw_nizami_arrow(d7, (ox + w7 - 15, oy + 175), (cx7 - 5, 255), color=themes['purple']['primary'])
draw_info_card(d7, (cx7, 205, 430, 95), 2, "KATI MİKTAR GİRİŞ VALİDASYONU", [
    "• 0, 00, 000 veya harf gibi gecersiz girisler regex ile engellenir.",
    "• Sayisal parse kontrolu: miktar <= 0 ise 'Islem miktari pozitif",
    "  bir tam sayi olmalidir!' hatasi firlatilir."
], themes['purple'], f_num, f_title, f_body)

draw_badge(d7, (ox + w7 - 30, oy + 260), 3, bg_color=themes['green']['primary'], font=f_num)
draw_nizami_arrow(d7, (ox + w7 - 15, oy + 260), (cx7 - 5, 370), color=themes['green']['primary'])
draw_info_card(d7, (cx7, 320, 430, 95), 3, "ZORUNLU TEDARİKÇİ AÇIKLAMASI", [
    "• Depoya mal kabulunde irsaliye/fatura numarasi zorunludur.",
    "• En az 3 karakter girilmeden 'Stok Girisi Yap' butonu islemi",
    "  onaylamaz; denetim izinde aciklama net olarak saklanir."
], themes['green'], f_num, f_title, f_body)

c7.save(os.path.join(out_dir, "07_StokGiris_Rehberi.png"))


# =========================================================================
# 8. AKTİVİTE 8: STOK ÇIKIŞI
# =========================================================================
print("Generating Activity 8...")
c8, raw8, (ox, oy) = create_base_canvas(
    os.path.join(raw_dir, "08_StokCikis.png"),
    "AKTİVİTE 8: BAKİYE KONTROLLÜ STOK ÇIKIŞI İŞLEMİ",
    "Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009) • Saydam Vurgu ve Numara Rehberi"
)
w8, h8 = raw8.size
cx8 = w8 + 50

# Highlight 1: Current Stock Info [ox+15, oy+40, ox+w8-15, oy+140]
# Highlight 2: Quantity & Balance Check [ox+15, oy+145, ox+w8-15, oy+215]
# Highlight 3: Customer Note & Exit Button [ox+15, oy+220, ox+w8-15, oy+360]
c8 = draw_transparent_box(c8, [ox + 15, oy + 40, ox + w8 - 15, oy + 140], fill_rgba=themes['blue']['rgba'], outline_rgb=themes['blue']['rgb'])
c8 = draw_transparent_box(c8, [ox + 15, oy + 145, ox + w8 - 15, oy + 215], fill_rgba=themes['red']['rgba'], outline_rgb=themes['red']['rgb'])
c8 = draw_transparent_box(c8, [ox + 15, oy + 220, ox + w8 - 15, oy + 360], fill_rgba=themes['amber']['rgba'], outline_rgb=themes['amber']['rgb'])

d8 = ImageDraw.Draw(c8)

draw_badge(d8, (ox + w8 - 30, oy + 70), 1, bg_color=themes['blue']['primary'], font=f_num)
draw_nizami_arrow(d8, (ox + w8 - 15, oy + 70), (cx8 - 5, 140), color=themes['blue']['primary'])
draw_info_card(d8, (cx8, 90, 430, 95), 1, "MEVCUT BAKİYE TESPİTİ", [
    "• Cikis yapilacak urunun depoda kac adet oldugu gosterilir.",
    "• Ornekte: Mevcut Stok: 15 adet olarak listelenmektedir.",
    "• Personel cikis yapmadan once depodaki reel miktari gorur."
], themes['blue'], f_num, f_title, f_body)

draw_badge(d8, (ox + w8 - 30, oy + 175), 2, bg_color=themes['red']['primary'], font=f_num)
draw_nizami_arrow(d8, (ox + w8 - 15, oy + 175), (cx8 - 5, 255), color=themes['red']['primary'])
draw_info_card(d8, (cx8, 205, 430, 95), 2, "YETERSİZ STOK VE EKSİ BAKİYE KİLİDİ", [
    "• StokCikisiYap() isleminde: miktar > StokMiktari kontrol edilir.",
    "• 15 adetten fazla (ornegin 20 adet) cikis yapilmasi engellenir.",
    "• 'Yetersiz stok! Mevcut bakiye: 15' hatasi ile stok eksiye dusmez."
], themes['red'], f_num, f_title, f_body)

draw_badge(d8, (ox + w8 - 30, oy + 260), 3, bg_color=themes['amber']['primary'], font=f_num)
draw_nizami_arrow(d8, (ox + w8 - 15, oy + 260), (cx8 - 5, 370), color=themes['amber']['primary'])
draw_info_card(d8, (cx8, 320, 430, 95), 3, "MÜŞTERİ SEVKİYAT AÇIKLAMASI", [
    "• Sevkiyatin hangi musteriye veya faturaya ait oldugu girilir.",
    "• Gecerli aciklama girildiginde cikis gerceklesir ve",
    "  onceki bakiye: 15, sonraki bakiye: 10 seklinde loglanir."
], themes['amber'], f_num, f_title, f_body)

c8.save(os.path.join(out_dir, "08_StokCikis_Rehberi.png"))

print("All 8 refined activity images successfully generated with transparent highlight boxes, neat numbered badges and clean pointer arrows!")
