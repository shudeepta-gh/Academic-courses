import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number:");
    int number = sc.nextInt();
    int divisor = 0;
    for(int count=1;count<=number;count++)
    {
      if(number%count==0)
      {
        divisor++;
      }
    }
    if(divisor==2)
    {
      System.out.println(number+" is a prime number");
    }
  }
}
