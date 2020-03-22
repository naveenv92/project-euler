import java.util.Hashtable;
import java.util.HashSet;
import java.util.Iterator;

public class Problem21 {

	public static void main(String[] args) {
		Hashtable<Integer, Integer> divisorTable = new Hashtable<Integer, Integer>(10000);
		HashSet<Integer> numTable = new HashSet<Integer>(10000);
		int divisorSum;

		for (int i = 1; i <= 10000; i++) {
			divisorSum = getDivSum(i);
			divisorTable.put(i, divisorSum);
		}

		int currSum;
		int amiSum = 0;
		for (int i = 1; i <= 10000; i++) {
			currSum = divisorTable.get(i);
			for (int j = i+1; j <= 10000; j++) {
				if (currSum == j && divisorTable.get(j) == i) {
					numTable.add(i);
					numTable.add(j);
				}
			}
		}

		Iterator<Integer> numIterator = numTable.iterator();

		while (numIterator.hasNext()) {
			amiSum += numIterator.next();
		}

		System.out.println("Sum of the amicable numbers under 10000 is: " + amiSum);

	}

	public static int getDivSum(int a) {
		int divSum = 1;
		for (int i = 2; i*i <= a; i++) {
			if (a % i == 0) {
				divSum += i + (a/i);
			}
		}
		return divSum;
	}

}