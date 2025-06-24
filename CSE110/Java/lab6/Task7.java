public class Test
{
  public static void main(String [] args)
  {

    int arr [] = {-5,10,-7,-5};
    int [] new_arr = new int[arr.length];
    System.out.println("Input array:");
    for(int i = 0;i<arr.length;i++)
    {
      System.out.print(arr[i]+" ");

    }
    System.out.println();
    System.out.println("New array:");
    for(int i = 0;i<arr.length;i++)
    {

       boolean isDuplicate = false;
       for(int j=0;j<i;j++)
       {
         if(arr[i]==arr[j])
         {
           isDuplicate=true;
           break;
         }

       }

       if(isDuplicate==false)
       {
         System.out.print(arr[i]+" ");
       }
    }
  }
}
