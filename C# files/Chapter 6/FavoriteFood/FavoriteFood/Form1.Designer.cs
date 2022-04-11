namespace FavoriteFood
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
            this.radioChinese = new System.Windows.Forms.RadioButton();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.radioMexican = new System.Windows.Forms.RadioButton();
            this.radioIndian = new System.Windows.Forms.RadioButton();
            this.buttonChoose = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // radioChinese
            // 
            this.radioChinese.AutoSize = true;
            this.radioChinese.Location = new System.Drawing.Point(27, 26);
            this.radioChinese.Name = "radioChinese";
            this.radioChinese.Size = new System.Drawing.Size(81, 24);
            this.radioChinese.TabIndex = 0;
            this.radioChinese.TabStop = true;
            this.radioChinese.Text = "Chinese";
            this.radioChinese.UseVisualStyleBackColor = true;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.radioIndian);
            this.groupBox1.Controls.Add(this.radioMexican);
            this.groupBox1.Controls.Add(this.radioChinese);
            this.groupBox1.Location = new System.Drawing.Point(286, 120);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(250, 125);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "My favorite food is:";
            // 
            // radioMexican
            // 
            this.radioMexican.AutoSize = true;
            this.radioMexican.Location = new System.Drawing.Point(27, 56);
            this.radioMexican.Name = "radioMexican";
            this.radioMexican.Size = new System.Drawing.Size(85, 24);
            this.radioMexican.TabIndex = 1;
            this.radioMexican.TabStop = true;
            this.radioMexican.Text = "Mexican";
            this.radioMexican.UseVisualStyleBackColor = true;
            // 
            // radioIndian
            // 
            this.radioIndian.AutoSize = true;
            this.radioIndian.Location = new System.Drawing.Point(27, 86);
            this.radioIndian.Name = "radioIndian";
            this.radioIndian.Size = new System.Drawing.Size(71, 24);
            this.radioIndian.TabIndex = 2;
            this.radioIndian.TabStop = true;
            this.radioIndian.Text = "Indian";
            this.radioIndian.UseVisualStyleBackColor = true;
            // 
            // buttonChoose
            // 
            this.buttonChoose.Location = new System.Drawing.Point(350, 287);
            this.buttonChoose.Name = "buttonChoose";
            this.buttonChoose.Size = new System.Drawing.Size(94, 29);
            this.buttonChoose.TabIndex = 2;
            this.buttonChoose.Text = "Choose";
            this.buttonChoose.UseVisualStyleBackColor = true;
            this.buttonChoose.Click += new System.EventHandler(this.buttonChoose_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.buttonChoose);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private RadioButton radioChinese;
        private GroupBox groupBox1;
        private RadioButton radioIndian;
        private RadioButton radioMexican;
        private Button buttonChoose;
    }
}