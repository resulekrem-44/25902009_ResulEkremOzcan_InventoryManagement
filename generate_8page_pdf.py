# -*- coding: utf-8 -*-
"""
Generate the exact reference-style PDF report matching the user's uploaded sample PDF:
- Page 1: Elegant modern cover page with header bar, title badge, metadata table, and footer.
- Page 2: 1. Proje Özeti ve Amaç, 2. Sistem Mimarisi ve Nesne Tabanlı Programlama İlkeleri (OOP tablosu, C# kod örneği).
- Page 3: 3. Uygulama Modülleri ve Ekran Görüntüleri:
          3.1. Ana Ekran ve Canlı Özet Paneli (Şekil 1)
          3.2. Anlık Arama, Filtreleme ve Yönetim Çubuğu (Şekil 2)
- Page 4: 3.3. Kritik Stok Takibi ve Uyarı Filtresi (Şekil 3)
          3.4. Yeni Ürün Kayıt Formu ve Veri Doğrulama (Şekil 4)
- Page 5: 3.5. Kontrollü Stok Giriş ve Çıkış İşlemleri (Şekil 5 & Şekil 6)
- Page 6: 4. Test Senaryoları ve Doğrulama Sonuçları (Tablo T1-T8),
          5. Karşılaşılan Sorunlar, Çözümler ve Sonuç.
Footer on every page: 'Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009)                       Sayfa X'
"""
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

def add_page_footer(ax, page_num):
    ax.plot([0, 1], [0.03, 0.03], color='#e2e8f0', lw=0.8, transform=ax.transAxes)
    ax.text(0, 0.015, "Stok Yönetim Sistemi • Resul Ekrem ÖZCAN (25902009)", fontsize=8, color='#94a3b8', transform=ax.transAxes)
    ax.text(1, 0.015, f"Sayfa {page_num}", ha='right', fontsize=8, color='#94a3b8', transform=ax.transAxes)

