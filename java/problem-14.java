public class Problem14 {

    public static void main(String[] args) {
        int length = 0;
        int templen = 0;
        int longnum = 0;
        for (long i = 1; i < 1000000; i++) {
            templen = collatz(i);
            if (templen > length) {
                length = templen;
                longnum = (int)  i;
            }
        }
        System.out.println("The number under 1,000,000 with the longest Collatz Sequence: " + longnum);
    }

    public static int collatz(long a) {
        int counter = 1;
        
        while (a != 1) {
            if (a % 2 == 0) {
                a = a/2;
            }
            else {
                a = 3*a + 1;
            }
            counter++;
        }

        return counter;

    }

}
