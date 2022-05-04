/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cmdpackage;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Base64;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author USER
 */
public class CMDinvoker {
    private String pythonCommand;
    
    public CMDinvoker(String jsonData) {
        String jsonEncoded = Base64.getEncoder().encodeToString(jsonData.getBytes());
        this.pythonCommand = "cd.. && py python/invokedByUI.py -d " + jsonEncoded ;
        System.out.println(this.pythonCommand);
    }
    
    public void run(){
        try{
            Process process = Runtime.getRuntime().exec("cmd /c \"" + this.pythonCommand+"\"");
            process.waitFor();
            BufferedReader reader=new BufferedReader(
                new InputStreamReader(process.getInputStream())
            ); 
            String line; 
            while((line = reader.readLine()) != null) 
            { 
                System.out.println(line);
            } 
        } catch (IOException ex) {
            Logger.getLogger(CMDinvoker.class.getName()).log(Level.SEVERE, null, ex);
        } catch (InterruptedException ex) {
            Logger.getLogger(CMDinvoker.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    
    
    /**
     * This main function is just used for running demo & test
     * @param args 
     */
    public static void main(String[] args) {
//        System.out.println(System.getProperty("user.dir"));
        try {
            Process process = Runtime.getRuntime().exec("cmd /c \"cd.. && py python/demo.py\"");
            process.waitFor();
//            BufferedReader reader=new BufferedReader(
//                new InputStreamReader(process.getInputStream())
//            ); 
//            String line; 
//            while((line = reader.readLine()) != null) 
//            { 
//                System.out.println(line);
//            } 
        } catch (IOException ex) {
            Logger.getLogger(CMDinvoker.class.getName()).log(Level.SEVERE, null, ex);
        } catch (InterruptedException ex) {
            Logger.getLogger(CMDinvoker.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
