import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the number: ");
    int num = sc.nextInt();


    if(num%2==0)
    {
      if (num>0)
      {
        System.out.println("Number is positive and even");
      }

      else if(num<0)
      {
        System.out.println("Number is negative");
      }

      else
      {
        System.out.println("Number is zero");
      }
    }

    else
    {

     if (num>0)
      {
        System.out.println("Number is positive and odd");
      }

      else if(num<0)
      {
        System.out.println("Number is negative");
      }

      else
      {
        System.out.println("Number is zero");
      }
    }
  }
}
