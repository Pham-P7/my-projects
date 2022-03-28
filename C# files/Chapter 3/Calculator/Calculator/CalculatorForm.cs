using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            WelcomeLabel.Text = "New greeting";
            this.BackgroundImage = Image.FromFile("background.png");
            this.BackgroundImageLayout = ImageLayout.Stretch;

            PrintButton.Text = "";
            PrintButton.Image = Image.FromFile("printer.png");
        }
    }
}