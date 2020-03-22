public class Problem9 {
    
    public static void main(String[] args) {
        int a = 0;
        int b = 0;
        int c = 0;

        for (int i = 1; i < 1000; i++) {
            for (int j = 1; j < 1000; j++) {
                for (int k = 1; k < 1000; k++) {
                    if (i*i + j*j == k*k) {
                        if (i + j + k == 1000) {
                            a = i;
                            b = j;
                            c = k;
                        }
                    }
                }
            }
        }

        System.out.println("The Pythaogorean Triple is: (" + a + "," +  b + "," + c + ")");
        long product = a*b*c;
        System.out.println("The product of the three is: " + product);
    }

}
