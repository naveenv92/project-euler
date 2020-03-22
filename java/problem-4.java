public class Problem4 {

    public static void main(String[] args) {
        int a = longestpal();
        System.out.println("The longest palindrome of 3 digit products is: " + a);
    }

    public static int longestpal() {
        int num = 0;
        String strnum = new String();
        int strlen = 0;
        int begind = 0;
        int endind = 0;
        int currpal = 0;
        int frontdigit = 0;
        int backdigit = 0;

        for (int i = 100; i < 1000; i++) {
          for (int j = 100; j < 1000; j++) {
            num = i*j;
            strnum = "" + num;
            strlen = strnum.length();
            begind = 0;
            endind = strlen-1;
            for (int k = 0; k < strlen; k++) {
                if (begind == endind) {
                    if (num > currpal) {
                        currpal = num;
                        break;
                    }
                }
                frontdigit = Integer.parseInt("" + strnum.charAt(begind));
                backdigit = Integer.parseInt("" + strnum.charAt(endind));

                if (frontdigit == backdigit) {
                    if (begind + 1 == endind) {
                        if (num > currpal) {
                            currpal = num;
                            break;
                        }
                    }
                    begind++;
                    endind--;
                }
            }

          }
       }
       return currpal;
    }

}
