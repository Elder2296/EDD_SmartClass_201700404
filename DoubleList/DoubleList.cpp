#ifndef LIST_H
#define LIST_H
#include <stdlib.h>
#include <iostream>
#include "Nodo.cpp"

class List
{
    private:
    /* data */
        
    public:
        Nodo * first;
        Nodo * last;
        List(/* args */);
        void insert(Student student);
        void print();
        static List * getList();
        Student &getStudent(int carnet);
        Student &getStudent(string dpi);
        void Delete(string dpi);
        bool search(int carnet);
        bool searchDPI(string dpi);
};

List::List(/* args */){
    this->first = NULL;
    this->last = NULL;
}

void List::insert(Student student){
    Nodo * newNodo = new Nodo(student);
    if(this->first == NULL){
        this->first = newNodo;
        this->last = newNodo;

    }else{
        Nodo * aux = this->last;

        aux->next = newNodo;
        newNodo->next = this->first;
        newNodo->back = aux;
        this->first->back = newNodo;
        this->last = newNodo;

    }

}
void List::Delete(string dpi){
    if(this->first->student.getDpi() == dpi  ){
        this->first = this->first->next;
        this->first->back = this->last;
        this->last->next = this->first;
    }else if(this->last->student.getDpi() == dpi){
        this->last =this->last->back;
        this->last->next = this->first;
        this->first->back = this->last;
    }else{
        Nodo * aux = this->first;

        do{
            if(aux->student.getDpi()== dpi){
                
                aux->back->next = aux->next;
                aux->next->back = aux->back;
                break;
            }
            aux = aux->next;
        }while(aux != this->first);

    }
}

void List::print(){
    Nodo * aux = this->first;

    do{
        cout<<"carnet: "<<aux->student.getCarnet()<<endl;
        aux = aux->next;

    }while (aux!= this->first);
    
    
}
bool List::search(int carnet){  
    Nodo * aux = this->first;
    int i = 0;
    do{
        if(aux->student.getCarnet() == carnet){
            i = -1;
            break;
        }
        aux = aux->next;
        

    }while(aux != this->first);
    if(i!=0){return true;}
    else{return false;}

}
bool List::searchDPI(string dpi){  
    Nodo * aux = this->first;
    int i = 0;
    do{
        if(aux->student.getDpi() == dpi){
            i = -1;
            break;
        }
        aux = aux->next;
        

    }while(aux != this->first);
    if(i!=0){return true;}
    else{return false;}

}
Student & List::getStudent(int carnet){
    Nodo * aux = this->first;
    do{
        if(aux->student.getCarnet() == carnet){
            break;
        }
        aux = aux->next;

    }while(aux !=  this->first);
    return aux->student;
}
Student & List::getStudent(string dpi){
    Nodo * aux = this->first;
    do{
        if(aux->student.getDpi() == dpi){
            break;
        }
        aux = aux->next;

    }while(aux !=  this->first);
    return aux->student;

}

List * List::getList(){
    static List list;
    return &list;
}
#endif
