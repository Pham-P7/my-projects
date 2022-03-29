namespace Data_Types
{
    public partial class DataForm : Form
    {
        public DataForm()
        {
            InitializeComponent();
        }

        private void ConstantButton_Click(object sender, EventArgs e)
        {
            const double MyCounstant = 3.14159;
            MessageBox.Show("My counstant: " + MyCounstant.ToString());
        }

        private void StringButton_Click(object sender, EventArgs e)
        {
            string MyString = "Hello, world!";
            MessageBox.Show("My string: " + MyString.ToString());
        }

        private void NumericButton_Click(object sender, EventArgs e)
        {
            int MyInt = 12;
            MessageBox.Show("My int: " + MyInt.ToString());
        }

        private void BoolButton_Click(object sender, EventArgs e)
        {
            bool MyBool = false;
            MessageBox.Show("My bool: " + MyBool.ToString());
        }
    }
}