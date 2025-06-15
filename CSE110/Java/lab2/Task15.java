public class Test
{
  public static void main(String [] args)
  {
    int sum = 0;
    float average = 0;
    for(int number = 1; number<= 200; number++)
    {
      sum+=number;


    }
    average=(sum/200);
    System.out.println("Sum: "+sum);
    System.out.println("Average: "+average);
  }
}
