import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("What is the string you want to give?:");
    String input_string = sc.nextLine();
    int length = input_string.length();
    String final_string = "";
    String temporary_str="";
    for(int index=length-1;index>-1;index-=1)
    {
      char each_character = input_string.charAt(index);

      if(each_character==' ')
      {
        for(int i=final_string.length()-1;i>-1;i-=1)
        {
          temporary_str+=Character.toString(final_string.charAt(i));
        }

        final_string="";
        System.out.print(temporary_str+" ");
        temporary_str="";

      }

      else
      {
        final_string+=Character.toString(each_character);
      }

    }
    for (int i = final_string.length() - 1; i >= 0; i--)
    {
       temporary_str += Character.toString(final_string.charAt(i));
    }

    System.out.print(temporary_str+" ");
  }
}
