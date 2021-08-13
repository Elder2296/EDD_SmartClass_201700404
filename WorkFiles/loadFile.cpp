#ifndef LOADFILE_H
#define LOADFILE_H

#include <fstream>
#include <sstream>
#include <cstdlib>
#include "../DoubleList/DoubleList.cpp"

using namespace std;


class loadFile
{
private:
    /* data */
public:
    loadFile(/* args */);
    void loadStudents(string path);
};

loadFile::loadFile(/* args */)
{
}
void loadFile::loadStudents(string path){
    List * list = List::getList();
    string url = path.c_str();

    
    ifstream file(url);

    string line;
    char delimitador=',';
    
    getline(file, line);

    while(getline(file,line)){
        cout<<line<<endl;

        stringstream stream(line);
        string carnet, dpi, name,run,email,pass,credits,age;
        getline(stream, carnet, delimitador);
        getline(stream, dpi, delimitador);
        getline(stream, name, delimitador);
        getline(stream, run, delimitador);
        getline(stream, email, delimitador);
        getline(stream, pass, delimitador);
        getline(stream, credits, delimitador);
        getline(stream, age, delimitador);

        int newDpi = atoi(dpi.c_str());
        int newCarnet= atoi(carnet.c_str());
        int newCredits = atoi(credits.c_str());
        int newAge = atoi(age.c_str());

        Student * stud = new Student(newDpi,newCarnet,name,run,email,pass,newCredits,newAge);
        list->insert(*stud);
    }
    list->print();
    //cout<<"llego aca"<<endl;
}

#endif