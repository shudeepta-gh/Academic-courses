import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number: ");
    int number = sc.nextInt();

    while(number>0)
    {

      int remainder = number%10;
      number=number/10;

      if(number%10!=0)
      {
        System.out.print(remainder+",");
      }
      else
      {
        System.out.println(remainder);
      }
    }

  }
}
