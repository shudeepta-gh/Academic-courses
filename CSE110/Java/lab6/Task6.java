import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the length of the array:");
    int N = sc.nextInt();
    double [] array = new double [N];


    for(int index = 0;index<array.length;index++)
    {
      System.out.println("Enter a number:");
      array[index] = sc.nextDouble();
    }
    double maximum_num = -999999999.0;
    double minimum_num = 999999999.0;
    double sum = 0;
    int maximum_num_ind = 0;
    int minimum_num_ind = 0;
    for(int index = 0;index<array.length;index++)
    {
      sum += array[index];

      if(array[index]>maximum_num)
      {
        maximum_num = array[index];
        maximum_num_ind = index;
      }
      else
      {
        if(array[index]<minimum_num)
        {
           minimum_num = array[index];
           minimum_num_ind = index;
        }
      }

    }
    double average = sum/N;
    System.out.println("Maximum element "+maximum_num+" found at index "+maximum_num_ind);
    System.out.println("Minimum element "+minimum_num+" found at index "+minimum_num_ind);
    System.out.println("Summation: "+sum);
    System.out.println("Average: "+average);
  }
}
