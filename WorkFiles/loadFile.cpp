#ifndef LOADFILE_H
#define LOADFILE_H
#include <regex>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include "../DoubleList/DoubleList.cpp"
#include "../Errors/Cola.cpp"

using namespace std;


class loadFile
{
private:
    /* data */
public:
    loadFile(/* args */);
    void loadStudents(string path);
    bool validarCorreo(const string&);
};

loadFile::loadFile(/* args */){
}
void loadFile::loadStudents(string path){
    List * list = List::getList();
    Cola * cola = Cola::getCola();
    string url = path.c_str();

    
    ifstream file(url);

    string line;
    char delimitador=',';
    
    getline(file, line);

    while(getline(file,line)){
        //cout<<line<<endl;

        stringstream stream(line);
        string carnet, dpi, name,run,email,pass,credits,age;
        getline(stream, carnet, delimitador);
        getline(stream, dpi, delimitador);
        getline(stream, name, delimitador);
        getline(stream, run, delimitador);
        getline(stream, pass, delimitador);
        getline(stream, credits, delimitador);
        getline(stream, age, delimitador);
        getline(stream, email, delimitador);
        int newCredits = atoi(credits.c_str());
        int newAge = atoi(age.c_str());
        int newCarnet= atoi(carnet.c_str());
        Student * stud = new Student(dpi,newCarnet,name,run,email,pass,newCredits,newAge);

        if(!(carnet.length()==9)){
            Error * error = new Error(Error::index,stud->getCarnet(),"Estudiante","Se encontro un error en la longitud del carnet");
            Error::index = Error::index+1;
            cout<<"Error en tamaño de carnet"<<endl;
            cola->push(*error);
            
            

        }
        if(!(dpi.length()==13)){
            Error * error = new Error(Error::index,stud->getCarnet(),"Estudiante","Se encontro un error en la longitud del DPI");
            Error::index = Error::index+1;
            cout<<"Error en tamaño de DPI"<<endl;
            cola->push(*error);
                

        }
        if(!(validarCorreo(email))){
            Error * error = new Error(Error::index,stud->getCarnet(),"Estudiante","El correo no presenta el formato debido");
            Error::index = Error::index+1;
            cout<<"Error en formato de correo"<<endl;
            cola->push(*error);
                      
        }
        list->insert(*stud);
        
        
        
        

        
    }
    //list->print();
    //cout<<"llego aca"<<endl;
}
bool loadFile::validarCorreo(const string& mail){
    const regex exReg("([a-z0-9]|[A-Z])+((.[a-z0-9]+)|[A-Z])*@([a-z0-9]|[A-Z])+(.([a-z0-9]|[A-Z])+)*(.([a-z]{2,3}|[A-Z]))");
    return regex_match(mail,exReg);
}

#endif