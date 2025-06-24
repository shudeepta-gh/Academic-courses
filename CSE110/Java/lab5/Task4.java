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
    for(int index=length-1;index>=0;index-=1)
    {
      char each_character = input_string.charAt(index);

      final_string+=Character.toString(each_character);

    }
    System.out.println(final_string);

  }
}
