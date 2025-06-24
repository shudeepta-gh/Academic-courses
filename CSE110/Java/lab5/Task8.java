import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    String input = sc.nextLine();
    String output = "";
    boolean toLower = true;
    for(int index=0; index<input.length(); index++)
    {
      char ch = input.charAt(index);
      if((ch>='A' && ch<='Z')||(ch>='a' && ch<='z'))
      {
        if(toLower)
        {
          if(ch>= 'A' && ch<= 'Z')
          {
            ch = (char)(ch+32);
          }
        }
        else
        {
          if(ch>='a' && ch<='z')
          {
            ch = (char)(ch-32);
          }
        }
        toLower = !toLower;
      }
      output += ch;
    }
    System.out.println(output);
  }
}
