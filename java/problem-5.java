public class Problem5{

	public static boolean isDivisible(int n) {

		if (n%3 == 0 && n%6 == 0 && n%7 == 0 && n%8 == 0 && n%9 == 0) {
			if (n%11 == 0 && n%12 == 0 && n%13 == 0 && n%14 == 0 && n%15 == 0) {
				if (n%16 == 0 && n%17 == 0 && n%18 == 0 && n%19 == 0) {
					return true;
				}
			}
		}
		return false;

	}

	public static void main(String[] args) {

		int n = 20;

		while (true) {
			if (isDivisible(n)) {
				break;
			}

			n += 20;

		}

		System.out.println(n);

	}
	

}