import java.math.BigInteger;

public class Problem20 {

	public static void main(String[] args) {
		BigInteger factorialNum = BigInteger.valueOf(1);
		BigInteger digitSum = BigInteger.valueOf(0);
		int counter = 100;


		while (counter > 0) {
			factorialNum = factorialNum.multiply(BigInteger.valueOf(counter));
			counter--;
		}

		while (factorialNum.compareTo(BigInteger.valueOf(0)) > 0) {
			BigInteger[] remArray = factorialNum.divideAndRemainder(BigInteger.valueOf(10));
			digitSum = digitSum.add(remArray[1]);
			factorialNum = remArray[0];
		}
		System.out.println("Sum of digits of 100! is: " + digitSum);
	}

}