import javax.swing.*; import java.awt.*; import java.awt.event.*; import java.util.*;

  public class TicTacToe extends JFrame implements ActionListener
  {
    Random random = new Random();
    JFrame frame = new JFrame();
    JPanel titlePanel = new JPanel();
    JPanel button_panel = new JPanel();
    JLabel textfield = new JLabel();
    JButton[] buttons = new JButton[9];
    boolean playerturn;
    String Winner;
    String line = null;
    String Fill = null;
    public void firstTurn(){
      for(int i = 0; i < 9; i++)
      {
        buttons[i].setText("");
      }
      if(random.nextInt(2) == 0)
      {
        textfield.setText("X turn");
        playerturn = true;
      }
      else
      {
        textfield.setText("O turn");
        playerturn = false;
      }
    }
      public String checkWinner() {
        for (int a = 0; a < 8; a++) {
            switch (a) {
            case 0:
                line = buttons[0].getText() + buttons[1].getText() + buttons[2].getText();
                break;
            case 1:
                line = buttons[3].getText() + buttons[4].getText() + buttons[5].getText();
                break;
            case 2:
                line = buttons[6].getText() + buttons[7].getText() + buttons[8].getText();
                break;
            case 3:
                line = buttons[0].getText() + buttons[3].getText() + buttons[6].getText();
                break;
            case 4:
                line = buttons[1].getText() + buttons[4].getText() + buttons[7].getText();
                break;
            case 5:
                line = buttons[2].getText() + buttons[5].getText() + buttons[8].getText();
                break;
            case 6:
                line = buttons[0].getText() + buttons[4].getText() + buttons[8].getText();
                break;
            case 7:
                line = buttons[2].getText() + buttons[4].getText() + buttons[6].getText();
                break;
            }
              if (line.equals("XXX")) {
                  Fill = "X";
                  break;
              } 
              else if (line.equals("OOO")) {
                  Fill = "O";
                  break;
              }
            }
            return Fill;
        }
    public void tictactoe()
    {
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setSize(800,800);
      frame.getContentPane().setBackground(new Color(255,255,255));
      frame.setLayout(new BorderLayout());
      frame.setVisible(true);
  
      textfield.setBackground(new Color(50,50,50));
      textfield.setForeground(new Color(25, 225, 0));
      textfield.setFont(new Font("Comic Sans MS", Font.BOLD,75));
      textfield.setHorizontalAlignment(JLabel.CENTER);
      textfield.setText("Tic-Tac-Toe");
      textfield.setOpaque(true);
  
      titlePanel.setLayout(new BorderLayout());
      titlePanel.setBounds(0,0,800,150);
  
      button_panel.setLayout(new GridLayout(3,3));
      button_panel.setBackground(new Color(0,0,0));
  
      for(int i = 0; i < 9; i++)
      {
        buttons[i] = new JButton();
        button_panel.add(buttons[i]);
        buttons[i].setFont(new Font("Comic Sans MS",Font.BOLD,100));
        buttons[i].setFocusable(false);
        buttons[i].addActionListener(this);
      }
  
      titlePanel.add(textfield);
      frame.add(titlePanel,BorderLayout.NORTH);
      frame.add(button_panel);
    }
    public void actionPerformed(ActionEvent e)
    {
      for(int i = 0; i < 9; i++)
    {
        if(e.getSource() == buttons[i])
        {
          if(playerturn)
          {
            if(buttons[i].getText() == "")
            {
                buttons[i].setForeground(new Color(255,0,0));
                buttons[i].setText("X");
                playerturn = false;
                textfield.setText("O turn");
                Winner = checkWinner();
                if(Winner.equals("X")){
                  textfield.setText("X won");
                  break;
                }

            }
          }
          else
            {
                if(buttons[i].getText() == "")
                {
                    buttons[i].setForeground(new Color(0,0,255));
                    buttons[i].setText("O");
                    playerturn = true;
                    textfield.setText("X turn");
                    Winner = checkWinner();
                    if(Winner.equals("O")){
                      textfield.setText("O won");
                      break;
                    }
                }
            }
        }
    }
    if((!(Winner.equals("X"))) && (!(Winner.equals("O")))){
      textfield.setText("Tie");
    for(int i = 0; i < 9; i++){
      buttons[i].setEnabled(false);
      } 
    }
  }

public static void main(String[] args){

}
} 