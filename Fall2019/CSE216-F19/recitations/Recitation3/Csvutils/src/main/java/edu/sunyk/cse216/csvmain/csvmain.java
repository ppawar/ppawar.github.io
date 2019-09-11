/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.sunyk.cse216.csvmain;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author SUNY Korea CS
 */
public class csvmain {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
            csvmain csvReaderDemo = new csvmain();
            //csvReaderDemo.readCSVFile("resources/gdp_csv.csv");
            System.out.println("Arguments are: " + args[0]);
            csvReaderDemo.readCSVFile(args[0]);
    }
    
    public void readCSVFile(String fileName) {
        System.out.println("Reading file " + fileName);
        try {
        /* Write your implementation here */
        } catch (Exception ex) {
            Logger.getLogger(csvmain.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
}
