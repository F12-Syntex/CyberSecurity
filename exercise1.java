import java.util.Scanner;

public class Caesar{
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        scan.close();
        char[] inputArray = input.toCharArray();
        int counter = 1;
        while(counter<27){
            for(int i = 0; i < inputArray.length; i++){
                if(inputArray[i]=='z'){ //! If letter is z reset array to begining
                    inputArray[i] = inputArray[i]='a';
                }else{
                    inputArray[i]++;
                }
            }
            System.out.println(new String(inputArray));
            counter++;   
        }
        System.out.println("finished shifting");
    }
}
