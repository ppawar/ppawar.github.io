package edu.sunyk.cse216.statistics;

import java.util.Arrays;

/**
 *
 * @author SUNY Korea CS
 */
public class MathLib {
    //Calculate standard deviation
    public static double mean(int[] list){
        double sum = 0.0;
        double mean = 0.0;
        for (int i : list) {
            sum+=i;
        }
        mean = sum/list.length;
        return mean;
    }

    //Calculate variance
    public static double variance(int[] list){
        double sum = 0.0;
        double mean = 0.0;
        double num=0.0;
        double numi = 0.0;
        for (int i : list) {
            sum+=i;
        }
        mean = sum/list.length;
        for (int i : list) {
            numi = Math.pow(((double) i - mean), 2);
            num+=numi;
        }
        return (num/list.length);
    }
    
    //Calculate standard deviation
    //Taken from: https://stackoverflow.com/questions/1735870/simple-statistics-java-packages-for-calculating-mean-standard-deviation-etc
    public static double stdev(int[] list){
        double sum = 0.0;
        double mean = 0.0;
        double num=0.0;
        double numi = 0.0;
        for (int i : list) {
            sum+=i;
        }
        mean = sum/list.length;
        for (int i : list) {
            numi = Math.pow(((double) i - mean), 2);
            num+=numi;
        }
        return Math.sqrt(num/list.length);
    }
    
    //Calculate median: code taken from https://codippa.com/how-to-calculate-median-from-array-values-in-java/
    public static double median(int[] values) {
        // sort array
        Arrays.sort(values);
        double median;
        // get count of scores
        int totalElements = values.length;
        // check if total number of scores is even
        if (totalElements % 2 == 0) {
            int sumOfMiddleElements = values[totalElements / 2] + values[totalElements / 2 - 1];
            // calculate average of middle elements
            median = ((double) sumOfMiddleElements) / 2;
        } else {
            // get the middle element
            median = (double) values[values.length / 2];
        }
        return median;
    }
    
    //Calculate mode. Code taken from https://www.sanfoundry.com/java-program-find-mode-data-set/
    public static double mode(int[] sequence) 
    {
        int maxValue = 0, maxCount = 0;
        for (int i = 0; i < sequence.length; ++i) 
        {
            int count = 0;
            for (int j = 0; j < sequence.length; ++j) 
            {
                if (sequence[j] == sequence[i])
                    ++count;
            }
            if (count > maxCount) 
            {
                maxCount = count;
                maxValue = sequence[i];
            }
        }
         return maxValue;
    }
}
