using System.Drawing;
using System.Windows.Forms;

namespace InventoryManagementSystem.Forms
{
    partial class FormUrunEkleGuncelle
    {
        private System.ComponentModel.IContainer components = null;

        private Label lblBaslik;
        private Label lblUrunKodu;
        private TextBox txtUrunKodu;
        private Label lblUrunAdi;
        private TextBox txtUrunAdi;
        private Label lblKategori;
        private ComboBox cmbKategori;
        private Label lblBirimFiyat;
        private NumericUpDown numBirimFiyat;
        private Label lblStokMiktari;
        private NumericUpDown numStokMiktari;
        private Label lblKritikStok;
        private NumericUpDown numKritikStok;

        // Dinamik paneller (Kategoriye özgü ek alanlar)
        private Panel pnlElektronik;
        private Label lblEk1;
        private TextBox txtEk1;
        private Label lblEk2;
        private NumericUpDown numEk2;

        private Panel pnlGida;
        private Label lblEkTarih;
        private DateTimePicker dtpEkTarih;
        private CheckBox chkEkBool;

        private Panel pnlGiyim;
        private Label lblEk3;
        private TextBox txtEk3;

        private Button btnKaydet;
        private Button btnIptal;

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
            this.lblBaslik = new Label();
            this.lblUrunKodu = new Label();
            this.txtUrunKodu = new TextBox();
            this.lblUrunAdi = new Label();
            this.txtUrunAdi = new TextBox();
            this.lblKategori = new Label();
            this.cmbKategori = new ComboBox();
            this.lblBirimFiyat = new Label();
            this.numBirimFiyat = new NumericUpDown();
            this.lblStokMiktari = new Label();
            this.numStokMiktari = new NumericUpDown();
            this.lblKritikStok = new Label();
            this.numKritikStok = new NumericUpDown();

            this.pnlElektronik = new Panel();
            this.lblEk1 = new Label();
            this.txtEk1 = new TextBox();
            this.lblEk2 = new Label();
            this.numEk2 = new NumericUpDown();

            this.pnlGida = new Panel();
            this.lblEkTarih = new Label();
            this.dtpEkTarih = new DateTimePicker();
            this.chkEkBool = new CheckBox();

            this.pnlGiyim = new Panel();
            this.lblEk3 = new Label();
            this.txtEk3 = new TextBox();

            this.btnKaydet = new Button();
            this.btnIptal = new Button();

