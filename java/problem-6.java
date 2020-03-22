public class Problem6 {

	public static long SumSquare(long a) {
		long sumsquare = 0;
		for (int i = 0; i < a+1; i++) {
			sumsquare += i;
		}
		return sumsquare*sumsquare;
	}

	public static long SquareSum(long a) {
		long squaresum = 0;
		for (int i = 0; i < a+1; i++) {
			squaresum += i*i;
		}
		return squaresum;
	}

	public static void main(String [] args) {
		System.out.println((SumSquare((long) 100) - SquareSum((long) 100)));
	}

}