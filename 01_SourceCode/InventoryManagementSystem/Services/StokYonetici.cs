using System;
using System.Collections.Generic;
using System.Linq;
using InventoryManagementSystem.Models;

namespace InventoryManagementSystem.Services
{
    /// <summary>
    /// İş Mantığı Katmanı (Business Logic Layer).
    /// Şartname gereği arayüz kodları ile iş mantığı ayrıştırılmıştır.
    /// Generic List koleksiyonları üzerinden bellek içi (in-memory) veri yönetimi yapar.
    /// </summary>
    public class StokYonetici
    {
        private readonly List<Urun> _urunler;
        private readonly List<IslemKaydi> _islemGecmisi;

        public StokYonetici()
        {
            _urunler = new List<Urun>();
            _islemGecmisi = new List<IslemKaydi>();
            OrnekVerileriYukle();
        }

        #region Koleksiyon Okuma Özellikleri

        public IReadOnlyList<Urun> UrunleriGetir()
        {
            return _urunler.AsReadOnly();
        }

        public IReadOnlyList<IslemKaydi> IslemGecmisiniGetir()
        {
            return _islemGecmisi.AsReadOnly();
        }

        #endregion

        #region Ürün Yönetimi İşlemleri

        public bool UrunEkle(Urun yeniUrun)
        {
            if (yeniUrun == null)
                throw new ArgumentNullException("yeniUrun", "Eklenecek ürün boş olamaz!");

            // Ürün kodu benzersizlik kontrolü
            if (UrunKoduVarMi(yeniUrun.UrunKodu))
                throw new InvalidOperationException(string.Format("'{0}' kodlu ürün zaten sistemde kayıtlı!", yeniUrun.UrunKodu));

            _urunler.Add(yeniUrun);
            _islemGecmisi.Add(new IslemKaydi(yeniUrun.UrunKodu, yeniUrun.UrunAdi, IslemTuru.UrunEkleme, yeniUrun.StokMiktari, "Yeni ürün eklendi."));
            return true;
        }

        public bool UrunGuncelle(string urunKodu, string yeniAd, decimal yeniFiyat, int yeniKritikSeviye, Action<Urun> ekGuncelleme = null)
        {
            Urun bulunan = UrunBul(urunKodu);
            if (bulunan == null)
                throw new KeyNotFoundException(string.Format("'{0}' kodlu ürün bulunamadı!", urunKodu));

            bulunan.UrunAdi = yeniAd;
            bulunan.BirimFiyat = yeniFiyat;
            bulunan.KritikStokSeviyesi = yeniKritikSeviye;

            if (ekGuncelleme != null)
            {
                ekGuncelleme(bulunan);
            }

            _islemGecmisi.Add(new IslemKaydi(bulunan.UrunKodu, bulunan.UrunAdi, IslemTuru.UrunGuncelleme, 0, "Ürün bilgileri güncellendi."));
            return true;
        }

        public bool UrunSil(string urunKodu)
        {
            Urun bulunan = UrunBul(urunKodu);
            if (bulunan == null)
                throw new KeyNotFoundException(string.Format("'{0}' kodlu ürün bulunamadı!", urunKodu));

            _urunler.Remove(bulunan);
            _islemGecmisi.Add(new IslemKaydi(bulunan.UrunKodu, bulunan.UrunAdi, IslemTuru.UrunSilme, bulunan.StokMiktari, "Ürün sistemden silindi."));
            return true;
        }

        public Urun UrunBul(string urunKodu)
        {
            if (string.IsNullOrWhiteSpace(urunKodu))
                return null;

            return _urunler.FirstOrDefault(u => u.UrunKodu.Equals(urunKodu.Trim(), StringComparison.OrdinalIgnoreCase));
        }

        public bool UrunKoduVarMi(string urunKodu)
        {
            return UrunBul(urunKodu) != null;
        }

        #endregion

        #region Stok Hareketleri (Giriş / Çıkış)

        public bool StokGirisYap(string urunKodu, int miktar, string aciklama = "Stok girişi")
        {
            Urun urun = UrunBul(urunKodu);
            if (urun == null)
                throw new KeyNotFoundException(string.Format("'{0}' kodlu ürün bulunamadı!", urunKodu));

            urun.StokGiris(miktar);
            _islemGecmisi.Add(new IslemKaydi(urun.UrunKodu, urun.UrunAdi, IslemTuru.StokGiris, miktar, aciklama));
            return true;
        }

