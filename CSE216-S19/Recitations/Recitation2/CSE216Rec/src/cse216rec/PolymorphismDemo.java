package cse216rec;

/*
Courtesy: Prof. Paul Fodor - SBU
*/

public class PolymorphismDemo {
  public static void main(String[] args) {
    m(new GraduateStudent1());
    m(new Student1());
    m(new Person1());
    m(new Object());
  }
  public static void m(Object x) {
    System.out.println(x.toString());
  }
}
class GraduateStudent1 extends Student1 {
    public String toString() {
    return "GraduateStudent";
  }
}
class Student1 extends Person1 {

}

class Person1  {

}
