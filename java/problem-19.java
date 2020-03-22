import java.util.Hashtable;

public class Problem19 {

	// Use Constants for Months
	public static final int JAN = 0;
	public static final int FEB = 1;
	public static final int MAR = 2;
	public static final int APR = 3;
	public static final int MAY = 4;
	public static final int JUN = 5;
	public static final int JUL = 6;
	public static final int AUG = 7;
	public static final int SEP = 8;
	public static final int OCT = 9;
	public static final int NOV = 10;
	public static final int DEC = 11;

	// Use Constants for Days
	public static final int SUN = 0;
	public static final int MON = 1;
	public static final int TUE = 2;
	public static final int WED = 3;
	public static final int THU = 4;
	public static final int FRI = 5;
	public static final int SAT = 6;

	public static void main(String[] args) {
		
		Hashtable<Integer,Integer> dayTable = new Hashtable<Integer,Integer>();
		dayTable.put(JAN,31);
		dayTable.put(FEB,28);
		dayTable.put(MAR,31);
		dayTable.put(APR,30);
		dayTable.put(MAY,31);
		dayTable.put(JUN,30);
		dayTable.put(JUL,31);
		dayTable.put(AUG,31);
		dayTable.put(SEP,30);
		dayTable.put(OCT,31);
		dayTable.put(NOV,30);
		dayTable.put(DEC,31);

		// 1/1/00 is the first day
		int currMonth = JAN;
		int currDayOfMonth = 1;
		int currDay = MON;
		int currYear = 1900;

		int sundayCounter = 0;

		while (currYear <= 2000) {
			if (currDay == SUN && currDayOfMonth == 1 && currYear != 1900) {
				sundayCounter++;
			}
			int monthDayTotal = dayTable.get(currMonth);
			if (currMonth == FEB && isLeapYear(currYear)) {
				monthDayTotal++;
			}
			currDay = (currDay + 1) % 7;
			currDayOfMonth++;
			if (currDayOfMonth > monthDayTotal) {
				if (currMonth == DEC) {
					currYear++;
				}
				currDayOfMonth = 1;
				currMonth = (currMonth + 1) % 12;
			}
		}

		System.out.println("The number of Sundays that fell on the first of the month: " + sundayCounter);
	}

	public static boolean isLeapYear(int year) {
		if (year % 4 == 0) {
			if (year % 100 == 0) {
				if (year % 400 == 0) {
					return true;
				}
				return false;
			}
			return true;
		}
		return false;
	}


}