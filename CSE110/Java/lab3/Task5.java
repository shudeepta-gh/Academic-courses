public class Test
{
  public static void main(String [] args)
  {
   int number = 0;
   for(int count = 0;count<=600;count+=1)
   {
    if(count%7==0 && count%9!=0)
    {

      number+=count;
    }

    else if(count%7!=0 && count%9==0)
    {
      number+=count;
    }
   }
   System.out.println(number);
  }
}
