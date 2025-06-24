import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the radius:");
    int radius = sc.nextInt();
    sc.nextLine();
    System.out.print("Enter the shape name:");
    String shape = sc.nextLine();
    double result = findSpace(radius,shape);
    if(result==-1.0)
    {
      System.out.println("Wrong Parameter");
    }
    else
    {
      System.out.printf("%.4f",result);
    }
  }

  public static double circleArea(int radius)
  {

    double area = Math.PI* Math.pow(radius,2);
    return area;
  }
  public static double sphereVolume(int radius)
  {
    double volume = 4.0/3.0*Math.PI*Math.pow(radius,3);
    return volume;
  }

  public static double findSpace(int r, String shape)
  {
    if(shape.equals("circle"))
    {
      double area = circleArea(r);
      return area;
    }
    else if(shape.equals("sphere"))
    {
      double volume = sphereVolume(r);
      return volume;
    }
    else
    {
      return -1.0;
    }
  }


}
