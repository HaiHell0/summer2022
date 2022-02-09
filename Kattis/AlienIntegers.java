import java.util.*;
public class AlienIntegers {
    public static void main(String[] args){
        String og = "0123456789";
        ArrayList<Integer> uNums = new ArrayList<>();
        ArrayList<Integer> num = new ArrayList<>();
        Scanner in = new Scanner(System.in);
        String N = in.nextLine();

        for(int i = 0; i < N.length();i++){
            num.add(Character.getNumericValue(N.charAt(i)));
        }
        for(int i = 0; i < og.length();i++){
            uNums.add(Character.getNumericValue(og.charAt(i)));
        }

        for(int x : num){
            if(uNums.contains(x)) uNums.remove((Integer) x);
        }

        if(uNums.size()==0){
            System.out.println("Impossible");
            System.exit(0);
        }
        if(num.size()==1){
            if(num.get(0)==0){
                System.out.println("1");
                System.exit(0);
            }
            if(num.get(0)==9){
                System.out.println("8");
                System.exit(0);
            }
        }
        ArrayList<Integer> under = new ArrayList<>();
        ArrayList<Integer> over = new ArrayList<>();
        for(int i = 0; i < uNums.size() ; i++){
            if (num.get(0) < uNums.get(i)){
                if(i>0)under.add(uNums.get(i-1));
                else under.add(0);
                over.add(uNums.get(i));
                break;
            }
        }

        for(int i = 1; i < num.size();i++) {
            under.add(uNums.get(uNums.size() - 1));
            over.add(uNums.get(0));
            }


        StringBuilder a = new StringBuilder();
        StringBuilder b = new StringBuilder();


        for(int i : under){
            a.append(i);
        }
        for(int i : over){
            b.append(i);
        }
        long overN =Long.parseLong(b.toString());
        long underN =Long.parseLong(a.toString());
        long x = Math.abs(Long.parseLong(N)-underN);
        long y = Math.abs(overN-Long.parseLong(N));
        if(x-y > 0) System.out.println(overN);
        else if(x-y < 0) System.out.println(underN);
        else System.out.println(underN+" "+ overN);
        System.exit(0);

    }
}
