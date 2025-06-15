import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the year: ");
    int year = sc.nextInt();

    if(year%100!=0)
    {
      if(year%4==0)
      {
        System.out.printf("%d is a leap year", year);
      }
      else
      {
        System.out.printf("%d is not a leap year", year);
      }
    }
    else if(year%100==0)
    {
      if(year%400==0 && year%4==0)
      {
        System.out.printf("%d is a leap year",year);
      }
      else
      {
        System.out.printf("%d is not a leap year",year);
      }
    }

  }
}
