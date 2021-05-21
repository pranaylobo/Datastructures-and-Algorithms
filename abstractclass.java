abstract class honda{
    abstract void display()
}

public class Main{
    public void display(){
        System.out.println("Mei chali")
    }
    public static void main(String[] args)
    {
        honda h1 = new Main();
        h1.display();
    }
}
