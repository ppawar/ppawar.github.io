import java.util.*;
import java.util.stream.Collectors;
import java.util.function.BiFunction;
import java.util.function.Function;
import static java.util.stream.Collectors.counting;
/**
 *
 * @author SUNY Korea CS
 */
public class MathLib {
    public static double mean(Number... list){
        if (list.length == 0) {
            return Double.NaN;
        }
        final double average = Arrays.stream(list).mapToDouble((x) -> x.doubleValue()).summaryStatistics().getAverage();
        return average;
    }

    public static double variance(Number... list){
        if (list.length == 0) {
            return Double.NaN;
        }
        final double average = Arrays.stream(list).mapToDouble((x) -> x.doubleValue()).summaryStatistics().getAverage();
        final double sum = Arrays.stream(list).mapToDouble((x) -> Math.pow(x.doubleValue() - average,2.0)).sum();
        return (sum / (list.length - 1));
    }
   
    public static double stdev(Number... list){
        if (list.length == 0) {
            return Double.NaN;
        }
        final double average = Arrays.stream(list).mapToDouble((x) -> x.doubleValue()).summaryStatistics().getAverage();
        final double sum = Arrays.stream(list).mapToDouble((x) -> Math.pow(x.doubleValue() - average,2.0)).sum();
        return Math.sqrt(sum / (list.length - 1));
    }
    
    public static double median(Integer[] values) {
        Comparator<Integer> sortByNumber = (Integer n1, Integer n2) -> (n1.compareTo(n2));
        Arrays.sort(values, sortByNumber);
        double median;
        int totalElements = values.length;
        if (totalElements % 2 == 0) {
            int sumOfMiddleElements = values[totalElements / 2] + values[totalElements / 2 - 1];
            median = ((double) sumOfMiddleElements) / 2;
        } else {
            median = (double) values[values.length / 2];
        }
        return median;
    }
    
    public static double mode(Integer[] sequence)
    {  //double ans= 0;
        Map<Integer, Long> mode = Arrays.stream(sequence).collect(Collectors.groupingBy(Function.identity(), counting()));
        double ans = mode.entrySet().stream().max((first, second) -> {return (int) (first.getValue() - second.getValue());}).get().getKey();
        return ans;
    }
    
    public static double percent(Integer[] values){
        Integer fromYear = values[0];
        Integer toYear = values[values.length - 1];
        BiFunction<Integer, Integer, Integer> change = (a, b) -> a - b;
        double changenum = change.apply(toYear, fromYear);
        return changenum / fromYear * 100;
    }
    
            public static void main(String[] args) {
            // Create an ArrayList
            List<Integer> myList = new ArrayList<Integer>();
            myList.add(1);
            myList.add(5);
            myList.add(5);
            myList.add(5);
            myList.add(5);
            myList.add(8);
            myList.add(8);
            myList.add(8);
            MathLib ml = new MathLib();
            Integer[] itemsArray = new Integer[myList.size()];
            itemsArray = myList.toArray(itemsArray);
            System.out.println(ml.mode(itemsArray));
        }
}
