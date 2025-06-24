import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the number n:");
    int n = sc.nextInt();
    int x = sumDigits(n);

    System.out.println(x);
  }
  public static int sumDigits(int n)
  {
    if(n==0)
    {
      return 0;
    }
    int last_digit = n%10;

    return last_digit+sumDigits(n/10);
  }
}
