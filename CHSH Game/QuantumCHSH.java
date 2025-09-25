import java.util.Random;
public class QuantumCHSH {
	static final Random r = new Random();
    public static void main(String[] args) {
        int rounds = 10000000, wins=0;
        for (int i = 0; i < rounds; i++) {
            int Alice = r.nextInt(2), Bob = r.nextInt(2);

            int packed = quantumMeasurements(Alice, Bob);
            int a = (packed >> 1) & 1, b = packed & 1;    

            if ((a ^ b) == (Alice | Bob)) wins++;
        }
        System.out.println("Wins: " + wins + ", Losses: " + (rounds - wins));
        System.out.println("Win Percentage: "+ (double) wins / rounds * 100+"%");
    }
    
    public static int quantumMeasurements(int Alice, int Bob) {
        final double optimalProb = (1 + Math.sqrt(2) / 2) / 2;
        boolean needCorrelation = (Alice == 0 && Bob == 0);
        int a, b;

        if (r.nextDouble() < optimalProb) {
            if (needCorrelation) a = b = r.nextInt(2);
            else {
                a = r.nextInt(2);
                b = 1 - a;
            }
        } 
        else {
            if (needCorrelation) {
                a = r.nextInt(2);
                b = 1 - a;
            } 
            else a = b= r.nextInt(2);
        }
        return (a << 1) | b;
    }
}
