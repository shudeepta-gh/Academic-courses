import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the string:");
    String input_string = sc.nextLine();
    int length = input_string.length();
    String final_string = "";

    for(int index=0;index<length;index++)
    {
      char character = input_string.charAt(index);
      int convert = (int) character;

      if(97<=convert && convert<=122)
      {
        char converted_char = (char) (convert-32);
        final_string+= converted_char;

      }

      else
      {
        final_string+=character;
      }
    }
    System.out.println(final_string);

  }
}
