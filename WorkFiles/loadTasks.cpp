#ifndef LOADTASKS_H
#define LOADTASKS_H
#include <iostream>
#include "../Tasks/Task.cpp"
#include "../DoubleList/DoubleList.cpp"
#include "../Tasks/doubleList.cpp"
#include "Casilla.cpp"
#include <fstream>
#include <sstream>
#include <cstdlib>


using namespace std;


class loadTasks{
    private:
    Task * tasks [5][30][9];
    /* data */

    public:
        loadTasks(/* args */);
        void load(string path);
        void initMatriz();
        bool existCarnet(int carnet);
        void printMatriz();
        void lineation();
};

loadTasks::loadTasks(/* args */){
    this->initMatriz();
}
void loadTasks::initMatriz(){
    for (int fil = 0; fil < 5; fil++){
        for (int col = 0; col < 30; col++){
            for (int d = 0; d < 9; d++){
                tasks[fil][col][d] = new Task();
            }
            
        }
        
    }
    
}

void loadTasks::printMatriz(){
    for (int fil = 0; fil < 5; fil++){
        for (int col = 0; col < 30; col++){
            for (int d = 0; d < 9; d++){
                cout<<"id: "<<tasks[fil][col][d]->getId()<<endl;
            }
            
        }
        
    }
    
}

void loadTasks::load(string path){
    string url = path.c_str();

    ifstream file(url);

    string line;
    char delimitador=',';
    List * students = List::getList();
    
    while(getline(file,line)){
        //cout<<"paso aca"<<endl;
        stringstream stream(line);
        string mounth, day, hour,carnet, name,description,course,date,state;

        getline(stream, mounth, delimitador);
        getline(stream, day, delimitador);
        getline(stream, hour, delimitador);
        getline(stream, carnet, delimitador);
        getline(stream, name, delimitador);
        getline(stream, description, delimitador);
        getline(stream, course, delimitador);
        getline(stream, date, delimitador);
        getline(stream, state, delimitador);
        
        
        
        int newCarnet =  atoi(carnet.c_str());
        if(students->search(newCarnet)){
            cout<<"encontro coincidencia"<<endl;
            int fil = atoi(mounth.c_str());
            int col = atoi(day.c_str());
            int  d = atoi(hour.c_str());
            Date *date = new Date(2021,fil,col);
            if(fil > 6 && fil<12 ){
                if(col >0 && col < 31){
                    if(d > 7 && d < 17){
                        tasks[fil-1-6][col-1][d-1-7]  = new Task(Task::identi,newCarnet,name,description,course,*date,d,state);
                        Task::identi = Task::identi+1;
                    }else{
                        cout<<"Error en el la hora"<<endl;
                    }
                }else{
                    cout<<"error en el día"<<endl;
                }
            }else{
                cout<<"Error en el mes"<<endl;
            }
            //Task * homework 
            
        }else{
            cout<<"Error not found carnet"<<endl;
            //Error
        }
        //cout<<"carnet: "<<carnet<<endl;
    }
    //this->printMatriz();
    this->lineation();
}
bool loadTasks::existCarnet(int carnet){
    List * students  = List::getList();
    return students->search(carnet);
}


void loadTasks::lineation(){
    doubleList * list = doubleList::getList();
    Casilla * vector[1350];
    int id = 0; 
    for (int  i = 0; i < 5; i++){
        for (int j = 0; j < 30; j++){
            for (int k = 0; k < 9; k++){
                //tasks[i][j][k]
                vector[k+9*(j+30*i)] = new Casilla(id,*tasks[i][j][k]);
                id++;
            }
                    
            
        }
        
    }

    for (int i = 0; i < 1350; i++){
        list->insert(*vector[i]);
    }
    
    list->print();
    
}




#endif