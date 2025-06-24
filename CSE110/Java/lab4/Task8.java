import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the length of the rectangular:");
    int length = sc.nextInt();
    System.out.print("Enter the width of the rectangular:");
    int width = sc.nextInt();
    for(int count=1;count<=width;count++)
    {
      for(int counter=1;counter<=length;counter++)
      {
        System.out.print(counter+" ");
      }
      System.out.println("");
    }

  }
}
