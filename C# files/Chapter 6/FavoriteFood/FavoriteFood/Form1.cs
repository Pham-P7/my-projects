namespace FavoriteFood
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void buttonChoose_Click(object sender, EventArgs e)
        {
            if (radioChinese.Checked)
            {
                MessageBox.Show("General Tso's Chicken is tasty!");
                radioChinese.Checked = false;
            }
            else if (radioMexican.Checked)
            {
                MessageBox.Show("I love burritos!");
                radioMexican.Checked = false;
            }
            else if (radioIndian.Checked)
            {
                MessageBox.Show("Try Chicken Tikka Masala!");
                radioIndian.Checked = false;
            }
            else  // this should run if none of the above are true
            {
                MessageBox.Show("Make a selection!");
            }
        }
    }
}