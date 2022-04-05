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
            int index1 = listEquipment.SelectedIndex;
            int index2 = comboCars.SelectedIndex;
            String message = "Your player name is: " + textBoxName.Text +
             " And you have chosen the following equipment: " + (string)listEquipment.Items[index1] + 
             " And the following vehicle: " + comboCars.Items[index2];
            MessageBox.Show(message);

            textBoxName.Text = "";
            listEquipment.SelectedIndex = -1;
            comboCars.SelectedIndex = -1;
        }

    }
}