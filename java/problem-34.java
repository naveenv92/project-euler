public class Problem34 {

	public static int factorial(int n) {
		int returnVal = 1;
		for (int i = 1; i <= n; i++) {
			returnVal *= i;
		}
		return returnVal;
	}

	public static void main(String[] args) {
		int[] facArr = {factorial(0), factorial(1), factorial(2), factorial(3), factorial(4), factorial(5), factorial(6), factorial(7), factorial(8), factorial(9)};
		int facSums = 0;
		int currSum = 0;
		String currNum;
		for (int i = 10; i < 2540160; i++) {
			currSum = 0;
			currNum = "" + i;
			for (int j = 0; j < currNum.length(); j++) {
				currSum += facArr[Integer.parseInt("" + currNum.charAt(j))];
			}
			if (currSum == i) {
				facSums += i;
			}
		}
		System.out.println("The sum of digit factorial numbers is: " + facSums);
	}

}