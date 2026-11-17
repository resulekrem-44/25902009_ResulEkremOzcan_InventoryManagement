using System;
using System.Drawing;
using System.Text.RegularExpressions;
using System.Windows.Forms;
using InventoryManagementSystem.Models;

namespace InventoryManagementSystem.Forms
{
    public partial class FormStokIslem : Form
    {
        private readonly Urun _urun;
        private readonly bool _girisMi; // true: Giriş (+), false: Çıkış (-)

        public int GirilenMiktar { get; private set; }
        public string GirilenAciklama { get; private set; }

        public FormStokIslem(Urun urun, bool girisMi)
        {
            _urun = urun;
            _girisMi = girisMi;
            InitializeComponent();
            SetupForm();
        }

        private void SetupForm()
        {
            this.Text = _girisMi ? "Stok Girişi Yap (+)" : "Stok Çıkışı Yap (-)";
            lblBaslik.Text = _girisMi ? "STOK GİRİŞ İŞLEMİ" : "STOK ÇIKIŞ İŞLEMİ";
            lblBaslik.ForeColor = _girisMi ? Color.FromArgb(16, 185, 129) : Color.FromArgb(239, 68, 68);

            lblUrunBilgi.Text = string.Format("Ürün: [{0}] {1}\nMevcut Stok: {2} Adet | Kategori: {3}",
                _urun.UrunKodu, _urun.UrunAdi, _urun.StokMiktari, _urun.Kategori);

            btnOnayla.Text = _girisMi ? "Stok Ekle" : "Stok Düş";
            btnOnayla.BackColor = _girisMi ? Color.FromArgb(16, 185, 129) : Color.FromArgb(239, 68, 68);

            txtAciklama.Text = _girisMi ? "Tedarikçi Girişi" : "Müşteri Satışı";
            numMiktar.Value = 1;
            numMiktar.Minimum = 0; // Doğrulama kodunda sıfır ve türevlerini yakalamak için minimum 0 yapıldı
            numMiktar.Maximum = _girisMi ? 100000 : Math.Max(1, _urun.StokMiktari);
        }

        private void btnOnayla_Click(object sender, EventArgs e)
        {
            // 1. Miktar alanının metin ve sayısal doğrulaması (0, 00, 000, boş veya geçersiz giriş kontrolü)
            string hamMiktarMetin = numMiktar.Text.Trim();

            if (string.IsNullOrWhiteSpace(hamMiktarMetin))
            {
                MessageBox.Show("Lütfen geçerli bir miktar giriniz!", "Geçersiz Miktar", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                numMiktar.Focus();
                return;
            }

            // Sayısal olmayan karakter veya sadece sıfırlardan oluşan girişlerin ("0", "00", "000") kontrolü
            if (!int.TryParse(hamMiktarMetin, out int parsedMiktar) || parsedMiktar <= 0)
            {
                MessageBox.Show("İşlem miktarı 0 (sıfır) veya geçersiz olamaz! Lütfen 0'dan büyük pozitif bir tam sayı giriniz.", 
                    "Hatalı Miktar", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                numMiktar.Focus();
                return;
            }

            int miktar = (int)numMiktar.Value;
            if (miktar <= 0)
            {
                MessageBox.Show("İşlem miktarı 0 (sıfır) olamaz! Lütfen en az 1 adet giriniz.", 
                    "Hatalı Değer", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                numMiktar.Focus();
                return;
            }

            // 2. Yetersiz Stok Kontrolü (Stok çıkışında mevcut stoktan fazlasına izin verilmez)
            if (!_girisMi && miktar > _urun.StokMiktari)
            {
                MessageBox.Show(string.Format("Çıkış miktarı mevcut stok miktarından ({0}) fazla olamaz!", _urun.StokMiktari),
                    "Yetersiz Stok", MessageBoxButtons.OK, MessageBoxIcon.Error);
                numMiktar.Focus();
                return;
            }

            // 3. Açıklama Alanı Doğrulaması (Boşluk ve Yabancı/Özel Karakter Kontrolü)
            string aciklama = txtAciklama.Text.Trim();
            if (string.IsNullOrWhiteSpace(aciklama))
            {
                MessageBox.Show("Lütfen işlem için bir açıklama giriniz!", "Açıklama Boş Olamaz", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                txtAciklama.Focus();
                return;
            }

            // Açıklamada zararlı özel karakterleri engelleme (@, #, $, <, >, ;, { }, vb.)
            if (!Regex.IsMatch(aciklama, @"^[a-zA-ZçÇğĞıİöÖşŞüÜ0-9\s\-\.\,\/\(\)]+$"))
            {
                MessageBox.Show("Açıklama alanı yabancı/özel karakterler içeremez! (@ # $ % & * < > vb. kullanılamaz)", 
                    "Geçersiz Karakter", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                txtAciklama.Focus();
                return;
            }

            GirilenMiktar = miktar;
            GirilenAciklama = aciklama;
            this.DialogResult = DialogResult.OK;
            this.Close();
        }

        private void btnIptal_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.Cancel;
            this.Close();
        }
    }
}
