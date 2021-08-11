#ifndef STUDENT_H
#define STUDENT_H
#include <stdlib.h>
#include <iostream>
using namespace  std;

class Student
{
private:
    /* data */
    int dpi;
    int carnet;
    string nombre;
public:
    Student(int dpi, int carnet, string name);
    Student();
    int getDpi();
    int getCarnet();
    string getName();
    
};

Student::Student(int dpi, int carnet, string name)
{
    this->dpi = dpi;
    this->carnet= carnet;
    this->nombre = name;
}
Student::Student(){

}

int Student::getDpi(){
    return this->dpi;
}
int Student::getCarnet(){
    return this->carnet;
}
string Student::getName(){
    return this->nombre;
}


#endif