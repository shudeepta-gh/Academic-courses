import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the first number:");
    double fnum = sc.nextDouble();
    System.out.println("Enter the second number:");
    double snum = sc.nextDouble();
    System.out.println("Enter the third number:");
    double tnum = sc.nextDouble();

    if(fnum>snum && fnum>tnum)
    {
      System.out.println("Maximum number is "+fnum);
      if(snum>tnum)
      {
       System.out.println("Minimum number is "+tnum);
      }
      else
      {
        System.out.println("Minimum number is "+snum);
      }
    }
    else if (snum>fnum && snum>tnum)
    {
      System.out.println("Maximum number is "+snum);
      if(fnum>tnum)
      {
       System.out.println("Minimum number is "+tnum);
      }
      else
      {
        System.out.println("Minimum number is "+fnum);
      }
    }
    if(tnum>fnum && tnum>snum)
    {
      System.out.println("Maximum number is "+tnum);
      if(fnum>snum)
      {
       System.out.println("Minimum number is "+snum);
      }
      else
      {
        System.out.println("Minimum number is "+fnum);
      }
    }
  }
}
