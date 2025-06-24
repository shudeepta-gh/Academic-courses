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
      original_array[index] = sc.nextInt();
    }
    System.out.println("Original array:");
    for(int index=0;index<original_array.length;index++)
    {
       System.out.print(original_array[index]+" ");
    }
    System.out.println();


    for(int index=0;index<original_array.length;index++)
    {
      if(original_array[index]>0 && original_array[index]!=0)
      {
        original_array[index]=1;
      }
      else if(original_array[index]<0 && original_array[index]!=0)
      {
        original_array[index]=0;
      }
    }
    System.out.println("After modifying: ");
    for(int index=0;index<original_array.length;index++)
    {
       System.out.print(original_array[index]+" ");
    }
    System.out.println();

  }
}
