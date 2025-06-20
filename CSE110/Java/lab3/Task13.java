import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number: ");
    int number = sc.nextInt();
    int total_digits=0;
    int given_value=number;
    while(given_value>0)
    {
      given_value = given_value/10;
      int remainder = given_value%10;
      total_digits++;

    }

    int power=1;
    for(int count=1;count<=(total_digits-1);count++)
    {
      power=power*10;
    }

    for(int counter=0;number>0;counter++)
    {
      int each_digit=number/power;
      number=number%power;
      power=power/10;

      if(power!=0)
      {
        System.out.print(each_digit+",");
      }
      else
      {
         System.out.println(each_digit);
      }
    }
  }
}
