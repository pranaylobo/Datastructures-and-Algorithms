class adder
{
    public void add(int a,int b)

    {
        return a + b;
    }
    public void add(int a,int b,int c)

    {
        return a + b + c;
    }
}

public class Main
{
    public static void main(String[] args)
    {
        adder a1 = new adder();
        a1.add(1,1);
        a1.add(1,1,1);
    }
}