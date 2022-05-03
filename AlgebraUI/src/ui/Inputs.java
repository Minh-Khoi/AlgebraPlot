/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ui;

import java.awt.Component;
import java.awt.event.ActionEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import javax.swing.JFrame;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

/**
 *
 * @author USER
 */
public class Inputs extends javax.swing.JDialog {
    public JFrame parent;
    /**
     * Creates new form Inputs
     * @param parent
     * @param modal
     * @param param
     */
    public Inputs(java.awt.Frame parent, boolean modal, String param ) {
        super(parent, modal);
        initComponents();
        this.submitButton.setEnabled(false);
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jRadioButton2 = new javax.swing.JRadioButton();
        buttonGroup1 = new javax.swing.ButtonGroup();
        buttonGroup2 = new javax.swing.ButtonGroup();
        buttonGroup3 = new javax.swing.ButtonGroup();
        buttonGroup4 = new javax.swing.ButtonGroup();
        buttonGroup5 = new javax.swing.ButtonGroup();
        plotTypePanel = new javax.swing.JPanel();
        choosePlotTypeLabel = new javax.swing.JLabel();
        lineChoosen = new javax.swing.JRadioButton();
        parabolChoosen = new javax.swing.JRadioButton();
        cubicChoosen = new javax.swing.JRadioButton();
        quarticChoosen = new javax.swing.JRadioButton();
        colorPanel = new javax.swing.JPanel();
        getColor = new javax.swing.JLabel();
        colorField = new javax.swing.JTextField();
        jLabel14 = new javax.swing.JLabel();
        findColorButton = new javax.swing.JButton();
        parametersPanel = new javax.swing.JPanel();
        getParamsLabel = new javax.swing.JLabel();
        aField = new javax.swing.JTextField();
        aLabel = new javax.swing.JLabel();
        dLabel = new javax.swing.JLabel();
        dField = new javax.swing.JTextField();
        bLabel = new javax.swing.JLabel();
        bField = new javax.swing.JTextField();
        cLabel = new javax.swing.JLabel();
        cField = new javax.swing.JTextField();
        eLabel = new javax.swing.JLabel();
        eField = new javax.swing.JTextField();
        errorLabel = new javax.swing.JLabel();
        titlePanel = new javax.swing.JLabel();
        submitButton = new javax.swing.JButton();

        jRadioButton2.setText("jRadioButton2");

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);

