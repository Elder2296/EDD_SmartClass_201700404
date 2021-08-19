#ifndef loadTask_H
#define loadTask_H
#include "Task.cpp"
#include <stdlib.h>
#include "../WorkFiles/Casilla.cpp"

class NodoT
{
    private:
    /* data */
    public:
        NodoT * back;
        NodoT * next;
        Casilla casilla;
        NodoT(Casilla &casilla);
    
};

NodoT::NodoT(Casilla &casilla){
    this->casilla = casilla;
    this->back = NULL;
    this->next = NULL;
}




#endif