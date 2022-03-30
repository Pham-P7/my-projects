namespace Beepers
{
    public partial class BeeperForm : Form
    {
        public BeeperForm()
        {
            InitializeComponent();
        }
        private void ForButton_Click(object sender, EventArgs e)
        {
            int numBeeps = int.Parse(NumBeepsText.Text);
            if (numBeeps > 0)
            {
                for (int i = 0; i < numBeeps; i++)
                    Console.Beep();
            }
            else
                MessageBox.Show("please enter a valid number");
        }

        private void WhileButton_Click(object sender, EventArgs e)
        {
            int numBeeps = int.Parse(NumBeepsText.Text);
            int count = 0;
            if (numBeeps > 0)
            {
                while (count < numBeeps)
                {
                    Console.Beep();
                    count++;
                }
            }
            else
                MessageBox.Show("please enter a valid number");
        }

        private void DoButton_Click(object sender, EventArgs e)
        {
            int numBeeps = int.Parse(NumBeepsText.Text);
            int count = 0;
            if (numBeeps > 0)
            {
                do
                {
                    Console.Beep();
                    count++;
                }
                while (count < numBeeps);
            }
            else
                MessageBox.Show("please enter a valid number");
        }
    }
}