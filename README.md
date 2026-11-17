# STOK YÖNETİM SİSTEMİ (INVENTORY MANAGEMENT SYSTEM)

**Ders Kodu & Adı:** BGT331 / BST301 - .NET Programlama - I  
**Öğretim Elemanı:** Dr. Öğr. Üyesi Tohid YOUSEFİ  
**Geliştiren Öğrenci:** Resul Ekrem ÖZCAN  
**Öğrenci Numarası:** 25902009  
**GitHub Repository:** `25902009_ResulEkremOzcan_InventoryManagement` (Private)  

---

## 📌 Proje Genel Bakış ve Mimarisi
Bu proje; modern Nesne Yönelimli Programlama (OOP) prensiplerini ve C# Windows Forms mimarisini kullanarak işletmelerin ürün portföylerini, stok giriş-çıkış hareketlerini ve anlık envanter durumlarını takip edebilmesini sağlayan bir **Stok Yönetim Sistemi** masaüstü uygulamasıdır.

Şartname ilkeleri gereğince, veri yönetimi bellek içinde (In-Memory) Generic `List<T>` koleksiyonları üzerinde gerçekleştirilmiş olup herhangi bir harici SQL/veritabanı bağımlılığı bulunmamaktadır.

---

## 🖼️ GÖRSEL KULLANIM VE KONTROL REHBERİ

### 1. Ana Ekran, Canlı Dashboard ve Envanter Yönetimi
![Ana Ekran Rehberi](03_Report/Gorseller/01_AnaEkran_Rehberi.png)

#### 🔍 Bileşen ve Kontrol Açıklamaları:
* **[1] Canlı Dashboard Kartları:** Toplam ürün çeşidi, toplam fiziksel stok adedi, kritik stoktaki ürün sayısı ve toplam mali değeri anlık hesaplar. Sabit sayı değil; generic `List<Urun>` üzerinde LINQ metotlarıyla (`Count`, `Sum`) her işlem sonrası dinamik yenilenir.
* **[2] Canlı Arama ve Kategori Filtresi:** `txtArama_TextChanged` ile ürün adı veya kodu yazıldıkça liste anında filtrelenir. ComboBox ile `Elektronik`, `Gıda` veya `Giyim` kategorilerine göre tek tıkla süzme yapılır.
* **[3] Kritik Stok Filtresi & Renkli Uyarı:** Kritik stok seviyesinin altına düşen ürünler tabloda **açık kırmızı renkle** boyanır. Onay kutusu seçildiğinde sadece acil tedarik gereken kritik ürünler listelenir.
* **[4] Polimorfik Detay Sütunu (OOP):** `DetayBilgisiGetir()` soyut metodunun polimorfik çağrısıdır. Elektronik için *Marka & Garanti Süresi*, Gıda için *Son Tüketim Tarihi & Soğuk Zincir*, Giyim için *Beden & Kumaş* bilgisi DataGridView üzerinde dinamik sergilenir.
* **[5] Ürün Yönetimi Butonları (CRUD):** Yeni ürün kaydı, seçili ürünü düzenleme ve silme işlemleri. Mükerrer ürün kodu eklenmesi engellenir.
* **[6] Stok Giriş (+) ve Çıkış (-) İşlemleri:** Seçilen ürünün stoğunu kontrollü artırır veya düşürür. Eksi/negatif stok oluşması imkansız kılınmıştır.

---

### 2. Yeni Ürün Ekleme ve Kapsülleme (Validation) Diyaloğu
![Ürün Ekleme Rehberi](03_Report/Gorseller/02_UrunEkleme_Rehberi.png)

