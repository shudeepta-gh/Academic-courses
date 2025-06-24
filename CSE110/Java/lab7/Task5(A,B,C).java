import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number:");
    int number = sc.nextInt();
    String result = showDiamond(number);
    System.out.println(result);

  }
  public static String showDots(int number)
  {
    String dots = "";
    for(int i=0;i<number;i++)
    {
      dots+=".";
    }
    return dots;
  }

  public static String show_palindrome(int number)
  {
    String sequence="";
    for(int i=1;i<=number;i++)
    {
      sequence+=Integer.toString(i);
    }
    for(int j =number-1;j>0;j--)
    {
      sequence+=Integer.toString(j);
    }
    return sequence;
  }

  public static String showDiamond(int number)
  {
    String diamond="";
    for(int i=1;i<=number;i++)
    {
      diamond+=showDots(number-i);
      diamond+=show_palindrome(i);
      diamond+=showDots(number-i);
      diamond+="\n";
    }
    for(int i=1;i<number;i++)
    {
      diamond+=showDots(i);
      diamond+=show_palindrome(number-i);
      diamond+=showDots(i);
      diamond+="\n";
    }
    return diamond;
  }

}
