import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number:");
    int number = sc.nextInt();
    int sum = 0;
    for(int count=1;count<=number;count++)
    {
      if(number%count==0)
      {
        if(count!=number)
        {
          sum+=count;
        }
      }
    }
    if(sum==number)
    {
      System.out.println(number+" is a perfect number");
    }
  }
}
