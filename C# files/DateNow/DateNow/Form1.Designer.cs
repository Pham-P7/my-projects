namespace DateNow
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
            this.Now = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // Now
            // 
            this.Now.Location = new System.Drawing.Point(268, 197);
            this.Now.Name = "Now";
            this.Now.Size = new System.Drawing.Size(263, 45);
            this.Now.TabIndex = 0;
            this.Now.Text = "What time is it?";
            this.Now.UseVisualStyleBackColor = true;
            this.Now.Click += new System.EventHandler(this.Now_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Now);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private Button Now;
    }
}