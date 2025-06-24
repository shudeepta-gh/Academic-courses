import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the starting value:");
    int start = sc.nextInt();
    System.out.print("Enter the ending value:");
    int end = sc.nextInt();
    System.out.println("Armstrong numbers:");
    for(int number = start;number<=end;number++)
    {
      int sum = 0;
      String count = String.valueOf(number);
      for(int counter = 0;counter<count.length();counter++)
      {
        int digit = Character.getNumericValue(count.charAt(counter));
        sum+=(int) Math.pow(digit,count.length());
      }

      if(sum==number)
       {
          System.out.println(number);
       }

    }

  }
}
