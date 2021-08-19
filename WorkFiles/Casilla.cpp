#ifndef Casilla_H
#define Casilla_H

#include "../Tasks/Task.cpp"

class Casilla
{
private:
    /* data */
public:
    int id;
    Task  task;
    Casilla(/* args */);
    Casilla(int id, Task &task);
};

Casilla::Casilla(/* args */)
{
}

Casilla::Casilla(int id, Task &task){
    this->id = id;
    this->task = task;
}





#endif 