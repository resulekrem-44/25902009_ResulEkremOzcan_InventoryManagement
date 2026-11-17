using System;
using System.Drawing;
using System.Windows.Forms;
using InventoryManagementSystem.Models;

namespace InventoryManagementSystem.Forms
{
    public partial class FormUrunEkleGuncelle : Form
    {
        private readonly Urun _duzenlenecekUrun;
        public Urun OlusturulanUrun { get; private set; }

        public FormUrunEkleGuncelle() : this(null)
        {
        }

        public FormUrunEkleGuncelle(Urun duzenlenecekUrun)
        {
            _duzenlenecekUrun = duzenlenecekUrun;
            InitializeComponent();
            SetupForm();
        }

        private void SetupForm()
        {
            if (_duzenlenecekUrun != null)
            {
                this.Text = "Ürün Bilgilerini Güncelle";
                btnKaydet.Text = "Güncelle";
                txtUrunKodu.Text = _duzenlenecekUrun.UrunKodu;
                txtUrunKodu.ReadOnly = true; // Ürün kodu değiştirilemez
                txtUrunAdi.Text = _duzenlenecekUrun.UrunAdi;
                numBirimFiyat.Value = _duzenlenecekUrun.BirimFiyat;
                numKritikStok.Value = _duzenlenecekUrun.KritikStokSeviyesi;
                numStokMiktari.Value = _duzenlenecekUrun.StokMiktari;
                numStokMiktari.Enabled = false; // Stok değişimi ana ekrandan yapılmalı

                if (_duzenlenecekUrun is ElektronikUrun elk)
                {
                    cmbKategori.SelectedItem = "Elektronik";
                    txtEk1.Text = elk.Marka;
                    numEk2.Value = elk.GarantiSuresiAy;
                }
                else if (_duzenlenecekUrun is GidaUrunu gida)
                {
                    cmbKategori.SelectedItem = "Gıda";
                    dtpEkTarih.Value = gida.SonTuketimTarihi;
                    chkEkBool.Checked = gida.SogukZincir;
                }
                else if (_duzenlenecekUrun is GiyimUrunu gym)
                {
                    cmbKategori.SelectedItem = "Giyim";
                    txtEk1.Text = gym.Beden;
                    txtEk3.Text = gym.KumasTuru;
                }
                cmbKategori.Enabled = false; // Kategori güncellemede değiştirilemez
            }
            else
            {
                this.Text = "Yeni Ürün Ekle";
                btnKaydet.Text = "Kaydet";
                cmbKategori.SelectedIndex = 0;
            }
        }

        private void cmbKategori_SelectedIndexChanged(object sender, EventArgs e)
        {
            string secilen = cmbKategori.SelectedItem?.ToString();
            pnlElektronik.Visible = (secilen == "Elektronik");
            pnlGida.Visible = (secilen == "Gıda");
            pnlGiyim.Visible = (secilen == "Giyim");
        }

        private void btnKaydet_Click(object sender, EventArgs e)
        {
            try
            {
                string kod = txtUrunKodu.Text.Trim();
                string ad = txtUrunAdi.Text.Trim();
                decimal fiyat = numBirimFiyat.Value;
                int kritik = (int)numKritikStok.Value;
                int stok = (int)numStokMiktari.Value;
                string kat = cmbKategori.SelectedItem.ToString();

                if (string.IsNullOrWhiteSpace(kod))
                {
                    MessageBox.Show("Lütfen ürün kodunu giriniz!", "Eksik Bilgi", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    txtUrunKodu.Focus();
                    return;
                }

                if (string.IsNullOrWhiteSpace(ad))
                {
                    MessageBox.Show("Lütfen ürün adını giriniz!", "Eksik Bilgi", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    txtUrunAdi.Focus();
                    return;
                }

                if (_duzenlenecekUrun != null)
                {
                    // Güncelleme işlemi
                    _duzenlenecekUrun.UrunAdi = ad;
                    _duzenlenecekUrun.BirimFiyat = fiyat;
                    _duzenlenecekUrun.KritikStokSeviyesi = kritik;

                    if (_duzenlenecekUrun is ElektronikUrun elk)
                    {
                        elk.Marka = txtEk1.Text.Trim();
                        elk.GarantiSuresiAy = (int)numEk2.Value;
                    }
                    else if (_duzenlenecekUrun is GidaUrunu gida)
                    {
                        gida.SonTuketimTarihi = dtpEkTarih.Value;
                        gida.SogukZincir = chkEkBool.Checked;
                    }
                    else if (_duzenlenecekUrun is GiyimUrunu gym)
                    {
                        gym.Beden = txtEk1.Text.Trim();
                        gym.KumasTuru = txtEk3.Text.Trim();
                    }

                    OlusturulanUrun = _duzenlenecekUrun;
                }
                else
                {
                    // Yeni ürün oluşturma (Polymorphic nesne örnekleme)
                    if (kat == "Elektronik")
                    {
                        string marka = txtEk1.Text.Trim();
                        int garanti = (int)numEk2.Value;
                        OlusturulanUrun = new ElektronikUrun(kod, ad, fiyat, stok, marka, garanti, kritik);
                    }
                    else if (kat == "Gıda")
                    {
                        DateTime stt = dtpEkTarih.Value;
                        bool soguk = chkEkBool.Checked;
                        OlusturulanUrun = new GidaUrunu(kod, ad, fiyat, stok, stt, soguk, kritik);
                    }
                    else if (kat == "Giyim")
                    {
                        string beden = txtEk1.Text.Trim();
                        string kumas = txtEk3.Text.Trim();
                        OlusturulanUrun = new GiyimUrunu(kod, ad, fiyat, stok, beden, kumas, kritik);
                    }
                }

                this.DialogResult = DialogResult.OK;
                this.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Hata: " + ex.Message, "Doğrulama Hatası", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnIptal_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.Cancel;
            this.Close();
        }
    }
}
