public class Problem28 {

	public static void main(String[] args) {
		int numLayers = (1001 + 1)/2;
		int diagSum = 1;
		int currNum = 1;
		int increment;
		for (int i = 1; i < numLayers; i++) {
			increment = 2*i;
			for (int j = 0; j < 4; j++) {
				currNum += increment;
				diagSum += currNum;
			}
		}

		System.out.println("Diagonal Sum Is: " + diagSum);
	}

}