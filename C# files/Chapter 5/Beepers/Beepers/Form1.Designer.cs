namespace Beepers
{
    partial class BeeperForm
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
            this.NumBeepsText = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.ForButton = new System.Windows.Forms.Button();
            this.WhileButton = new System.Windows.Forms.Button();
            this.DoButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // NumBeepsText
            // 
            this.NumBeepsText.Location = new System.Drawing.Point(401, 96);
            this.NumBeepsText.Name = "NumBeepsText";
            this.NumBeepsText.Size = new System.Drawing.Size(125, 27);
            this.NumBeepsText.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(261, 99);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(134, 20);
            this.label1.TabIndex = 1;
            this.label1.Text = "Number Of Beeps: ";
            // 
            // ForButton
            // 
            this.ForButton.Location = new System.Drawing.Point(335, 165);
            this.ForButton.Name = "ForButton";
            this.ForButton.Size = new System.Drawing.Size(146, 29);
            this.ForButton.TabIndex = 2;
            this.ForButton.Text = "For Loop Beep";
            this.ForButton.UseVisualStyleBackColor = true;
            this.ForButton.Click += new System.EventHandler(this.ForButton_Click);
            // 
            // WhileButton
            // 
            this.WhileButton.Location = new System.Drawing.Point(335, 235);
            this.WhileButton.Name = "WhileButton";
            this.WhileButton.Size = new System.Drawing.Size(146, 29);
            this.WhileButton.TabIndex = 3;
            this.WhileButton.Text = "While Loop Beep";
            this.WhileButton.UseVisualStyleBackColor = true;
            this.WhileButton.Click += new System.EventHandler(this.WhileButton_Click);
            // 
            // DoButton
            // 
            this.DoButton.Location = new System.Drawing.Point(335, 306);
            this.DoButton.Name = "DoButton";
            this.DoButton.Size = new System.Drawing.Size(146, 29);
            this.DoButton.TabIndex = 4;
            this.DoButton.Text = "Do Loop Beep";
            this.DoButton.UseVisualStyleBackColor = true;
            this.DoButton.Click += new System.EventHandler(this.DoButton_Click);
            // 
            // BeeperForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.DoButton);
            this.Controls.Add(this.WhileButton);
            this.Controls.Add(this.ForButton);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.NumBeepsText);
            this.Name = "BeeperForm";
            this.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.Text = "Beepers, Jeepers";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private TextBox NumBeepsText;
        private Label label1;
        private Button ForButton;
        private Button WhileButton;
        private Button DoButton;
    }
}