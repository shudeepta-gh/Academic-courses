import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    for(int count=1;;count++)
    {

      System.out.print("Enter the sample input");
      int sample_input = sc.nextInt();
      if(sample_input>0)
      {
        int square_number = (int) Math.pow(sample_input,2);
        System.out.println(square_number);
      }
      else
      {
        break;
      }
    }

  }
}
