import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the given number: ");
    int number = sc.nextInt();
    int total_divisor = 0;
    System.out.println("Divisor of" + number + ": ");
    for(int count=1;count<=number;count++)
    {
      if(number%count==0)
      {
        System.out.println(count);
        total_divisor+=1;
      }

    }
    System.out.println("Total Divisors:" + total_divisor);
  }
}
