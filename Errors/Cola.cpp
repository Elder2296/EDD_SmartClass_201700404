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
    int tamanio;
    Cola(/* args */);
    void push(Error error);
    Error getOut();
    void pop();
    static Cola * getCola();
};

Cola::Cola(/* args */){
    this->tamanio = 0;
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
    tamanio++;
    
}
void Cola::pop(){
    this->first =this->first->next;
    tamanio--;

}

Error Cola::getOut(){
    return this->first->error;

}


Cola * Cola::getCola(){
    static Cola cola;
    return &cola;
}



#endif