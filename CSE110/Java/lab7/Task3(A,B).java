import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the first side of the trangle:");
    int f_side = sc.nextInt();

    System.out.print("Enter the second side of the triangle:");;
    int s_side = sc.nextInt();

    System.out.print("Enter the third side of the traingle:");
    int t_side = sc.nextInt();
    double res = triArea(f_side,s_side,t_side);
    if(res==-1)
    {
      System.out.println("Can't form a triangle");
    }
    else
    {
      System.out.printf("%.3f",res);
    }
  }
  public static boolean isTriangle(int a,int b,int c)
  {
    if(a+b>c && b+c>a && c+a>b)
    {
      return true;
    }
    else
    {
      return false;
    }
  }

  public static double triArea(int a, int b, int c)
  {
    double s =(a+b+c)/2;
    if(isTriangle(a,b,c)==true)
    {
      double area = Math.sqrt(s*(s-a)*(s-b)*(s-c));
      return area;
    }
    else
    {
      return -1.0;
    }

  }
}
