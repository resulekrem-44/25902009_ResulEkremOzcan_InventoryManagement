using System;

namespace InventoryManagementSystem.Models
{
    public enum IslemTuru
    {
        StokGiris,
        StokCikis,
        UrunEkleme,
        UrunGuncelleme,
        UrunSilme
    }

    /// <summary>
    /// Stok hareketlerini ve denetim izini tutan sınıf.
    /// Kapsülleme ve veri takibi sağlar.
    /// </summary>
    public class IslemKaydi
    {
        private Guid _islemId;
        private DateTime _tarih;
        private string _urunKodu;
        private string _urunAdi;
        private IslemTuru _islemTipi;
        private int _miktar;
        private string _aciklama;

        public IslemKaydi(string urunKodu, string urunAdi, IslemTuru islemTipi, int miktar, string aciklama)
        {
            _islemId = Guid.NewGuid();
            _tarih = DateTime.Now;
            _urunKodu = urunKodu;
            _urunAdi = urunAdi;
            _islemTipi = islemTipi;
            _miktar = miktar;
            _aciklama = aciklama;
        }

        public Guid IslemId { get { return _islemId; } }
        public DateTime Tarih { get { return _tarih; } }
        public string UrunKodu { get { return _urunKodu; } }
        public string UrunAdi { get { return _urunAdi; } }
        public IslemTuru IslemTipi { get { return _islemTipi; } }
        public int Miktar { get { return _miktar; } }
        public string Aciklama { get { return _aciklama; } }

        public string IslemOzeti()
        {
            return string.Format("[{0:dd.MM.yyyy HH:mm:ss}] {1} | Ürün: {2} ({3}) | Miktar: {4} | Not: {5}",
                _tarih, _islemTipi, _urunKodu, _urunAdi, _miktar, _aciklama);
        }
    }
}
