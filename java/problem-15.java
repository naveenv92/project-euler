import java.io.*;

public class Problem15 {
   
    public static void main(String[] args) throws Exception {
        BufferedReader keybd = new BufferedReader(new InputStreamReader (System.in));
        System.out.print("Enter Dimension of Grid: ");
        String inputnum = keybd.readLine();
        try {
             Integer inp = Integer.parseInt(inputnum);
             long[][] mat = latticepaths(inp);
             System.out.print("X Index of Grid: ");
             String index_x = keybd.readLine();
             System.out.print("Y Index of Grid: ");
             String index_y = keybd.readLine();
             Integer indx = Integer.parseInt(index_x);
             Integer indy = Integer.parseInt(index_y);
             long paths = mat[indx][indy];
             System.out.println("Number of paths to get to index (" + indx + "," + indy + "): " + paths);
        } catch (Exception e) {
            System.out.println("Invalid dimension or index!");
        }
    }

    public static long[][] latticepaths(Integer a) {
        long[][] matrix = new long[a+1][a+1];
        matrix[1][1] = 2;
        
        for (int i = 1; i <= a; i++) {
            for (int j = 1; j <= a; j++) {
                if (i == 1) {
                    if (j == 1) {
                        continue;
                    }
                    matrix[i][j] = matrix[i][j-1] + 1;
                }
                else if (j == 1) {
                    matrix[i][j] = matrix[i-1][j] + 1;
                }
                else {
                    matrix[i][j] += matrix[i-1][j] + matrix[i][j-1];
                }
            }
        }

        return  matrix;    
    }

}
