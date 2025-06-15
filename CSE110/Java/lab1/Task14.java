import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a value:");
    int value = sc.nextInt();
    double converted_value = (value*0.0254);
    System.out.println(value + " inch is " + converted_value + " meters");
  }
}
