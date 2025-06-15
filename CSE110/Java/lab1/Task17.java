import java.util.Scanner;
  public class Test
  {
    public static void main(String [] args)
    {
      Scanner sc = new Scanner(System.in);
      System.out.print("Enter the value of a:");
      int a = sc.nextInt();
      int b = sc.nextInt();
      int c = sc.nextInt();
      int d = (2*b*((c-a)/3))+7;


      System.out.println("Answer: "+ d);
    }
  }
