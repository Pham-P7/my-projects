namespace PlayerOne
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.textBoxName = new System.Windows.Forms.TextBox();
            this.StartButton = new System.Windows.Forms.Button();
            this.comboCars = new System.Windows.Forms.ComboBox();
            this.listEquipment = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(331, 30);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(132, 15);
            this.label1.TabIndex = 0;
            this.label1.Text = "enter your player name:";
            // 
            // textBoxName
            // 
            this.textBoxName.Location = new System.Drawing.Point(297, 111);
            this.textBoxName.Name = "textBoxName";
            this.textBoxName.Size = new System.Drawing.Size(201, 23);
            this.textBoxName.TabIndex = 1;
            // 
            // StartButton
            // 
            this.StartButton.Location = new System.Drawing.Point(297, 380);
            this.StartButton.Name = "StartButton";
            this.StartButton.Size = new System.Drawing.Size(201, 42);
            this.StartButton.TabIndex = 2;
            this.StartButton.Text = "ENTER";
            this.StartButton.UseVisualStyleBackColor = true;
            this.StartButton.Click += new System.EventHandler(this.StartButton_Click);
            // 
            // comboCars
            // 
            this.comboCars.FormattingEnabled = true;
            this.comboCars.Items.AddRange(new object[] {
            "Turbo Car",
            "Space Plane",
            "Stealth Sub",
            "Pogo Stick"});
            this.comboCars.Location = new System.Drawing.Point(297, 274);
            this.comboCars.Name = "comboCars";
            this.comboCars.Size = new System.Drawing.Size(201, 23);
            this.comboCars.TabIndex = 3;
            // 
            // listEquipment
            // 
            this.listEquipment.FormattingEnabled = true;
            this.listEquipment.ItemHeight = 15;
            this.listEquipment.Items.AddRange(new object[] {
            "Utility Belt",
            "Rocket Boots ",
            "Hockey Mask",
            "Rubber Ducky"});
            this.listEquipment.Location = new System.Drawing.Point(297, 155);
            this.listEquipment.Name = "listEquipment";
            this.listEquipment.Size = new System.Drawing.Size(201, 64);
            this.listEquipment.TabIndex = 4;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.listEquipment);
            this.Controls.Add(this.comboCars);
            this.Controls.Add(this.StartButton);
            this.Controls.Add(this.textBoxName);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Label label1;
        private TextBox textBoxName;
        private Button StartButton;
        private ComboBox comboCars;
        private ListBox listEquipment;
    }
}