        plotTypePanel.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 1, true));

        choosePlotTypeLabel.setFont(new java.awt.Font("Dialog", 0, 18)); // NOI18N
        choosePlotTypeLabel.setText("<html><body>Choose the type of plot <br/> Chọn loại đồ thị hàm số</body></html>");

        lineChoosen.setFont(new java.awt.Font("Dialog", 0, 14)); // NOI18N
        lineChoosen.setSelected(true);
        lineChoosen.setText("<html><body>Line <br/> Hàm số bậc nhất</body></html>");
        lineChoosen.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                lineChoosenActionPerformed(evt);
            }
        });

        parabolChoosen.setFont(new java.awt.Font("Dialog", 0, 14)); // NOI18N
        parabolChoosen.setText("<html><body>Parabol <br/> Hàm số bậc hai</body></html>");
        parabolChoosen.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                parabolChoosenActionPerformed(evt);
            }
        });

        cubicChoosen.setFont(new java.awt.Font("Dialog", 0, 14)); // NOI18N
        cubicChoosen.setText("<html><body>Cubic <br/> Hàm số bậc ba</body></html>");
        cubicChoosen.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                cubicChoosenActionPerformed(evt);
            }
        });

        quarticChoosen.setFont(new java.awt.Font("Dialog", 0, 14)); // NOI18N
        quarticChoosen.setText("<html><body>Quartic <br/> Hàm số bậc bốn</body></html>");
        quarticChoosen.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                quarticChoosenActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout plotTypePanelLayout = new javax.swing.GroupLayout(plotTypePanel);
        plotTypePanel.setLayout(plotTypePanelLayout);
        plotTypePanelLayout.setHorizontalGroup(
            plotTypePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(plotTypePanelLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(choosePlotTypeLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 245, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(112, 112, 112)
                .addGroup(plotTypePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(lineChoosen, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(parabolChoosen, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 161, Short.MAX_VALUE)
                .addGroup(plotTypePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(cubicChoosen, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(quarticChoosen, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(88, 88, 88))
        );
        plotTypePanelLayout.setVerticalGroup(
            plotTypePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(plotTypePanelLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(plotTypePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(plotTypePanelLayout.createSequentialGroup()
                        .addGroup(plotTypePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(lineChoosen, javax.swing.GroupLayout.PREFERRED_SIZE, 39, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(cubicChoosen, javax.swing.GroupLayout.PREFERRED_SIZE, 39, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addGroup(plotTypePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(parabolChoosen, javax.swing.GroupLayout.PREFERRED_SIZE, 39, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(quarticChoosen, javax.swing.GroupLayout.PREFERRED_SIZE, 39, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(0, 0, Short.MAX_VALUE))
                    .addComponent(choosePlotTypeLabel))
                .addContainerGap())
        );

        colorPanel.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));

        getColor.setFont(new java.awt.Font("Dialog", 0, 18)); // NOI18N
        getColor.setText("<html><body>Get color <br/>Chọn màu </body></html>");

        jLabel14.setFont(new java.awt.Font("Dialog", 1, 18)); // NOI18N
        jLabel14.setText("color");

        findColorButton.setFont(new java.awt.Font("Dialog", 1, 14)); // NOI18N
        findColorButton.setText("Find Color");
        findColorButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                findColorButtonActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout colorPanelLayout = new javax.swing.GroupLayout(colorPanel);
        colorPanel.setLayout(colorPanelLayout);
        colorPanelLayout.setHorizontalGroup(
            colorPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(colorPanelLayout.createSequentialGroup()
                .addGap(22, 22, 22)
                .addComponent(getColor, javax.swing.GroupLayout.PREFERRED_SIZE, 272, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(164, 164, 164)
                .addComponent(colorField, javax.swing.GroupLayout.PREFERRED_SIZE, 93, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jLabel14)
                .addGap(33, 33, 33)
                .addComponent(findColorButton, javax.swing.GroupLayout.PREFERRED_SIZE, 131, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        colorPanelLayout.setVerticalGroup(
            colorPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(colorPanelLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(colorPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(colorPanelLayout.createSequentialGroup()
                        .addGap(8, 8, 8)
                        .addGroup(colorPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel14, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(colorField, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(findColorButton))
                        .addGap(0, 0, Short.MAX_VALUE))
                    .addGroup(colorPanelLayout.createSequentialGroup()
                        .addComponent(getColor, javax.swing.GroupLayout.PREFERRED_SIZE, 65, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))))
        );

        parametersPanel.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));

        getParamsLabel.setFont(new java.awt.Font("Dialog", 0, 18)); // NOI18N
        getParamsLabel.setText("<html><body>Get Parameters <br/>Chọn tham số </body></html>");

        aField.addFocusListener(new java.awt.event.FocusAdapter() {
            public void focusLost(java.awt.event.FocusEvent evt) {
                aFieldFocusLost(evt);
            }
        });

        aLabel.setDisplayedMnemonic('a');
        aLabel.setFont(new java.awt.Font("Dialog", 1, 18)); // NOI18N
        aLabel.setText("a");

        dLabel.setFont(new java.awt.Font("Dialog", 1, 18)); // NOI18N
        dLabel.setText("d");
        dLabel.setVisible(false);

        dField.setVisible(false);
        dField.addFocusListener(new java.awt.event.FocusAdapter() {
            public void focusLost(java.awt.event.FocusEvent evt) {
                dFieldFocusLost(evt);
            }
        });

        bLabel.setFont(new java.awt.Font("Dialog", 1, 18)); // NOI18N
        bLabel.setText("b");

        bField.addFocusListener(new java.awt.event.FocusAdapter() {
            public void focusLost(java.awt.event.FocusEvent evt) {
                bFieldFocusLost(evt);
            }
        });

        cLabel.setFont(new java.awt.Font("Dialog", 1, 18)); // NOI18N
        cLabel.setText("c");
        cLabel.setVisible(false);

        cField.setVisible(false);
        cField.addFocusListener(new java.awt.event.FocusAdapter() {
            public void focusLost(java.awt.event.FocusEvent evt) {
                cFieldFocusLost(evt);
            }
        });

        eLabel.setFont(new java.awt.Font("Dialog", 1, 18)); // NOI18N
        eLabel.setText("e");
        eLabel.setVisible(false);

        eField.setToolTipText("");
        eField.setVisible(false);
        eField.addFocusListener(new java.awt.event.FocusAdapter() {
            public void focusLost(java.awt.event.FocusEvent evt) {
                eFieldFocusLost(evt);
            }
        });

        errorLabel.setFont(new java.awt.Font("Dialog", 0, 14)); // NOI18N
        errorLabel.setForeground(new java.awt.Color(255, 0, 0));
        errorLabel.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        errorLabel.setText("<html><body>Please type number in the right numeric format <br/> Hãy nhập đúng định dạng số</body></html>");
        errorLabel.setVisible(false);

        javax.swing.GroupLayout parametersPanelLayout = new javax.swing.GroupLayout(parametersPanel);
        parametersPanel.setLayout(parametersPanelLayout);
        parametersPanelLayout.setHorizontalGroup(
            parametersPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(parametersPanelLayout.createSequentialGroup()
                .addGap(22, 22, 22)
                .addComponent(getParamsLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 272, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(87, 87, 87)
                .addComponent(aField, javax.swing.GroupLayout.PREFERRED_SIZE, 59, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(parametersPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(parametersPanelLayout.createSequentialGroup()
                        .addComponent(aLabel)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(bField, javax.swing.GroupLayout.PREFERRED_SIZE, 59, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, parametersPanelLayout.createSequentialGroup()
                        .addGap(0, 3, Short.MAX_VALUE)
                        .addComponent(dField, javax.swing.GroupLayout.PREFERRED_SIZE, 59, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(dLabel)
                        .addGap(82, 82, 82)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(parametersPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(parametersPanelLayout.createSequentialGroup()
                        .addComponent(bLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(68, 68, 68)
                        .addComponent(cField, javax.swing.GroupLayout.PREFERRED_SIZE, 59, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(cLabel))
                    .addGroup(parametersPanelLayout.createSequentialGroup()
                        .addGap(12, 12, 12)
                        .addComponent(eField, javax.swing.GroupLayout.PREFERRED_SIZE, 59, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(eLabel)))
                .addGap(78, 78, 78))
            .addGroup(parametersPanelLayout.createSequentialGroup()
                .addGap(232, 232, 232)
                .addComponent(errorLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 566, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        parametersPanelLayout.setVerticalGroup(
            parametersPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(parametersPanelLayout.createSequentialGroup()
                .addGroup(parametersPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(parametersPanelLayout.createSequentialGroup()
                        .addGap(8, 8, 8)
                        .addGroup(parametersPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(aField, javax.swing.GroupLayout.PREFERRED_SIZE, 26, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(aLabel)
                            .addComponent(bField, javax.swing.GroupLayout.PREFERRED_SIZE, 26, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(bLabel)
                            .addComponent(cField, javax.swing.GroupLayout.PREFERRED_SIZE, 26, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(cLabel))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addGroup(parametersPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(eLabel, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, parametersPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                .addComponent(dField, javax.swing.GroupLayout.DEFAULT_SIZE, 26, Short.MAX_VALUE)
                                .addComponent(dLabel, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                            .addComponent(eField, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, 29, Short.MAX_VALUE)))
                    .addComponent(getParamsLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 65, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(errorLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
        );

        titlePanel.setFont(new java.awt.Font("Dialog", 1, 48)); // NOI18N
        titlePanel.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        titlePanel.setText("PLOT 1");

        submitButton.setFont(new java.awt.Font("Freestyle Script", 1, 24)); // NOI18N
        submitButton.setText("Submit");
        submitButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                submitButtonActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(plotTypePanel, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(colorPanel, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(parametersPanel, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(22, 22, 22)
                        .addComponent(titlePanel, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
                .addContainerGap())
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(submitButton, javax.swing.GroupLayout.PREFERRED_SIZE, 158, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(148, 148, 148))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(21, 21, 21)
                .addComponent(titlePanel, javax.swing.GroupLayout.PREFERRED_SIZE, 78, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 31, Short.MAX_VALUE)
                .addComponent(plotTypePanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(15, 15, 15)
                .addComponent(parametersPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(colorPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(submitButton, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(9, 9, 9))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void generateParametersField(JRadioButton radioButton){
        if (radioButton.equals(this.lineChoosen)){
            this.cField.setVisible(false);
            this.cLabel.setVisible(false);
            this.dField.setVisible(false);
            this.dLabel.setVisible(false);
            this.eField.setVisible(false);
            this.eLabel.setVisible(false);
        } else if (radioButton.equals(this.parabolChoosen)){
            this.cField.setVisible(true);
            this.cLabel.setVisible(true);
            this.dField.setVisible(false);
            this.dLabel.setVisible(false);
            this.eField.setVisible(false);
            this.eLabel.setVisible(false);
        } else if (radioButton.equals(this.cubicChoosen)){
            this.cField.setVisible(true);
            this.cLabel.setVisible(true);
            this.dField.setVisible(true);
            this.dLabel.setVisible(true);
            this.eField.setVisible(false);
            this.eLabel.setVisible(false);
        } else if (radioButton.equals(this.quarticChoosen)){
            this.cField.setVisible(true);
            this.cLabel.setVisible(true);
            this.dField.setVisible(true);
            this.dLabel.setVisible(true);
            this.eField.setVisible(true);
            this.eLabel.setVisible(true);
        }
    }
    
    private void plotChoosenAction(ActionEvent evt){
        Object eventTarget = evt.getSource();
        Component[] componentsInPlotTypePanel = this.plotTypePanel.getComponents();
        if (eventTarget instanceof JRadioButton){
            for(Component comp : componentsInPlotTypePanel){
                if (comp instanceof JRadioButton ){
                    if (((JRadioButton) comp).getText() == ((JRadioButton) eventTarget).getText()){
                        ((JRadioButton) comp).setSelected(true);
                        this.generateParametersField((JRadioButton) comp);
                    } else {
                        ((JRadioButton) comp).setSelected(false);
                    }
                }
            }
        }
    }
    
    private void lineChoosenActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_lineChoosenActionPerformed
        // TODO add your handling code here:
        this.plotChoosenAction(evt);
    }//GEN-LAST:event_lineChoosenActionPerformed

    private void parabolChoosenActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_parabolChoosenActionPerformed
        // TODO add your handling code here:
        this.plotChoosenAction(evt);
    }//GEN-LAST:event_parabolChoosenActionPerformed

    private void cubicChoosenActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_cubicChoosenActionPerformed
        // TODO add your handling code here:
        this.plotChoosenAction(evt);
    }//GEN-LAST:event_cubicChoosenActionPerformed

    private void quarticChoosenActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_quarticChoosenActionPerformed
        // TODO add your handling code here:
        this.plotChoosenAction(evt);
    }//GEN-LAST:event_quarticChoosenActionPerformed

    private boolean allCharactersIsValid(String str){
        boolean isValid = true;
        int numOfSlash = 0, numOfDot = 0, numOfMinus =0;
        for(char character : str.toCharArray()){
            if (character == '/' || character == '.' || character == '-' || Character.isDigit(character)){
                if (character == '/' ){
                    numOfSlash ++;
                }
                if (character == '.'){
                    numOfDot ++;
                }
                if (character == '-'){
                    numOfMinus ++;
                }
                
                boolean specialCharOccurLessThanTwo = numOfDot < 2 && numOfMinus<2 && numOfSlash<2;
                boolean slashRightPosition = (numOfSlash ==1 && str.indexOf('/') != 0) || numOfSlash==0;
                boolean minusRightPosition = (numOfMinus ==1 && str.indexOf('-') == 0) || numOfMinus==0;
                boolean specialCharNotNextToEachOther = 
                            (Math.abs(str.indexOf('/') - str.indexOf('.')) != 1 || numOfSlash==0 || numOfDot==0) &&
                            (str.indexOf('-') - str.indexOf('.') != 1  || numOfMinus==0 || numOfDot==0) &&
                            (Math.abs(str.indexOf('/') - str.indexOf('-')) != 1 || numOfSlash==0 || numOfMinus==0);
//                System.out.println(character);
//                System.out.println( numOfSlash);
//                System.out.println(specialCharNotNextToEachOther);
                if (!specialCharOccurLessThanTwo || !slashRightPosition || !minusRightPosition || !specialCharNotNextToEachOther){
//                    System.out.println("----" + character + " -----------");
//                    System.out.println(specialCharOccurLessThanTwo);
//                    System.out.println(slashRightPosition);
//                    System.out.println(minusRightPosition);
//                    System.out.println(specialCharNotNextToEachOther);
                    isValid = false;
                    break;
                }
            } else {
                isValid = false;
                break;
            }
        }
        return isValid;
    }
    
    private void validateKeyTyped(){
        boolean isValid = true;
        Component[] componentsInParametersPanel = this.parametersPanel.getComponents();
        boolean emptyFieldExist = false;
        for (Component comp : componentsInParametersPanel){
            if (comp instanceof JTextField && comp.isShowing()){
                JTextField compConverted = (JTextField) comp;
                String txt = compConverted.getText();
                if (txt.trim().length()==0){
                    emptyFieldExist = true;
                }
//                System.out.println(emptyFieldExist);
//                System.out.println(txt);
                if (!this.allCharactersIsValid(txt)){
                    isValid = false;
                    break;
                }
            }
        }
        this.errorLabel.setVisible(!isValid);
        this.submitButton.setEnabled(isValid && !emptyFieldExist);
    }
        
    private void findColorButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_findColorButtonActionPerformed
        // TODO add your handling code here:
        ColorChooser pickColorDialog = new ColorChooser(this.parent, true);
        pickColorDialog.setVisible(true);
        Inputs self= this;
        pickColorDialog.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosed(WindowEvent e) {
                if (pickColorDialog.hexChoosenColor.length() > 0){
                    self.colorField.setText(pickColorDialog.hexChoosenColor);
                } else {
                    self.colorField.setText("blue");
                }
            }
        });
    }//GEN-LAST:event_findColorButtonActionPerformed

    private void aFieldFocusLost(java.awt.event.FocusEvent evt) {//GEN-FIRST:event_aFieldFocusLost
        // TODO add your handling code here:
        this.validateKeyTyped();
    }//GEN-LAST:event_aFieldFocusLost

    private void bFieldFocusLost(java.awt.event.FocusEvent evt) {//GEN-FIRST:event_bFieldFocusLost
        // TODO add your handling code here:
        this.validateKeyTyped();
    }//GEN-LAST:event_bFieldFocusLost

    private void cFieldFocusLost(java.awt.event.FocusEvent evt) {//GEN-FIRST:event_cFieldFocusLost
        // TODO add your handling code here:
        this.validateKeyTyped();
    }//GEN-LAST:event_cFieldFocusLost

    private void dFieldFocusLost(java.awt.event.FocusEvent evt) {//GEN-FIRST:event_dFieldFocusLost
        // TODO add your handling code here:
        this.validateKeyTyped();
    }//GEN-LAST:event_dFieldFocusLost

    private void eFieldFocusLost(java.awt.event.FocusEvent evt) {//GEN-FIRST:event_eFieldFocusLost
        // TODO add your handling code here:
        this.validateKeyTyped();
    }//GEN-LAST:event_eFieldFocusLost

    private void submitButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_submitButtonActionPerformed
        // TODO add your handling code here:
        // Its not necessary to invoke the function this.validateKeyTyped(). That function will be invoked when  
        // any of JTextFields in parametersPanel lose focus. 
    }//GEN-LAST:event_submitButtonActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Inputs.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Inputs.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Inputs.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Inputs.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the dialog */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                Inputs dialog = new Inputs(new javax.swing.JFrame(), true,"");
                dialog.addWindowListener(new java.awt.event.WindowAdapter() {
                    @Override
                    public void windowClosing(java.awt.event.WindowEvent e) {
                        System.exit(0);
                    }
                });
                dialog.setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JTextField aField;
    private javax.swing.JLabel aLabel;
    private javax.swing.JTextField bField;
    private javax.swing.JLabel bLabel;
    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.ButtonGroup buttonGroup2;
    private javax.swing.ButtonGroup buttonGroup3;
    private javax.swing.ButtonGroup buttonGroup4;
    private javax.swing.ButtonGroup buttonGroup5;
    private javax.swing.JTextField cField;
    private javax.swing.JLabel cLabel;
    private javax.swing.JLabel choosePlotTypeLabel;
    private javax.swing.JTextField colorField;
    private javax.swing.JPanel colorPanel;
    private javax.swing.JRadioButton cubicChoosen;
    private javax.swing.JTextField dField;
    private javax.swing.JLabel dLabel;
    private javax.swing.JTextField eField;
    private javax.swing.JLabel eLabel;
    private javax.swing.JLabel errorLabel;
    private javax.swing.JButton findColorButton;
    private javax.swing.JLabel getColor;
    private javax.swing.JLabel getParamsLabel;
    private javax.swing.JLabel jLabel14;
    private javax.swing.JRadioButton jRadioButton2;
    private javax.swing.JRadioButton lineChoosen;
    private javax.swing.JRadioButton parabolChoosen;
    private javax.swing.JPanel parametersPanel;
    private javax.swing.JPanel plotTypePanel;
    private javax.swing.JRadioButton quarticChoosen;
    private javax.swing.JButton submitButton;
    private javax.swing.JLabel titlePanel;
    // End of variables declaration//GEN-END:variables
}
