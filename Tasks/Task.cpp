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
    string falsedate;
    Date  date;
    int hour;
    string state;
    /* data */
public:
    static int identi;
    
    Task();
    Task(int id, int carnet, string nombre, string description, string materia, Date &date, int hour, string state, string falsedate );
    int getId();
    int getCarnet();
    string getName();
    string getDescription();
    string getMateria();
    string getDate();
    string getHour();
    string getState();
    void setCarnet(int carnet);
    void ChangeDate();
    
      
};
int Task::identi=1;



Task::Task(int id, int carnet, string nombre, string description, string materia, Date &date, int hour, string state,string falsedate ){
    this->id = id;
    this->carnet = carnet;
    this->taskname  = nombre;
    this->description  = description;
    this->materia  = materia;
    this->date = date;
    this->hour = hour;
    this->state = state;
    this->falsedate = falsedate;
    
}
Task::Task(){this->id = -1;this->carnet = -1;}
int Task::getId(){return this->id;}
int Task::getCarnet(){return this->carnet;}
string Task::getName(){return this->taskname;}
string Task::getDescription(){return this->description;}
string Task::getMateria(){return this->materia;}
string Task::getDate(){return to_string(this->date.getDay())+"/"+to_string(this->date.getMounth())+"/"+to_string(this->date.getYear());}
string Task::getHour(){return to_string(this->hour)+":00";}
string Task::getState(){return this->state;}
void Task::setCarnet(int carnet){this->carnet = carnet;}
void Task::ChangeDate(){this->falsedate = this->getDate();}


#endif

