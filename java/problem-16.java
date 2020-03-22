import java.math.BigInteger;

public class Problem16 {

    public static void main(String[] args) {
	BigInteger num = BigInteger.valueOf(1);
	BigInteger digitSum = BigInteger.valueOf(0);
	for (int i = 0; i < 1000; i++) {
	    num = num.add(num);
	}
	BigInteger[] currVals = new BigInteger[2];
	while (num.compareTo(BigInteger.valueOf(0)) > 0) {
		currVals = num.divideAndRemainder(BigInteger.valueOf(10));
		digitSum = digitSum.add(currVals[1]);
		num = currVals[0];
	}
	System.out.println(digitSum);
    }
}