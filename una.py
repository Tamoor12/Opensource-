import java.util.Random;

#public class UserAgentGenerator {
  #  public static void main(String[] args) {
         Random random = new Random()

        for (int i = 0; i < 66; i++) {
            int androidVersionMajor = random.nextInt(7) + 4;
            int androidVersionMinor = random.nextInt(5);
            int androidVersionPatch = random.nextInt(5);
            String androidVersion = androidVersionMajor + "." + androidVersionMinor + "." + androidVersionPatch;

            int modelNumber = random.nextInt(989) + 11;
            String model = "SM-" + modelNumber;

            String[] brandNames = {"Samsung"};
            String brandName = brandNames[random.nextInt(brandNames.length)];

            int fbav = random.nextInt(990) + 10;
            long fbbv = (long) (Math.random() * (999999999 - 111111111 + 1) + 111111111);

            int width = random.nextInt(761) + 320;
            int height = random.nextInt(1441) + 480;

            String userAgent = String.format("Davik/2.1.0 (Linux; U; Android %s.0.0; %s Build/8BFOHT) [FBAN/FB4A;FBAV/%d.0.0.31.63;FBPN/com.facebook.katana;FBLC/en_US;FBBV/%d;FBCR/null;FBMF/%s;FBBD/%s;FBDV/%s;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{{density=3.5,width=%d,height=%d}}];",
                    androidVersion, model, fbav, fbbv, brandName, brandName, model, width, height);

            System.out.println(userAgent);
        }
    }
}

