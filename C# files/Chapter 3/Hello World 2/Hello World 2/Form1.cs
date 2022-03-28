namespace Hello_World_2
{
    public partial class HelloWorld2 : Form
    {
        public HelloWorld2()
        {
            InitializeComponent();
        }

        private void MyButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Hello, World!");
        }
    }
}