#### 🔍 Bileşen ve Kontrol Açıklamaları:
* **[1] Benzersiz Ürün Kodu ve Karakter Filtresi:** Boş bırakılamaz; en az 2 karakter olmalıdır. `@, #, $, %, &` gibi sisteme zarar verebilecek yabancı karakterler kesinlikle engellenir.
* **[2] Kategori Seçimi & Dinamik Kalıtım Panelleri:** Seçilen kategoriye göre alt paneller dinamik olarak değişir ve ilgili somut sınıf (`ElektronikUrun`, `GidaUrunu`, `GiyimUrunu`) polimorfik olarak üretilir.
* **[3] Kapsülleme (Encapsulation): 0 TL ve Negatif Fiyat Engeli:** NumericUpDown kontrolleri ve `Urun.cs` kapsülleme katmanındaki `if (value <= 0)` kontrolü ile bedelsiz (0 TL) veya eksi fiyatlı ürün girişi engellenir.
* **[4] Polimorfik Alanlar ve Güçlü Doğrulama:** Marka, Beden ve Kumaş alanlarına regex doğrulama kuralları uygulanarak veri kalitesi korunur.
* **[5] Kaydet ve Doğrulama Butonu:** Try-Catch bloklarıyla tüm kontroller denetlenir ve işlem geçmişine log atılır.

---

### 3. Stok Giriş (+) ve Stok Çıkış (-) Güvenlik Diyalogları
![Stok Hareketleri Rehberi](03_Report/Gorseller/03_StokHareketleri_Rehberi.png)

#### 🔍 Bileşen ve Kontrol Açıklamaları:
* **[1] Stok Girişi (+) ve 0 / 000 Miktar Engeli:** Miktar alanına `0`, `00`, `000` veya negatif sayı yazılması string denetimi ve `<= 0` kuralıyla tamamen engellenmiştir.
* **[2] Zorunlu Açıklama ve Özel Karakter Filtresi:** Tedarikçi, fatura veya sevkiyat bilgisi girilmesi zorunludur. Zararlı script/özel karakterler engellenir.
* **[3] Stok Çıkışı (-) ve Yetersiz Bakiye Kilidi:** Eldeki mevcut stoktan (örneğin 12 adetten) daha fazla çıkış yapılması imkansızdır. Kontrolün `Maximum` değeri anlık olarak eldeki stoğa eşitlenir.
* **[4] Anlık Düşüm ve İşlem Kaydı:** Başarılı çıkış sonrası stok düşürülür, denetim izine yazılır ve dashboard kartları anında güncellenir.

---

### 4. Stok Hareketleri Geçmişi ve Denetim İzi (Audit Log)
![Denetim İzi Rehberi](03_Report/Gorseller/04_DenetimIzi_Rehberi.png)

#### 🔍 Bileşen ve Kontrol Açıklamaları:
* **[1] Kesin Zaman Damgası (`DateTime.Now`):** Yapılan her işlem saniyesine kadar tarih/saat damgasıyla saklanır. En son yapılan hareket en üstte listelenir.
* **[2] Tip Güvenli İşlem Türleri (`Enum`):** `UrunEkleme`, `UrunGuncelleme`, `UrunSilme`, `StokGiris` ve `StokCikis` türleri C# Enum yapısıyla saklanır.
* **[3] Ürün ve Miktar Detayları:** İşlem yapılan ürün kodu ve miktarı şeffaf biçimde sunulur.
* **[4] Denetim Açıklamaları:** Kullanıcının yazdığı açıklamalar izlenebilirlik sağlar.

---

## 🛠️ Nesne Yönelimli Programlama (OOP) Prensipleri
1. **Kapsülleme (Encapsulation):** Tüm alanlar `private` tutulmuş, kontrollü `get`/`set` özellikleri kullanılmıştır. Fiyat <= 0, miktar <= 0 kontrolleri sınıf içinde yapılmıştır.
2. **Kalıtım (Inheritance):** Soyut `Urun` sınıfından `ElektronikUrun`, `GidaUrunu` ve `GiyimUrunu` türetilmiş, `: base(...)` ile üst sınıf yapıcıları çağrılmıştır.
3. **Çok Biçimlilik (Polymorphism):** `KDVOraniGetir()`, `DetayBilgisiGetir()` ve `BilgiOzeti()` metotları alt sınıflarda `override` edilmiştir.
4. **Soyutlama (Abstraction):** `IStoklanabilir` arayüzü (interface) ve `Urun` soyut sınıfı (abstract class) tanımlanmıştır.

---

## 🚀 Projeyi Çalıştırma Adımları
1. Visual Studio ile `01_SourceCode/InventoryManagementSystem.sln` dosyasını açıp `F5` tuşuna basabilirsiniz.
2. Veya derlenmiş halini doğrudan çalıştırmak için `02_Application/InventoryManagementSystem.exe` dosyasına çift tıklayabilirsiniz.