        public bool StokCikisYap(string urunKodu, int miktar, string aciklama = "Stok çıkışı / Satış")
        {
            Urun urun = UrunBul(urunKodu);
            if (urun == null)
                throw new KeyNotFoundException(string.Format("'{0}' kodlu ürün bulunamadı!", urunKodu));

            bool basarili = urun.StokCikis(miktar);
            if (basarili)
            {
                _islemGecmisi.Add(new IslemKaydi(urun.UrunKodu, urun.UrunAdi, IslemTuru.StokCikis, miktar, aciklama));
            }
            return basarili;
        }

        #endregion

        #region Arama, Filtreleme ve Özet İstatistikler

        public List<Urun> UrunAra(string aramaMetni, string kategori, bool sadeceKritikStok)
        {
            var sonuc = _urunler.AsEnumerable();

            // Arama filtresi (Ad veya Kod)
            if (!string.IsNullOrWhiteSpace(aramaMetni))
            {
                string aranan = aramaMetni.Trim().ToLower();
                sonuc = sonuc.Where(u => u.UrunAdi.ToLower().Contains(aranan) || u.UrunKodu.ToLower().Contains(aranan));
            }

            // Kategori filtresi
            if (!string.IsNullOrWhiteSpace(kategori) && kategori != "Tümü")
            {
                sonuc = sonuc.Where(u => u.Kategori.Equals(kategori, StringComparison.OrdinalIgnoreCase));
            }

            // Kritik stok filtresi
            if (sadeceKritikStok)
            {
                sonuc = sonuc.Where(u => u.KritikStoktaMi);
            }

            return sonuc.ToList();
        }

        public int ToplamUrunSayisi()
        {
            return _urunler.Count;
        }

        public int ToplamStokAdedi()
        {
            return _urunler.Sum(u => u.StokMiktari);
        }

        public int KritikStoktakiUrunSayisi()
        {
            return _urunler.Count(u => u.KritikStoktaMi);
        }

        public decimal ToplamEnvanterDegeri()
        {
            return _urunler.Sum(u => u.ToplamDegerHesapla());
        }

        #endregion

        #region Başlangıç Örnek Verileri

        private void OrnekVerileriYukle()
        {
            // Elektronik Ürünler
            _urunler.Add(new ElektronikUrun("ELK-101", "Dizüstü Bilgisayar 15.6\"", 24500m, 12, "Asus", 24, 5));
            _urunler.Add(new ElektronikUrun("ELK-102", "Kablosuz Optik Fare", 350m, 4, "Logitech", 12, 10)); // Kritik stok örneği (4 <= 10)
            _urunler.Add(new ElektronikUrun("ELK-103", "Mekanik Klavye RGB", 1200m, 18, "Razer", 24, 8));

            // Gıda Ürünleri
            _urunler.Add(new GidaUrunu("GID-201", "Tam Yağlı Süt 1L", 32.50m, 45, DateTime.Today.AddDays(15), true, 20));
            _urunler.Add(new GidaUrunu("GID-202", "Sızma Zeytinyağı 5L", 850m, 6, DateTime.Today.AddMonths(12), false, 10)); // Kritik stok örneği (6 <= 10)
            _urunler.Add(new GidaUrunu("GID-203", "Kırmızı Mercimek 1Kg", 45m, 60, DateTime.Today.AddMonths(18), false, 15));

            // Giyim Ürünleri
            _urunler.Add(new GiyimUrunu("GYM-301", "Erkek Polo Yaka Tişört", 420m, 25, "L", "100% Pamuk", 10));
            _urunler.Add(new GiyimUrunu("GYM-302", "Kapüşonlu Sweatshirt", 780m, 7, "XL", "Pamuk / Polyester", 12)); // Kritik stok (7 <= 12)

            // Başlangıç işlem geçmişi
            foreach (var urun in _urunler)
            {
                _islemGecmisi.Add(new IslemKaydi(urun.UrunKodu, urun.UrunAdi, IslemTuru.UrunEkleme, urun.StokMiktari, "Sistem açılışı başlangıç envanteri."));
            }
        }

        #endregion
    }
}
