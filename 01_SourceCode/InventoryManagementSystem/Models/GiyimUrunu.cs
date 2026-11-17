using System;
using System.Text.RegularExpressions;

namespace InventoryManagementSystem.Models
{
    /// <summary>
    /// Giyim ve Tekstil ürünleri için alt sınıf.
    /// Kalıtım ve çok biçimlilik zenginliğini artırır.
    /// </summary>
    public class GiyimUrunu : Urun
    {
        private string _beden;
        private string _kumasTuru;

        public GiyimUrunu() : base()
        {
            this.Kategori = "Giyim";
            _beden = "M";
            _kumasTuru = "Pamuk";
        }

        public GiyimUrunu(string urunKodu, string urunAdi, decimal birimFiyat, int stokMiktari, string beden, string kumasTuru, int kritikStok = 10)
            : base(urunKodu, urunAdi, "Giyim", birimFiyat, stokMiktari, kritikStok)
        {
            this.Beden = beden;
            this.KumasTuru = kumasTuru;
        }

        public string Beden
        {
            get { return _beden; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("Beden boş bırakılamaz!");
                string temiz = value.Trim().ToUpper();
                if (!Regex.IsMatch(temiz, @"^[a-zA-ZçÇğĞıİöÖşŞüÜ0-9\s\-\.]+$"))
                    throw new ArgumentException("Beden özel karakter içeremez!");
                _beden = temiz;
            }
        }

        public string KumasTuru
        {
            get { return _kumasTuru; }
            set
            {
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("Kumaş türü boş bırakılamaz!");
                string temiz = value.Trim();
                if (!Regex.IsMatch(temiz, @"^[a-zA-ZçÇğĞıİöÖşŞüÜ0-9\s\-\.\/\%\,]+$"))
                    throw new ArgumentException("Kumaş türü özel karakter içeremez!");
                _kumasTuru = temiz;
            }
        }

        // Çok Biçimlilik: Giyim ürünlerinde KDV oranı %10'dur
        public override decimal KDVOraniGetir()
        {
            return 0.10m;
        }

        public override string DetayBilgisiGetir()
        {
            return string.Format("Beden: {0}, Kumaş: {1}", _beden, _kumasTuru);
        }

        public override string BilgiOzeti()
        {
            return string.Format("{0} [Beden: {1}, Kumaş: {2}]", base.BilgiOzeti(), _beden, _kumasTuru);
        }
    }
}
