public class Problem40 {

	public static void main(String[] args) {
		int product = digitNum(1) * digitNum(10) * digitNum(100) * digitNum(1000) * digitNum(10000) * digitNum(100000) * digitNum(1000000);
		System.out.println("The product of the digits is: " + product);
	}

	public static int digitNum(int n) {
		int counter = 1;
		int totIndex = 0;
		String currNum = "";

		while (true) {
			currNum = "" + counter;
			if (n <= (totIndex + currNum.length())) {
				String charInd = "" + currNum.charAt(n - totIndex - 1);
				return Integer.parseInt(charInd);
			}
			totIndex += currNum.length();
			counter++;
		}

	}

}