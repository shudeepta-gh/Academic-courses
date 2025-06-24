import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("What is the first string you want to enter?:");
    String first_string = sc.nextLine();
    int f_length = first_string.length();
    System.out.print("Write down the second string you want to enter:");
    String second_string = sc.nextLine();
    int s_length = second_string.length();
    String final_string="";
    for(int f_index=0;f_index<f_length;f_index++)
    {
      int count = 0;
      char f_character = first_string.charAt(f_index);
      for(int s_index=0;s_index<s_length;s_index++)
      {
        char s_character = second_string.charAt(s_index);
        if(f_character!=s_character)
        {
          count+=1;
        }
      }
      if(count==s_length)
      {
        char uppercase = (char)((int)f_character-32);
        final_string+= Character.toString(uppercase);
      }
    }
    for(int s_index=0;s_index<s_length;s_index++)
    {
      int count = 0;
      char s_character = second_string.charAt(s_index);
      for(int f_index=0;f_index<f_length;f_index++)
      {
        char f_character = first_string.charAt(f_index);
        if(s_character!=f_character)
        {
          count+=1;
        }
      }
      if(count==f_length)
      {
        char uppercase = (char)((int)s_character-32);
        final_string+= Character.toString(uppercase);
      }
    }

    System.out.println(final_string);

  }
}
