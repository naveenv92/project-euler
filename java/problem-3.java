public class Problem3{

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

	public static void main(String[] args) {

		long n = 600851475143l;
		long largestpfactor = 0;

		for (long div = 2; div*div <= n; div++) {
			if (n%div == 0) {
				if (isPrime(div)) {
					largestpfactor = div;
			}
		}

	}

		System.out.println(largestpfactor);

}

}