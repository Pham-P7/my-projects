namespace PlayerOne
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void StartButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Your name is: " + textBoxName.Text);
            textBoxName.Text = "";
        }
    }
}