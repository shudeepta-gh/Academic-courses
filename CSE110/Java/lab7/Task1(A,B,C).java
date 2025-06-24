import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number you want to check:");
    int number = sc.nextInt();
    String sequence = sequence(number);
    System.out.println(sequence);

  }



  public static String evenChecker(int num)
  {
    if(num%2==0)
    {
      return "Even!!";
    }
    else
    {
      return "Odd!!";
    }
  }

  public static boolean isEven(int num)
  {
    String result = evenChecker(num);
    if (result=="Even!!")
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  public static boolean isPos(int num)
  {
    if(num>0)
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  public static String sequence(int num)
  {
    String numbers = "";
    if(isPos(num)==true)
    {
      for(int i = 0;i<=num;i++)
      {
        if(isEven(i)==true)
        {
          numbers+=(Integer.toString(i)+" ");
        }

      }
    }
    else
    {
      for(int i = num;i<0;i++)
      {
        if(isEven(i)==false)
        {
          numbers+=(Integer.toString(i)+" ");
        }
      }
    }
    return numbers;
  }
}
