namespace Hello_World_2
{
    partial class HelloWorld2
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
            this.MyButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // MyButton
            // 
            this.MyButton.Location = new System.Drawing.Point(340, 189);
            this.MyButton.Name = "MyButton";
            this.MyButton.Size = new System.Drawing.Size(94, 29);
            this.MyButton.TabIndex = 0;
            this.MyButton.Text = "Click here";
            this.MyButton.UseVisualStyleBackColor = true;
            this.MyButton.Click += new System.EventHandler(this.MyButton_Click);
            // 
            // HelloWorld2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.MyButton);
            this.Name = "HelloWorld2";
            this.Text = "Hello, World";
            this.Load += new System.EventHandler(this.HelloWorld2_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private Button MyButton;
    }
}