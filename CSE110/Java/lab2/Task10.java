import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the first side of the triangle:");
    int a = sc.nextInt();
    System.out.println("Enter the second side of the triangle:");
    int b = sc.nextInt();
    System.out.println("Enter the third side of the triangle:");
    double c = sc.nextDouble();

    if(a==b && b==c)
    {
      System.out.println("This is a Equilateral triangle");
    }
    else if(a==b || b==c || c==a)
    {
      System.out.println("This is a Isosceles triangle");
    }
    else if(a!=b && b!=c && c!=a)
    {
      System.out.println("This is a Scalene triangle");
    }
  }
}
