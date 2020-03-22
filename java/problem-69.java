public class Problem69 {

	public static boolean isPrime(int n) {
		if (n == 1) {
			return false;
		}
		if (n == 2) {
			return true;
		}
		for (int i = 2; i*i <= n; i++) {
			if (n % i == 0) {
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args) {
		int totalNum = 1;
		int currPrime = 1;

		while (true) {
			while (true) {
				if (isPrime(currPrime)) {
					break;
				}
				else {
					currPrime++;
				}
			}
			totalNum *= currPrime;
			if (totalNum > 1000000) {
				totalNum = totalNum/currPrime;
				break;
			}
			currPrime++;
		}

		System.out.println("The value that results in the largest ratio is: " + totalNum);
	}

}