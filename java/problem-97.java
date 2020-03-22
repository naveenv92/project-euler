import java.math.BigInteger;

public class Problem97 {

	public static void main(String[] args) {
		BigInteger prime = BigInteger.valueOf(1);
		String tempNumString;

		for (int i = 0; i < 7830457; i++) {
			prime = prime.multiply(BigInteger.valueOf(2));
			tempNumString = prime.toString();
			if (tempNumString.length() < 10) {
				// Do Nothing
			}
			else {
				prime = new BigInteger(tempNumString.substring(tempNumString.length() - 10));
			}
		}

		prime = prime.multiply(BigInteger.valueOf(28433));
		tempNumString = prime.toString();
		prime = new BigInteger(tempNumString.substring(tempNumString.length() - 10));
		prime = prime.add(BigInteger.valueOf(1));

		System.out.println("The last ten digits of this prime number are: " + prime);
	}

}