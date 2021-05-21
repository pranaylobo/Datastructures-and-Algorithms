public class student
{
    int rollno;
    String name;

    student(int rollno, String name)
    {
        this.rollno = rollno;
        this.name = name;
    }

    void display()
    {
        System.out.println("Student Name:"+" "+name);
        System.out.println("Student Rolno:"+" "+rollno);
    }
}

public class Main
{
    public static void main(String[] args)
    {
        student s1 = new student(8472,"Pranay")
        s1.display()
    }
}