import java.util.Hashtable;

public class Problem31 {

	public static void main(String[] args) {

		int[][] coinMatrix = new int[8][201];
		Hashtable<Integer,Integer> coinTable = new Hashtable<Integer,Integer>();
		coinTable.put(0,1);
		coinTable.put(1,2);
		coinTable.put(2,5);
		coinTable.put(3,10);
		coinTable.put(4,20);
		coinTable.put(5,50);
		coinTable.put(6,100);
		coinTable.put(7,200);

		for (int i = 1; i < 201; i++) {
			for (int j = 0; j < 8; j++) {
				if (j == 0) {
					coinMatrix[j][i] = 1;
				}
				else {
					coinMatrix[j][i] = coinMatrix[j-1][i];
					if ((i - coinTable.get(j)) >= 0) {
						coinMatrix[j][i] += coinMatrix[j][i-coinTable.get(j)];
					}
					if (i == coinTable.get(j)) {
						coinMatrix[j][i] += 1;
					}
				}
			}
		}

		System.out.println("The number of ways to make $2 is: " + coinMatrix[7][200]);

	}


}