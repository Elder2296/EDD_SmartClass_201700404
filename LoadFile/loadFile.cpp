#include <iostream>

#include <fstream>
#include <sstream>

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
    cout<<"the path: "<<path<<endl;
    string url = path.c_str();

    cout<<"nuevo path: "<<url<<endl;
    ifstream file(url);

    string line;
    char delimitador=',';
    
    getline(file, line);

    while(getline(file,line)){
        cout<<line<<endl;
    }

    cout<<"llego aca"<<endl;
}

