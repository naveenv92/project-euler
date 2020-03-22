public class Problem39 {

	public static boolean isRightTrig(int a, int b, int c) {
		if (a*a + b*b == c*c) {
			return true;
		}
		else {
			return false;
		}
	}

	public static void main(String[] args) {
		int maxSols = 0;
		int maxPerim = 0;
		for (int p = 1; p < 1000; p++) {
			int currSols = 0;
			for (int a = 1; a <= p/2; a++) {
				for (int b = a; b <= p/2; b++) {
					for (int c = b; c <= p/2; c++) {
						if (a+b+c == p) {
							if (isRightTrig(a,b,c)) {
								currSols++;
							}
						}
					}
				}
			}
			if (currSols > maxSols) {
				maxSols = currSols;
				maxPerim = p;
			}
		}
		System.out.println("The max number of solutions is: " + maxSols);
		System.out.println("This corresponds to a perimeter of: " + maxPerim);
	}

}