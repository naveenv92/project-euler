public class Problem7 {

	public static Boolean isPrime(long n) {

		if (n == 2) {
			return true;
		}
		else if (n == 1) {
			return false;
		}
		else {
			for (long div = 2; div*div <= n; div++) {
				if (n%div == 0) {
					return false;
				}
			}
		}
		return true;
	}

	public static void main(String [] args) {
		int primecount = 0;
		long currnum = 1;

		while (true) {
			if (primecount > 10000) {
				break;
			}
			if (isPrime(currnum)) {
				primecount += 1;
			}
			currnum += 1;
		}

		System.out.println("The 10001st Prime is: " + (currnum-1));
	}

}
