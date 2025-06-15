import java.util.Scanner;
  public class Test
  {
    public static void main(String [] args)
    {
      Scanner sc = new Scanner(System.in);
      System.out.print("Enter the value of a in the picture:");
      int a = sc.nextInt();
      System.out.print("Enter the value of b in the picture:");
      int b = sc.nextInt();
      double s= Math.sqrt(Math.pow(a/2,2)+Math.pow(b,2));
      double area = (3*Math.sqrt(3)/2)*Math.pow(s,2);
      double circumferance = 6*s;
      System.out.printf("Area: %.2f", area);
      System.out.printf("\nCircumferance: %.2f", circumferance);
    }
  }
