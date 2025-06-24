import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {

    String total_tax = calcYearlyTax();
    System.out.println(total_tax);


  }
  public static double calcTax(int age,int salary)
  {
    double tax = 0.0;
    if(age<18)
    {
      tax+=0.0;
    }
    else if(age>18)
    {
      if(salary<10000)
      {
        tax+=0.0;
      }
      else
      {
        if(10000<=salary && salary<=20000)
        {
          tax += salary*(7.0/100.0);
        }
        else if(salary>20000)
        {
          tax+= salary*(14.0/100.0);
        }
      }
    }
    return tax;
  }
  public static String calcYearlyTax()
  {
    String chart = "";
    double total_tax = 0.0;
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter your age:");
    int age = sc.nextInt();
    for(int i=1;i<=12;i++)
    {
      System.out.print("Enter your salary:");
      int salary = sc.nextInt();
      double tax = calcTax(age,salary);
      total_tax+=tax;
      chart+= "Month"+i+" tax: "+String.format("%.1f",tax)+"\n";
    }
    chart+="Total Yearly Tax: "+String.format("%.1f",total_tax);
    return chart;
  }

}
