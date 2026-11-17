using System;

namespace InventoryManagementSystem.Models
{
    /// <summary>
    /// Gıda ürünleri için alt sınıf.
    /// Kalıtım (Inheritance): Urun sınıfından türetilmiştir.
    /// Çok Biçimlilik (Polymorphism): Farklı KDV oranı (%1) ve son tüketim tarihi kontrolü barındırır.
    /// </summary>
    public class GidaUrunu : Urun
    {
        private DateTime _sonTuketimTarihi;
        private bool _sogukZincir;

        public GidaUrunu() : base()
        {
            this.Kategori = "Gıda";
            _sonTuketimTarihi = DateTime.Today.AddMonths(6);
            _sogukZincir = false;
        }

        public GidaUrunu(string urunKodu, string urunAdi, decimal birimFiyat, int stokMiktari, DateTime sonTuketimTarihi, bool sogukZincir, int kritikStok = 20)
            : base(urunKodu, urunAdi, "Gıda", birimFiyat, stokMiktari, kritikStok)
        {
            this.SonTuketimTarihi = sonTuketimTarihi;
            this.SogukZincir = sogukZincir;
        }

        public DateTime SonTuketimTarihi
        {
            get { return _sonTuketimTarihi; }
            set { _sonTuketimTarihi = value; }
        }

        public bool SogukZincir
        {
            get { return _sogukZincir; }
            set { _sogukZincir = value; }
        }

        // Çok Biçimlilik: Temel gıda maddelerinde KDV oranı %1'dir
        public override decimal KDVOraniGetir()
        {
            return 0.01m;
        }

        public override string DetayBilgisiGetir()
        {
            return string.Format("STT: {0:dd.MM.yyyy}, Soğuk Zincir: {1}", 
                _sonTuketimTarihi, _sogukZincir ? "Evet" : "Hayır");
        }

        public override string BilgiOzeti()
        {
            return string.Format("{0} [STT: {1:dd.MM.yyyy}, Soğuk Zincir: {2}]", 
                base.BilgiOzeti(), _sonTuketimTarihi, _sogukZincir ? "Gerektirir" : "Gerekmez");
        }
    }
}
