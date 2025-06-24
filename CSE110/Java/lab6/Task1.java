import java.util.Scanner;
//import java.util.Arrays;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the length of the array:");
    int N = sc.nextInt();
    int [] initial_array  = new int [N];
    int [] resized_array = new int [N+1];
    System.out.println("The elements of the array are:");

    for(int index=0;index<initial_array.length;index++)
    {
      System.out.println("Enter a number:");
      initial_array[index]= sc.nextInt();
      resized_array[index]=initial_array[index];
    }
    System.out.print("Enter another number:");
    int another_number = sc.nextInt();
    resized_array[resized_array.length-1]=another_number;

    for(int index=0;index<initial_array.length;index++)
    {
      System.out.println(index+" : "+initial_array[index]);
    }
    System.out.println("After resizing the array:");
    //System.out.println(Arrays.toString(resized_array));

    for(int index=0;index<resized_array.length;index++)
    {
      System.out.print(resized_array[index]+" ");
    }


  }
}
