public class Test
{
  public static void main(String [] args)
  {
   for(int count = 18;count<=63;count+=9)
   {
     if (count!=63)
     {
       if(count%2==0)
       {
         System.out.print((count*1)+",");
       }
       else
       {
         System.out.print((count*-1)+",");
       }
     }
     else
     {
        System.out.println(count*-1);
     }

   }
  }
}
