import java.util.HashSet;
import java.math.BigInteger;

public class Problem29 {

	public static void main(String[] args) {
		BigInteger currInt;
		BigInteger currVal;
		HashSet<BigInteger> intSet = new HashSet<BigInteger>();

		for (int i = 2; i <= 100; i++) {
			currInt = BigInteger.valueOf(i);
			for (int j = 2; j <= 100; j++) {
				currVal = currInt.pow(j);
				intSet.add(currVal);
			}
		}

		System.out.println("Number of distinct terms: " + intSet.size());

	}


}