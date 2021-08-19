#include <iostream>
#include "./Menu/Menu.cpp"
#include "./DoubleList/DoubleList.cpp"
#include "./Tasks/doubleList.cpp"





int main(){
    /*cout<<"Paso aca"<<endl;
     Task * matriz[5][30][9];

    for (int f = 0; f < 5; f++){
        
        for (int  i = 0; i < 30; i++){
            
            for (int d = 0; d < 9; d++){
            
                matriz[f][i][d] = new Task();
            }
            
        }
        
    }
    for (int f = 0; f < 5; f++){
       
        for (int  i = 0; i < 30; i++){
            
            for (int d = 0; d < 9; d++){
                
                cout<<"el id: "<<matriz[f][i][d]->getId()<<endl;
            }
            
        }
        
    }*/

    new Menu();
    /*doubleList * list =  doubleList::getList();
    
    //int id, int carnet, string nombre, string description, string materia, Date &date, int hour, string state
    Date * date = new Date(2021,8,14);

    Task * task = new Task(Task::identi,201700404,"elder","saber","materia",*date,8,"state");
    Task::identi = Task::identi+1;
    Task * task2 = new Task(Task::identi,201700404,"elder","saber","materia",*date,8,"state");
    Task::identi = Task::identi+1;
    Task * task3 = new Task(Task::identi,201700404,"elder","saber","materia",*date,8,"state");
    Task::identi = Task::identi+1;
    Task * task4 = new Task(Task::identi,201700404,"elder","saber","materia",*date,8,"state");
    Task::identi = Task::identi+1;
    Task * task5 = new Task(Task::identi,201700404,"elder","saber","materia",*date,8,"state");
    
    list->insert(*task);
    list->insert(*task2);
    list->insert(*task3);
    list->insert(*task4);
    list->insert(*task5);
    list->print();*/
    
    
    /*List * list = List::getList();
    Student * student3 = new Student(123,247,"Mary");
    Student * student1 = new Student(456,245,"Elder");
    Student * student2 = new Student(789,246,"Ariel");

    list->insert(*student1);
    list->insert(*student2);Carnet: 
    list->insert(*student3);
    
    list->print();*/
    
    system("PAUSE");
    return 0;

}