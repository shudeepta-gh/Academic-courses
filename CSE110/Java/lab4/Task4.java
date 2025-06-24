import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("How many inputs do you want to put?");
    int input_number = sc.nextInt();

    int count=0;
    for(int number=2;count<input_number;number++)
    {
      int counter = 0;
      for(int divisor=1;divisor<=number;divisor++)
      {
        if(number%divisor==0)
        {
          counter++;
        }
      }
      if(counter==2)
      {
        System.out.println(number);
        count++;
      }
    }

  }
}