            ((System.ComponentModel.ISupportInitialize)(this.numBirimFiyat)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numStokMiktari)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numKritikStok)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numEk2)).BeginInit();
            this.pnlElektronik.SuspendLayout();
            this.pnlGida.SuspendLayout();
            this.pnlGiyim.SuspendLayout();
            this.SuspendLayout();

            // Form ayarları
            this.ClientSize = new Size(420, 480);
            this.FormBorderStyle = FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.StartPosition = FormStartPosition.CenterParent;
            this.BackColor = Color.FromArgb(245, 247, 250);
            this.Font = new Font("Segoe UI", 9.5F, FontStyle.Regular, GraphicsUnit.Point);

            // Başlık
            this.lblBaslik.Font = new Font("Segoe UI", 13F, FontStyle.Bold, GraphicsUnit.Point);
            this.lblBaslik.ForeColor = Color.FromArgb(33, 43, 54);
            this.lblBaslik.Location = new Point(20, 15);
            this.lblBaslik.Size = new Size(380, 30);
            this.lblBaslik.Text = "Ürün Bilgi Formu";

            // Urun Kodu
            this.lblUrunKodu.Location = new Point(25, 60);
            this.lblUrunKodu.Size = new Size(130, 20);
            this.lblUrunKodu.Text = "Ürün Kodu (*):";
            this.txtUrunKodu.Location = new Point(160, 57);
            this.txtUrunKodu.Size = new Size(220, 25);

            // Urun Adi
            this.lblUrunAdi.Location = new Point(25, 95);
            this.lblUrunAdi.Size = new Size(130, 20);
            this.lblUrunAdi.Text = "Ürün Adı (*):";
            this.txtUrunAdi.Location = new Point(160, 92);
            this.txtUrunAdi.Size = new Size(220, 25);

            // Kategori
            this.lblKategori.Location = new Point(25, 130);
            this.lblKategori.Size = new Size(130, 20);
            this.lblKategori.Text = "Kategori:";
            this.cmbKategori.DropDownStyle = ComboBoxStyle.DropDownList;
            this.cmbKategori.Items.AddRange(new object[] { "Elektronik", "Gıda", "Giyim" });
            this.cmbKategori.Location = new Point(160, 127);
            this.cmbKategori.Size = new Size(220, 25);
            this.cmbKategori.SelectedIndexChanged += new System.EventHandler(this.cmbKategori_SelectedIndexChanged);

            // Birim Fiyat
            this.lblBirimFiyat.Location = new Point(25, 165);
            this.lblBirimFiyat.Size = new Size(130, 20);
            this.lblBirimFiyat.Text = "Birim Fiyat (TL):";
            this.numBirimFiyat.DecimalPlaces = 2;
            this.numBirimFiyat.Maximum = 1000000M;
            this.numBirimFiyat.Location = new Point(160, 162);
            this.numBirimFiyat.Size = new Size(220, 25);

            // Stok Miktari
            this.lblStokMiktari.Location = new Point(25, 200);
            this.lblStokMiktari.Size = new Size(130, 20);
            this.lblStokMiktari.Text = "Başlangıç Stok:";
            this.numStokMiktari.Maximum = 1000000M;
            this.numStokMiktari.Location = new Point(160, 197);
            this.numStokMiktari.Size = new Size(220, 25);

            // Kritik Stok
            this.lblKritikStok.Location = new Point(25, 235);
            this.lblKritikStok.Size = new Size(130, 20);
            this.lblKritikStok.Text = "Kritik Stok Sınırı:";
            this.numKritikStok.Maximum = 10000M;
            this.numKritikStok.Value = 10;
            this.numKritikStok.Location = new Point(160, 232);
            this.numKritikStok.Size = new Size(220, 25);

            // Panel: Elektronik
            this.pnlElektronik.Location = new Point(20, 270);
            this.pnlElektronik.Size = new Size(380, 80);
            this.lblEk1.Location = new Point(5, 5);
            this.lblEk1.Size = new Size(130, 20);
            this.lblEk1.Text = "Marka:";
            this.txtEk1.Location = new Point(140, 2);
            this.txtEk1.Size = new Size(220, 25);
            this.lblEk2.Location = new Point(5, 40);
            this.lblEk2.Size = new Size(130, 20);
            this.lblEk2.Text = "Garanti (Ay):";
            this.numEk2.Location = new Point(140, 37);
            this.numEk2.Size = new Size(220, 25);
            this.numEk2.Maximum = 120M;
            this.numEk2.Value = 24M;
            this.pnlElektronik.Controls.Add(this.lblEk1);
            this.pnlElektronik.Controls.Add(this.txtEk1);
            this.pnlElektronik.Controls.Add(this.lblEk2);
            this.pnlElektronik.Controls.Add(this.numEk2);

            // Panel: Gida
            this.pnlGida.Location = new Point(20, 270);
            this.pnlGida.Size = new Size(380, 80);
            this.lblEkTarih.Location = new Point(5, 5);
            this.lblEkTarih.Size = new Size(130, 20);
            this.lblEkTarih.Text = "Son Tüketim Tarihi:";
            this.dtpEkTarih.Format = DateTimePickerFormat.Short;
            this.dtpEkTarih.Location = new Point(140, 2);
            this.dtpEkTarih.Size = new Size(220, 25);
            this.chkEkBool.Location = new Point(140, 40);
            this.chkEkBool.Size = new Size(220, 25);
            this.chkEkBool.Text = "Soğuk Zincir Gerektirir";
            this.pnlGida.Controls.Add(this.lblEkTarih);
            this.pnlGida.Controls.Add(this.dtpEkTarih);
            this.pnlGida.Controls.Add(this.chkEkBool);
            this.pnlGida.Visible = false;

            // Panel: Giyim
            this.pnlGiyim.Location = new Point(20, 270);
            this.pnlGiyim.Size = new Size(380, 80);
            this.lblEk3.Location = new Point(5, 40);
            this.lblEk3.Size = new Size(130, 20);
            this.lblEk3.Text = "Kumaş Türü:";
            this.txtEk3.Location = new Point(140, 37);
            this.txtEk3.Size = new Size(220, 25);
            this.pnlGiyim.Controls.Add(this.lblEk3);
            this.pnlGiyim.Controls.Add(this.txtEk3);
            this.pnlGiyim.Visible = false;

            // Butonlar
            this.btnKaydet.Location = new Point(180, 390);
            this.btnKaydet.Size = new Size(100, 35);
            this.btnKaydet.Text = "Kaydet";
            this.btnKaydet.BackColor = Color.FromArgb(37, 99, 235);
            this.btnKaydet.ForeColor = Color.White;
            this.btnKaydet.FlatStyle = FlatStyle.Flat;
            this.btnKaydet.Click += new System.EventHandler(this.btnKaydet_Click);

            this.btnIptal.Location = new Point(290, 390);
            this.btnIptal.Size = new Size(90, 35);
            this.btnIptal.Text = "İptal";
            this.btnIptal.BackColor = Color.FromArgb(148, 163, 184);
            this.btnIptal.ForeColor = Color.White;
            this.btnIptal.FlatStyle = FlatStyle.Flat;
            this.btnIptal.Click += new System.EventHandler(this.btnIptal_Click);

            // Kontrolleri ekle
            this.Controls.Add(this.lblBaslik);
            this.Controls.Add(this.lblUrunKodu);
            this.Controls.Add(this.txtUrunKodu);
            this.Controls.Add(this.lblUrunAdi);
            this.Controls.Add(this.txtUrunAdi);
            this.Controls.Add(this.lblKategori);
            this.Controls.Add(this.cmbKategori);
            this.Controls.Add(this.lblBirimFiyat);
            this.Controls.Add(this.numBirimFiyat);
            this.Controls.Add(this.lblStokMiktari);
            this.Controls.Add(this.numStokMiktari);
            this.Controls.Add(this.lblKritikStok);
            this.Controls.Add(this.numKritikStok);
            this.Controls.Add(this.pnlElektronik);
            this.Controls.Add(this.pnlGida);
            this.Controls.Add(this.pnlGiyim);
            this.Controls.Add(this.btnKaydet);
            this.Controls.Add(this.btnIptal);

            ((System.ComponentModel.ISupportInitialize)(this.numBirimFiyat)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numStokMiktari)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numKritikStok)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numEk2)).EndInit();
            this.pnlElektronik.ResumeLayout(false);
            this.pnlElektronik.PerformLayout();
            this.pnlGida.ResumeLayout(false);
            this.pnlGida.PerformLayout();
            this.pnlGiyim.ResumeLayout(false);
            this.pnlGiyim.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}
