import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the student ID:");
    int student_id = sc.nextInt();
    int first_3_digit =  student_id/100000;
    int year = first_3_digit/10;
    int session = first_3_digit%10;

    if(session==1)
    {
      System.out.println("Student Joined BRAC in Spring "+ year);
    }
    else if(session==2)
    {
      System.out.println("Student Joined BRAC in Fall "+ year);
    }
    else if(session==3)
    {
      System.out.println("Student Joined BRAC in Summer "+ year);
    }

  }
}
