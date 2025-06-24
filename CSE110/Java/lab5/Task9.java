import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("What is your password?:");
    String input_password = sc.nextLine();
    int length = input_password.length();
    int uppercase=0;
    int lowercase=0;
    int digits=0;
    int special_char=0;
    for(int index=0;index<length;index++)
    {
      char each_character = input_password.charAt(index);
      int ascii_value = (int)each_character;
      if(65<=ascii_value && ascii_value<=90)
      {
        uppercase+=1;
      }
      else if(97<=ascii_value && ascii_value<=122)
      {
        lowercase+=1;
      }
      else if(48<=ascii_value && ascii_value<=57)
      {
        digits+=1;
      }
      else
      {
        special_char+=1;
      }
    }

    if(lowercase>=1 && uppercase>=1 && digits>=1 && special_char>=1)
    {
      System.out.println("True");
    }
    else
    {
      System.out.println("False");
    }
  }
}
