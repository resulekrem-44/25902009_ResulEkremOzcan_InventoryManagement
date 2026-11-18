# -*- coding: utf-8 -*-
"""
Generate professional documentation visuals matching the exact reference sample style:
- Clean light grey/blue canvas background (#f1f5f9 / #f8fafc)
- Centered raw screenshot with subtle boundary/shadow
- Rounded pill callout boxes (white background, subtle colored border, number circle on left)
- Number circle (solid colored background, white bold number)
- Clean, orthogonal (vertical/horizontal L-bend or straight) connecting pointer lines with start dot on the callout and arrowhead on the target UI element
- NO giant right-hand sidebar; callouts positioned neatly above, below, or to the sides of the window exactly like the sample!
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont

desktop = os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop')
proj_dir = os.path.join(desktop, '.NET PROJE ÖDEVİ', '25902009_ResulEkremOzcan_InventoryManagement')
raw_dir = os.path.join(proj_dir, 'Screenshots_Raw')
out_dir = os.path.join(proj_dir, '03_Report', 'Gorseller')
os.makedirs(out_dir, exist_ok=True)

# Fonts
try:
    f_num = ImageFont.truetype("arialbd.ttf", 11)
    f_title = ImageFont.truetype("arialbd.ttf", 10)
    f_sub = ImageFont.truetype("arial.ttf", 9)
except:
    f_num = ImageFont.load_default()
    f_title = ImageFont.load_default()
    f_sub = ImageFont.load_default()

# Color palettes exactly like the sample:
# Dark blue/black, Red/crimson, Green, Amber/orange
PALETTES = {
    'dark':   {'pill_border': '#cbd5e1', 'badge_bg': '#0f172a', 'text_title': '#0f172a', 'text_sub': '#64748b', 'line': '#0f172a'},
    'blue':   {'pill_border': '#bfdbfe', 'badge_bg': '#1d4ed8', 'text_title': '#1e3a8a', 'text_sub': '#475569', 'line': '#2563eb'},
    'red':    {'pill_border': '#fecaca', 'badge_bg': '#dc2626', 'text_title': '#991b1b', 'text_sub': '#475569', 'line': '#dc2626'},
    'green':  {'pill_border': '#bbf7d0', 'badge_bg': '#16a34a', 'text_title': '#166534', 'text_sub': '#475569', 'line': '#16a34a'},
    'amber':  {'pill_border': '#fed7aa', 'badge_bg': '#d97706', 'text_title': '#9a3412', 'text_sub': '#475569', 'line': '#d97706'}
}

def draw_pill_callout(draw, rect, number, title, subtext, palette_name='dark'):
    """Draws a rounded pill callout exactly like the sample."""
    x, y, w, h = rect
    pal = PALETTES[palette_name]
    
    # White pill with subtle border
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill='#ffffff', outline=pal['pill_border'], width=1)
    
    # Number circle on the left
    cr = 10
    cx = x + 16
    cy = y + h // 2
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=pal['badge_bg'])
    
    # Text number centered inside circle
    num_str = str(number)
    nw = 6 if len(num_str) == 1 else 10
    draw.text((cx - nw // 2, cy - 6), num_str, fill='#ffffff', font=f_num)
    
    # Title and Subtext on right of circle
    tx = cx + cr + 8
    draw.text((tx, cy - 11), title, fill=pal['text_title'], font=f_title)
    if subtext:
        draw.text((tx, cy + 1), subtext, fill=pal['text_sub'], font=f_sub)

def draw_pointer(draw, start, end, palette_name='dark', bend_first='y'):
    """Draws an orthogonal (L-bend) or straight pointer line from callout to target element."""
    pal = PALETTES[palette_name]
    color = pal['line']
    x0, y0 = start
    x1, y1 = end
    
    # Start dot at callout edge
    draw.ellipse([x0 - 2, y0 - 2, x0 + 2, y0 + 2], fill=color)
    
    # If points are roughly aligned, draw straight line
    if abs(x0 - x1) < 8 or abs(y0 - y1) < 8:
        draw.line([(x0, y0), (x1, y1)], fill=color, width=1)
        dx = x1 - x0
        dy = y1 - y0
    else:
        # L-bend
        if bend_first == 'y':
            corner = (x0, y1)
        else:
            corner = (x1, y0)
        draw.line([(x0, y0), corner], fill=color, width=1)
        draw.line([corner, (x1, y1)], fill=color, width=1)
        dx = x1 - corner[0]
        dy = y1 - corner[1]
    
    if dx == 0 and dy == 0:
        dx = x1 - x0
        dy = y1 - y0
        
    angle = math.atan2(dy, dx)
    arrow_len = 7
    a1 = angle + math.pi - math.pi / 5
    a2 = angle + math.pi + math.pi / 5
    p1 = (x1 + arrow_len * math.cos(a1), y1 + arrow_len * math.sin(a1))
    p2 = (x1 + arrow_len * math.cos(a2), y1 + arrow_len * math.sin(a2))
    draw.polygon([end, p1, p2], fill=color)

# =========================================================================
# GÖRSEL 1: ANA EKRAN, DASHBOARD VE DETAY ÇUBUĞU (Şekil 1 gibi)
# =========================================================================
print("Rendering Visual 1: Ana Ekran & Dashboard...")
raw1 = Image.open(os.path.join(raw_dir, "01_AnaEkran.png"))
rw, rh = raw1.size # 1096 x 719

# Canvas with margin: top 70px (for top pills), bottom 80px (for bottom pills), left/right 40px
cw = rw + 80
ch = rh + 150
c1 = Image.new('RGB', (cw, ch), color='#f1f5f9')

# Subtle shadow under raw screenshot
sdraw = ImageDraw.Draw(c1)
sdraw.rounded_rectangle([38, 70, 38 + rw + 4, 70 + rh + 4], radius=6, fill='#cbd5e1')

# Paste screenshot
ox, oy = 40, 70
c1.paste(raw1, (ox, oy))
d1 = ImageDraw.Draw(c1)

# Pill 1: CANLI STOK SAYAÇLARI (Top Left)
p1_rect = (ox + 100, 18, 220, 32)
draw_pill_callout(d1, p1_rect, 1, "CANLI STOK SAYAÇLARI", "Ürün çeşidi ve toplam stok adedi", 'dark')
# Target: Dashboard Card 1 (ox + 80, oy + 55)
draw_pointer(d1, (p1_rect[0] + 110, p1_rect[1] + p1_rect[3]), (ox + 160, oy + 12), palette_name='dark', bend_first='y')

# Pill 2: KRİTİK STOK SAYACI (Top Center)
p2_rect = (ox + 460, 18, 210, 32)
draw_pill_callout(d1, p2_rect, 2, "KRİTİK STOK SAYACI", "Eşik altındaki acil ürün adedi", 'red')
# Target: Dashboard Card 3 (ox + 600, oy + 12)
draw_pointer(d1, (p2_rect[0] + 105, p2_rect[1] + p2_rect[3]), (ox + 580, oy + 12), palette_name='red', bend_first='y')

# Pill 3: ENVANTER DEĞERİ (Top Right)
p3_rect = (ox + 780, 18, 210, 32)
draw_pill_callout(d1, p3_rect, 3, "ENVANTER DEĞERİ", "Tüm stokların anlık toplam tutarı", 'dark')
# Target: Dashboard Card 4 (ox + 860, oy + 12)
draw_pointer(d1, (p3_rect[0] + 105, p3_rect[1] + p3_rect[3]), (ox + 860, oy + 12), palette_name='dark', bend_first='y')

# Pill 4: ÜRÜN LİSTESİ TABLOSU (Bottom Left)
p4_rect = (ox + 150, oy + rh + 22, 230, 32)
draw_pill_callout(d1, p4_rect, 4, "ÜRÜN LİSTESİ TABLOSU", "Kod, fiyat, stok, tür ve kritik durumlar", 'dark')
# Target: Grid area (ox + 260, oy + rh - 40)
draw_pointer(d1, (p4_rect[0] + 115, p4_rect[1]), (ox + 260, oy + 420), palette_name='dark', bend_first='y')

# Pill 5: CRUD VE STOK İŞLEM BUTONLARI (Bottom Right)
p5_rect = (ox + 620, oy + rh + 22, 260, 32)
draw_pill_callout(d1, p5_rect, 5, "YÖNETİM VE STOK BUTONLARI", "Ürün ekle, düzenle, sil, giriş ve çıkış", 'green')
# Target: Buttons panel at bottom (ox + 750, oy + rh - 15)
draw_pointer(d1, (p5_rect[0] + 130, p5_rect[1]), (ox + 800, oy + 512), palette_name='green', bend_first='y')

c1.save(os.path.join(out_dir, "01_AnaEkran_Rehberi.png"))


# =========================================================================
# GÖRSEL 2: ANLIK ARAMA VE FİLTRELEME (Şekil 2 gibi)
# =========================================================================
print("Rendering Visual 2: Arama ve Filtreleme...")
raw2 = Image.open(os.path.join(raw_dir, "02_AramaFiltre.png"))
rw2, rh2 = raw2.size

cw2 = rw2 + 280 # width extended slightly on left/right for pills like sample
ch2 = rh2 + 150
c2 = Image.new('RGB', (cw2, ch2), color='#f1f5f9')

sdraw2 = ImageDraw.Draw(c2)
sdraw2.rounded_rectangle([138, 70, 138 + rw2 + 4, 70 + rh2 + 4], radius=6, fill='#cbd5e1')

ox2, oy2 = 140, 70
c2.paste(raw2, (ox2, oy2))
d2 = ImageDraw.Draw(c2)

# Pill 1: ANLIK ARAMA (Far Left)
p2_1 = (10, oy2 + 140, 120, 32)
draw_pill_callout(d2, p2_1, 1, "ANLIK ARAMA", "Yazıldıkça anında süzer", 'dark')
# Target: txtArama (ox2 + 60, oy2 + 152)
draw_pointer(d2, (p2_1[0] + p2_1[2], p2_1[1] + 16), (ox2 + 45, oy2 + 152), palette_name='dark', bend_first='x')

# Pill 2: FİLTRE VE KATEGORİ (Far Right Top)
p2_2 = (ox2 + rw2 + 10, oy2 + 138, 120, 32)
draw_pill_callout(d2, p2_2, 2, "KATEGORİ SEÇİMİ", "Elektronik, Gıda, Giyim", 'dark')
# Target: cmbKategoriFiltre (ox2 + 350, oy2 + 152)
draw_pointer(d2, (p2_2[0], p2_2[1] + 16), (ox2 + 400, oy2 + 152), palette_name='dark', bend_first='x')

# Pill 3: EŞLEŞEN ARAMA SONUÇLARI (Bottom Center)
p2_3 = (ox2 + 380, oy2 + rh2 + 25, 240, 32)
draw_pill_callout(d2, p2_3, 3, "EŞLEŞEN ARAMA SONUÇLARI", "Yalnızca 'Fare' içeren ürünler listelendi", 'dark')
# Target: Grid Row (ox2 + 450, oy2 + 240)
draw_pointer(d2, (p2_3[0] + 120, p2_3[1]), (ox2 + 450, oy2 + 245), palette_name='dark', bend_first='y')

c2.save(os.path.join(out_dir, "02_AramaFiltre_Rehberi.png"))


# =========================================================================
# GÖRSEL 3: KRİTİK STOK VE KIRMIZI UYARI (Şekil 3 gibi)
# =========================================================================
print("Rendering Visual 3: Kritik Stok Uyarı...")
raw3 = Image.open(os.path.join(raw_dir, "03_KritikStok.png"))
rw3, rh3 = raw3.size

cw3 = rw3 + 80
ch3 = rh3 + 150
c3 = Image.new('RGB', (cw3, ch3), color='#f1f5f9')

sdraw3 = ImageDraw.Draw(c3)
sdraw3.rounded_rectangle([38, 70, 38 + rw3 + 4, 70 + rh3 + 4], radius=6, fill='#cbd5e1')

ox3, oy3 = 40, 70
c3.paste(raw3, (ox3, oy3))
d3 = ImageDraw.Draw(c3)

# Pill 1: KRİTİK STOK SAYACI (Top Center-Left)
p3_1 = (ox3 + 360, 18, 220, 32)
draw_pill_callout(d3, p3_1, 1, "KRİTİK STOK SAYACI", "Listelenen kritik ürün sayısıyla eşleşir", 'dark')
# Target: Red KPI Card (ox3 + 580, oy3 + 12)
draw_pointer(d3, (p3_1[0] + 110, p3_1[1] + p3_1[3]), (ox3 + 580, oy3 + 12), palette_name='dark', bend_first='y')

# Pill 2: KRİTİK STOK FİLTRESİ (Top Center-Right)
p3_2 = (ox3 + 630, 18, 220, 32)
draw_pill_callout(d3, p3_2, 2, "KRİTİK STOK FİLTRESİ", "İşaretlenince yalnızca acil ürünleri ayıklar", 'red')
# Target: chkKritikStok (ox3 + 560, oy3 + 152)
draw_pointer(d3, (p3_2[0] + 110, p3_2[1] + p3_2[3]), (ox3 + 560, oy3 + 140), palette_name='red', bend_first='y')

# Pill 3: KIRMIZI UYARI VURGUSU (Bottom Center)
p3_3 = (ox3 + 420, oy3 + rh3 + 25, 260, 32)
draw_pill_callout(d3, p3_3, 3, "KIRMIZI UYARI VURGUSU", "Eşik altındaki ürünler otomatik kırmızı boyanır", 'red')
# Target: Red row in grid (ox3 + 450, oy3 + 260)
draw_pointer(d3, (p3_3[0] + 130, p3_3[1]), (ox3 + 450, oy3 + 260), palette_name='red', bend_first='y')

c3.save(os.path.join(out_dir, "03_KritikStok_Rehberi.png"))


# =========================================================================
# GÖRSEL 4: DENETİM İZİ (AUDIT LOG)
# =========================================================================
print("Rendering Visual 4: Denetim İzi...")
raw4 = Image.open(os.path.join(raw_dir, "04_DenetimIzi.png"))
rw4, rh4 = raw4.size

cw4 = rw4 + 80
ch4 = rh4 + 150
c4 = Image.new('RGB', (cw4, ch4), color='#f1f5f9')

sdraw4 = ImageDraw.Draw(c4)
sdraw4.rounded_rectangle([38, 70, 38 + rw4 + 4, 70 + rh4 + 4], radius=6, fill='#cbd5e1')

ox4, oy4 = 40, 70
c4.paste(raw4, (ox4, oy4))
d4 = ImageDraw.Draw(c4)

# Pill 1: ZAMAN DAMGASI VE İŞLEM TÜRÜ (Top Left)
p4_1 = (ox4 + 120, 18, 260, 32)
draw_pill_callout(d4, p4_1, 1, "ZAMAN DAMGASI VE İŞLEM TÜRÜ", "DateTime.Now ve IslemTuru Enum kaydı", 'dark')
# Target: Column 1 & 2 in Log Grid (ox4 + 150, oy4 + 160)
draw_pointer(d4, (p4_1[0] + 130, p4_1[1] + p4_1[3]), (ox4 + 150, oy4 + 150), palette_name='dark', bend_first='y')

# Pill 2: ÖNCEKİ VE SONRAKİ STOK (Top Right)
p4_2 = (ox4 + 680, 18, 250, 32)
draw_pill_callout(d4, p4_2, 2, "ÖNCEKİ VE SONRAKİ STOK", "Bakiye değişim miktarı ve net sonuç", 'blue')
# Target: Columns Before/After in Log Grid (ox4 + 580, oy4 + 160)
draw_pointer(d4, (p4_2[0] + 125, p4_2[1] + p4_2[3]), (ox4 + 580, oy4 + 150), palette_name='blue', bend_first='y')

# Pill 3: ZORUNLU İŞLEM NOTLARI (Bottom Center)
p4_3 = (ox4 + 400, oy4 + rh4 + 25, 270, 32)
draw_pill_callout(d4, p4_3, 3, "ZORUNLU İŞLEM AÇIKLAMALARI", "İrsaliye, fatura ve sevkiyat takip geçmişi", 'green')
# Target: Notes Column (ox4 + 750, oy4 + 220)
draw_pointer(d4, (p4_3[0] + 135, p4_3[1]), (ox4 + 750, oy4 + 220), palette_name='green', bend_first='y')

c4.save(os.path.join(out_dir, "04_DenetimIzi_Rehberi.png"))


# =========================================================================
# GÖRSEL 5: YENİ ÜRÜN EKLEME FORMU (Şekil 4 gibi)
# =========================================================================
print("Rendering Visual 5: Yeni Ürün Ekleme (Form)...")
raw5 = Image.open(os.path.join(raw_dir, "05_UrunEkle_Elektronik.png"))
rw5, rh5 = raw5.size # 436 x 519

# In sample (Şekil 4), dialog is centered, callouts on LEFT and RIGHT!
cw5 = rw5 + 540 # 270 on left, 270 on right
ch5 = rh5 + 80
c5 = Image.new('RGB', (cw5, ch5), color='#f1f5f9')

ox5, oy5 = 270, 40

sdraw5 = ImageDraw.Draw(c5)
sdraw5.rounded_rectangle([ox5 - 2, oy5, ox5 + rw5 + 2, oy5 + rh5 + 4], radius=6, fill='#cbd5e1')

c5.paste(raw5, (ox5, oy5))
d5 = ImageDraw.Draw(c5)

# Left Side Pills:
# 1: KATEGORİ SEÇİMİ (y=60)
p5_1 = (20, oy5 + 30, 220, 32)
draw_pill_callout(d5, p5_1, 1, "KATEGORİ SEÇİMİ", "Elektronik, Gıda veya Giyim", 'dark')
draw_pointer(d5, (p5_1[0] + p5_1[2], p5_1[1] + 16), (ox5 + 35, oy5 + 68), palette_name='dark', bend_first='x')

# 2: ÜRÜN KODU KURALI (y=120)
p5_2 = (20, oy5 + 85, 220, 32)
draw_pill_callout(d5, p5_2, 2, "ÜRÜN KODU KURALI", "Benzersiz kod; özel karakter yasaktır", 'red')
draw_pointer(d5, (p5_2[0] + p5_2[2], p5_2[1] + 16), (ox5 + 35, oy5 + 118), palette_name='red', bend_first='x')

# 3: ÜRÜN ADI VE GÜVENLİK (y=175)
p5_3 = (20, oy5 + 140, 220, 32)
draw_pill_callout(d5, p5_3, 3, "ÜRÜN ADI GÜVENLİĞİ", "XSS ve enjeksiyon karakterleri filtrelenir", 'green')
draw_pointer(d5, (p5_3[0] + p5_3[2], p5_3[1] + 16), (ox5 + 35, oy5 + 168), palette_name='green', bend_first='x')

# 4: DOĞRULA VE KAYDET (y=440)
p5_4 = (20, oy5 + 430, 220, 32)
draw_pill_callout(d5, p5_4, 4, "DOĞRULA VE KAYDET", "Kuralları denetler ve sisteme ekler", 'green')
draw_pointer(d5, (p5_4[0] + p5_4[2], p5_4[1] + 16), (ox5 + 100, oy5 + 465), palette_name='green', bend_first='x')

# Right Side Pills:
# 5: MİNİMUM FİYAT (y=215)
p5_5 = (ox5 + rw5 + 25, oy5 + 215, 220, 32)
draw_pill_callout(d5, p5_5, 5, "MİNİMUM FİYAT KURALI", "Sıfır ve eksi yasak (Min: 0,01 ₺)", 'amber')
draw_pointer(d5, (p5_5[0], p5_5[1] + 16), (ox5 + rw5 - 35, oy5 + 225), palette_name='amber', bend_first='x')

# 6: BAŞLANGIÇ STOĞU (y=265)
p5_6 = (ox5 + rw5 + 25, oy5 + 270, 220, 32)
draw_pill_callout(d5, p5_6, 6, "BAŞLANGIÇ STOĞU", "Sıfır veya pozitif tam sayı", 'amber')
draw_pointer(d5, (p5_6[0], p5_6[1] + 16), (ox5 + rw5 - 35, oy5 + 275), palette_name='amber', bend_first='x')

# 7: TÜRE ÖZEL ALAN (y=340)
p5_7 = (ox5 + rw5 + 25, oy5 + 340, 220, 32)
draw_pill_callout(d5, p5_7, 7, "TÜRE ÖZEL DİNAMİK ALAN", "Garanti (Ay) ve Voltaj (V)", 'dark')
draw_pointer(d5, (p5_7[0], p5_7[1] + 16), (ox5 + rw5 - 35, oy5 + 345), palette_name='dark', bend_first='x')

c5.save(os.path.join(out_dir, "05_UrunEkle_Elektronik_Rehberi.png"))


# =========================================================================
# GÖRSEL 6: ÜRÜN DÜZENLEME FORMU
# =========================================================================
print("Rendering Visual 6: Ürün Düzenleme (Form)...")
raw6 = Image.open(os.path.join(raw_dir, "06_UrunDuzenle.png"))
rw6, rh6 = raw6.size

cw6 = rw6 + 540
ch6 = rh6 + 80
c6 = Image.new('RGB', (cw6, ch6), color='#f1f5f9')

ox6, oy6 = 270, 40

sdraw6 = ImageDraw.Draw(c6)
sdraw6.rounded_rectangle([ox6 - 2, oy6, ox6 + rw6 + 2, oy6 + rh6 + 4], radius=6, fill='#cbd5e1')

c6.paste(raw6, (ox6, oy6))
d6 = ImageDraw.Draw(c6)

# Left Side Pills:
# 1: KİLİTLİ ÜRÜN KODU
p6_1 = (20, oy5 + 60, 220, 32)
draw_pill_callout(d6, p6_1, 1, "KİLİTLİ ÜRÜN KODU", "ReadOnly = true; değiştirilemez", 'red')
draw_pointer(d6, (p6_1[0] + p6_1[2], p6_1[1] + 16), (ox6 + 35, oy6 + 80), palette_name='red', bend_first='x')

# 2: KORUMALI BAŞLANGIÇ STOĞU
p6_2 = (20, oy5 + 200, 220, 32)
draw_pill_callout(d6, p6_2, 2, "KİLİTLİ STOK DEĞERİ", "Doğrudan elle müdahale engellidir", 'red')
draw_pointer(d6, (p6_2[0] + p6_2[2], p6_2[1] + 16), (ox6 + 35, oy6 + 225), palette_name='red', bend_first='x')

# Right Side Pills:
# 3: GÜNCELLENEBİLİR FİYAT
p6_3 = (ox6 + rw6 + 25, oy6 + 180, 220, 32)
draw_pill_callout(d6, p6_3, 3, "BİRİM FİYAT DÜZENLEME", "Geçerli yeni satış fiyatı girilir", 'blue')
draw_pointer(d6, (p6_3[0], p6_3[1] + 16), (ox6 + rw6 - 35, oy6 + 185), palette_name='blue', bend_first='x')

# 4: TEKNİK BİLGİ REVİZYONU
p6_4 = (ox6 + rw6 + 25, oy6 + 320, 220, 32)
draw_pill_callout(d6, p6_4, 4, "TEKNİK BİLGİ REVİZYONU", "Kategoriye özel alanlar güncellenir", 'dark')
draw_pointer(d6, (p6_4[0], p6_4[1] + 16), (ox6 + rw6 - 35, oy6 + 335), palette_name='dark', bend_first='x')

c6.save(os.path.join(out_dir, "06_UrunDuzenle_Rehberi.png"))


# =========================================================================
# GÖRSEL 7: KONTROLLÜ STOK GİRİŞİ (Şekil 5 gibi)
# =========================================================================
print("Rendering Visual 7: Stok Giriş (Şekil 5 gibi)...")
raw7 = Image.open(os.path.join(raw_dir, "07_StokGiris.png"))
rw7, rh7 = raw7.size # 396 x 329

cw7 = rw7 + 540
ch7 = rh7 + 80
c7 = Image.new('RGB', (cw7, ch7), color='#f1f5f9')

ox7, oy7 = 270, 40

sdraw7 = ImageDraw.Draw(c7)
sdraw7.rounded_rectangle([ox7 - 2, oy7, ox7 + rw7 + 2, oy7 + rh7 + 4], radius=6, fill='#cbd5e1')

c7.paste(raw7, (ox7, oy7))
d7 = ImageDraw.Draw(c7)

# Left Side Pills:
# 1: SEÇİLİ ÜRÜN ÖZETİ
p7_1 = (20, oy7 + 50, 220, 32)
draw_pill_callout(d7, p7_1, 1, "SEÇİLİ ÜRÜN ÖZETİ", "Ürün adı, kodu ve güncel stok adedi", 'dark')
draw_pointer(d7, (p7_1[0] + p7_1[2], p7_1[1] + 16), (ox7 + 35, oy7 + 85), palette_name='dark', bend_first='x')

# 4: STOK ARTIR VE KAYDET
p7_4 = (20, oy7 + 230, 220, 32)
draw_pill_callout(d7, p7_4, 4, "STOK ARTIR VE KAYDET", "Stoğu günceller ve sayaçları yeniler", 'green')
draw_pointer(d7, (p7_4[0] + p7_4[2], p7_4[1] + 16), (ox7 + 100, oy7 + 265), palette_name='green', bend_first='x')

# Right Side Pills:
# 2: GİRİŞ MİKTARI
p7_2 = (ox7 + rw7 + 25, oy7 + 120, 220, 32)
draw_pill_callout(d7, p7_2, 2, "GİRİŞ MİKTARI KURALI", "Pozitif tam sayı zorunlu (Min: 1)", 'green')
draw_pointer(d7, (p7_2[0], p7_2[1] + 16), (ox7 + rw7 - 35, oy7 + 135), palette_name='green', bend_first='x')

# 3: HAREKET AÇIKLAMASI
p7_3 = (ox7 + rw7 + 25, oy7 + 175, 220, 32)
draw_pill_callout(d7, p7_3, 3, "HAREKET AÇIKLAMASI", "İşlem geçmişine kaydedilen not", 'blue')
draw_pointer(d7, (p7_3[0], p7_3[1] + 16), (ox7 + rw7 - 35, oy7 + 185), palette_name='blue', bend_first='x')

c7.save(os.path.join(out_dir, "07_StokGiris_Rehberi.png"))


# =========================================================================
# GÖRSEL 8: BAKİYE KONTROLLÜ STOK ÇIKIŞI (Şekil 6 gibi)
# =========================================================================
print("Rendering Visual 8: Stok Çıkış (Şekil 6 gibi)...")
raw8 = Image.open(os.path.join(raw_dir, "08_StokCikis.png"))
rw8, rh8 = raw8.size # 396 x 329

cw8 = rw8 + 540
ch8 = rh8 + 80
c8 = Image.new('RGB', (cw8, ch8), color='#f1f5f9')

ox8, oy8 = 270, 40

sdraw8 = ImageDraw.Draw(c8)
sdraw8.rounded_rectangle([ox8 - 2, oy8, ox8 + rw8 + 2, oy8 + rh8 + 4], radius=6, fill='#cbd5e1')

c8.paste(raw8, (ox8, oy8))
d8 = ImageDraw.Draw(c8)

# Left Side Pills:
# 1: MEVCUT STOK BİLGİSİ
p8_1 = (20, oy8 + 50, 220, 32)
draw_pill_callout(d8, p8_1, 1, "MEVCUT STOK BİLGİSİ", "Ürünün kalan stok üst sınırını gösterir", 'dark')
draw_pointer(d8, (p8_1[0] + p8_1[2], p8_1[1] + 16), (ox8 + 35, oy8 + 85), palette_name='dark', bend_first='x')

# 3: ÇIKIŞI ONAYLA
p8_3 = (20, oy8 + 230, 220, 32)
draw_pill_callout(d8, p8_3, 3, "ÇIKIŞI ONAYLA", "Stoktan düşer ve kritik durumu denetler", 'red')
draw_pointer(d8, (p8_3[0] + p8_3[2], p8_3[1] + 16), (ox8 + 100, oy8 + 265), palette_name='red', bend_first='x')

# Right Side Pills:
# 2: NEGATİF STOK KORUMASI
p8_2 = (ox8 + rw8 + 25, oy8 + 120, 230, 32)
draw_pill_callout(d8, p8_2, 2, "NEGATİF STOK KORUMASI", "Mevcut stoktan fazla çıkış engellidir", 'red')
draw_pointer(d8, (p8_2[0], p8_2[1] + 16), (ox8 + rw8 - 35, oy8 + 135), palette_name='red', bend_first='x')

c8.save(os.path.join(out_dir, "08_StokCikis_Rehberi.png"))

print("ALL 8 visuals successfully rendered in EXACT reference PDF style (pills, badges, orthogonal arrows)!")
