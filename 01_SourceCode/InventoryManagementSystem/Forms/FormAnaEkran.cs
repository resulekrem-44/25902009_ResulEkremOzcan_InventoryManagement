using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using InventoryManagementSystem.Models;
using InventoryManagementSystem.Services;

namespace InventoryManagementSystem.Forms
{
    public partial class FormAnaEkran : Form
    {
        private readonly StokYonetici _stokYonetici;

        public FormAnaEkran()
        {
            _stokYonetici = new StokYonetici();
            InitializeComponent();
            SetupGridDesign();
            ListeyiGuncelle();
        }

        private void SetupGridDesign()
        {
            dgvUrunler.AutoGenerateColumns = false;
            dgvUrunler.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            dgvUrunler.MultiSelect = false;
            dgvUrunler.ReadOnly = true;
            dgvUrunler.AllowUserToAddRows = false;
            dgvUrunler.RowHeadersVisible = false;

            dgvUrunler.Columns.Clear();
            dgvUrunler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "UrunKodu", HeaderText = "Ürün Kodu", Width = 110 });
            dgvUrunler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "UrunAdi", HeaderText = "Ürün Adı", Width = 230 });
            dgvUrunler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "Kategori", HeaderText = "Kategori", Width = 110 });
            dgvUrunler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "BirimFiyat", HeaderText = "Birim Fiyat", Width = 120, DefaultCellStyle = new DataGridViewCellStyle { Format = "C2", Alignment = DataGridViewContentAlignment.MiddleRight } });
            dgvUrunler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "StokMiktari", HeaderText = "Mevcut Stok", Width = 110, DefaultCellStyle = new DataGridViewCellStyle { Alignment = DataGridViewContentAlignment.MiddleCenter } });
            dgvUrunler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "KritikStokSeviyesi", HeaderText = "Kritik Sınır", Width = 100, DefaultCellStyle = new DataGridViewCellStyle { Alignment = DataGridViewContentAlignment.MiddleCenter } });

            // Polymorphism göstergesi: Detay sütunu (Pencere büyüdüğünde kalan tüm boşluğu kaplaması için AutoSizeMode = Fill)
            var colDetay = new DataGridViewTextBoxColumn { 
                HeaderText = "Özel Nitelikler / Detay (Polymorphism)", 
                Name = "ColDetay",
                AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill,
                MinimumWidth = 200
            };
            dgvUrunler.Columns.Add(colDetay);

            cmbFiltreKategori.SelectedIndex = 0; // "Tümü"

            // İşlem geçmişi tablosu
            dgvIslemler.AutoGenerateColumns = false;
            dgvIslemler.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            dgvIslemler.ReadOnly = true;
            dgvIslemler.AllowUserToAddRows = false;
            dgvIslemler.RowHeadersVisible = false;
            dgvIslemler.Columns.Clear();
            dgvIslemler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "Tarih", HeaderText = "Tarih / Saat", Width = 150, DefaultCellStyle = new DataGridViewCellStyle { Format = "dd.MM.yyyy HH:mm:ss" } });
            dgvIslemler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "IslemTipi", HeaderText = "İşlem Türü", Width = 130 });
            dgvIslemler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "UrunKodu", HeaderText = "Ürün Kodu", Width = 100 });
            dgvIslemler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "UrunAdi", HeaderText = "Ürün Adı", Width = 220 });
            dgvIslemler.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "Miktar", HeaderText = "Miktar", Width = 80, DefaultCellStyle = new DataGridViewCellStyle { Alignment = DataGridViewContentAlignment.MiddleCenter } });
            
            // Açıklama kolonu kalan tüm alanı esnek doldursun
            var colAciklama = new DataGridViewTextBoxColumn { 
                DataPropertyName = "Aciklama", 
                HeaderText = "Açıklama / Denetim İzi", 
                AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill,
                MinimumWidth = 220
            };
            dgvIslemler.Columns.Add(colAciklama);

            // Dashboard kartlarını form boyutu değiştikçe dinamik hizalama olayı
            pnlDashboard.Resize += PnlDashboard_Resize;
            pnlIslemButonlari.Resize += PnlIslemButonlari_Resize;
            DuzenleDashboardKartlari();
            DuzenleAltButonlar();
        }

        private void PnlIslemButonlari_Resize(object sender, EventArgs e)
        {
            DuzenleAltButonlar();
        }

        private void DuzenleAltButonlar()
        {
            if (pnlIslemButonlari == null) return;
            int sagKenar = pnlIslemButonlari.ClientSize.Width - 15;
            btnStokCikis.Location = new Point(sagKenar - btnStokCikis.Width, 12);
            btnStokGiris.Location = new Point(btnStokCikis.Left - btnStokGiris.Width - 10, 12);
        }

        private void PnlDashboard_Resize(object sender, EventArgs e)
        {
            DuzenleDashboardKartlari();
        }

        private void DuzenleDashboardKartlari()
        {
            if (pnlDashboard == null) return;
            
            int toplamGenislik = pnlDashboard.ClientSize.Width - 30; // 15 sol, 15 sağ boşluk
            int bosluk = 12;
            int kartGenislik = (toplamGenislik - (3 * bosluk)) / 4;
            if (kartGenislik < 180) kartGenislik = 180;

            pnlKart1.Location = new Point(15, 10);
            pnlKart1.Size = new Size(kartGenislik, 70);

            pnlKart2.Location = new Point(15 + kartGenislik + bosluk, 10);
            pnlKart2.Size = new Size(kartGenislik, 70);

            pnlKart3.Location = new Point(15 + (kartGenislik + bosluk) * 2, 10);
            pnlKart3.Size = new Size(kartGenislik, 70);

            pnlKart4.Location = new Point(15 + (kartGenislik + bosluk) * 3, 10);
            pnlKart4.Size = new Size(kartGenislik, 70);
        }

        private void ListeyiGuncelle()
        {
            try
            {
                string aranan = txtArama.Text.Trim();
                string kategori = cmbFiltreKategori.SelectedItem?.ToString() ?? "Tümü";
                bool kritikMi = chkKritikFiltre.Checked;

                List<Urun> filtrelenen = _stokYonetici.UrunAra(aranan, kategori, kritikMi);

                dgvUrunler.Rows.Clear();
                foreach (var urun in filtrelenen)
                {
                    int rowIndex = dgvUrunler.Rows.Add(
                        urun.UrunKodu,
                        urun.UrunAdi,
                        urun.Kategori,
                        urun.BirimFiyat,
                        urun.StokMiktari,
                        urun.KritikStokSeviyesi,
                        urun.DetayBilgisiGetir() // Polymorphic metot çağrısı
                    );

                    // Kritik stokta olan satırları dikkat çekmesi için renklendir
                    if (urun.KritikStoktaMi)
                    {
                        dgvUrunler.Rows[rowIndex].DefaultCellStyle.BackColor = Color.FromArgb(254, 242, 242);
                        dgvUrunler.Rows[rowIndex].DefaultCellStyle.ForeColor = Color.FromArgb(185, 28, 28);
                        dgvUrunler.Rows[rowIndex].DefaultCellStyle.Font = new Font("Segoe UI", 9F, FontStyle.Bold);
                    }
                }

                // Canlı Özet Göstergeleri (Dashboard) Güncellemesi
                lblOzetToplamUrun.Text = _stokYonetici.ToplamUrunSayisi().ToString();
                lblOzetToplamStok.Text = _stokYonetici.ToplamStokAdedi().ToString();
                lblOzetKritikUrun.Text = _stokYonetici.KritikStoktakiUrunSayisi().ToString();
                lblOzetEnvanterDeger.Text = _stokYonetici.ToplamEnvanterDegeri().ToString("C2");

                // İşlem geçmişi tablosu yenileme
                dgvIslemler.DataSource = null;
                var islemler = new List<IslemKaydi>(_stokYonetici.IslemGecmisiniGetir());
                islemler.Reverse(); // En son işlem en üstte
                dgvIslemler.DataSource = islemler;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Veriler listelenirken hata oluştu: " + ex.Message, "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private Urun SecilenUrunuGetir()
        {
            if (dgvUrunler.SelectedRows.Count == 0)
            {
                MessageBox.Show("Lütfen listeden işlem yapmak istediğiniz bir ürünü seçiniz!", "Seçim Yapılmadı", MessageBoxButtons.OK, MessageBoxIcon.Information);
                return null;
            }

            string kod = dgvUrunler.SelectedRows[0].Cells[0].Value?.ToString();
            return _stokYonetici.UrunBul(kod);
        }

        #region Buton Olayları (Event Handlers)

        private void btnYeniUrun_Click(object sender, EventArgs e)
        {
            using (var form = new FormUrunEkleGuncelle())
            {
                if (form.ShowDialog(this) == DialogResult.OK && form.OlusturulanUrun != null)
                {
                    try
                    {
                        _stokYonetici.UrunEkle(form.OlusturulanUrun);
                        ListeyiGuncelle();
                        MessageBox.Show(string.Format("'{0}' kodlu ürün başarıyla eklendi.", form.OlusturulanUrun.UrunKodu), "İşlem Başarılı", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("Ürün eklenemedi: " + ex.Message, "Kayıt Hatası", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }
        }

        private void btnUrunGuncelle_Click(object sender, EventArgs e)
        {
            Urun secilen = SecilenUrunuGetir();
            if (secilen == null) return;

            using (var form = new FormUrunEkleGuncelle(secilen))
            {
                if (form.ShowDialog(this) == DialogResult.OK)
                {
                    ListeyiGuncelle();
                    MessageBox.Show(string.Format("'{0}' kodlu ürün bilgileri güncellendi.", secilen.UrunKodu), "İşlem Başarılı", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
        }

        private void btnUrunSil_Click(object sender, EventArgs e)
        {
            Urun secilen = SecilenUrunuGetir();
            if (secilen == null) return;

            var onay = MessageBox.Show(string.Format("'{0} - {1}' ürününü silmek istediğinize emin misiniz?", secilen.UrunKodu, secilen.UrunAdi),
                "Silme Onayı", MessageBoxButtons.YesNo, MessageBoxIcon.Question);

            if (onay == DialogResult.Yes)
            {
                try
                {
                    _stokYonetici.UrunSil(secilen.UrunKodu);
                    ListeyiGuncelle();
                    MessageBox.Show("Ürün başarıyla silindi.", "Başarılı", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Silme işlemi sırasında hata: " + ex.Message, "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        private void btnStokGiris_Click(object sender, EventArgs e)
        {
            Urun secilen = SecilenUrunuGetir();
            if (secilen == null) return;

            using (var form = new FormStokIslem(secilen, true))
            {
                if (form.ShowDialog(this) == DialogResult.OK)
                {
                    try
                    {
                        _stokYonetici.StokGirisYap(secilen.UrunKodu, form.GirilenMiktar, form.GirilenAciklama);
                        ListeyiGuncelle();
                        MessageBox.Show(string.Format("{0} adet stok girişi tamamlandı. Yeni Stok: {1}", form.GirilenMiktar, secilen.StokMiktari),
                            "Stok Girişi Başarılı", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("Stok giriş hatası: " + ex.Message, "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }
        }

        private void btnStokCikis_Click(object sender, EventArgs e)
        {
            Urun secilen = SecilenUrunuGetir();
            if (secilen == null) return;

            if (secilen.StokMiktari <= 0)
            {
                MessageBox.Show("Bu ürünün stok miktarı sıfırdır, çıkış yapılamaz!", "Stok Yok", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            using (var form = new FormStokIslem(secilen, false))
            {
                if (form.ShowDialog(this) == DialogResult.OK)
                {
                    try
                    {
                        _stokYonetici.StokCikisYap(secilen.UrunKodu, form.GirilenMiktar, form.GirilenAciklama);
                        ListeyiGuncelle();
                        MessageBox.Show(string.Format("{0} adet stok çıkışı yapıldı. Kalan Stok: {1}", form.GirilenMiktar, secilen.StokMiktari),
                            "Stok Çıkışı Başarılı", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("Stok çıkış hatası: " + ex.Message, "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
            }
        }

        private void txtArama_TextChanged(object sender, EventArgs e)
        {
            ListeyiGuncelle();
        }

        private void cmbFiltreKategori_SelectedIndexChanged(object sender, EventArgs e)
        {
            ListeyiGuncelle();
        }

        private void chkKritikFiltre_CheckedChanged(object sender, EventArgs e)
        {
            ListeyiGuncelle();
        }

        private void btnFiltreSifirla_Click(object sender, EventArgs e)
        {
            txtArama.Text = string.Empty;
            cmbFiltreKategori.SelectedIndex = 0;
            chkKritikFiltre.Checked = false;
            ListeyiGuncelle();
        }

        #endregion
    }
}
