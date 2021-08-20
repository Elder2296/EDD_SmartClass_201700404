#include <iostream>
#include <string>
#include "../WorkFiles/loadFile.cpp"
#include "../WorkFiles/GenerateFile.cpp"
#include "../WorkFiles/loadTasks.cpp"



using namespace std;
class Menu
{
    private:
        void principal();
        void subMenuUsers();
        void Manual_Input();
        void Reports();
        void loadUsers();
        void subMenuTasks();
        void loadTasksMenu();
    /* data */
public:
    Menu(/* args */);
    
};

Menu::Menu(/* args */)
{
    principal();
}

void Menu::principal(){
    cout << "\n\n******** Principal Menu ********"<<endl;
    cout << "1     Carga de Usuarios"<<endl;
    cout << "2     Carga de Tareas"<<endl;
    cout << "3     Ingreso Manual"<<endl;
    cout << "4     Reportes\n\n"<<endl;
    cout << "Ingrese el numero de opcion"<<endl;
    int option;
    cin >>option;
    if(option == 3){Manual_Input();}
    else if(option == 4){Reports();}
    else if(option ==1){loadUsers();}
    else if(option ==2){loadTasksMenu();}
}
void Menu::subMenuUsers(){
    cout<<"\n\nIngrese la ruta del archivo:"<<endl;
    string path;
    cin>>path;
    cout<<"Archivo cargado"<<endl;

}

void Menu::Manual_Input(){
    cout << "\n\n1     Usuarios"<<endl;
    cout << "2     Tareas"<<endl;
    cout << "3     Salir"<<endl;
    cout << "\nIngrese el numero de opcion"<<endl;
    int option;
    cin >>option;
    if(option==3){principal();}

}
void Menu::Reports(){
    cout<<"\n\n1    Lista de Usuarios "<<endl;
    cout<<"2    Linealizacion de Tareas"<<endl;
    cout<<"3    Busqueda en estructura linealizada"<<endl;
    cout<<"4    Busqueda en posicion de lista linealizada"<<endl;
    cout<<"5    Cola de Errores"<<endl;
    cout<<"6    Codigo generado de salida"<<endl;
    cout<<"7    Regresar al Menu principal\n\n"<<endl;
        
    cout<<"Ingrese el numero de opcion"<<endl;
    int option;
    cin>>option;
    GenerateFile generator;
    if(option==7){principal();}
    else if(option==1){
        
        generator.generateFileUsers();
        
    }else if(option ==2){
        generator.generateFileTasks();
    }else if(option == 3){
        generator.getTaskofLineation();
        
    }else if(option == 4){
        generator.getPosicion();
    }else if(option == 5){

    }else if(option == 6){
        generator.generateTxt();
    } 
    this->principal();


}
void Menu::loadUsers(){

    cout<<"\nIngrese una direccion:"<<endl;
    string path;
    cin>>path;
    loadFile load;
    load.loadStudents(path);
    principal();    

}
void Menu::loadTasksMenu(){

    cout<<"\nIngrese una direccion:"<<endl;
    string path;
    cin>>path;
    loadTasks load;
    
    load.load(path);


    principal();    

}