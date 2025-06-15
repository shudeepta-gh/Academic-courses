import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter your salary:");
    int salary = sc.nextInt();
    System.out.println("Enter your age:");
    int age = sc.nextInt();
    int tax_amount=0;
    if(age<18)
    {
      tax_amount+=0;
    }
    else
    {
      if(salary<10000)
      {
        tax_amount+=0;
      }
      else if((salary==10000 || salary>10000)&& salary<20000)
      {
        tax_amount+= (int) (salary*(5.0/100));
      }
      else if(salary>20000)
      {
        tax_amount+=(int) (salary*(10.0/100));
      }
    }

    System.out.printf("Your tax amounts in %d Tk",tax_amount);
  }
}
