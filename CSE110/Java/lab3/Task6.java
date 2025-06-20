import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the value of n: ");
    int n = sc.nextInt();
    int sum = 0;
    for(int count= 1;count<=n;count+=1)
    {
      int number = (int) Math.pow(count,2);
      if (number%2==0)
      {
        number = number*(-1);
      }
      sum += number;
    }
    System.out.println(sum);

  }
}
