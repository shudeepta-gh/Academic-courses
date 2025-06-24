import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("What is the password?:");
    String input_string = sc.nextLine();
    int length = input_string.length();
    String final_string = "";
    String vowel ="AEIOU";

    int length_vowel=vowel.length();
    int vowel_count = 0;
    int consonant_count = 0;
    for(int index = 0;index<length;index++)
    {
      char input_str_char= input_string.charAt(index);
      int con_string = (int)input_str_char;
      if((65<=con_string  && 90>=con_string) || (97<=con_string && 122>=con_string))
      {
        boolean isVowel = false;
        for(int vowel_index=0;vowel_index<length_vowel;vowel_index++)
        {
           char large_vowel=vowel.charAt(vowel_index);
           int convert =(int)large_vowel+32;
           char small_vowel=(char)convert;

           if(input_str_char==large_vowel || input_str_char==small_vowel)
           {
             vowel_count++;
             isVowel = true;
             break;

           }
        }
        if(!isVowel)
        {
          consonant_count++;
        }
      }
    }

    if(vowel_count>0 && consonant_count>0)
    {
       if(vowel_count%3==0 && consonant_count%5==0)
       {
         System.out.println("Aaarr! Me Plunder!!");
       }

       else
       {
         System.out.println("Blimey! No Plunder!!");
       }
    }
    else
    {

       System.out.println("Blimey! No Plunder!!");
    }

  }
}
