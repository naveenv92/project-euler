import java.math.BigInteger;

public class Problem48 {

	public static void main(String[] args) {
		BigInteger sum = BigInteger.valueOf(0);
		String tempNumString;
		BigInteger tempNum;

		for (int i = 1; i <= 1000; i++) {
			tempNum = BigInteger.valueOf(i);
			for (int j = 1; j < i; j++) {
				tempNum = tempNum.multiply(BigInteger.valueOf(i));
				tempNumString = tempNum.toString();
				if (tempNumString.length() < 10) {
					// Do Nothing
				}
				else {
					tempNum = new BigInteger(tempNumString.substring(tempNumString.length() - 10));
				}
			}
			sum = sum.add(tempNum);
		}
		String numString = sum.toString();
		System.out.println("The last ten digits are: " + numString.substring(numString.length() - 10));
	}

}