#ifndef NODOE_H
#define NODOE_H


#include "Error.cpp"
#include <stdlib.h>

class NodoE
{
private:
    /* data */
public:
    
    NodoE * next;
    Error error;
    
    NodoE(Error &error);
    
};

NodoE::NodoE(Error &error){
    this->error = error;
    
    this->next = NULL;


}




#endif