import java.util.Scanner;
  public class Test
  {
    public static void main(String [] args)
    {
      Scanner sc = new Scanner(System.in);
      System.out.print("Write your student id:");
      int student_id = sc.nextInt();
      int last_2_digits = student_id%100;
      int last_digit= last_2_digits%10;
      int second_last_digit= last_2_digits/10;
      System.out.println(last_digit + "" + second_last_digit);
    }
  }