with PdfPages(report_pdf) as pdf:
    # =============================================================
    # SAYFA 1: KAPAK (Örnek PDF Sayfa 1 ile birebir aynı kurumsal şablon)
    # =============================================================
    fig_cover = plt.figure(figsize=(8.27, 11.69))
    fig_cover.patch.set_facecolor('white')
    ax = fig_cover.add_axes([0.1, 0.08, 0.8, 0.84])
    ax.axis('off')

    # Top dark accent bar
    ax.add_patch(plt.Rectangle((0, 0.94), 1, 0.008, color='#1e293b', transform=ax.transAxes))

    # Badge: BGT331 / BST301 • .NET PROGRAMLAMA - I
    ax.add_patch(plt.Rectangle((0, 0.87), 0.44, 0.032, color='#1e293b', transform=ax.transAxes))
    ax.text(0.22, 0.886, "BGT331 / BST301  •  .NET PROGRAMLAMA - I", ha='center', va='center', fontsize=8.5, weight='bold', color='#ffffff', transform=ax.transAxes)

    # Title
    ax.text(0, 0.81, "Stok Yönetim Sistemi", fontsize=26, weight='bold', color='#0f172a', transform=ax.transAxes)
    ax.text(0, 0.76, "C# ve Windows Forms Tabanlı Nesne Yönelimli Masaüstü Uygulaması\nProje Raporu", fontsize=12, color='#64748b', linespacing=1.4, transform=ax.transAxes)

    # Summary box paragraph
    intro_txt = (
        "Bu rapor; ürün envanteri, stok giriş ve çıkış hareketleri ile kritik stok takibini yöneten, "
        "kapsülleme, kalıtım, çok biçimlilik ve soyutlama ilkelerini işlevsel olarak uygulayan "
        "Stok Yönetim Sistemi uygulamasının mimari tasarımını, doğrulama mekanizmalarını, "
        "kullanım ekranlarını ve test senaryolarını içermektedir."
    )
    ax.text(0, 0.68, intro_txt, fontsize=9.2, color='#475569', linespacing=1.45, va='top', transform=ax.transAxes)

    # Table of Metadata
    meta_rows = [
        ("Öğrenci Adı Soyadı", "Resul Ekrem ÖZCAN"),
        ("Öğrenci Numarası", "25902009"),
        ("Ders", "BGT331 / BST301 - .NET Programlama - I"),
        ("Ders Sorumlusu", "Dr. Öğr. Üyesi Tohid YOUSEFİ"),
        ("Geliştirme Teknolojisi", "C# / .NET Framework 4.8 / Windows Forms"),
        ("Teslim Tarihi", "Kasım 2026")
    ]
    
    table_y = 0.48
    row_height = 0.052
    for label, val in meta_rows:
        # Subtle horizontal divider line
        ax.plot([0, 1], [table_y, table_y], color='#f1f5f9', lw=1, transform=ax.transAxes)
        ax.text(0, table_y - 0.025, label, fontsize=9.5, weight='bold', color='#1e293b', transform=ax.transAxes)
        ax.text(0.38, table_y - 0.025, val, fontsize=9.5, color='#334155', transform=ax.transAxes)
        table_y -= row_height

    ax.plot([0, 1], [table_y, table_y], color='#f1f5f9', lw=1, transform=ax.transAxes)

    # Cover footer
    ax.plot([0, 1], [0.08, 0.08], color='#e2e8f0', lw=0.8, transform=ax.transAxes)
    ax.text(0.5, 0.05, "Stok Yönetim Sistemi  •  Proje Raporu  •  2026", ha='center', va='center', fontsize=8.5, color='#94a3b8', transform=ax.transAxes)

    pdf.savefig(fig_cover, dpi=300)
    plt.close(fig_cover)

    # =============================================================
    # SAYFA 2: PROJE ÖZETİ, MİMARİ VE OOP İLKELERİ (Örnek Sayfa 2 ile aynı)
    # =============================================================
    fig2 = plt.figure(figsize=(8.27, 11.69))
    fig2.patch.set_facecolor('white')
    ax2 = fig2.add_axes([0.08, 0.06, 0.84, 0.88])
    ax2.axis('off')

    ax2.text(0, 1.0, "1. Proje Özeti ve Amaç", fontsize=12.5, weight='bold', color='#0f172a')
    ax2.plot([0, 1], [0.985, 0.985], color='#cbd5e1', lw=1.2)

    p1_text = (
        "Stok Yönetim Sistemi, bir işletmenin ürün envanterini, stok giriş ve çıkış hareketlerini, kritik stok seviyelerini ve toplam stok değerini tek bir masaüstü uygulaması "
        "üzerinden hızlı, düzenli ve hatasız şekilde yönetmesini sağlamak amacıyla C# ve .NET Framework Windows Forms kullanılarak geliştirilmiştir.\n\n"
        "Uygulama tamamen nesne tabanlı programlama (OOP) prensipleri esas alınarak katmanlı (Models, Services, Forms) biçimde tasarlanmıştır. Şartname kapsamı gereği "
        "harici veritabanı kullanılmamış; tüm veriler uygulama belleğinde güçlü tipli generic List<T> koleksiyonları üzerinde tutulmakta, kullanıcı hatalarına karşı kapsamlı veri "
        "doğrulama ve try-catch hata yakalama mekanizmaları uygulanmaktadır."
    )
    ax2.text(0, 0.965, p1_text, fontsize=8.5, color='#334155', linespacing=1.35, va='top')

    ax2.text(0, 0.835, "2. Sistem Mimarisi ve Nesne Tabanlı Programlama İlkeleri", fontsize=12.5, weight='bold', color='#0f172a')
    ax2.plot([0, 1], [0.820, 0.820], color='#cbd5e1', lw=1.2)

    arch_text = (
        "Proje sorumlulukların ayrılması prensibine uygun olarak üç ana katman altında yapılandırılmıştır:\n"
        "• Models Katmanı: İş alanına ait veri modellerini, soyut sınıfları, arayüzleri ve hareket kayıtlarını barındırır (IStoklanabilir, Urun, ElektronikUrun, GidaUrunu, GiyimUrunu, IslemKaydi).\n"
        "• Services Katmanı: İş kurallarını, generic koleksiyon yönetimini, LINQ sorgularını, kategori standardizasyonunu ve stok hareketi denetimlerini yürütür (StokYonetici).\n"
        "• Forms Katmanı: Kullanıcı etkileşim pencerelerini ve olay yönetimini içerir (FormAnaEkran, FormUrunEkleGuncelle, FormStokIslem)."
    )
    ax2.text(0, 0.805, arch_text, fontsize=8.2, color='#334155', linespacing=1.35, va='top')

    # OOP Table matching sample page 2 exactly
    cell_text = [
        ["Kapsülleme\n(Encapsulation)", "Urun,\nIslemKaydi", "Tüm alanlar private/protected olarak saklanır; property setter bloklarında boş metin, negatif fiyat, 0/eksi stok ve geçersiz kod formatı engellenir."],
        ["Soyutlama\n(Abstraction)", "abstract class Urun,\ninterface IStoklanabilir", "Temel Urun sınıfından doğrudan nesne üretilemez; tüm ürünlerin ortak özelliklerini ve zorunlu abstract metotlarını (OzelBilgiFormatli) tanımlar. IStoklanabilir stok sözleşmesini belirler."],
        ["Kalıtım\n(Inheritance)", "ElektronikUrun : Urun,\nGidaUrunu : Urun,\nGiyimUrunu : Urun", "Ortak ürün özellikleri temel sınıftan base(...) ile devralınır. ElektronikUrun garanti süresi ve voltajı, GidaUrunu SKT ve sıcaklığı, GiyimUrunu beden ve kumaş türünü ekler."],
        ["Çok Biçimlilik\n(Polymorphism)", "override OzelBilgiFormatli(),\nvirtual ToplamDegerHesapla()", "Tablodan bir ürün seçildiğinde çalışma zamanı türüne göre elektronik, gıda veya giyim özellikleri dinamik olarak durum çubuğuna ve listeye yansıtılır."],
        ["Koleksiyonlar &\nHata Yönetimi", "List<Urun>,\nList<IslemKaydi>,\nLINQ & try-catch", "Veriler generic listelerde tutulur ve LINQ (Where, Sum, Count) ile filtrelenir. Kural ihlallerinde özel hata mesajları kullanıcıya sunulur."]
    ]

    col_widths = [0.18, 0.25, 0.57]
    tab = ax2.table(
        cellText=cell_text,
        colLabels=["OOP İlkesi", "Uygulandığı Yapılar", "Projedeki İşlevsel Kullanımı"],
        colWidths=col_widths,
        cellLoc='left',
        loc='upper center',
        bbox=[0, 0.35, 1, 0.32]
    )
    tab.auto_set_font_size(False)
    tab.set_fontsize(7.8)

    for (row, col), cell in tab.get_celld().items():
        cell.set_edgecolor('#cbd5e1')
        if row == 0:
            cell.set_facecolor('#0f172a')
            cell.set_text_props(weight='bold', color='#ffffff', ha='left')
            cell.set_height(0.04)
        else:
            cell.set_facecolor('#ffffff' if row % 2 != 0 else '#f8fafc')
            cell.set_text_props(color='#1e293b')
            cell.set_height(0.055)

    # C# Code snippet block matching sample page 2 exactly
    ax2.add_patch(plt.Rectangle((0, 0.08), 1, 0.22, color='#f8fafc', ec='#cbd5e1', lw=1))
    code_sample = (
        "// Çok Biçimlilik (Polymorphism) & Kapsülleme (Encapsulation) Örneği\n"
        "public override string OzelBilgiFormatli() // ElektronikUrun.cs\n"
        "    => $\"Garanti: {GarantiSuresiAy} Ay | Voltaj: {Voltaj:N1} V [Tür: {KategoriAdi}]\";\n\n"
        "public void StokCikisiYap(string urunKodu, int miktar, string aciklama) // StokYonetici.cs\n"
        "{\n"
        "    if (miktar <= 0) throw new ArgumentException(\"Çıkış miktarı 0 veya negatif olamaz!\");\n"
        "    var urun = UrunBul(urunKodu);\n"
        "    if (miktar > urun.StokMiktari) throw new InvalidOperationException(\"Yetersiz stok! Negatif stok engellendi.\");\n"
        "    urun.StokMiktari -= miktar;\n"
        "}"
    )
    ax2.text(0.02, 0.28, code_sample, fontsize=7.8, family='monospace', color='#0f172a', linespacing=1.3, va='top')

    add_page_footer(ax2, 2)
    pdf.savefig(fig2, dpi=300)
    plt.close(fig2)

    # =============================================================
    # SAYFA 3: 3.1 ANA EKRAN & 3.2 ANLIK ARAMA FİLTRELEME
    # =============================================================
    fig3 = plt.figure(figsize=(8.27, 11.69))
    fig3.patch.set_facecolor('white')
    ax3 = fig3.add_axes([0.08, 0.06, 0.84, 0.88])
    ax3.axis('off')

    ax3.text(0, 1.0, "3. Uygulama Modülleri ve Ekran Görüntüleri", fontsize=12.5, weight='bold', color='#0f172a')
    ax3.plot([0, 1], [0.985, 0.985], color='#cbd5e1', lw=1.2)

    # 3.1
    ax3.text(0, 0.965, "3.1. Ana Ekran ve Canlı Özet Paneli", fontsize=10.5, weight='bold', color='#1e293b')
    p31_text = (
        "Uygulama açıldığında kullanıcıyı sistem özet paneli ve ürün listesi karşılar. Toplam ürün çeşidi, toplam stok adedi, kritik seviyedeki ürün sayısı ve toplam envanter "
        "değeri koleksiyonlardan anlık olarak hesaplanır. Tablodan bir ürün seçildiğinde alt durum çubuğunda polimorfik olarak o ürüne ait özel teknik detaylar gösterilir."
    )
    ax3.text(0, 0.945, p31_text, fontsize=8.2, color='#475569', linespacing=1.3, va='top')

    # Visual 1
    v1_path = os.path.join(shots_dir, "01_AnaEkran_Rehberi.png")
    if os.path.exists(v1_path):
        v1_img = mpimg.imread(v1_path)
        ax3_img1 = fig3.add_axes([0.1, 0.55, 0.8, 0.33])
        ax3_img1.imshow(v1_img)
        ax3_img1.axis('off')

    ax3.text(0.5, 0.53, "Şekil 1: Ana Ekran Genel Görünümü, İstatistik Kartları, Ürün Tablosu ve Seçili Ürün Detay Çubuğu", ha='center', fontsize=8, style='italic', color='#64748b')

    # 3.2
    ax3.text(0, 0.495, "3.2. Anlık Arama, Filtreleme ve Yönetim Çubuğu", fontsize=10.5, weight='bold', color='#1e293b')
    p32_text = (
        "Arama kutusuna yazılan her harf ürün kodu ve adında anlık eşleştirme yapar. Kategori açılır listesiyle ürünler bölümlere ayrılabilir, tüm filtreler tek tıkla sıfırlanabilir ve "
        "yönetim butonlarıyla yeni ürün ekleme, düzenleme, silme ile stok giriş/çıkış pencerelerine ulaşılır."
    )
    ax3.text(0, 0.475, p32_text, fontsize=8.2, color='#475569', linespacing=1.3, va='top')

    # Visual 2
    v2_path = os.path.join(shots_dir, "02_AramaFiltre_Rehberi.png")
    if os.path.exists(v2_path):
        v2_img = mpimg.imread(v2_path)
        ax3_img2 = fig3.add_axes([0.1, 0.09, 0.8, 0.33])
        ax3_img2.imshow(v2_img)
        ax3_img2.axis('off')

    ax3.text(0.5, 0.07, "Şekil 2: Anlık Arama, Filtre Sıfırlama, Yönetim Butonları ve Eşleşen Sonuçlar", ha='center', fontsize=8, style='italic', color='#64748b')

    add_page_footer(ax3, 3)
    pdf.savefig(fig3, dpi=300)
    plt.close(fig3)

    # =============================================================
    # SAYFA 4: 3.3 KRİTİK STOK & 3.4 YENİ ÜRÜN KAYIT FORMU
    # =============================================================
    fig4 = plt.figure(figsize=(8.27, 11.69))
    fig4.patch.set_facecolor('white')
    ax4 = fig4.add_axes([0.08, 0.06, 0.84, 0.88])
    ax4.axis('off')

    # 3.3
    ax4.text(0, 1.0, "3.3. Kritik Stok Takibi ve Uyarı Filtresi", fontsize=10.5, weight='bold', color='#1e293b')
    ax4.plot([0, 1], [0.985, 0.985], color='#cbd5e1', lw=1.2)
    p33_text = (
        "Stok miktarı belirlenen kritik eşiğin altına düşen ürünler tabloda otomatik olarak kırmızı tonla vurgulanır. 'Sadece Kritik Stokları Göster' seçeneği işaretlendiğinde "
        "yalnızca acil tedarik gerektiren ürünler süzülür ve üstteki kritik sayaç ile birebir eşleşir."
    )
    ax4.text(0, 0.965, p33_text, fontsize=8.2, color='#475569', linespacing=1.3, va='top')

    # Visual 3
    v3_path = os.path.join(shots_dir, "03_KritikStok_Rehberi.png")
    if os.path.exists(v3_path):
        v3_img = mpimg.imread(v3_path)
        ax4_img1 = fig4.add_axes([0.1, 0.58, 0.8, 0.33])
        ax4_img1.imshow(v3_img)
        ax4_img1.axis('off')

    ax4.text(0.5, 0.56, "Şekil 3: Kritik Stok Filtresi, Sayaç Uyumu ve Otomatik Kırmızı Uyarı Satırları", ha='center', fontsize=8, style='italic', color='#64748b')

    # 3.4
    ax4.text(0, 0.52, "3.4. Yeni Ürün Kayıt Formu ve Veri Doğrulama", fontsize=10.5, weight='bold', color='#1e293b')
    ax4.plot([0, 1], [0.505, 0.505], color='#cbd5e1', lw=1.2)
    p34_text = (
        "Yeni ürün ekleme ve düzenleme ekranında seçilen ürün türüne göre (Elektronik, Gıda veya Giyim) ek özellik alanı dinamik değişir. "
        "Ürün kodunda özel karakter engeli (Regex), 0 TL fiyat yasağı ve minimum stok kuralları aktif olarak denetlenir."
    )
    ax4.text(0, 0.485, p34_text, fontsize=8.2, color='#475569', linespacing=1.3, va='top')

    # Visual 5 (Form)
    v5_path = os.path.join(shots_dir, "05_UrunEkle_Elektronik_Rehberi.png")
    if os.path.exists(v5_path):
        v5_img = mpimg.imread(v5_path)
        ax4_img2 = fig4.add_axes([0.1, 0.10, 0.8, 0.34])
        ax4_img2.imshow(v5_img)
        ax4_img2.axis('off')

    ax4.text(0.5, 0.08, "Şekil 4: Yeni Ürün Kayıt Formu, Korunaklı Kategori Listesi ve Doğrulama Kuralları", ha='center', fontsize=8, style='italic', color='#64748b')

    add_page_footer(ax4, 4)
    pdf.savefig(fig4, dpi=300)
    plt.close(fig4)

    # =============================================================
    # SAYFA 5: 3.5 KONTROLLÜ STOK GİRİŞ VE ÇIKIŞ İŞLEMLERİ
    # =============================================================
    fig5 = plt.figure(figsize=(8.27, 11.69))
    fig5.patch.set_facecolor('white')
    ax5 = fig5.add_axes([0.08, 0.06, 0.84, 0.88])
    ax5.axis('off')

    ax5.text(0, 1.0, "3.5. Kontrollü Stok Giriş ve Çıkış İşlemleri", fontsize=10.5, weight='bold', color='#1e293b')
    ax5.plot([0, 1], [0.985, 0.985], color='#cbd5e1', lw=1.2)
    p35_text = (
        "Tablodan seçilen bir ürün için stok girişi veya stok çıkışı yapılabilir. Stok girişinde yalnızca pozitif tam sayı (Min: 1) kabul edilir. Stok çıkışında ise mevcut stok adedi üst "
        "sınır olarak belirlenerek stoğun negatife düşmesi hem arayüz hem de iş mantığı katmanında engellenir."
    )
    ax5.text(0, 0.965, p35_text, fontsize=8.2, color='#475569', linespacing=1.3, va='top')

    # Visual 7 (Stok Giriş)
    v7_path = os.path.join(shots_dir, "07_StokGiris_Rehberi.png")
    if os.path.exists(v7_path):
        v7_img = mpimg.imread(v7_path)
        ax5_img1 = fig5.add_axes([0.1, 0.58, 0.8, 0.33])
        ax5_img1.imshow(v7_img)
        ax5_img1.axis('off')

    ax5.text(0.5, 0.56, "Şekil 5: Kontrollü Stok Giriş İşlemi Formu ve Hareket Açıklaması", ha='center', fontsize=8, style='italic', color='#64748b')

    # Visual 8 (Stok Çıkış)
    v8_path = os.path.join(shots_dir, "08_StokCikis_Rehberi.png")
    if os.path.exists(v8_path):
        v8_img = mpimg.imread(v8_path)
        ax5_img2 = fig5.add_axes([0.1, 0.15, 0.8, 0.33])
        ax5_img2.imshow(v8_img)
        ax5_img2.axis('off')

    ax5.text(0.5, 0.13, "Şekil 6: Kontrollü Stok Çıkış İşlemi Formu ve Negatif Stok Koruması", ha='center', fontsize=8, style='italic', color='#64748b')

    add_page_footer(ax5, 5)
    pdf.savefig(fig5, dpi=300)
    plt.close(fig5)

    # =============================================================
    # SAYFA 6: TEST SENARYOLARI, KARŞILAŞILAN SORUNLAR VE SONUÇ
    # =============================================================
    fig6 = plt.figure(figsize=(8.27, 11.69))
    fig6.patch.set_facecolor('white')
    ax6 = fig6.add_axes([0.08, 0.06, 0.84, 0.88])
    ax6.axis('off')

    ax6.text(0, 1.0, "4. Test Senaryoları ve Doğrulama Sonuçları", fontsize=12.5, weight='bold', color='#0f172a')
    ax6.plot([0, 1], [0.985, 0.985], color='#cbd5e1', lw=1.2)
    ax6.text(0, 0.965, "Sistemin tüm fonksiyonel gereksinimleri, veri doğrulama kuralları ve hata yönetim senaryoları aşağıda özetlenen 8 test senaryosu üzerinden doğrulanmıştır.", fontsize=8.2, color='#475569')

    # Test Table matching sample page 6
    test_rows = [
        ["T1", "Ürün Kodu Tekrarı ve\nFormat Kontrolü", "Sistemde kayıtlı 'ELK001' koduyla tekrar ekleme;\nardından 'A#$%' özel karakterli kod girişi.", "Aynı kodda InvalidOperationException yakalanıp uyarı\nverildi; özel karakterli kod Regex ile reddedildi.", "BAŞARILI"],
        ["T2", "Sıfır ve Negatif\nStok Koruması", "Yeni ürün kaydında başlangıç stoğu veya fiyat alanına\n0 ya da negatif değer girme denemesi.", "NumericUpDown alt sınırları (Min: 1 / 0,01 ₺) ve model\ndoğrulaması hatalı kaydı engelledi.", "BAŞARILI"],
        ["T3", "Geçersiz Kategori\nGirişi Engeli", "Ürün eklerken tek harf ('a') veya rastgele metinle\nkategori oluşturma denemesi.", "DropDownList koruması sayesinde yalnızca 3 kurumsal\nkategoriden seçim yapılabilmesi sağlandı.", "BAŞARILI"],
        ["T4", "Negatif Stok Çıkışı\nEngelleme", "Mevcut stoğu 15 adet olan üründen 20 adet stok\nçıkışı yapma denemesi.", "Üst sınır kontrolü ve StokCikisi kuralı çıkışa izin vermedi;\nmevcut stok 15 adette korundu.", "BAŞARILI"],
        ["T5", "Pozitif Stok Girişi ve\nKritik Durum Güncelleme", "Stoğu 4 adet (kritik) olan ürüne +10 adet stok girişi\nyapılması.", "Stok 14'e yükseldi; satırdaki kırmızı kritik vurgu kalktı ve üst\nsayaçlar anlık güncellendi.", "BAŞARILI"],
        ["T6", "Anlık Arama ve\nÇoklu Filtreleme", "Arama kutusuna 'Fare' yazılması; ardından 'Sadece\nKritik Stokları Göster' kutusunun işaretlenmesi.", "Tablo yalnızca eşleşen kablosuz fare ürününü\nlisteledi; Sıfırla ile tam liste döndü.", "BAŞARILI"],
        ["T7", "Polimorfik Detay\nGösterimi", "Tablodan önce Elektronik, ardından Gıda bir ürünün\nsatırının seçilmesi.", "Alt durum çubuğunda OzelBilgiFormatli() override\nmetoduyla garanti süresi ve SKT dinamik gösterildi.", "BAŞARILI"],
        ["T8", "Denetim İzi (Audit Log)\nZaman Damgası Takibi", "Giriş ve çıkış işlemlerinin log tablosundan kontrolü.", "Tüm hareketler DateTime.Now, önceki/sonraki bakiye ve\nzorunlu açıklamasıyla doğru listelendi.", "BAŞARILI"]
    ]

    t_widths = [0.06, 0.22, 0.34, 0.28, 0.10]
    tab2 = ax6.table(
        cellText=test_rows,
        colLabels=["No", "Test Senaryosu", "Test Adımları / Girdi", "Beklenen ve Gözlenen Sonuç", "Durum"],
        colWidths=t_widths,
        cellLoc='left',
        loc='upper center',
        bbox=[0, 0.42, 1, 0.51]
    )
    tab2.auto_set_font_size(False)
    tab2.set_fontsize(7.2)

    for (row, col), cell in tab2.get_celld().items():
        cell.set_edgecolor('#cbd5e1')
        if row == 0:
            cell.set_facecolor('#0f172a')
            cell.set_text_props(weight='bold', color='#ffffff', ha='left')
            cell.set_height(0.035)
        else:
            cell.set_facecolor('#ffffff' if row % 2 != 0 else '#f8fafc')
            if col == 4:
                cell.set_text_props(weight='bold', color='#16a34a', ha='center')
            else:
                cell.set_text_props(color='#1e293b')
            cell.set_height(0.055)

    # 5. Karşılaşılan Sorunlar, Çözümler ve Sonuç matching sample page 6
    ax6.text(0, 0.37, "5. Karşılaşılan Sorunlar, Çözümler ve Sonuç", fontsize=12.5, weight='bold', color='#0f172a')
    ax6.plot([0, 1], [0.355, 0.355], color='#cbd5e1', lw=1.2)

    concl_items = (
        "• Arayüz Düzeni ve Okunabilirlik: Form genişliği optimize edilerek buton çakışmaları giderildi; sade, göz yormayan kurumsal renk paleti uygulandı.\n"
        "• Geçersiz Kategori ve Kod Girişleri: Serbest metin kategorisi kutusu yerine 3 kurumsal kategorili DropDownList kullanıldı; ürün kodlarına Regex denetimi eklendi.\n"
        "• Sıfır ve Negatif Stok Riski: NumericUpDown sınırları (Min: 1) ve Temel Urun/StokCikis kontrolleriyle çift katmanlı koruma sağlandı.\n\n"
        "Sonuç olarak: .NET Framework 4.8 ve C# Windows Forms kullanılarak şartnamede talep edilen tüm OOP ilkeleri (Kapsülleme, Kalıtım, Çok Biçimlilik, Soyutlama), "
        "koleksiyon yönetimi ve doğrulama kuralları eksiksiz uygulanmıştır. Modüler mimarisi sayesinde sistem ileride veritabanı entegrasyonu veya rapor dışa aktarımı gibi "
        "özelliklerle kolayca genişletilebilir yapıdadır."
    )
    ax6.text(0, 0.335, concl_items, fontsize=8.0, color='#334155', linespacing=1.35, va='top')

    add_page_footer(ax6, 6)
    pdf.savefig(fig6, dpi=300)
    plt.close(fig6)

print("6-Page Exact Reference Matching PDF Report Generated Successfully!")
