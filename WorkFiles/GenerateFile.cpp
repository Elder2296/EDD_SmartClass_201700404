#ifndef GENERATE_H
#define GENERATEFILE_H

#include "../DoubleList/DoubleList.cpp"
#include "../Tasks/doubleList.cpp"
#include <iostream>
#include <fstream>


class GenerateFile
{
private:
    /* data */
public:
    GenerateFile(/* args */);
    void generateFileUsers();
    void generateFileTasks();
    
};

GenerateFile::GenerateFile(/* args */)
{
}
void GenerateFile::generateFileUsers(){
    List *list = List::getList();

    ofstream file;

    file.open("/home/losa/Ciencias_y_Sistemas/2021/Segundo_Semestre/Lab_Estructuras/Fase1/EDD_SmartClass_201700404/Archivos_DOT/users.dot");
    Nodo * aux = list->first;
    file<<"digraph A{\n";
    file<<"rankdir = LR;\n";
    do{
        /*cout<<"carnet: "<<aux->student.getCarnet()<<endl;
        aux = aux->next;*/
        file<<"node "<<"[shape = box label=\"Carnet: "<<aux->student.getCarnet()<<"\\nDPI: "<<aux->student.getDpi()<<"\\nNombre: "<<aux->student.getName()<<"\\nCarrera: "<<aux->student.getCarrera()<<"\\nPassword: "<<aux->student.getPass()<<"\\nCreditos: "<<aux->student.getCredits()<<"\\nEdad: "<<aux->student.getAge()<<"\\n Email: "<<aux->student.getMail()<<"\"] "<<aux->student.getCarnet()<<"\n";
        aux= aux->next;

    }while (aux!= list->first);

    do{
        
        file<<aux->student.getCarnet()<<" -> "<<aux->next->student.getCarnet() <<"\n";
        file<<aux->next->student.getCarnet()<<" -> "<<aux->next->back->student.getCarnet() <<"\n";
        
        aux= aux->next;

    }while (aux!= list->last);

    file<<list->first->student.getCarnet()<<" -> "<<list->last->student.getCarnet()<<"\n";
    file<<list->last->student.getCarnet()<<" -> "<<list->first->student.getCarnet()<<"\n";
    file<<"}\n";
            
        
    
    file.close();
    cout<<"archivo generado con exito"<<endl;



}
void GenerateFile::generateFileTasks(){
    doubleList * list = doubleList::getList();
    ofstream file;

    file.open("/home/losa/Ciencias_y_Sistemas/2021/Segundo_Semestre/Lab_Estructuras/Fase1/EDD_SmartClass_201700404/Archivos_DOT/tasks.dot");
    
    file<<"digraph A{\n";
    file<<"rankdir = LR;\n";

    NodoT *aux = list->first;

    while (aux!=NULL){
        if(aux->casilla.task.getId()==-1){
            
            file<<"node [shape = box label = \"SIN TAREA ASIGNADA \"]"<<aux->casilla.id<<"\n";
        }else{
            file<<"node [shape = box label = \"Carnet: "<<aux->casilla.task.getCarnet()<<"\\nNombre:"<<aux->casilla.task.getName()<<"\\nDescription: ..."<<"\\nMateria: "<<aux->casilla.task.getMateria()<<"\\nFecha: "<<aux->casilla.task.getDate()<<"\\nHora: "<<aux->casilla.task.getHour()<<"\\nEstado: "<<aux->casilla.task.getState()<<"\"]"<<aux->casilla.id<<"\n";      
        }
        
        aux = aux->next;
    }
    NodoT *aux2 = list->first;
    while(aux2->next!=NULL){
        file<<aux2->casilla.id<<" -> "<<aux2->next->casilla.id<<"\n";
        file<<aux2->next->casilla.id<<" -> "<<aux2->casilla.id<<"\n";
        aux2 = aux2->next;
        
    }
    
    file<<"}\n";
    file.close();
    cout<<"archivo generado con exito"<<endl;

}

#endif


