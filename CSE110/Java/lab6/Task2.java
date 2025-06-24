public class Test
{
  public static void main(String [] args)
  {
    int arr [] = {9,-5, 7, 9,-5, 5, 7};
    System.out.println("Before removing duplicates:");
    for(int i = 0; i < arr.length; i++)
    {
      System.out.print(arr[i]+" ");
    }
    System.out.println();
    int [] final_arr = new int [arr.length];

    for (int i = 0; i < arr.length; i++)
    {
         final_arr[i] = arr[i];
    }


    for (int i = 0; i < final_arr.length; i++)
    {
         for (int j = i + 1; j < final_arr.length; j++)
         {
             if (final_arr[i] == final_arr[j] && final_arr[i] != 0)
             {
                  final_arr[j] = 0;
             }
         }
    }
    System.out.println("After replacing duplicates with 0:");

    for (int i =0 ; i < final_arr.length; i++)
    {
      System.out.print(final_arr[i]+" ");
    }
  }
}
