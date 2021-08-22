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
        void subMenuCola();
        void loadTasksMenu();
        void MenuCorrections();
        bool validarCorreo(const string& mail);
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
void Menu::subMenuCola(){
    cout<<"\n\n"<<endl;
    cout<<"1    Corregir errores"<<endl;
    cout<<"2    generar grafo "<<endl;
    int option;
    cin>>option;
    GenerateFile generator;
    Cola * cola =  Cola::getCola();
    if(option == 1){
        if(cola->tamanio == 0){
            cout<<"\n\nNo hay errores que corregir!!!\n\n"<<endl;

        }else{
            cout<<"id: "<<cola->getOut().index<<endl;
            cout<<"tipo: "<<cola->getOut().type<<endl;
            cout<<"Description: "<<cola->getOut().description<<"\n"<<endl;
            this->MenuCorrections();
        }

    }else if(option == 2){
        
        if(cola->tamanio == 0 ){
            cout<<"\n\n No hay ningun error.\n\n"<<endl;
        }else{
            generator.generateCola();
        }

    }
    this->principal();
    
    
}
void Menu::MenuCorrections(){
    Cola *cola = Cola::getCola();
    List * students = List::getList();
    doubleList * tasks = doubleList::getList();
    if(cola->getOut().type=="Estudiante"){
        cout<<"1    Corregir Carnet"<<endl;
        cout<<"2    Corregir DPI"<<endl;
        cout<<"3    Corregir Correo"<<endl;
        int option;
        cin>>option;
        if(option == 1){
            cout<<"Carnet actual: "<<students->getStudent(cola->getOut().id).getCarnet()<<endl;
            bool condition = true;
            while(condition){
                cout<<"ingrese el nuevo carnet: "<<endl;
                string carnet;
                cin>>carnet;
                if(carnet.length()==9){
                    int newCarnet= atoi(carnet.c_str());
                    students->getStudent(cola->getOut().id).setCarnet(newCarnet);
                    condition = false;
                }
            }
        }else if(option == 2){
            cout<<"DPI actual: "<<students->getStudent(cola->getOut().id).getDpi()<<endl;
            bool condition = true;
            while(condition){
                cout<<"ingrese el nuevo DPI: "<<endl;
                string dpi;
                cin>>dpi;
                if(dpi.length()==13){
                    //int newCarnet= atoi(carnet.c_str());
                    students->getStudent(cola->getOut().id).setDpi(dpi);
                    condition = false;
                }
            }

        }else if(option == 3){
            cout<<"Correo actual: "<<students->getStudent(cola->getOut().id).getMail()<<endl;
            bool condition = true;
            while(condition){
                cout<<"ingrese el nuevo correo: "<<endl;
                string correo;
                cin>>correo;
                if(validarCorreo(correo)){
                    //int newCarnet= atoi(carnet.c_str());
                    students->getStudent(cola->getOut().id).setMail(correo);
                    condition = false;
                }
            }

        }

        
    }else if(cola->getOut().type == "Task"){
        cout<<"1    Corregir Carnet"<<endl;
        cout<<"2    Corregir Fecha"<<endl;
        int option;
        cin>>option;
        if(option ==  1){
            cout<<"Carnet actual: "<<tasks->getTask(cola->getOut().id).getCarnet()<<endl;
            bool condition = true;
            while(condition){
                cout<<"ingrese el nuevo carnet: "<<endl;
                string carnet;
                cin>>carnet;
                if(carnet.length()==9){
                    int newCarnet= atoi(carnet.c_str());
                    if(students->search(newCarnet)){
                        tasks->getTask(cola->getOut().id).setCarnet(newCarnet);
                        students->getStudent(cola->getOut().id).setCarnet(newCarnet);
                        condition = false;
                    }
                    
                }
            }
            
        }else if(option == 2){
            tasks->getTask(cola->getOut().id).ChangeDate();
            
        }
    }
    cout<<"CAMBIO HECHO CORRECTAMENTE!!!"<<endl;
    cola->pop();
    this->subMenuCola();

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
        this->subMenuCola();
        

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
bool Menu::validarCorreo(const string& mail){
    const regex exReg("([a-z]|[A-Z]|[0-9]|.)+@([a-z]|[A-Z])+(.([a-z]|[A-Z]))+");
    return regex_match(mail,exReg);
}