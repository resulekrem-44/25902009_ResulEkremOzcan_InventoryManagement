using System.Drawing;
using System.Windows.Forms;

namespace InventoryManagementSystem.Forms
{
    partial class FormAnaEkran
    {
        private System.ComponentModel.IContainer components = null;

        // Üst Banner Paneli
        private Panel pnlHeader;
        private Label lblBaslik;
        private Label lblOgrenciBilgi;

        // Özet İstatistik Kartları (Dashboard)
        private Panel pnlDashboard;
        private Panel pnlKart1;
        private Label lblKart1Baslik;
        private Label lblOzetToplamUrun;
        private Panel pnlKart2;
        private Label lblKart2Baslik;
        private Label lblOzetToplamStok;
        private Panel pnlKart3;
        private Label lblKart3Baslik;
        private Label lblOzetKritikUrun;
        private Panel pnlKart4;
        private Label lblKart4Baslik;
        private Label lblOzetEnvanterDeger;

        // Arama ve Filtre Çubuğu
        private Panel pnlFiltreler;
        private Label lblArama;
        private TextBox txtArama;
        private Label lblFiltreKat;
        private ComboBox cmbFiltreKategori;
        private CheckBox chkKritikFiltre;
        private Button btnFiltreSifirla;

        // İşlem Butonları Çubuğu
        private Panel pnlIslemButonlari;
        private Button btnYeniUrun;
        private Button btnUrunGuncelle;
        private Button btnUrunSil;
        private Button btnStokGiris;
        private Button btnStokCikis;

        // Sekmeli Yapı (TabControl): 1. Ürün Listesi, 2. İşlem Geçmişi
        private TabControl tabAna;
        private TabPage tabUrunler;
        private TabPage tabGecmis;
        private DataGridView dgvUrunler;
        private DataGridView dgvIslemler;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.pnlHeader = new Panel();
            this.lblBaslik = new Label();
            this.lblOgrenciBilgi = new Label();

            this.pnlDashboard = new Panel();
            this.pnlKart1 = new Panel();
            this.lblKart1Baslik = new Label();
            this.lblOzetToplamUrun = new Label();

            this.pnlKart2 = new Panel();
            this.lblKart2Baslik = new Label();
            this.lblOzetToplamStok = new Label();

            this.pnlKart3 = new Panel();
            this.lblKart3Baslik = new Label();
            this.lblOzetKritikUrun = new Label();

            this.pnlKart4 = new Panel();
            this.lblKart4Baslik = new Label();
            this.lblOzetEnvanterDeger = new Label();

            this.pnlFiltreler = new Panel();
            this.lblArama = new Label();
            this.txtArama = new TextBox();
            this.lblFiltreKat = new Label();
            this.cmbFiltreKategori = new ComboBox();
            this.chkKritikFiltre = new CheckBox();
            this.btnFiltreSifirla = new Button();

            this.pnlIslemButonlari = new Panel();
            this.btnYeniUrun = new Button();
            this.btnUrunGuncelle = new Button();
            this.btnUrunSil = new Button();
            this.btnStokGiris = new Button();
            this.btnStokCikis = new Button();

            this.tabAna = new TabControl();
            this.tabUrunler = new TabPage();
            this.tabGecmis = new TabPage();
            this.dgvUrunler = new DataGridView();
            this.dgvIslemler = new DataGridView();

