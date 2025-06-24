import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the string:");
    String input_string = sc.nextLine();
    int length = input_string.length();
    int count = 0;
    for(int index = 0;index<length;index++)
    {
      char each_character=input_string.charAt(index);

      char character_backward=input_string.charAt((length-1)-index);

      if(each_character==character_backward)
      {
        count++;
      }
    }

    if(count==length)
    {
      System.out.println(true);
    }
    else
    {
      System.out.println(false);
    }
  }
}
