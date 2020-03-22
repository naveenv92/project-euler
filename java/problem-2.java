public class Problem2{

	public static void main(String[] args) {

		int fib1 = 1;
		int fib2 = 1;
		int fibn = 0;
		int sum = 0;

		while (true) {

			fibn = fib1 + fib2;
			fib1 = fib2;
			fib2 = fibn;

			if (fibn > 4000000) {
				break;
			}

			if (fibn%2 == 0) {
				sum += fibn;
			}

		}

		System.out.println(sum);

	}

}