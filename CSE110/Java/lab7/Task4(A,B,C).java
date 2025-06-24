import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number:");
    int number = sc.nextInt();
    int result = special_sum(number);
    System.out.println(result);

  }
  public static boolean isPrime(int number)
  {
    int count = 0;
    for(int i=1;i<=number;i++)
    {
      if(number%i==0)
      {
        count++;
      }
    }
    if(count<=2)
    {
      return true;
    }
    else
    {
      return false;
    }
  }

  public static boolean isPerfect(int number)
  {
    int sum = 0;
    for(int i=1;i<number;i++)
    {
      if(number%i==0)
      {
        sum+=i;
      }
    }
    if(sum==number)
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  public static int special_sum(int number)
  {
    int sum=0;
    for(int i=2;i<=8;i++)
    {
      if(isPrime(i)==true || isPerfect(i)==true)
      {
        sum+=i;
      }
    }
    return sum;
  }


}
