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
    void  getTaskofLineation();
    void getPosicion();
    void generateTxt();
    
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
void  GenerateFile::getTaskofLineation(){
    cout<<"ingrese la hora"<<endl;
    int hour;
    cin>>hour;
    cout<<"Ingrese el mes"<<endl;
    int mes;
    cin>>mes;
    cout<<"Ingrese el dia"<<endl;
    int day;
    cin>>day;
    
    int  index = (hour-8)+9*((day-1)+30*(mes-7));
    doubleList * list = doubleList::getList();
    Task * task = &list->searchForIndex(index);
    if(task->getId()!=-1){
            cout<<"Carnet: "<<task->getCarnet()<<endl;
            cout<<"Nombre: "<<task->getDescription()<<endl;
            cout<<"Materia: "<<task->getMateria()<<endl;
            cout<<"Fecha: "<<task->getDate()<<endl;
            cout<<"Hora: "<<task->getHour()<<endl;
            cout<<"Estado: "<<task->getState()<<endl;
            cout<<"\n\n"<<endl;
            

        }else{
            cout<<"\n\nPosicion vacia!!\n\n"<<endl;
        }

    
}
void GenerateFile::generateTxt(){
    ofstream file;
    List * list = List::getList();
    doubleList * lst = doubleList::getList();

    file.open("/home/losa/Ciencias_y_Sistemas/2021/Segundo_Semestre/Lab_Estructuras/Fase1/EDD_SmartClass_201700404/Archivos_DOT/Students.txt");
    file<<"¿Elemets?\n";
    Nodo * aux = list->first;
    do{
        file<<"\t¿element type=\"user\"?\n";
        file<<"\t\t¿item Carnet = \""<<aux->student.getCarnet()<<"\" $?\n";
        file<<"\t\t¿item DPI = \""<<aux->student.getDpi()<<"\" $?\n";
        file<<"\t\t¿item Nombre = \""<<aux->student.getName()<<"\" $?\n";
        file<<"\t\t¿item Carrera = \""<<aux->student.getCarrera()<<"\" $?\n";
        file<<"\t\t¿item Password = \""<<aux->student.getPass()<<"\" $?\n";
        file<<"\t\t¿item Creditos = "<<aux->student.getCredits()<<" $?\n";
        file<<"\t\t¿item Edad = "<<aux->student.getAge()<<" $?\n";
        
        file<<"\t¿$element?\n";
        
        NodoT * temp = lst->first;
        while(temp != NULL){
            if(temp->casilla.task.getId()!=-1){
                if(temp->casilla.task.getCarnet() == aux->student.getCarnet()){
                    file<<"\t¿element type=\"task\"?\n";
                        file<<"\t\t¿item Carnet = \""<<temp->casilla.task.getCarnet()<<"\" $?\n";
                        file<<"\t\t¿item Nombre = \""<<temp->casilla.task.getName()<<"\" $?\n";
                        file<<"\t\t¿item Descripcion = \""<<temp->casilla.task.getDescription()<<"\" $?\n";
                        file<<"\t\t¿item Materia = \""<<temp->casilla.task.getMateria()<<"\" $?\n";
                        file<<"\t\t¿item Fecha = \""<<temp->casilla.task.getDate()<<"\" $?\n";
                        file<<"\t\t¿item Hora = \""<<temp->casilla.task.getHour()<<"\" $?\n";
                        file<<"\t\t¿item Estado = \""<<temp->casilla.task.getState()<<"\" $?\n";
        
                    file<<"\t¿$element?\n";
                }
            }
            

            temp = temp->next;

        }

        aux = aux->next;

    }while(aux != list->first);
    
    file<<"¿$Elemets?\n";
    file.close();
    cout<<"Reporte .txt generado!!!"<<endl;

}

void GenerateFile::getPosicion(){
    cout<<"ingrese la hora"<<endl;
    int hour;
    cin>>hour;
    cout<<"Ingrese el mes"<<endl;
    int mes;
    cin>>mes;
    cout<<"Ingrese el dia"<<endl;
    int day;
    cin>>day;
    
    int  index = (hour-8)+9*((day-1)+30*(mes-7));
    cout<<"La posicion donde se encuentra la tareas es: "<<index<<endl;        
}

#endif


