using System;

namespace InventoryManagementSystem.Models
{
    /// <summary>
    /// Stok takip sistemindeki işlemler için sözleşme (Interface).
    /// Soyutlama (Abstraction) ilkesi gereği arayüz tanımlanmıştır.
    /// </summary>
    public interface IStoklanabilir
    {
        string UrunKodu { get; }
        string UrunAdi { get; }
        int StokMiktari { get; }
        decimal BirimFiyat { get; }

        void StokGiris(int miktar);
        bool StokCikis(int miktar);
        decimal ToplamDegerHesapla();
    }
}
