import java.util.Random;
public class ClassicalCHSH {
	public static void main(String[] args) {
		Random r = new Random();
		int rounds = 100000, wins=0;
		for (int i=0; i<rounds; i++) {
			int Alice=r.nextInt(2), Bob=r.nextInt(2);
			if (Alice==0 && Bob==0) wins++;
			else if (Alice != Bob) wins++;			
		}
		System.out.println("Wins: "+wins+", Losses: "+(rounds-wins));
		System.out.println("Win Percentage: "+ ((double)wins/rounds)*100+"%");		
	}
}
