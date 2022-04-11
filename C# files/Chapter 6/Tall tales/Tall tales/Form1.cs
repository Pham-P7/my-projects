namespace Tall_tales
{
    public partial class TalesForm : Form
    {
        public TalesForm()
        {
            InitializeComponent();
        }

        private void StoryButton_Click(object sender, EventArgs e)
        {
            FinalStoryText.Text = "";
            string myStoryText = "Once upon a time, there was a ";
            myStoryText += SpeciesComboBox.Text + "named " + NameTextBox.Text + "."; // new sentence
            myStoryText += " " + ActivityLabel.Text + " " + ActivityList.Text;
            if (CheckBox1.Checked)
            {
                myStoryText += " and " + CheckBox1.Text;
            }
            if (CheckBox2.Checked)
            {
                myStoryText += " and " + CheckBox2.Text;
            }
            if (CheckBox3.Checked)
            {
                myStoryText += " and " + CheckBox3.Text;
            }
            myStoryText += "." + " "; // new sentence 
            myStoryText += SawLabel.Text + " ";
            if (RadioButton1.Checked)
            {
                myStoryText += RadioButton1.Text;
            }
            else if (RadioButton2.Checked)
            {
                myStoryText += RadioButton2.Text;
            }
            else if (RadioButton3.Checked)
            {
                myStoryText += RadioButton3.Text;
            }
            myStoryText += "." + " ";
            myStoryText += MoodLabel.Text + " ";
            myStoryText += GoodBadList.Text + " " + DayLabel.Text + ".";
            FinalStoryText.Text = myStoryText;
        }
    }
}