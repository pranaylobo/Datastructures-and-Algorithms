class Animal
{
    public void bark()
    {
        System.out.println("Barnking");
    }
}

class dog extends Animal
{
    public void sleep()
    {
        System.out.println("Sleeping");
    }
}

public class Main()
{
    public void main(String[] args)
    {
        Animal a1 = new Animal();
        a1.bark();
        a2.spleep();
    }
}