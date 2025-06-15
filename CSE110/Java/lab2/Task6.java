import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("What is the value of x??");
    int num = sc.nextInt();

    if(num<0)
    {
      num=2*num;
      //System.out.println("output:"+num);
    }
    else if((0<num || num==0) && num<2)
    {
      num+=1;
    }

    else if((2<num || num==2) && num<5)
    {
      num= (int) (Math.pow(num,2)-1); #Math.pow() function makes the value double so its need to be converted if I have declared the value as int

    }
    else if(num>5 || num==5)
    {
      num= (int) (3*Math.pow(num,2)+2);

    }
    System.out.println("output:"+num);
  }
}
