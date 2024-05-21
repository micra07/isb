import java.util.Random;

public class RandomSequenceGenerator {

    public static void main(String[] args) {
        Random random = new Random(System.currentTimeMillis());

        StringBuilder sequence = new StringBuilder();
        for (int i = 0; i < 128; ++i) {
            int randomBit = random.nextInt(2);
            sequence.append(randomBit);
        }

        System.out.println(sequence.toString());
    }
}
