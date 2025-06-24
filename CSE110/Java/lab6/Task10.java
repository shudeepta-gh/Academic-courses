import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    int [] marks = {100,47,85,94,5,50};
    String [] names = {"Henry","Mari","Herry","Jack","Lily","Oliver"};
    for(int i = 0; i<marks.length-1; i++)
    {
      for(int j = 0; j<marks.length-i-1; j++)
      {
        if(marks[j]>marks[j+1])
        {
          int temp = marks[j];
          String interim = names[j];
          marks[j] = marks[j+1];
          names[j] = names[j+1];
          marks[j+1] = temp;
          names[j+1] = interim;
        }
      }
    }

    System.out.println("Sorted Array:");
    for(int i = 0; i<marks.length; i++)
    {
      System.out.print(marks[i]+" ");
    }
    System.out.println();
    for(int j = 0; j<names.length; j++)
    {
      System.out.print(names[j]+" ");
    }
  }
}