            this.pnlHeader.SuspendLayout();
            this.pnlDashboard.SuspendLayout();
            this.pnlKart1.SuspendLayout();
            this.pnlKart2.SuspendLayout();
            this.pnlKart3.SuspendLayout();
            this.pnlKart4.SuspendLayout();
            this.pnlFiltreler.SuspendLayout();
            this.pnlIslemButonlari.SuspendLayout();
            this.tabAna.SuspendLayout();
            this.tabUrunler.SuspendLayout();
            this.tabGecmis.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvUrunler)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvIslemler)).BeginInit();
            this.SuspendLayout();

            // Form Boyutu ve Ana Özellikler
            this.ClientSize = new Size(1080, 680);
            this.MinimumSize = new Size(1000, 650);
            this.StartPosition = FormStartPosition.CenterScreen;
            this.Text = "Stok Yönetim Sistemi - Inventory Management System";
            this.BackColor = Color.FromArgb(241, 245, 249);
            this.Font = new Font("Segoe UI", 9F, FontStyle.Regular, GraphicsUnit.Point);

            // ================= 1. ÜST HEADER PANELİ =================
            this.pnlHeader.Dock = DockStyle.Top;
            this.pnlHeader.Height = 70;
            this.pnlHeader.BackColor = Color.FromArgb(15, 23, 42); // Derin Lacivert
            this.pnlHeader.Padding = new Padding(20, 10, 20, 10);

            this.lblBaslik.Text = "STOK YÖNETİM SİSTEMİ";
            this.lblBaslik.Font = new Font("Segoe UI", 16F, FontStyle.Bold, GraphicsUnit.Point);
            this.lblBaslik.ForeColor = Color.White;
            this.lblBaslik.Location = new Point(20, 12);
            this.lblBaslik.AutoSize = true;

            this.lblOgrenciBilgi.Text = "Resul Ekrem ÖZCAN - 25902009 | .NET Programlama - I Proje Ödevi";
            this.lblOgrenciBilgi.Font = new Font("Segoe UI", 9.5F, FontStyle.Regular, GraphicsUnit.Point);
            this.lblOgrenciBilgi.ForeColor = Color.FromArgb(148, 163, 184);
            this.lblOgrenciBilgi.Location = new Point(22, 42);
            this.lblOgrenciBilgi.AutoSize = true;

            this.pnlHeader.Controls.Add(this.lblBaslik);
            this.pnlHeader.Controls.Add(this.lblOgrenciBilgi);

            // ================= 2. DASHBOARD / ÖZET KARTLARI =================
            this.pnlDashboard.Dock = DockStyle.Top;
            this.pnlDashboard.Height = 90;
            this.pnlDashboard.BackColor = Color.Transparent;
            this.pnlDashboard.Padding = new Padding(15, 10, 15, 5);

            // Kart 1: Toplam Ürün
            this.pnlKart1.Size = new Size(245, 70);
            this.pnlKart1.Location = new Point(15, 10);
            this.pnlKart1.BackColor = Color.White;
            this.pnlKart1.BorderStyle = BorderStyle.FixedSingle;
            this.lblKart1Baslik.Text = "TOPLAM ÜRÜN ÇEŞİDİ";
            this.lblKart1Baslik.Font = new Font("Segoe UI", 8F, FontStyle.Bold);
            this.lblKart1Baslik.ForeColor = Color.FromArgb(100, 116, 139);
            this.lblKart1Baslik.Location = new Point(12, 10);
            this.lblKart1Baslik.AutoSize = true;
            this.lblOzetToplamUrun.Text = "0";
            this.lblOzetToplamUrun.Font = new Font("Segoe UI", 18F, FontStyle.Bold);
            this.lblOzetToplamUrun.ForeColor = Color.FromArgb(30, 41, 59);
            this.lblOzetToplamUrun.Location = new Point(10, 28);
            this.lblOzetToplamUrun.AutoSize = true;
            this.pnlKart1.Controls.Add(this.lblKart1Baslik);
            this.pnlKart1.Controls.Add(this.lblOzetToplamUrun);

            // Kart 2: Toplam Stok Adedi
            this.pnlKart2.Size = new Size(245, 70);
            this.pnlKart2.Location = new Point(275, 10);
            this.pnlKart2.BackColor = Color.White;
            this.pnlKart2.BorderStyle = BorderStyle.FixedSingle;
            this.lblKart2Baslik.Text = "TOPLAM STOK ADEDİ";
            this.lblKart2Baslik.Font = new Font("Segoe UI", 8F, FontStyle.Bold);
            this.lblKart2Baslik.ForeColor = Color.FromArgb(100, 116, 139);
            this.lblKart2Baslik.Location = new Point(12, 10);
            this.lblKart2Baslik.AutoSize = true;
            this.lblOzetToplamStok.Text = "0";
            this.lblOzetToplamStok.Font = new Font("Segoe UI", 18F, FontStyle.Bold);
            this.lblOzetToplamStok.ForeColor = Color.FromArgb(37, 99, 235);
            this.lblOzetToplamStok.Location = new Point(10, 28);
            this.lblOzetToplamStok.AutoSize = true;
            this.pnlKart2.Controls.Add(this.lblKart2Baslik);
            this.pnlKart2.Controls.Add(this.lblOzetToplamStok);

            // Kart 3: Kritik Stoktaki Ürün Sayısı
            this.pnlKart3.Size = new Size(245, 70);
            this.pnlKart3.Location = new Point(535, 10);
            this.pnlKart3.BackColor = Color.White;
            this.pnlKart3.BorderStyle = BorderStyle.FixedSingle;
            this.lblKart3Baslik.Text = "KRİTİK STOKTAKİ ÜRÜNLER";
            this.lblKart3Baslik.Font = new Font("Segoe UI", 8F, FontStyle.Bold);
            this.lblKart3Baslik.ForeColor = Color.FromArgb(220, 38, 38);
            this.lblKart3Baslik.Location = new Point(12, 10);
            this.lblKart3Baslik.AutoSize = true;
            this.lblOzetKritikUrun.Text = "0";
            this.lblOzetKritikUrun.Font = new Font("Segoe UI", 18F, FontStyle.Bold);
            this.lblOzetKritikUrun.ForeColor = Color.FromArgb(220, 38, 38);
            this.lblOzetKritikUrun.Location = new Point(10, 28);
            this.lblOzetKritikUrun.AutoSize = true;
            this.pnlKart3.Controls.Add(this.lblKart3Baslik);
            this.pnlKart3.Controls.Add(this.lblOzetKritikUrun);

            // Kart 4: Toplam Envanter Değeri
            this.pnlKart4.Size = new Size(245, 70);
            this.pnlKart4.Location = new Point(795, 10);
            this.pnlKart4.BackColor = Color.White;
            this.pnlKart4.BorderStyle = BorderStyle.FixedSingle;
            this.lblKart4Baslik.Text = "TOPLAM ENVANTER DEĞERİ";
            this.lblKart4Baslik.Font = new Font("Segoe UI", 8F, FontStyle.Bold);
            this.lblKart4Baslik.ForeColor = Color.FromArgb(5, 150, 105);
            this.lblKart4Baslik.Location = new Point(12, 10);
            this.lblKart4Baslik.AutoSize = true;
            this.lblOzetEnvanterDeger.Text = "0 TL";
            this.lblOzetEnvanterDeger.Font = new Font("Segoe UI", 16F, FontStyle.Bold);
            this.lblOzetEnvanterDeger.ForeColor = Color.FromArgb(5, 150, 105);
            this.lblOzetEnvanterDeger.Location = new Point(10, 30);
            this.lblOzetEnvanterDeger.AutoSize = true;
            this.pnlKart4.Controls.Add(this.lblKart4Baslik);
            this.pnlKart4.Controls.Add(this.lblOzetEnvanterDeger);

            this.pnlDashboard.Controls.Add(this.pnlKart1);
            this.pnlDashboard.Controls.Add(this.pnlKart2);
            this.pnlDashboard.Controls.Add(this.pnlKart3);
            this.pnlDashboard.Controls.Add(this.pnlKart4);

            // ================= 3. FİLTRELEME & ARAMA ÇUBUĞU =================
            this.pnlFiltreler.Dock = DockStyle.Top;
            this.pnlFiltreler.Height = 50;
            this.pnlFiltreler.BackColor = Color.White;
            this.pnlFiltreler.Padding = new Padding(15, 10, 15, 10);

            this.lblArama.Text = "Ara (Ad veya Kod):";
            this.lblArama.Location = new Point(15, 15);
            this.lblArama.AutoSize = true;
            this.lblArama.Font = new Font("Segoe UI", 9F, FontStyle.Bold);

            this.txtArama.Location = new Point(135, 12);
            this.txtArama.Size = new Size(180, 23);
            this.txtArama.TextChanged += new System.EventHandler(this.txtArama_TextChanged);

            this.lblFiltreKat.Text = "Kategori:";
            this.lblFiltreKat.Location = new Point(335, 15);
            this.lblFiltreKat.AutoSize = true;
            this.lblFiltreKat.Font = new Font("Segoe UI", 9F, FontStyle.Bold);

            this.cmbFiltreKategori.DropDownStyle = ComboBoxStyle.DropDownList;
            this.cmbFiltreKategori.Items.AddRange(new object[] { "Tümü", "Elektronik", "Gıda", "Giyim" });
            this.cmbFiltreKategori.Location = new Point(400, 12);
            this.cmbFiltreKategori.Size = new Size(130, 23);
            this.cmbFiltreKategori.SelectedIndexChanged += new System.EventHandler(this.cmbFiltreKategori_SelectedIndexChanged);

            this.chkKritikFiltre.Text = "Sadece Kritik Stok Seviyesindekiler";
            this.chkKritikFiltre.Location = new Point(555, 14);
            this.chkKritikFiltre.AutoSize = true;
            this.chkKritikFiltre.ForeColor = Color.FromArgb(185, 28, 28);
            this.chkKritikFiltre.Font = new Font("Segoe UI", 9F, FontStyle.Bold);
            this.chkKritikFiltre.CheckedChanged += new System.EventHandler(this.chkKritikFiltre_CheckedChanged);

            this.btnFiltreSifirla.Text = "Filtreleri Temizle";
            this.btnFiltreSifirla.Location = new Point(810, 10);
            this.btnFiltreSifirla.Size = new Size(120, 27);
            this.btnFiltreSifirla.BackColor = Color.FromArgb(226, 232, 240);
            this.btnFiltreSifirla.FlatStyle = FlatStyle.Flat;
            this.btnFiltreSifirla.Click += new System.EventHandler(this.btnFiltreSifirla_Click);

            this.pnlFiltreler.Controls.Add(this.lblArama);
            this.pnlFiltreler.Controls.Add(this.txtArama);
            this.pnlFiltreler.Controls.Add(this.lblFiltreKat);
            this.pnlFiltreler.Controls.Add(this.cmbFiltreKategori);
            this.pnlFiltreler.Controls.Add(this.chkKritikFiltre);
            this.pnlFiltreler.Controls.Add(this.btnFiltreSifirla);

            this.btnFiltreSifirla.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            this.btnFiltreSifirla.Location = new Point(this.pnlFiltreler.Width - 145, 10);

            // ================= 4. İŞLEM BUTONLARI =================
            this.pnlIslemButonlari.Dock = DockStyle.Bottom;
            this.pnlIslemButonlari.Height = 60;
            this.pnlIslemButonlari.BackColor = Color.White;
            this.pnlIslemButonlari.Padding = new Padding(15, 10, 15, 10);

            // Sol Butonlar (CRUD)
            this.btnYeniUrun.Text = "+ Yeni Ürün Ekle";
            this.btnYeniUrun.Location = new Point(15, 12);
            this.btnYeniUrun.Size = new Size(130, 36);
            this.btnYeniUrun.BackColor = Color.FromArgb(37, 99, 235);
            this.btnYeniUrun.ForeColor = Color.White;
            this.btnYeniUrun.FlatStyle = FlatStyle.Flat;
            this.btnYeniUrun.Font = new Font("Segoe UI", 9F, FontStyle.Bold);
            this.btnYeniUrun.Anchor = AnchorStyles.Bottom | AnchorStyles.Left;
            this.btnYeniUrun.Click += new System.EventHandler(this.btnYeniUrun_Click);

            this.btnUrunGuncelle.Text = "✎ Ürün Düzenle";
            this.btnUrunGuncelle.Location = new Point(155, 12);
            this.btnUrunGuncelle.Size = new Size(125, 36);
            this.btnUrunGuncelle.BackColor = Color.FromArgb(71, 85, 105);
            this.btnUrunGuncelle.ForeColor = Color.White;
            this.btnUrunGuncelle.FlatStyle = FlatStyle.Flat;
            this.btnUrunGuncelle.Anchor = AnchorStyles.Bottom | AnchorStyles.Left;
            this.btnUrunGuncelle.Click += new System.EventHandler(this.btnUrunGuncelle_Click);

            this.btnUrunSil.Text = "🗑 Ürün Sil";
            this.btnUrunSil.Location = new Point(290, 12);
            this.btnUrunSil.Size = new Size(100, 36);
            this.btnUrunSil.BackColor = Color.FromArgb(220, 38, 38);
            this.btnUrunSil.ForeColor = Color.White;
            this.btnUrunSil.FlatStyle = FlatStyle.Flat;
            this.btnUrunSil.Anchor = AnchorStyles.Bottom | AnchorStyles.Left;
            this.btnUrunSil.Click += new System.EventHandler(this.btnUrunSil_Click);

            // Sağ Butonlar (Stok İşlemleri - Anchor Right ile sağa kenetlenir)
            this.btnStokGiris.Text = "⬆ Stok Girişi (+)";
            this.btnStokGiris.Size = new Size(150, 36);
            this.btnStokGiris.BackColor = Color.FromArgb(16, 185, 129);
            this.btnStokGiris.ForeColor = Color.White;
            this.btnStokGiris.FlatStyle = FlatStyle.Flat;
            this.btnStokGiris.Font = new Font("Segoe UI", 9.5F, FontStyle.Bold);
            this.btnStokGiris.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
            this.btnStokGiris.Location = new Point(740, 12);
            this.btnStokGiris.Click += new System.EventHandler(this.btnStokGiris_Click);

            this.btnStokCikis.Text = "⬇ Stok Çıkışı (-)";
            this.btnStokCikis.Size = new Size(150, 36);
            this.btnStokCikis.BackColor = Color.FromArgb(239, 68, 68);
            this.btnStokCikis.ForeColor = Color.White;
            this.btnStokCikis.FlatStyle = FlatStyle.Flat;
            this.btnStokCikis.Font = new Font("Segoe UI", 9.5F, FontStyle.Bold);
            this.btnStokCikis.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
            this.btnStokCikis.Location = new Point(905, 12);
            this.btnStokCikis.Click += new System.EventHandler(this.btnStokCikis_Click);

            this.pnlIslemButonlari.Controls.Add(this.btnYeniUrun);
            this.pnlIslemButonlari.Controls.Add(this.btnUrunGuncelle);
            this.pnlIslemButonlari.Controls.Add(this.btnUrunSil);
            this.pnlIslemButonlari.Controls.Add(this.btnStokGiris);
            this.pnlIslemButonlari.Controls.Add(this.btnStokCikis);

            // ================= 5. SEKME VE GRIDLER =================
            this.tabAna.Dock = DockStyle.Fill;
            this.tabAna.Controls.Add(this.tabUrunler);
            this.tabAna.Controls.Add(this.tabGecmis);
            this.tabAna.Font = new Font("Segoe UI", 9.5F, FontStyle.Regular);

            // Tab 1: Ürün Envanter Tablosu
            this.tabUrunler.Text = "📦 Ürün Listesi ve Envanter";
            this.dgvUrunler.Dock = DockStyle.Fill;
            this.dgvUrunler.BackgroundColor = Color.White;
            this.dgvUrunler.BorderStyle = BorderStyle.None;
            this.tabUrunler.Controls.Add(this.dgvUrunler);

            // Tab 2: İşlem Hareketleri Geçmişi
            this.tabGecmis.Text = "📋 Stok Hareketleri ve Denetim İzi";
            this.dgvIslemler.Dock = DockStyle.Fill;
            this.dgvIslemler.BackgroundColor = Color.White;
            this.dgvIslemler.BorderStyle = BorderStyle.None;
            this.tabGecmis.Controls.Add(this.dgvIslemler);

            // Ana Forma Ekleme
            this.Controls.Add(this.tabAna);
            this.Controls.Add(this.pnlIslemButonlari);
            this.Controls.Add(this.pnlFiltreler);
            this.Controls.Add(this.pnlDashboard);
            this.Controls.Add(this.pnlHeader);

            this.pnlHeader.ResumeLayout(false);
            this.pnlHeader.PerformLayout();
            this.pnlDashboard.ResumeLayout(false);
            this.pnlKart1.ResumeLayout(false);
            this.pnlKart1.PerformLayout();
            this.pnlKart2.ResumeLayout(false);
            this.pnlKart2.PerformLayout();
            this.pnlKart3.ResumeLayout(false);
            this.pnlKart3.PerformLayout();
            this.pnlKart4.ResumeLayout(false);
            this.pnlKart4.PerformLayout();
            this.pnlFiltreler.ResumeLayout(false);
            this.pnlFiltreler.PerformLayout();
            this.pnlIslemButonlari.ResumeLayout(false);
            this.tabAna.ResumeLayout(false);
            this.tabUrunler.ResumeLayout(false);
            this.tabGecmis.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.dgvUrunler)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvIslemler)).EndInit();
            this.ResumeLayout(false);
        }
    }
}
