import java.lang.Math;

public class Problem27 {

	public static boolean isPrime(int n) {
		if (n == 1) {
			return false;
		}
		for (int i = 2; i*i <= n; i++) {
			if (n % i == 0) {
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args) {
		int maxCons = 0;
		int maxA = 0;
		int maxB = 0;
		for (int a = -1000; a <= 1000; a++) {
			for (int b = -1000; b <= 1000; b++) {
				int n = 0;
				while (isPrime(Math.abs(n*n + a*n + b))) {
					n++;
				}
				if (n > maxCons) {
					maxCons = n;
					maxA = a;
					maxB = b;
				}
			}
		}
		System.out.println("The product of a and b is: " + (maxA*maxB));
	}

}