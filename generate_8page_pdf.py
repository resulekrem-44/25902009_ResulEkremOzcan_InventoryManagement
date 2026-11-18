# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.image as mpimg

plt.rcParams['font.sans-serif'] = ['Segoe UI', 'DejaVu Sans', 'Arial', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

desktop = os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop')
proj_dir = os.path.join(desktop, '.NET PROJE ÖDEVİ', '25902009_ResulEkremOzcan_InventoryManagement')
report_pdf = os.path.join(proj_dir, "03_Report", "Proje_Raporu.pdf")
shots_dir = os.path.join(proj_dir, "03_Report", "Gorseller")

with PdfPages(report_pdf) as pdf:
    # -------------------------------------------------------------
    # SAYFA 1: KAPAK
    # -------------------------------------------------------------
    fig_cover = plt.figure(figsize=(8.27, 11.69))
    fig_cover.patch.set_facecolor('#f8fafc')
    ax = fig_cover.add_axes([0, 0, 1, 1])
    ax.axis('off')

    ax.add_patch(plt.Rectangle((0, 0.95), 1, 0.05, color='#0f172a', transform=ax.transAxes))
    ax.add_patch(plt.Rectangle((0, 0.94), 1, 0.01, color='#2563eb', transform=ax.transAxes))

    ax.text(0.5, 0.86, "T.C.\nKAPADOKYA ÜNİVERSİTESİ", ha='center', va='center', fontsize=18, weight='bold', color='#0f172a', linespacing=1.3)
    ax.text(0.5, 0.80, "İKTİSADİ, İDARİ VE SOSYAL BİLİMLER FAKÜLTESİ\nBİLİŞİM SİSTEMLERİ VE TEKNOLOJİLERİ BÖLÜMÜ", ha='center', va='center', fontsize=12, weight='semibold', color='#475569', linespacing=1.3)

    ax.add_patch(plt.Rectangle((0.1, 0.52), 0.8, 0.22, color='#ffffff', ec='#cbd5e1', lw=1.5, transform=ax.transAxes))
    ax.add_patch(plt.Rectangle((0.1, 0.72), 0.8, 0.02, color='#2563eb', transform=ax.transAxes))
    
    ax.text(0.5, 0.67, "STOK YÖNETİM SİSTEMİ", ha='center', va='center', fontsize=20, weight='bold', color='#1e293b')
    ax.text(0.5, 0.61, "INVENTORY MANAGEMENT SYSTEM", ha='center', va='center', fontsize=13, weight='semibold', color='#64748b')
    ax.text(0.5, 0.56, ".NET Programlama - I Dersi Dönem Proje Raporu", ha='center', va='center', fontsize=11, style='italic', color='#3b82f6')

    ax.add_patch(plt.Rectangle((0.15, 0.22), 0.7, 0.24, color='#ffffff', ec='#94a3b8', lw=1, transform=ax.transAxes))
    
    bilgiler = [
        ("Ders Kodu & Adı :", "BGT331 / BST301 - .NET Programlama - I"),
        ("Öğretim Elemanı :", "Dr. Öğr. Üyesi Tohid YOUSEFİ"),
        ("Öğrenci Adı Soyadı :", "Resul Ekrem ÖZCAN"),
        ("Öğrenci Numarası :", "25902009"),
        ("Dönem :", "2026-2027 Güz Dönemi"),
        ("Teslim Tarihi :", "20 Kasım 2026"),
        ("GitHub Repository :", "25902009_ResulEkremOzcan_InventoryManagement")
    ]
    
    y_pos = 0.42
    for etiket, deger in bilgiler:
        ax.text(0.18, y_pos, etiket, fontsize=10, weight='bold', color='#334155')
        ax.text(0.42, y_pos, deger, fontsize=10, color='#0f172a')
        y_pos -= 0.028

    ax.text(0.5, 0.08, "Nevşehir • 2026", ha='center', va='center', fontsize=11, weight='bold', color='#64748b')
    ax.add_patch(plt.Rectangle((0, 0), 1, 0.02, color='#0f172a', transform=ax.transAxes))
    pdf.savefig(fig_cover, dpi=300)
    plt.close(fig_cover)

    # -------------------------------------------------------------
    # SAYFA 2: PROJE AMACI VE MİMARİ
    # -------------------------------------------------------------
    fig2 = plt.figure(figsize=(8.27, 11.69))
    fig2.patch.set_facecolor('white')
    ax2 = fig2.add_axes([0.08, 0.06, 0.84, 0.88])
    ax2.axis('off')

    ax2.text(0, 1.0, "1. PROJENİN AMACI VE KAPSAMI", fontsize=13, weight='bold', color='#0f172a')
    p1 = (
        "Bu proje; modern nesne tabanlı programlama (OOP) prensiplerini ve C# Windows Forms mimarisini uygulayarak, "
        "bir işletmenin ürün kayıtlarını, stok seviyelerini ve envanter hareketlerini dinamik, güvenli ve hatasız bir şekilde "
        "yönetebilmesini sağlayan kurumsal bir 'Stok Yönetim Sistemi' masaüstü uygulamasıdır.\n\n"
        "Şartname Kapsamı ve Sınırlamalar: Proje şartnamesi doğrultusunda dönem ortası seviyesine sadık kalınmış; "
        "veritabanı/SQL bağımlılığı olmaksızın tüm veri yönetimi uygulama belleğinde (In-Memory) Generic List<T> "
        "koleksiyonları üzerinden yüksek hız ve performans ile gerçekleştirilmiştir."
    )
    ax2.text(0, 0.96, p1, fontsize=9.2, color='#334155', linespacing=1.35, va='top')

    ax2.text(0, 0.83, "2. GELİŞTİRME ORTAMI VE TEKNOLOJİ BİLGİSİ", fontsize=13, weight='bold', color='#0f172a')
    t_env = [
        ("• Programlama Dili :", "C# (C-Sharp) 7.3+ Standartları"),
        ("• Hedef Çerçeve :", ".NET Framework v4.8 (Windows Desktop Forms)"),
        ("• Geliştirme Ortamı :", "Microsoft Visual Studio 2022 Community"),
        ("• Mimari Yaklaşım :", "Çok Katmanlı Ayrıştırma (Forms, Models, Services)"),
        ("• Tasarım Standartları :", "Nesne Yönelimli Tasarım (Encapsulation, Inheritance, Polymorphism, Abstraction)")
    ]
    y_e = 0.79
    for k, v in t_env:
        ax2.text(0.02, y_e, k, fontsize=9, weight='bold', color='#1e293b')
        ax2.text(0.35, y_e, v, fontsize=9, color='#475569')
        y_e -= 0.024

    ax2.text(0, 0.65, "3. UYGULAMANIN GENEL YAPISI VE TEMEL İŞLEVLERİ", fontsize=13, weight='bold', color='#0f172a')
    p2 = (
        "Uygulama iş mantığı (Business Logic) ile arayüz kodlarını birbirinden kesin hatlarla ayrıştıran 3 temel katmandan oluşur:\n\n"
        "1. Models (Veri ve Varlık Katmanı): Ürün varlıklarını, soyut sınıfları, arayüzleri ve işlem kayıtlarını temsil eder.\n"
        "2. Services (İş Mantığı Katmanı): StokYonetici sınıfı ile tüm koleksiyon operasyonları, arama, filtreleme, stok giriş/çıkış "
        "doğrulamaları ve canlı envanter istatistikleri merkezi olarak yönetilir.\n"
        "3. Forms (Kullanıcı Arayüzü Katmanı): FormAnaEkran, FormUrunEkleGuncelle ve FormStokIslem pencereleri üzerinden son kullanıcı "
        "ile estetik ve modern kontroller (DataGridView, TabControl, NumericUpDown) aracılığıyla etkileşim kurulur.\n\n"
        "Temel İşlevler:\n"
        "• Ürün Ekleme/Düzenleme/Silme: Benzersiz kod kontrolü ile kategoriye özgü alanların girilmesi.\n"
        "• Stok Girişi (+): Sıfırdan büyük miktar doğrulamasıyla stok artırma ve denetim kaydı oluşturma.\n"
        "• Stok Çıkışı (-): Negatif stok oluşmasını kesin olarak engelleyen bakiye kontrolü ve stok düşümü.\n"
        "• Canlı Dashboard: Toplam ürün çeşidi, toplam fiziksel stok, kritik seviye altındaki ürünler ve envanter tutarı hesaplaması.\n"
        "• Arama ve Filtreleme: Ürün adı veya koduna göre canlı arama, kategoriye ve kritik stok durumuna göre anlık listeleme."
    )
    ax2.text(0, 0.61, p2, fontsize=9.2, color='#334155', linespacing=1.35, va='top')

    ax2.text(0.5, 0.01, "- Sayfa 2 -", ha='center', fontsize=9, color='#94a3b8')
    pdf.savefig(fig2, dpi=300)
    plt.close(fig2)

    # -------------------------------------------------------------
    # SAYFA 3: DETAYLI OOP İLKELERİ VE VALIDATION
    # -------------------------------------------------------------
    fig3 = plt.figure(figsize=(8.27, 11.69))
    fig3.patch.set_facecolor('white')
    ax3 = fig3.add_axes([0.08, 0.06, 0.84, 0.88])
    ax3.axis('off')

    ax3.text(0, 1.0, "4. SINIF VE NESNE TASARIMI (OOP İLKELERİNİN UYGULANIŞI)", fontsize=13, weight='bold', color='#0f172a')
    
    oop_sections = [
        ("A. Kapsülleme (Encapsulation - Ders Slaytları ile Birebir Uyum):",
         "Dr. Tohid Yousefi'nin ders sunumlarında vurguladığı gibi verilerin yetkisiz değiştirilmesini engellemek için tüm alanlar "
         "'private' yapılmıştır. Fiyata 0 veya negatif girildiğinde, miktar 0, 00, 000 veya eksi girildiğinde sistem kontrollü "
         "ArgumentException fırlatır. Ayrıca ürün kodunun dışarıdan değiştirilememesi için 'private set' uygulanmıştır."),

        ("B. Kalıtım (Inheritance & ': base(...)' Kullanımı):",
         "Soyut 'Urun' temel sınıfından 'ElektronikUrun', 'GidaUrunu' ve 'GiyimUrunu' olmak üzere 3 alt sınıf türetilmiştir. "
         "Alt sınıflar ': base(urunKodu, urunAdi, ...)' ile üst sınıf yapıcısını çağırır ve ortak nitelikleri devralır."),

        ("C. Çok Biçimlilik (Polymorphism - virtual / abstract / override):",
         "• KDVOraniGetir(): Elektronik için %20, Gıda için %1, Giyim için %10 olarak override edilmiştir.\n"
         "• DetayBilgisiGetir(): Elektronik için Marka/Garanti, Gıda için STT/Soğuk Zincir, Giyim için Beden/Kumaş "
         "bilgilerini polimorfik olarak döndürür ve arayüz tablosunda her ürün kendi detayını sergiler."),

        ("D. Soyutlama (Abstraction - abstract class & interface):",
         "'IStoklanabilir' arayüzü ile stok işlemleri sözleşmeye bağlanmış, 'Urun' soyut (abstract) sınıfı ile "
         "tek başına doğrudan nesne üretimi engellenmiştir.")
    ]

    y_oop = 0.96
    for baslik, icerik in oop_sections:
        ax3.text(0, y_oop, baslik, fontsize=10.5, weight='bold', color='#1d4ed8')
        y_oop -= 0.024
        ax3.text(0, y_oop, icerik, fontsize=8.8, color='#334155', linespacing=1.3, va='top')
        y_oop -= 0.125

    ax3.text(0, 0.38, "5. HATA YÖNETİMİ, DEBUGGING VE İSTİSNA YÖNETİMİ", fontsize=12, weight='bold', color='#0f172a')
    dbg_txt = (
        "Uygulamada olası tüm kullanıcı hataları çok katmanlı olarak engellenmiştir:\n"
        "• Boş Bırakılamaz & Uzunluk Doğrulaması: Ürün kodu ve adı en az 2 karakter olmalıdır.\n"
        "• Özel Karakter Filtresi: Ürün adı, kodu ve açıklamada @, #, $, <, > gibi yabancı karakterler engellenir.\n"
        "• 0, 00, 000 ve Negatif Bakiye Koruması: Stok giriş/çıkışında sıfır veya mevcut stoktan fazla çıkış kilitlenmiştir.\n"
        "• Visual Studio Debugging Örneği: 'StokCikisYap' metodu içine Breakpoint konulup Watch/Locals pencerelerinde "
        "adım adım incelenmiş, bakiye sınır değer testlerinde stokların kesinlikle eksiye düşmediği kanıtlanmıştır."
    )
    ax3.text(0, 0.34, dbg_txt, fontsize=8.8, color='#334155', linespacing=1.3, va='top')

    ax3.text(0.5, 0.01, "- Sayfa 3 -", ha='center', fontsize=9, color='#94a3b8')
    pdf.savefig(fig3, dpi=300)
    plt.close(fig3)

    # -------------------------------------------------------------
    # SAYFA 4: AKTİVİTE 1 (ANA EKRAN)
    # -------------------------------------------------------------
    fig4 = plt.figure(figsize=(8.27, 11.69))
    fig4.patch.set_facecolor('white')
    ax4 = fig4.add_axes([0.06, 0.06, 0.88, 0.88])
    ax4.axis('off')
    ax4.text(0, 1.0, "6. GÖRSEL BELGELENDİRME VE İŞLEVSEL AKTİVİTE REHBERİ", fontsize=13, weight='bold', color='#0f172a')
    ax4.text(0, 0.965, "Aktivite 1: Ana Ekran Kontrol ve Diyalog Bilgi Kartları Haritası", fontsize=10, weight='bold', color='#1d4ed8')

    img_act1 = os.path.join(shots_dir, "01_AnaEkran_Rehberi.png")
    if os.path.exists(img_act1):
        im = mpimg.imread(img_act1)
        ax_img = fig4.add_axes([0.06, 0.12, 0.88, 0.82])
        ax_img.imshow(im)
        ax_img.axis('off')

    ax4.text(0, 0.04, "Açıklama 1: Canlı Dashboard kartları, arama/kategori paneli, kritik stok renklendirmesi ve CRUD/Stok butonları yönlendirici oklarla eşleştirilmiştir.", fontsize=8.2, color='#475569', style='italic')
    ax4.text(0.5, 0.01, "- Sayfa 4 -", ha='center', fontsize=9, color='#94a3b8')
    pdf.savefig(fig4, dpi=300)
    plt.close(fig4)

    # -------------------------------------------------------------
    # SAYFA 5: AKTİVİTE 2 (ARAMA) VE AKTİVİTE 3 (KRİTİK STOK)
    # -------------------------------------------------------------
    fig5 = plt.figure(figsize=(8.27, 11.69))
    fig5.patch.set_facecolor('white')
    ax5 = fig5.add_axes([0.06, 0.06, 0.88, 0.88])
    ax5.axis('off')
    ax5.text(0, 1.0, "Aktivite 2 & 3: Canlı Arama Süzme ve Kritik Stok Tespiti", fontsize=12, weight='bold', color='#1d4ed8')

    img_act2 = os.path.join(shots_dir, "02_AramaFiltre_Rehberi.png")
    img_act3 = os.path.join(shots_dir, "03_KritikStok_Rehberi.png")

    if os.path.exists(img_act2):
        im = mpimg.imread(img_act2)
        ax_img = fig5.add_axes([0.06, 0.52, 0.88, 0.44])
        ax_img.imshow(im)
        ax_img.axis('off')

    if os.path.exists(img_act3):
        im = mpimg.imread(img_act3)
        ax_img = fig5.add_axes([0.06, 0.06, 0.88, 0.44])
        ax_img.imshow(im)
        ax_img.axis('off')

    ax5.text(0.5, 0.01, "- Sayfa 5 -", ha='center', fontsize=9, color='#94a3b8')
    pdf.savefig(fig5, dpi=300)
    plt.close(fig5)

    # -------------------------------------------------------------
    # SAYFA 6: AKTİVİTE 5 (ÜRÜN EKLEME) VE AKTİVİTE 6 (DÜZENLEME)
    # -------------------------------------------------------------
    fig6 = plt.figure(figsize=(8.27, 11.69))
    fig6.patch.set_facecolor('white')
    ax6 = fig6.add_axes([0.06, 0.06, 0.88, 0.88])
    ax6.axis('off')
    ax6.text(0, 1.0, "Aktivite 5 & 6: Yeni Ürün Ekleme (Validation) ve Bilgi Güncelleme", fontsize=12, weight='bold', color='#1d4ed8')

    img_act5 = os.path.join(shots_dir, "05_UrunEkle_Elektronik_Rehberi.png")
    img_act6 = os.path.join(shots_dir, "06_UrunDuzenle_Rehberi.png")

    if os.path.exists(img_act5):
        im = mpimg.imread(img_act5)
        ax_img = fig6.add_axes([0.06, 0.52, 0.88, 0.44])
        ax_img.imshow(im)
        ax_img.axis('off')

    if os.path.exists(img_act6):
        im = mpimg.imread(img_act6)
        ax_img = fig6.add_axes([0.06, 0.06, 0.88, 0.44])
        ax_img.imshow(im)
        ax_img.axis('off')

    ax6.text(0.5, 0.01, "- Sayfa 6 -", ha='center', fontsize=9, color='#94a3b8')
    pdf.savefig(fig6, dpi=300)
    plt.close(fig6)

    # -------------------------------------------------------------
    # SAYFA 7: AKTİVİTE 7 (STOK GİRİŞ) VE AKTİVİTE 8 (STOK ÇIKIŞ)
    # -------------------------------------------------------------
    fig7 = plt.figure(figsize=(8.27, 11.69))
    fig7.patch.set_facecolor('white')
    ax7 = fig7.add_axes([0.06, 0.06, 0.88, 0.88])
    ax7.axis('off')
    ax7.text(0, 1.0, "Aktivite 7 & 8: Stok Giriş (+) ve Stok Çıkış (-) Güvenlik Diyalogları", fontsize=12, weight='bold', color='#1d4ed8')

    img_act7 = os.path.join(shots_dir, "07_StokGiris_Rehberi.png")
    img_act8 = os.path.join(shots_dir, "08_StokCikis_Rehberi.png")

    if os.path.exists(img_act7):
        im = mpimg.imread(img_act7)
        ax_img = fig7.add_axes([0.06, 0.52, 0.88, 0.44])
        ax_img.imshow(im)
        ax_img.axis('off')

    if os.path.exists(img_act8):
        im = mpimg.imread(img_act8)
        ax_img = fig7.add_axes([0.06, 0.06, 0.88, 0.44])
        ax_img.imshow(im)
        ax_img.axis('off')

    ax7.text(0.5, 0.01, "- Sayfa 7 -", ha='center', fontsize=9, color='#94a3b8')
    pdf.savefig(fig7, dpi=300)
    plt.close(fig7)

    # -------------------------------------------------------------
    # SAYFA 8: AKTİVİTE 4 (DENETİM İZİ) VE UÇTAN UCA TEST SENARYOLARI
    # -------------------------------------------------------------
    fig8 = plt.figure(figsize=(8.27, 11.69))
    fig8.patch.set_facecolor('white')
    ax8 = fig8.add_axes([0.06, 0.06, 0.88, 0.88])
    ax8.axis('off')
    ax8.text(0, 1.0, "Aktivite 4: Stok Hareketleri Geçmişi ve Denetim İzi (Audit Log)", fontsize=11, weight='bold', color='#1d4ed8')

    img_act4 = os.path.join(shots_dir, "04_DenetimIzi_Rehberi.png")
    if os.path.exists(img_act4):
        im = mpimg.imread(img_act4)
        ax_img = fig8.add_axes([0.06, 0.56, 0.88, 0.41])
        ax_img.imshow(im)
        ax_img.axis('off')

    ax8.text(0, 0.51, "7. UÇTAN UCA TEST SENARYOLARI VE DOĞRULAMA TABLOSU", fontsize=11, weight='bold', color='#0f172a')

    col_x = [0.0, 0.20, 0.46, 0.74, 0.90]
    headers = ["Test Adı / Senaryo", "Girilen Değer / Girdi", "Beklenen Sonuç", "Gerçekleşen Sonuç", "Durum"]
    
    y_t = 0.47
    ax8.add_patch(plt.Rectangle((0, y_t-0.01), 1, 0.025, color='#f1f5f9', transform=ax8.transAxes))
    for i, h in enumerate(headers):
        ax8.text(col_x[i], y_t, h, fontsize=8, weight='bold', color='#1e293b')
    
    tests = [
        ("TS-01: Tekrarlayan Ürün Kodu", "Mevcut 'ELK-101' ile yeni kayıt", "Kayıt engellenmeli, hata fırlatılmalı", "Kayıt durduruldu, 'Ürün zaten kayıtlı' uyarısı verildi", "BAŞARILI"),
        ("TS-02: 0 TL ve Negatif Fiyat", "Fiyat alanına '0' veya '-100 TL'", "Kapsüllemede ArgumentException", "Veri girilemedi, 0 ve negatif fiyat engellendi", "BAŞARILI"),
        ("TS-03: Miktarda 000 ve Yabancı Karakter", "Miktar '000', Açıklama '<script>'", "Sayısal ve regex kontrolü ile ret", "İşlem durduruldu, 'Geçersiz miktar/karakter' uyarısı", "BAŞARILI"),
        ("TS-04: Yetersiz Stok Çıkışı", "Eldeki 12 adetten 50 adet çıkış", "Eksiye düşüş kesinlikle engellenmeli", "İşlem kilitlendi, 'Yetersiz stok bakiye' uyarısı verildi", "BAŞARILI"),
        ("TS-05: Kritik Stok & Canlı Dashboard", "Kritik Stok Kutucuğu Seçilmesi", "Sadece kritik seviyedekiler listelenmeli", "3 adet kritik ürün süzüldü, kırmızı renkle vurgulandı", "BAŞARILI")
    ]

    y_t -= 0.035
    for no, girdi, beklenen, gercek, durum in tests:
        ax8.text(col_x[0], y_t, no, fontsize=7.5, weight='bold', color='#334155')
        ax8.text(col_x[1], y_t, girdi, fontsize=7.2, color='#475569')
        ax8.text(col_x[2], y_t, beklenen, fontsize=7.2, color='#475569')
        ax8.text(col_x[3], y_t, gercek, fontsize=7.2, color='#059669')
        ax8.text(col_x[4], y_t, durum, fontsize=7.5, weight='bold', color='#16a34a')
        ax8.add_patch(plt.Rectangle((0, y_t-0.01), 1, 0.001, color='#e2e8f0', transform=ax8.transAxes))
        y_t -= 0.035

    ax8.text(0, 0.23, "8. SONUÇ VE DEĞERLENDİRME", fontsize=11, weight='bold', color='#0f172a')
    c_txt = (
        "Geliştirilen 'Stok Yönetim Sistemi', C# WinForms ve .NET Framework 4.8 altyapısında nesne yönelimli programlamanın 4 temel "
        "ilkesini (Encapsulation, Inheritance, Polymorphism, Abstraction) tam bir uyumla hayata geçirmiştir. Katmanlı mimari, "
        "dinamik dashboard, güçlü hata yönetimi ve modern arayüz tasarımıyla akademik teknik şartname beklentilerini eksiksiz karşılamaktadır."
    )
    ax8.text(0, 0.20, c_txt, fontsize=8.2, color='#334155', linespacing=1.3, va='top')

    ax8.text(0.5, 0.01, "- Sayfa 8 -", ha='center', fontsize=9, color='#94a3b8')
    pdf.savefig(fig8, dpi=300)
    plt.close(fig8)

print("8 Sayfalik Genisletilmis Proje Raporu PDF basariyla olusturuldu!")
