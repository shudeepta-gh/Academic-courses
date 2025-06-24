import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the length of the array:");
    int N = sc.nextInt();
    int [] original_array = new int [N];
    for(int index=0;index<original_array.length;index++)
    {
      System.out.println("Enter a number");
      original_array[index]=sc.nextInt();
    }

    int [] new_array = new int [N];
    for(int i=original_array.length-1;i>-1;i--)
    {
      new_array[new_array.length-1-i]=original_array[i];
    }
    System.out.println("Reversed using a new array:");
    for(int i=0;i<new_array.length;i++)
    {
      System.out.print(new_array[i]+" ");
    }

    for(int i=0;i<original_array.length-1;i++)
    {
      for(int j=0;j<original_array.length-i-1;j++)
      {
        int temp = original_array[j];
        original_array[j]=original_array[j+1];
        original_array[j+1]=temp;
      }

    }
    System.out.println();
    System.out.println("Reversed the original array:");
    for(int i=0;i<original_array.length;i++)
    {
      System.out.print(original_array[i]+" ");
    }
  }
}
