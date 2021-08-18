#ifndef GENERATE_H
#define GENERATEFILE_H

#include "../DoubleList/DoubleList.cpp"
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
        file<<"node "<<"[label=\""<<aux->student.getName()<<"\"] "<<aux->student.getCarnet()<<"\n";
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
    
}

#endif


