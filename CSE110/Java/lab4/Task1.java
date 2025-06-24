import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("How many inputs do you want to put?");
    int input_number = sc.nextInt();
    int max = 0;
    int min = 0;
    for(int count=1;count<=input_number;count++)
    {
      System.out.print("Enter the sample input");
      int sample_input = sc.nextInt();
      if(sample_input>0 && (sample_input%2==0))
      {
        if(sample_input>max)
        {
          max=sample_input;
        }
        else
        {
          min=sample_input;
        }
      }

    }
    int average = (max+min)/2;
    System.out.println("Max:"+max);
    System.out.println("Min:"+min);
    System.out.println("Average:"+average);
  }
}
