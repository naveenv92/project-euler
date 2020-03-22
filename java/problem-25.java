import java.math.BigInteger;

public class Problem25 {

	public static void main(String[] args) {
		BigInteger[] fibs = {BigInteger.valueOf(1), BigInteger.valueOf(1)};
		BigInteger currFib;
		int counter = 2;

		while (true) {
			currFib = fibs[0].add(fibs[1]);
			if ((currFib.toString()).length() >= 1000) {
				counter++;
				break;
			}
			fibs[0] = fibs[1];
			fibs[1] = currFib;
			counter++;
		}
		System.out.println("The Fibonacci number index with 1000 digits: " + counter);
	}

}