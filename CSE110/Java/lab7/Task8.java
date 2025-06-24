import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the number n:");
    int n = sc.nextInt();
    reverseDigits(n);
  }
  public static void reverseDigits(int n)
  {
    if(n==0)
    {
      return;
    }
    int last_digit = n%10;

    System.out.println(last_digit);
    reverseDigits(n/10);
  }
}
