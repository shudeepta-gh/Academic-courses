import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number of terms");
    int number = sc.nextInt();
    int sum = 0;
    for(int current_num=1;current_num<=number;current_num++)
    {
      sum+=current_num;
      System.out.println("Current Number : " + current_num + ", Sum: "+sum);
    }

  }
}
