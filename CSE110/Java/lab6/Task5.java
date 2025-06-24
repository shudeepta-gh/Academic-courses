import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the length of the array:");
    int N = sc.nextInt();
    int [] array = new int [N];
    boolean element = true;

    for(int index = 0;index<array.length;index++)
    {
      System.out.println("Enter a number:");
      array[index] = sc.nextInt();
    }
    System.out.println("Enter another number:");
    int another_number = sc.nextInt();
    for(int index = 0;index<array.length;index++)
    {
      if(array[index]==another_number)
      {
        System.out.println(another_number+" is at index "+index);
        element = true;
        break;
      }
      else
      {
        element = false;
      }
    }
    if(element==false)
    {
      System.out.println("Element not found");
    }
  }
}
