import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the mark: ");
    int mark = sc.nextInt();
    String grade = "Your grade is ";
    if(90<=mark && mark<=100)
    {
      System.out.println(grade + "A");
    }
    else if(85<=mark && mark<=89)
    {
      System.out.println(grade + "A-");
    }
    else if(70<=mark && mark<=84)
    {
      System.out.println(grade + "B");
    }
    else if(57<=mark && mark<=69)
    {
      System.out.println(grade + "C");
    }
    else if(50<=mark && mark<=56)
    {
      System.out.println(grade + "D");
    }
    else if(mark<50)
    {
      System.out.println(grade + "F");
    }
  }
}
