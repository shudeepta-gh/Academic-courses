import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {

    Scanner sc = new Scanner(System.in);
    for(int count=1;;count++)
    {
      System.out.print("Enter Number:");
      int input_number = sc.nextInt();

      if(input_number%2==0)
      {
        int counter = 0;
        for(int divisor=1;divisor<=input_number;divisor++)
        {
          if(input_number%divisor==0)
          {
             counter+=1;
          }
        }
        System.out.println(input_number+" has "+counter+" divisors");
      }
      else
      {
        break;
      }
    }

  }
}
