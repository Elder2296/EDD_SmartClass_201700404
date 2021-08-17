#ifndef Task_H
#define Task_H
#include <iostream>
#include "Date.cpp"
using namespace std;



class Task
{
    private:
    int id;
    int carnet;
    string taskname;
    string description;
    string materia;
    Date  date;
    int hour;
    string state;
    /* data */
public:
    static int identi;
    
    Task();
    Task(int id, int carnet, string nombre, string description, string materia, Date &date, int hour, string state );
    int getId();
      
};
int Task::identi=1;



Task::Task(int id, int carnet, string nombre, string description, string materia, Date &date, int hour, string state ){
    this->id = id;
    this->carnet = carnet;
    this->taskname  = nombre;
    this->description  = description;
    this->materia  = materia;
    this->date = date;
    this->hour = hour;
    this->state = state;
    
}
Task::Task(){this->id = -1;}
int Task::getId(){return this->id;}




#endif

