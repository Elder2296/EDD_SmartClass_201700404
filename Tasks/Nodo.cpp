#ifndef loadTask_H
#define loadTask_H
#include "Task.cpp"
#include <stdlib.h>

class NodoT
{
    private:
    /* data */
    public:
        NodoT * back;
        NodoT * next;
        Task task;
        NodoT(Task &task);
    
};

NodoT::NodoT(Task &task){
    this->task = task;
    this->back = NULL;
    this->next = NULL;
}




#endif