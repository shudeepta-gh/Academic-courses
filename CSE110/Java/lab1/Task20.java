import java.util.Scanner;
   public class Test
   {
     public static void main(String [] args)
     {
       Scanner sc =new Scanner(System.in);
       System.out.print("Enter the value of a:");
       double a = sc.nextDouble();
       System.out.print("Enter the value of b:");
       double b = sc.nextDouble();
       double c = Math.sqrt(Math.pow(a,2)+Math.pow(b,2));
       double sinA = a/c;
       double cosA = b/c;
       double sinB = b/c;
       double cosB = a/c;
       System.out.printf("SinA = %.2f\nCosA = %.2f\nSinB = %.2f\nCosB = %.2f", sinA,cosA,sinB,cosB);
     }
   }
