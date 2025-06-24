import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("How many inputs do you want to put?");
    int input_number = sc.nextInt();
    int non_negative_num=0;
    int negative_num=0;

    for(int count=1;count<=input_number;count++)
    {

      System.out.print("Enter number "+count+" :");
      int sample_input = sc.nextInt();
      if(sample_input>=0)
      {
        non_negative_num++;
      }
      else if(sample_input<1)
      {
        negative_num++;
      }
    }
    System.out.println(non_negative_num+" Non-negative Numbers");
    System.out.println(negative_num+" Negative Numbers");
  }
}
