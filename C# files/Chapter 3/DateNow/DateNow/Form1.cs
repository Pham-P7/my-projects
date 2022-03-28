namespace DateNow
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Now_Click(object sender, EventArgs e)
        {
            MessageBox.Show(DateTime.Now.ToString());
        }
    }
}