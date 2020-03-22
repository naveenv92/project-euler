// Project Euler - Problem 10
// Naveen Venkatesan
// March 22, 2014

public class Problem10 {

	public static boolean isPrime(int x) {
		
		if (x == 1) {
			return false;
		}
		
		if (x == 2) {
			return true;
		}

		for (int i = 2; i*i <= x; i++) {
			if (x % i == 0) {
				return false;
			}
		}

		return true;

	}

	public static void main(String[] args) {

		long sum = 0;

		for (int i = 1; i < 2000000; i++) {
			if (isPrime(i)) {
				sum += i;
			}
		}

		System.out.println("The sum of primes under two million is: " + sum);

	}

}