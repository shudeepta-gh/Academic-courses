import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the value of N:");
    int N = sc.nextInt();
    oneToN(1,N);
    System.out.println();
    nToOne(1,N);
    System.out.println();
    System.out.println(recursiveSum(1,N));
  }
  public static void oneToN(int num,int N)
  {
      int i = num;
      if(i>N)
      {
        return ;
      }

      System.out.print(i+" ");
      oneToN(i+1,N);
  }

  public static void nToOne(int num,int N)
  {
      if(N<num)
      {
        return;
      }

      System.out.print(N+" ");
      nToOne(num,N-1);
  }
  public static int recursiveSum(int num,int N)
  {

      int i = num;
      if(i>N)
      {
        return 0;
      }

      return num + recursiveSum(num + 1, N);
  }

}
