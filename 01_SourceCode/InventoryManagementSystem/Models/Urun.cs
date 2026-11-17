using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace InventoryManagementSystem.Models
{
    /// <summary>
    /// Tüm ürünlerin temelini oluşturan soyut (abstract) sınıf.
    /// OOP İlkeleri:
    /// 1. Soyutlama (Abstraction): abstract class ve abstract metotlar içerir.
    /// 2. Kapsülleme (Encapsulation): Alanlar private olarak tanımlanmış, erişim property'ler üzerinden kontrollü sağlanmıştır.
    /// 3. Kalıtım (Inheritance): Alt sınıflara temel oluşturur.
    /// 4. Çok Biçimlilik (Polymorphism): virtual ve abstract metotlar içerir.
    /// </summary>
    public abstract class Urun : IStoklanabilir
    {
        // Kapsülleme (Encapsulation): Alanlar private erişim belirleyicisi ile korunur.
        private string _urunKodu;
        private string _urunAdi;
        private string _kategori;
        private decimal _birimFiyat;
        private int _stokMiktari;
        private int _kritikStokSeviyesi;
        private DateTime _kayitTarihi;

        // Özel karakter kontrolü için yardımcı statik metot (Zararlı/anlamsız karakterleri engeller)
        private static bool OzelKarakterIcerir(string deger)
        {
            // İzin verilenler: Harfler, Türkçe karakterler, rakamlar, boşluk, tire, nokta, slash, çift tırnak (inç), parantez, yüzde
            return !Regex.IsMatch(deger, @"^[a-zA-ZçÇğĞıİöÖşŞüÜ0-9\s\-\.\/\""\'\(\)\%\,]+$");
        }

        // İsim alanları kontrolü
        private static bool GecersizIsimMi(string deger)
        {
            // Ürün adında model numaraları, inç ölçüleri (" veya ''), slash, parantez, virgül ve tire bulunabilir.
            // Zararlı özel karakterler engellenir: @, #, $, &, *, ;, <, >, {, }, [, ], |, ~, ^, !, ?
            return !Regex.IsMatch(deger, @"^[a-zA-ZçÇğĞıİöÖşŞüÜ0-9\s\-\.\/\""\'\(\)\%\,]+$");
        }

        // Parametresiz Yapıcı Metot (Constructor) - Default Constructor davranışı
        public Urun()
        {
            _kayitTarihi = DateTime.Now;
            _kritikStokSeviyesi = 10; // Varsayılan kritik seviye
            _stokMiktari = 0;
        }

        // Parametreli Yapıcı Metot (Constructor Overloading & this anahtar kelimesi kullanımı)
        public Urun(string urunKodu, string urunAdi, string kategori, decimal birimFiyat, int stokMiktari, int kritikStokSeviyesi = 10)
            : this()
        {
            this.UrunKodu = urunKodu;
            this.UrunAdi = urunAdi;
            this.Kategori = kategori;
            this.BirimFiyat = birimFiyat;
            this.StokMiktari = stokMiktari;
            this.KritikStokSeviyesi = kritikStokSeviyesi;
        }

        #region Kapsüllenmiş Özellikler (Properties & Validation)

        // Urun Kodu değiştirilemez (salt okunur/private set)
        public string UrunKodu
        {
            get { return _urunKodu; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("Ürün kodu boş bırakılamaz!");
                string temiz = value.Trim();
                if (temiz.Length < 2)
                    throw new ArgumentException("Ürün kodu en az 2 karakter olmalıdır!");
                if (OzelKarakterIcerir(temiz))
                    throw new ArgumentException("Ürün kodu özel karakter içeremez! (@ # $ % & * vb. kullanılamaz)");
                _urunKodu = temiz.ToUpper();
            }
        }

        public string UrunAdi
        {
            get { return _urunAdi; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("Ürün adı boş bırakılamaz!");
                string temiz = value.Trim();
                if (temiz.Length < 2)
                    throw new ArgumentException("Ürün adı en az 2 karakter olmalıdır!");
                if (GecersizIsimMi(temiz))
                    throw new ArgumentException("Ürün adı özel karakter içeremez! (@ # $ % & * vb. kullanılamaz)");
                _urunAdi = temiz;
            }
        }

        public string Kategori
        {
            get { return _kategori; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("Kategori alanı boş bırakılamaz!");
                _kategori = value.Trim();
            }
        }

        public decimal BirimFiyat
        {
            get { return _birimFiyat; }
            set
            {
                if (value < 0)
                    throw new ArgumentException("Birim fiyat negatif olamaz!");
                if (value == 0)
                    throw new ArgumentException("Birim fiyat 0 (sıfır) olamaz! Geçerli bir fiyat giriniz.");
                _birimFiyat = value;
            }
        }

        public int StokMiktari
        {
            get { return _stokMiktari; }
            protected set
            {
                if (value < 0)
                    throw new ArgumentException("Stok miktarı negatif olamaz!");
                _stokMiktari = value;
            }
        }

        public int KritikStokSeviyesi
        {
            get { return _kritikStokSeviyesi; }
            set
            {
                if (value < 0)
                    throw new ArgumentException("Kritik stok seviyesi negatif olamaz!");
                _kritikStokSeviyesi = value;
            }
        }

        public DateTime KayitTarihi
        {
            get { return _kayitTarihi; }
            private set { _kayitTarihi = value; }
        }

        // Salt okunur hesaplanan özellik (Read-only property)
        public bool KritikStoktaMi
        {
            get { return _stokMiktari <= _kritikStokSeviyesi; }
        }

        #endregion

        #region Temel İş Mantığı Metotları (Business Logic)

        public virtual void StokGiris(int miktar)
        {
            if (miktar <= 0)
                throw new ArgumentException("Stok giriş miktarı 0'dan büyük olmalıdır!");

            this.StokMiktari += miktar;
        }

        public virtual bool StokCikis(int miktar)
        {
            if (miktar <= 0)
                throw new ArgumentException("Stok çıkış miktarı 0'dan büyük olmalıdır!");

            if (miktar > this.StokMiktari)
                throw new InvalidOperationException(string.Format("Yetersiz stok! Mevcut stok: {0}, Talep edilen: {1}", this.StokMiktari, miktar));

            this.StokMiktari -= miktar;
            return true;
        }

        public virtual decimal ToplamDegerHesapla()
        {
            return _birimFiyat * _stokMiktari;
        }

        // Çok Biçimlilik (Polymorphism): Alt sınıflarca override edilmek üzere soyut metotlar
        public abstract decimal KDVOraniGetir();

        public abstract string DetayBilgisiGetir();

        // Virtual metot alt sınıfta ezilebilir (override)
        public virtual string BilgiOzeti()
        {
            return string.Format("[{0}] {1} - Fiyat: {2:C2} - Stok: {3} Adet ({4})", 
                _urunKodu, _urunAdi, _birimFiyat, _stokMiktari, _kategori);
        }

        #endregion
    }
}
