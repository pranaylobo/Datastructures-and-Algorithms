interface print{
    void print()
}
interface show{
    void show()
}

public class Main implements print,show{
    public void print(){
        System.out.println("Printing");
    }
    public void show(){
        System.out.println("Showing");
    }
    public static void main(String[] args){
        Main m1 = new Main();
        m1.print();
        m1.show();
    }
}