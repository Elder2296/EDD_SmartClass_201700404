#ifndef STUDENT_H
#define STUDENT_H
#include <stdlib.h>
#include <iostream>
using namespace  std;

class Student
{
private:
    /* data */
    string dpi;
    int carnet;
    string nombre;
    string carrera;
    string email;
    string password;
    int credits;
    int age;
public:
    Student(string dpi, int carnet, string name, string carrera, string email, string password, int credits, int age);
    Student();
    string getDpi();
    int getCarnet();
    string getName();
    string getCarrera();
    string getMail();
    string getPass();
    int getCredits();
    int getAge();
    void setCarnet(int carnet);
    void setName(string name);
    void setCarrera(string carrera);
    void setMail(string email);
    void setPass(string pass);
    void setCredits(int credits);
    void setAge(int age);

    
};

Student::Student(string dpi, int carnet, string name, string carrera, string email, string password, int credits, int age)
{
    this->dpi = dpi;
    this->carnet= carnet;
    this->nombre = name;
    this->carrera = carrera;
    this->email = email;
    this->password = password;
    this->credits = credits;
    this->age = age;
}
Student::Student(){

}

string Student::getDpi(){return this->dpi;}
int Student::getCarnet(){return this->carnet;}
string Student::getName(){return this->nombre;}
string Student::getCarrera(){return this->carrera; }
string Student::getMail(){return this->email;}
string Student::getPass(){return this->password;}
int Student::getCredits(){return this->credits;}
int Student::getAge(){return this->age;}
void Student::setCarnet(int carnet){this->carnet = carnet;}
void Student::setName(string name){this->nombre = name;}
void Student::setCarrera(string carrera){this->carrera = carrera;}
void Student::setMail(string mail){this->email = mail;}
void Student::setPass(string pass){this->password = pass;}
void Student::setCredits(int credits){this->credits= credits;}
void Student::setAge(int age){this->age= age;}



#endif