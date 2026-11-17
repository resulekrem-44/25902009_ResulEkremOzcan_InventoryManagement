using System;
using System.Text.RegularExpressions;

namespace InventoryManagementSystem.Models
{
    /// <summary>
    /// Elektronik ürünler için alt sınıf.
    /// Kalıtım (Inheritance): Urun sınıfından türetilmiştir (: base(...) kullanımı).
    /// Çok Biçimlilik (Polymorphism): KDVOraniGetir, DetayBilgisiGetir ve BilgiOzeti metotlarını override eder.
    /// </summary>
    public class ElektronikUrun : Urun
    {
        private int _garantiSuresiAy;
        private string _marka;

        public ElektronikUrun() : base()
        {
            this.Kategori = "Elektronik";
            _garantiSuresiAy = 24;
            _marka = "Genel";
        }

        // : base(...) ile üst sınıfın parametreli constructor'ını çağırma
        public ElektronikUrun(string urunKodu, string urunAdi, decimal birimFiyat, int stokMiktari, string marka, int garantiSuresiAy, int kritikStok = 5)
            : base(urunKodu, urunAdi, "Elektronik", birimFiyat, stokMiktari, kritikStok)
        {
            this.Marka = marka;
            this.GarantiSuresiAy = garantiSuresiAy;
        }

        public string Marka
        {
            get { return _marka; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("Marka alanı boş bırakılamaz!");
                string temiz = value.Trim();
                if (!Regex.IsMatch(temiz, @"^[a-zA-ZçÇğĞıİöÖşŞüÜ0-9\s\-\.]+$"))
                    throw new ArgumentException("Marka özel karakter içeremez!");
                _marka = temiz;
            }
        }

        public int GarantiSuresiAy
        {
            get { return _garantiSuresiAy; }
            set
            {
                if (value < 0)
                    throw new ArgumentException("Garanti süresi negatif olamaz!");
                _garantiSuresiAy = value;
            }
        }

        // Çok Biçimlilik: Elektronik ürünlerde KDV %20'dir
        public override decimal KDVOraniGetir()
        {
            return 0.20m;
        }

        public override string DetayBilgisiGetir()
        {
            return string.Format("Marka: {0}, Garanti: {1} Ay", _marka, _garantiSuresiAy);
        }

        public override string BilgiOzeti()
        {
            return string.Format("{0} [Garanti: {1} Ay, Marka: {2}]", base.BilgiOzeti(), _garantiSuresiAy, _marka);
        }
    }
}
