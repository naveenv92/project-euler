public class Problem12 {

	public static int numOfDivisors(int a) {
		int divisors = 0;
		for (int i = 1; i*i <= a; i++) {
			if (a % i == 0) {
				divisors++;
			}
		}
		return (2*divisors);
	}

	public static int triangleNumber(int n) {
		return ((n*(n+1))/2);
	}

	public static void main(String[] args) {
		int counter = 1;
		int divisors;

		while (true) {
			if (numOfDivisors(triangleNumber(counter)) > 500) {
				break;
			}
			counter++;
		}

		System.out.println("Value of Triangle Number: " + triangleNumber(counter));

	}

}