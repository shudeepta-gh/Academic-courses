import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("What is the value of N?");
    int input_number = sc.nextInt();
    int total_sum = 0;
    for(int count=1;count<=input_number;count++)
    {
      int sum=0;
      for(int counter=1;counter<=count;counter++)
      {
        sum+=counter;
      }
      total_sum+=(sum*-1);
    }
    System.out.println("The value of y: "+total_sum);
  }
}
