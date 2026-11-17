using System;
using System.Windows.Forms;
using InventoryManagementSystem.Forms;

namespace InventoryManagementSystem
{
    internal static class Program
    {
        /// <summary>
        /// Uygulamanın ana girdi noktasıdır.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new FormAnaEkran());
        }
    }
}
