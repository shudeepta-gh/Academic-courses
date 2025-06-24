import java.util.Scanner;
public class Test
{
  public static void main(String [] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Please enter the length of array");
    int row_1 = sc.nextInt();
    int col_1 = sc.nextInt();
    int [][] arr1 = new int [row_1][col_1];
    System.out.println("Please enter the elements of the arr1");
    for(int i=0 ; i<row_1 ; i++)
    {
      for(int j=0 ; j<col_1 ; j++)
      {
        arr1[i][j] = sc.nextInt();
      }
    }
    System.out.println("Please enter the length of array");
    int row_2 = sc.nextInt();
    int col_2 = sc.nextInt();
    int [][] arr2 = new int [row_2][col_2];
    System.out.println("Please enter the elements of the arr2");
    for(int i=0 ; i<row_2 ; i++)
    {
      for(int j=0 ; j<col_2 ; j++)
      {
        arr2[i][j] = sc.nextInt();
      }
    }
    boolean isSubset = true;
        for (int i = 0; i < row_2; i++)
        {
            for (int j = 0; j < col_2; j++)
            {
                boolean found = false;
                for (int k = 0; k < row_1; k++)
                {
                    for (int l = 0; l < col_1; l++)
                    {
                        if (arr1[k][l] == arr2[i][j])
                        {
                            found = true;
                            break;
                        }
                    }
                    if (found)
                    {
                        break;
                    }
                }
                if (!found)
                {
                    isSubset = false;
                    break;
                }
            }
            if (!isSubset)
            {
                break;
            }
        }


        if (isSubset)
        {
            System.out.println("Array2 is a subset of Array1.");
        }
        else
        {
            System.out.println("Array2 is NOT a subset of Array1.");
        }
    }
}
