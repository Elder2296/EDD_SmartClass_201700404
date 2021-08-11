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
        string carnet, dpi, name;
        getline(stream, carnet, delimitador);
        getline(stream, dpi, delimitador);
        getline(stream, name, delimitador);
        
        int newDpi = atoi(dpi.c_str());
        int newCarnet= atoi(carnet.c_str());
        Student * stud = new Student(newDpi,newCarnet,name);
        list->insert(*stud);
    }
    list->print();
    //cout<<"llego aca"<<endl;
}

#endif