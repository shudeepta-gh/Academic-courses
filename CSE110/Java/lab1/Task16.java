import java.util.Scanner;
  public class Test
  {
    public static void main(String [] args)
    {
      Scanner sc = new Scanner(System.in);
      System.out.print("Enter the minitues that you want to convert:");
      int minitues = sc.nextInt();
      int days = minitues/(60*24);
      int years = days/365;
      int rest_days = days%365;
      System.out.println(minitues + " minitues is approximately " + years + " years " +rest_days + " days");
    }
  }
