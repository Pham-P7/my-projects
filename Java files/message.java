import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

public class TicTacToe extends JFrame implements ActionListener{

    Random random = new Random();
    JFrame frame = new JFrame();
    JPanel title_panel = new JPanel();
    Jpanel button_panel = new JPanel();
    JLabel textfeild = new JLabel();
    JButton[] buttons = new JButton[9];
    boolean playerturn;

    public int firstTurn(){

      if(random.nextInt(2) == 0){
        playerturn = true;
        textfield.setText("X turn");
      }
      else{
          playerturn = false;
          textfield.setText("O turn");
      }
      return 0;
    }
    public void check(){
      if((buttons[0].getText()=="X") && (buttons[1].getText()=="X") && (buttons[2].getText()=="X")) {
        xWins(0,1,2);
      }
      if((buttons[3].getText()=="X") && (buttons[4].getText()=="X") && (buttons[5].getText()=="X")) {
        xWins(3,4,5);
      }
      if((buttons[6].getText()=="X") && (buttons[7].getText()=="X") && (buttons[8].getText()=="X")) {
        xWins(6,7,8);
      }
      if((buttons[0].getText()=="X") && (buttons[3].getText()=="X") && (buttons[6].getText()=="X")) {
        xWins(0,3,6);
      }
      if((buttons[1].getText()=="X") && (buttons[4].getText()=="X") && (buttons[7].getText()=="X")) {
        xWins(1,4,7);
      }
      if((buttons[2].getText()=="X") && (buttons[5].getText()=="X") && (buttons[8].getText()=="X")) {
        xWins(2,5,8);
      }
      if((buttons[0].getText()=="X") && (buttons[4].getText()=="X") && (buttons[8].getText()=="X")) {
        xWins(0,4,8);
      }
      if((buttons[2].getText()=="X") && (buttons[4].getText()=="X") && (buttons[6].getText()=="X")) {
        xWins(2,4,6);
      }
    }
    firstTurn();
  }
    public void actionPerformed(ActionEvent e){

      for(int i = 0; i < 9; i++){
        if(e.getSource()==buttons[i]){
          if(playerturn){
            if(buttons[i].getText()==""){
              buttons[i].setForeground(new Color(255,0,0));
              buttons[i].setText("X");
              playerturn = false;
              textfield.setText("O turn");
              check();
            }
          }
          else{
            if(buttons[i].getText()==""){
              buttons[i].setForeground(new Color(0,0,255));
              buttons[i].setText("O");
              playerturn = true;
              textfield.setText("X turn");
              check();
          }
        }
      }
    }

    public void xWins(int a, int b, int c){
      for(int i = 0; i < 9; i++){
        buttons[i].setEnabled(false);
      }
      textfield.setText("X Wins");
    }

    public void oWins(int a, int b, int c){
      for(int i = 0; i < 9; i++){
        buttons[i].setEnabled(false);
      }
      textfield.setText("O Wins");
    }
  }


  TicTacToe(){
    frame.setDeafaultCloseOperation(Jframe.EXIT_ON_CLOSE);
    frame.setSize(800,800);
    frame.getContentPane().setBackground(new Color(255,255,255));
    frame.setLayout(new BorderLayout());
    frame.setVisible(true);

    textfield.SetBackground(new Color(50,50,50));
    textfield.setForeground(new Color(25, 225, 0));
    textfield.setFont(new Font("Comic Sans MS", Font.BOLD,75));
    textfield.setHorizontalAlignment(JLabel.CENTER);
    textfield.setText("Tic-Tac-Toe");
    textfield.setOpaque(true);

    titlePanel.setLayout(new BorderLayout());
    titlePanel.setBounds(0,0,800,150);

    button_panel.setLayout(new GridLayout(3,3));
    button_panel.setBackground(new Color(0,0,0));

    for(int i = 0; i < 9; i++){
      buttons[i] = new JButton();
      button_panel.add(buttons[i]);
      buttons[i].setFont(new Font("Comic Sans MS",Font.BOLD,100));
      buttons[i].setFocusable(false);
      buttons[i].addActionListener(this);
    }

    titlePanel.add(textfield);
    frame.add(titlePanel,BorderLayout.NORTH);
    frame.add(button_panel);
