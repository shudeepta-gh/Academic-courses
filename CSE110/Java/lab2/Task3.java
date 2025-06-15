import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the number: ");
    int number = sc.nextInt();
    if(number%5 == 0 && number%7==0)
    {
      System.out.println("Divisible by both");
    }

    else if(number%5==0)
    {
      System.out.println("Invalid: Divisible by 5 only");
    }
    else if (number%7==0)
    {
      System.out.println("Invalid: Divisible by 7 only");
    }
    else
    {
      System.out.println("No");
    }
  }
}
