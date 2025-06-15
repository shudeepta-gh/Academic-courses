import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the first number: ");
    int fnum = sc.nextInt();
    System.out.println("Enter the second number: ");
    int snum = sc.nextInt();
    System.out.println("Enter the third number: ");
    int tnum = sc.nextInt();

    if(fnum>snum)
    {
      if (fnum>tnum)
      {
        System.out.printf("largest number: %d",fnum);
      }

      else
      {
        System.out.printf("largest number: %d",tnum);
      }
    }

    else
    {
      if (snum>tnum)
        {
        System.out.printf("largest number: %d",snum);
      }

      else
      {
        System.out.printf("largest number: %d",tnum);
      }
    }
  }
}
