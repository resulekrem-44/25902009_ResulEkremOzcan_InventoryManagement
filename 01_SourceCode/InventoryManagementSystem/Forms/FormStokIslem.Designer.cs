using System.Drawing;
using System.Windows.Forms;

namespace InventoryManagementSystem.Forms
{
    partial class FormStokIslem
    {
        private System.ComponentModel.IContainer components = null;

        private Label lblBaslik;
        private Label lblUrunBilgi;
        private Label lblMiktar;
        private NumericUpDown numMiktar;
        private Label lblAciklama;
        private TextBox txtAciklama;
        private Button btnOnayla;
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
            this.lblUrunBilgi = new Label();
            this.lblMiktar = new Label();
            this.numMiktar = new NumericUpDown();
            this.lblAciklama = new Label();
            this.txtAciklama = new TextBox();
            this.btnOnayla = new Button();
            this.btnIptal = new Button();

            ((System.ComponentModel.ISupportInitialize)(this.numMiktar)).BeginInit();
            this.SuspendLayout();

            // Form Ayarları
            this.ClientSize = new Size(380, 290);
            this.FormBorderStyle = FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.StartPosition = FormStartPosition.CenterParent;
            this.BackColor = Color.FromArgb(248, 250, 252);
            this.Font = new Font("Segoe UI", 9.5F, FontStyle.Regular, GraphicsUnit.Point);

            // Başlık
            this.lblBaslik.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            this.lblBaslik.Location = new Point(20, 15);
            this.lblBaslik.Size = new Size(340, 25);
            this.lblBaslik.TextAlign = ContentAlignment.MiddleCenter;

            // Ürün Bilgi Kutusu
            this.lblUrunBilgi.BackColor = Color.FromArgb(241, 245, 249);
            this.lblUrunBilgi.BorderStyle = BorderStyle.FixedSingle;
            this.lblUrunBilgi.Location = new Point(20, 50);
            this.lblUrunBilgi.Size = new Size(340, 50);
            this.lblUrunBilgi.TextAlign = ContentAlignment.MiddleLeft;
            this.lblUrunBilgi.Padding = new Padding(8);

            // Miktar
            this.lblMiktar.Location = new Point(20, 120);
            this.lblMiktar.Size = new Size(110, 20);
            this.lblMiktar.Text = "İşlem Miktarı:";
            this.numMiktar.Location = new Point(140, 117);
            this.numMiktar.Size = new Size(220, 25);

            // Açıklama
            this.lblAciklama.Location = new Point(20, 160);
            this.lblAciklama.Size = new Size(110, 20);
            this.lblAciklama.Text = "Açıklama / Not:";
            this.txtAciklama.Location = new Point(140, 157);
            this.txtAciklama.Size = new Size(220, 25);

            // Butonlar
            this.btnOnayla.Location = new Point(150, 220);
            this.btnOnayla.Size = new Size(100, 35);
            this.btnOnayla.ForeColor = Color.White;
            this.btnOnayla.FlatStyle = FlatStyle.Flat;
            this.btnOnayla.Click += new System.EventHandler(this.btnOnayla_Click);

            this.btnIptal.Location = new Point(260, 220);
            this.btnIptal.Size = new Size(100, 35);
            this.btnIptal.Text = "İptal";
            this.btnIptal.BackColor = Color.FromArgb(148, 163, 184);
            this.btnIptal.ForeColor = Color.White;
            this.btnIptal.FlatStyle = FlatStyle.Flat;
            this.btnIptal.Click += new System.EventHandler(this.btnIptal_Click);

            this.Controls.Add(this.lblBaslik);
            this.Controls.Add(this.lblUrunBilgi);
            this.Controls.Add(this.lblMiktar);
            this.Controls.Add(this.numMiktar);
            this.Controls.Add(this.lblAciklama);
            this.Controls.Add(this.txtAciklama);
            this.Controls.Add(this.btnOnayla);
            this.Controls.Add(this.btnIptal);

            ((System.ComponentModel.ISupportInitialize)(this.numMiktar)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();
        }
    }
}
