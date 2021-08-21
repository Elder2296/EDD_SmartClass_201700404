#ifndef ERROR_H
#define ERROR_H
#include "../Tasks/Task.cpp"
#include "../DoubleList/Student.cpp"
class Error
{
private:
    /* data */
public:
    Task * task;
    Student * student;
    int id;
    string type;
    string description;
    Error(int id, string type, string descripcion);
    Error(/* args */);
    
};
Error::Error(int id, string tipo, string descripcion){
    this->id = id;
    this->type = tipo;
    this->description = descripcion;
    this->task = new Task();
    this->student = new Student();
}

Error::Error(/* args */){
    this->task = new Task();
    this->student = new Student();
}





#endif