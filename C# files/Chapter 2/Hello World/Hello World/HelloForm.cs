using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Hello_World
{
    public partial class HelloForm : Form
    {
        public HelloForm()
        {
            InitializeComponent();
        }

        private void HelloForm_Load(object sender, EventArgs e)
        {
            CheckBox.Text = "GoodBye";
            MyImageButton.Text = "";
            MyImageButton.Image = Image.FromFile("arrow_button.png");
            this.BackgroundImage = Image.FromFile("BlueBackground.jpg");
            this.BackgroundImageLayout = ImageLayout.Stretch;
        }
    }
}