import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter an integer:");
    int number = sc.nextInt();
    int last2digits = number%100;
    System.out.println("The last digit of the integer is: " + last2digits);
  }
}
