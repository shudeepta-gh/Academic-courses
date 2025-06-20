public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number of terms");
    int number = sc.nextInt();
    int sum = 0;
    int count = 1;
    System.out.println("The odd numbers are:");
    for(int counter=1;count<=number;counter+=1)
      {
        if(counter%2!=0)
        {
          System.out.println(counter);
          count++;
          sum+=counter;
        }
      }
    System.out.println("The Sum of odd Natural Numbers up to"+number+" terms is : "+sum);

  }
}
