# STOK YÖNETİM SİSTEMİ (INVENTORY MANAGEMENT SYSTEM)

**Ders Kodu & Adı:** BGT331 / BST301 - .NET Programlama - I  
**Öğretim Elemanı:** Dr. Öğr. Üyesi Tohid YOUSEFİ  
**Geliştiren Öğrenci:** Resul Ekrem ÖZCAN  
**Öğrenci Numarası:** 25902009  
**GitHub Repository:** [https://github.com/resulekremozcan/25902009_ResulEkremOzcan_InventoryManagement](https://github.com/resulekremozcan/25902009_ResulEkremOzcan_InventoryManagement) *(Private repo - Collaborator: tohid.yousefi)*  

---

## 1. Proje Tanımı ve Amacı
Bu proje; modern Nesne Yönelimli Programlama (OOP) prensiplerini ve C# Windows Forms mimarisini kullanarak işletmelerin ürün portföylerini, stok giriş-çıkış hareketlerini ve anlık envanter durumlarını takip edebilmesini sağlayan bir **Stok Yönetim Sistemi** masaüstü uygulamasıdır.

Şartname ilkeleri gereğince, veri yönetimi bellek içinde (In-Memory) Generic `List<T>` koleksiyonları üzerinde gerçekleştirilmiş olup herhangi bir harici SQL/veritabanı bağımlılığı bulunmamaktadır.

---

## 2. Temel Özellikler ve İşlevler
* **CRUD Operasyonları:** Yeni ürün kaydı ekleme, seçilen ürün bilgilerini güncelleme, ürün silme ve dinamik listeleme.
* **Benzersiz Ürün Kodu Kontrolü:** Aynı ürün kodunun tekrar eklenmesini engelleyen iş mantığı doğrulaması.
* **Stok Girişi (+):** Sıfırdan büyük miktar doğrulamasıyla stok artırma ve işlem geçmişi oluşturma.
* **Stok Çıkışı (-):** Yetersiz stok ve negatif miktar korumasıyla güvenli stok düşürme.
* **Canlı Dashboard (Özet Bilgiler):**
  * Toplam Ürün Çeşidi Sayısı
  * Toplam Fiziksel Stok Adedi
  * Kritik Stok Sınırındaki Ürün Sayısı
  * Toplam Finansal Envanter Değeri
* **Dinamik Arama ve Filtreleme:** Ürün adına veya koduna göre canlı arama, kategoriye göre filtreleme ve kritik stoktakileri anlık görüntüleme.
* **Stok Hareketleri ve Denetim İzi (Audit Log):** Sistemde yapılan tüm ürün ve stok hareketlerinin tarih ve açıklamalarıyla ayrı bir sekmede listelenmesi.

---

## 3. Nesne Yönelimli Programlama (OOP) Mimarisi
Proje, Dr. Tohid Yousefi'nin ders materyallerinde işlenen 4 ana OOP ilkesini eksiksiz barındırır:
1. **Kapsülleme (Encapsulation):**
   * Alanlar `private` erişim belirleyicisiyle korunmuştur.
   * `BirimFiyat`, `StokMiktari` ve `KritikStokSeviyesi` alanlarında negatif değer girilmesini engelleyen get/set kontrolleri mevcuttur.
   * `UrunKodu` alanı için `private set` kullanılarak dışarıdan yetkisiz değişim engellenmiştir.
2. **Kalıtım (Inheritance):**
   * Soyut `Urun` temel sınıfından `ElektronikUrun`, `GidaUrunu` ve `GiyimUrunu` alt sınıfları türetilmiştir.
   * Alt sınıflar `: base(...)` sözdizimi ile üst sınıfın parametreli constructor'ını tetikler.
3. **Çok Biçimlilik (Polymorphism):**
   * `KDVOraniGetir()`: Elektronik için %20, Gıda için %1, Giyim için %10 olarak override edilmiştir.
   * `DetayBilgisiGetir()`: Her alt sınıf kendi özel niteliklerini (Garanti/Marka, STT/Soğuk Zincir, Beden/Kumaş) dinamik olarak üretir.
4. **Soyutlama (Abstraction):**
   * `IStoklanabilir` arayüzü (interface) ile stok işlemleri sözleşmeye bağlanmıştır.
   * `Urun` sınıfı `abstract` olarak tasarlanmıştır.

---

## 4. Kullanılan Teknolojiler
* **Programlama Dili:** C# (.NET Framework 4.8)
* **Arayüz Kütüphanesi:** Windows Forms (WinForms)
* **Geliştirme Ortamı:** Visual Studio 2022 Community
* **Derleme Aracı:** MSBuild / Roslyn C# Compiler

---

## 5. Projeyi Visual Studio Ortamında Açma ve Çalıştırma
1. `01_SourceCode/InventoryManagementSystem.sln` çözüm dosyasını Visual Studio ile açınız.
2. Çözüm Gezgini'nde projenin başarıyla yüklendiğini doğrulayınız.
3. `F5` tuşuna basarak veya üst menüdeki **Start (Başlat)** butonuna tıklayarak projeyi derleyip çalıştırabilirsiniz.
4. Doğrudan çalıştırmak isterseniz `02_Application/InventoryManagementSystem.exe` dosyasına çift tıklayabilirsiniz.

---

## 6. Proje Klasör Yapısı
```text
25902009_ResulEkremOzcan_InventoryManagement/
│
├── 01_SourceCode/
│   ├── InventoryManagementSystem.sln
│   └── InventoryManagementSystem/
│       ├── Forms/             (FormAnaEkran, FormUrunEkleGuncelle, FormStokIslem)
│       ├── Models/            (Urun, ElektronikUrun, GidaUrunu, GiyimUrunu, IslemKaydi, IStoklanabilir)
│       ├── Services/          (StokYonetici - İş mantığı ve veri yönetimi)
│       ├── Properties/        (AssemblyInfo.cs)
│       ├── Program.cs
│       └── InventoryManagementSystem.csproj
│
├── 02_Application/
│   ├── InventoryManagementSystem.exe
│   ├── InventoryManagementSystem.exe.config
│   └── InventoryManagementSystem.pdb
│
├── 03_Report/
│   └── Proje_Raporu.pdf       (Tüm şartname maddelerini ve ekran görüntülerini içeren resmi rapor)
│
├── 04_GitHub/
│   ├── README.md
│   └── GitHub_Bilgileri.txt
│
└── README.md
```

---

## 7. Öğrenci Bilgileri
* **Ad Soyad:** Resul Ekrem ÖZCAN
* **Öğrenci No:** 25902009
* **Bölüm:** Bilişim Sistemleri ve Teknolojileri (BST)
* **Ders:** .NET Programlama - I (BGT331 / BST301)
