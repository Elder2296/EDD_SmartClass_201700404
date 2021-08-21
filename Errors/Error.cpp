#ifndef ERROR_H
#define ERROR_H
#include "../Tasks/Task.cpp"
#include "../DoubleList/Student.cpp"
class Error
{
private:
    /* data */
public:
    static int index;
    Task * task;
    Student * student;
    int id;
    int indice;
    string type;
    string description;
    Error(int indice, int id, string type, string descripcion);
    Error(/* args */);
    
};
int Error::index=1;
Error::Error(int indice,int id, string tipo, string descripcion){
    this->indice = indice;
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