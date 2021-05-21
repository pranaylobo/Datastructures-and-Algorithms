public class student
{
    int id;
    String name;
    Student(int i,String n)
    {
        this.id = i;
        this.name=n;
    }

    public void display()
    {
        System.out.println("Student name",name);
        System.out.println("Student id",id);
    }
}

public class Main
{
    public static void main(String[] args)
    {
        Student s1 = new Student(1,"Pranay");
        s1.display();
    }
}