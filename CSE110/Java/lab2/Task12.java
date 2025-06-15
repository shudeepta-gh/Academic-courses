import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the first number:");
    int fnum = sc.nextInt();
    System.out.println("Enter the Enter the second number:");
    int snum =sc.nextInt();
    System.out.println("Enter the Enter the third number:");
    int tnum =sc.nextInt();

    if(fnum==snum && snum==tnum && fnum==tnum)
    {
      System.out.print("All numbers are equal");
    }
    else if(fnum!=snum && snum!=tnum && fnum!=tnum)
    {
      System.out.println("All numbers are different");
    }
    else
    {
      System.out.println("Neither all are equal or different");

    }
  }
}
