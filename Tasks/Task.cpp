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
    int getCarnet();
    string getName();
    string getDescription();
    string getMateria();
    string getDate();
    string getHour();
    string getState();
    
      
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
int Task::getCarnet(){return this->carnet;}
string Task::getName(){return this->taskname;}
string Task::getDescription(){return this->description;}
string Task::getMateria(){return this->materia;}
string Task::getDate(){return to_string(this->date.getDay())+"/"+to_string(this->date.getMounth())+"/"+to_string(this->date.getYear());}
string Task::getHour(){return to_string(this->hour)+":00";}
string Task::getState(){return this->state;}


#endif

