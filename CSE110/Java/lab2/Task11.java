import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the amount that the customer need to pay");
    int required_amount = sc.nextInt();
    System.out.println("Enter the amount that the customer paid:");
    int given_amount =sc.nextInt();
    int returned_amount= given_amount-required_amount;

    if (required_amount>given_amount)
    {

      System.out.printf("Please pay %d taka more",(required_amount-given_amount));
    }
    else if (required_amount==given_amount)
    {
      System.out.printf("The returned amount is %d taka",returned_amount);
    }
    else if(given_amount>required_amount)
    {
      System.out.printf("The returned amount is %d taka %n",returned_amount);
      int note_100 = returned_amount/100;
      int rest_amount = returned_amount%100;
      int note_50 = rest_amount/50;
      rest_amount = rest_amount%50;
      int note_20 = rest_amount/20;
      rest_amount =rest_amount%20;
      int note_10 = rest_amount/10;
      rest_amount = rest_amount%10;
      int coin_5 = rest_amount/5;
      rest_amount = rest_amount%5;
      int coin_2 =rest_amount/2;
      rest_amount =rest_amount%2;
      int coin_1 = rest_amount/1;
      rest_amount = rest_amount%1;

      System.out.printf("100 taka note: %d %n",note_100);
      System.out.printf("50 taka note: %d %n",note_50);
      System.out.printf("20 taka note: %d %n",note_20);
      System.out.printf("10 taka note: %d %n",note_10);
      System.out.printf("5 taka coin: %d %n",coin_5);
      System.out.printf("2 taka coin: %d %n",coin_2);
      System.out.printf("1 taka coin: %d %n",coin_1);

    }

  }
}
