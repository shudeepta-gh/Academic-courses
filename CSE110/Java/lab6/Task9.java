import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);

    System.out.println("Enter the length of the array:");
    int N = sc.nextInt();
    int [] original_array = new int [N];
    for(int index = 0;index<original_array.length;index++)
    {
      System.out.print("Enter a number:");
      original_array[index]=sc.nextInt();

    }
    for(int index = 0;index<original_array.length;index++)
    {
      System.out.print(original_array[index]+" ");
    }
    for(int i = 0;i<original_array.length-1;i++)
    {
      int min_index = i;
      for(int j = i+1;j<original_array.length;j++)
      {
        if(original_array[j]>original_array[min_index])
        {
          min_index = j;
        }
      }
      int temp = original_array[min_index];
      original_array[min_index] = original_array[i];
      original_array[i]=temp;
    }
    System.out.println();
    System.out.println("Sorted Array:");

    for(int i=0;i<original_array.length;i++)
    {
      System.out.print(original_array[i]+" ");
    }
  }
}
