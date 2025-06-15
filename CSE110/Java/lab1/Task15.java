//With Usig third variable

import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter integer number 1:");
    int a = sc.nextInt();
    System.out.print("Enter integer number 2:");
    int b = sc.nextInt();
    System.out.println("Before swap: a="+ a + " b="+b);

    int temp=a;
    a=b;
    b=temp;
    System.out.println("After swap: a="+ a + " b="+b);

  }
}
