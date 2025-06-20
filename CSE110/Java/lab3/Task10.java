import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number: ");
    int number = sc.nextInt();
    for(int count=0;count<=number;count++)
    {
      if(count%5==0 && count%3!=0)
      {
        System.out.println(count);
      }
    }

  }
}
