#ifndef NODO_H
#define NODO_H
#include <stdlib.h>
#include "Student.cpp"

class  Nodo
{
private:
    /* data */
public:
    Student student;
    Nodo(Student &student);
    Nodo * next;
    Nodo * back;
    
};

 Nodo::Nodo(Student &student){
     this->student = student;
     this->next = NULL;
     this->back = NULL;

}

#endif
