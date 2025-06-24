import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the height of the triangle:");
    int height = sc.nextInt();
    for(int count=1;count<=height;count++)
    {
      for(int gap=1;gap<=(height-count);gap++)
      {
        System.out.print(" ");
      }
      for(int counter=1;counter<=(2*count)-1;counter++)
      {
        System.out.print(counter);
      }


    System.out.println();

    }

  }
}
