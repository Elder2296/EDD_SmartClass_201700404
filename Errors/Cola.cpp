#ifndef COLA_H
#define COLA_H
#include "Nodo.cpp"
class Cola
{
private:
    /* data */
public:
    NodoE * first;
    NodoE * last;
    Cola(/* args */);
    void push(Error error);
    Error getOut();
    void pop();
    static Cola * getCola();
};

Cola::Cola(/* args */){
    this->first = NULL;
    this->last = NULL;

}
void Cola::push(Error error){
    NodoE * newNodo = new NodoE(error);

    if (this->first == NULL){
        this->first = newNodo;
        this->last = newNodo;
        this->first->next = NULL;
        this->last->next = NULL;
    }else{
        NodoE * aux = this->last;
        newNodo->next =NULL;
        aux->next = newNodo;
        this->last = newNodo;

    }
    
}
void Cola::pop(){
    this->first =this->first->next;

}

Error Cola::getOut(){
    return this->first->error;

}


Cola * Cola::getCola(){
    static Cola cola;
    return &cola;
}



#endif