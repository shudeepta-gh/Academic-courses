import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number of test cases N:");
    int test_cases = sc.nextInt();
    for(int count=1;count<=test_cases;count++)
    {
      System.out.print("Enter the starting number X:");
      int X = sc.nextInt();
      System.out.print("Enter the number of odd numbers Y:");
      int Y = sc.nextInt();
      int counter = 0;
      int sum = 0;
      for(int start=X;counter<Y;start++)
      {
        if(start%2!=0)
        {
          sum+=start;
          counter++;
        }
      }
      System.out.println(sum);
    }

  }
}
