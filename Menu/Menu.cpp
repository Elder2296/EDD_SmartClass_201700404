#ifndef MENU_H
#define MENU_H
#include <iostream>
#include <string>
#include "../WorkFiles/loadFile.cpp"
#include "../WorkFiles/GenerateFile.cpp"
#include "../WorkFiles/loadTasks.cpp"
#include <regex>



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
        void CargaManualUser();
        void CargaManualTask();
        void ChangeUser();
        void ChangeTask();
        
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
void Menu::ChangeUser(){
    List * list = List::getList();
    bool condition = true;
    string dpi;
    while(condition){
        cout<<"Ingrese el DPI: "<<endl;
        cin>>dpi;
        if(dpi.length()== 13){
            if(list->searchDPI(dpi)){
                condition = false;         
            }
        }
    }
    Student  stud = list->getStudent(dpi);
    cout<<"------------------------------------------"<<endl;
    cout<<"DPI: "<<stud.getDpi()<<endl;
    cout<<"Carnet: "<<stud.getCarnet()<<endl;
    cout<<"Nombre: "<<stud.getName()<<endl;
    cout<<"Carrera: "<<stud.getCarrera()<<endl;
    cout<<"Email: "<<stud.getMail()<<endl;
    cout<<"Password: "<<stud.getPass()<<endl;
    cout<<"Creditos: "<<stud.getCredits()<<endl;
    cout<<"Edad: "<<stud.getAge()<<endl;
    cout<<"------------------------------------------"<<endl;
    
    
    cout<<"1    Cambiar Nombre: "<<endl;
    cout<<"2    Cambiar Carrera: "<<endl;
    cout<<"3    Cambiar Email: "<<endl;
    cout<<"4    Cambiar Password: "<<endl;
    cout<<"5    Cambiar Creditos: "<<endl;
    cout<<"6    Cambiar Edad: "<<endl;
    cout<<"\nIngrese una opcion:"<<endl;
    int t;
    cin>>t;
    if(t == 1){
        cout<<"\nIngrese nuevo nombre:"<<endl;
        string name;
        cin>>name;
        list->getStudent(dpi).setName(name);

    }else if(t == 2){
        cout<<"\nIngrese nueva carrera:"<<endl;
        string carrera;
        cin>>carrera;
        list->getStudent(dpi).setCarrera(carrera);
    }else if(t == 3){
        condition = true;
        string mail;
        while(condition){
            cout<<"\nIngrese nuevo correo:"<<endl;
            string mail;
            cin>>mail;
            if(validarCorreo(mail)){
                condition = false;
            }
        }
        
        list->getStudent(dpi).setMail(mail);
    }else if(t == 4){
        cout<<"\nIngrese nueva contraseña:"<<endl;
        string pass;
        cin>>pass;
        list->getStudent(dpi).setPass(pass);
    }else if(t == 5){
        cout<<"\nIngrese nuevos creditos:"<<endl;
        int cre;
        cin>>cre;
        list->getStudent(dpi).setCredits(cre);
        
    }else if(t == 6){
        cout<<"\nIngrese nueva edad:"<<endl;
        int edad;
        cin>>edad;
        list->getStudent(dpi).setAge(edad);
        
    }
    this->principal();
    
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
void Menu::ChangeTask(){
    doubleList * list = doubleList::getList();
    List * students = List::getList();
    bool condition = true;
    int index;
    while(condition){
        cout<<"Ingrese el INDEX: "<<endl;
        cin>>index;
        if(index>= 0 && index <= 1350){
            condition = false;
        }
    }
    Task task = list->searchForIndex(index);
    cout<<"------------------------------------------"<<endl;
    
    cout<<"Carnet: "<<task.getCarnet()<<endl;
    cout<<"Nombre: "<<task.getName()<<endl;
    cout<<"Description: "<<task.getDescription()<<endl;
    cout<<"Materia: "<<task.getMateria()<<endl;
    cout<<"Fecha: "<<task.getDate()<<endl;
    cout<<"Hora: "<<task.getHour()<<endl;
    cout<<"Estado: "<<task.getState()<<endl;
    cout<<"------------------------------------------"<<endl;
    
    
    cout<<"1    Cambiar Carnet: "<<endl;
    cout<<"2    Cambiar Nombre: "<<endl;
    cout<<"3    Cambiar Description: "<<endl;
    cout<<"4    Cambiar Materia: "<<endl;
    cout<<"5    Cambiar Fecha: "<<endl;
    cout<<"6    Cambiar Hora: "<<endl;
    cout<<"7    Cambiar estado: "<<endl;
    cout<<"\nIngrese una opcion:"<<endl;
    int t;
    cin>>t;
    
    if(t == 1){
        int newCarnet;
        condition = true;
        while(condition){
            cout<<"\nIngrese nuevo carnet valido:"<<endl;
            string carnet;
            cin>>carnet;
            if(carnet.length() == 9){
                newCarnet = atoi(carnet.c_str());
                if(students->search(newCarnet)){

                }
            }
        }
        
        list->searchForIndex(index).setCarnet(newCarnet);

    }else if(t == 2){
        cout<<"\nIngrese nueva nombre:"<<endl;
        string nombre;
        cin>>nombre;
        list->searchForIndex(index).setName(nombre);
    }else if(t == 3){
        cout<<"\nIngrese nueva Description:"<<endl;
        string desc;
        cin>>desc;
        list->searchForIndex(index).setDescription(desc);
    }else if(t == 4){
        cout<<"\nIngrese nueva Materia:"<<endl;
        string materia;
        cin>>materia;
        list->searchForIndex(index).setMateria(materia);
    }else if(t == 5){
        condition = true;
        int day;
        int mounth;
        while(condition){
            cout<<"\nIngrese nueva dia:"<<endl;
            cin>>day;
            cout<<"\nIngrese nueva mes 7-11:"<<endl;
            cin>>mounth;
            if(day>0 && day<31 && mounth >6 && mounth <12){
                condition = false;
            }
        }
        Date * date = new Date(2021,mounth,day);
        
        list->searchForIndex(index).setFecha(*date);
        
    }else if(t == 6){
        condition = true;
        int hour;
        while(condition){
            cout<<"\nIngrese nueva hora:"<<endl;
            cin>>hour;
            if(hour>7 && hour < 17){
                condition = false;
            }
        }
        
        list->searchForIndex(index).setHour(hour);
        
    }else if(t == 7){
        cout<<"\nIngrese nueva estado:"<<endl;
        string estado;
        cin>>estado;
        list->searchForIndex(index).setState(estado);
    }
    this->principal();
    
}

void Menu::Manual_Input(){
    cout << "\n\n1     Usuarios"<<endl;
    cout << "2     Tareas"<<endl;
    cout << "3     Salir"<<endl;
    cout << "\nIngrese el numero de opcion"<<endl;
    int option;
    cin >>option;
    if(option==3){principal();}
    if(option ==1 ){
        cout << "\n\n1     Nuevo usuario"<<endl;
        cout << "2     Modificar usuario"<<endl;
        cout << "3     Eliminar usuario"<<endl;
        cout << "4     Salir"<<endl;
    
        cout << "\nIngrese el numero de opcion"<<endl;
        int opt;
        cin >>opt;
        if(opt == 1){
            this->CargaManualUser();
        }else if(opt == 4){
            this->principal();
        }else if(opt == 3){
            List * list = List::getList();
            bool condition = true;
            string dpi,carnet;
            while(condition){
                cout<<"Ingrese el DPI:"<<endl;
                cin>>dpi;
                if(dpi.length()== 13){
                    if(list->searchDPI(dpi)){
                        condition = false;
                    }else{
                        cout<<"\n\nIngrese un dpi valido\n\n"<<endl;
                    }
                    

                }

            }
            
            list->Delete(dpi);
            cout<<"Eliminacion exitosa!!!"<<endl;
        }else if(opt == 2){
            this->ChangeUser();
        }

    }else if(option == 2){
        cout << "\n\n1     Nueva Tarea"<<endl;
        cout << "2     Modificar Tarea"<<endl;
        cout << "3     Eliminar Tarea"<<endl;
        cout << "4     Salir"<<endl;
    
        cout << "\nIngrese el numero de opcion"<<endl;
        int opt;
        cin >>opt;
        if(opt == 1){
            this->CargaManualTask();
        }else if(opt == 4){
            this->principal();
        }else if(opt == 3){
            doubleList * list = doubleList::getList();
            bool condition = true;
            int indice;
            while(condition){
                cout<<"Ingrese el indice:"<<endl;
                cin>>indice;
                if(indice>=0 && indice <= 1350){
                    condition =false;
                }
                

            }
            
            list->Delete(indice);
            cout<<"Eliminacion exitosa!!!"<<endl;
        }else if(opt == 2){
            this->ChangeTask();

        }

    }
    this->principal();

}
void Menu::CargaManualUser(){
    List * students = List::getList();
    bool condition = true;
    string dpi,carnet;
    while(condition){
        cout<<"Ingrese el DPI:"<<endl;
        cin>>dpi;
        if(dpi.length()== 13){
            condition = false;
        }

    } 
    condition = true;
    while(condition){
        cout<<"Ingrese el carnet:"<<endl;
        cin>>carnet;
        if(carnet.length()== 9){
            condition = false;
        }

    } 
    //condition = true;
    cout<<"Ingrese el nombre:"<<endl;
    string name;
    cin>>name;
    cout<<"Ingrese el carrera:"<<endl;
    string carrera;
    cin>>carrera;

    string mail;

    condition = true;
    while(condition){
        cout<<"Ingrese el correo:"<<endl;
        cin>>mail;
        if(validarCorreo(mail)){
            condition = false;
        }

    } 
    cout<<"Ingrese el contraseña:"<<endl;
    string pass;
    cin>>pass;

    cout<<"Ingrese el creditos:"<<endl;
    int  credits;
    cin>>credits;


    cout<<"Ingrese el Edad:"<<endl;
    int  age;
    cin>>age;
    int newCarnet= atoi(carnet.c_str());
    Student *st = new Student(dpi,newCarnet,name,carrera,mail,pass,credits,age);
    students->insert(*st);
    cout<<"Se agrego Correctamente!!"<<endl;

    principal();
    
}
void Menu::CargaManualTask(){
    List * students = List::getList();
    doubleList * tareas = doubleList::getList();
    bool condition = true;
    string carnet;
    int newCarnet;
    while(condition){
        cout<<"Ingrese el carnet:"<<endl;
        cin>>carnet;
        if(carnet.length()== 9){
            newCarnet = atoi(carnet.c_str());
            if(students->search(newCarnet)){
                condition = false;
            }
            
        }

    } 
    //condition = true;
    cout<<"Ingrese el nombre de la tarea:"<<endl;
    string name;
    cin>>name;
    cout<<"Ingrese el descripcion:"<<endl;
    string description;
    cin>>description;
    cout<<"Ingrese la materia:"<<endl;
    string materia;
    cin>>materia;

    int day;

    condition = true;
    while(condition){
        cout<<"Ingrese un dia entre 1-30:"<<endl;
        cin>>day;
        if(day >0 && day < 31){
            condition = false;
        }

    } 

    int mounth;

    condition = true;
    while(condition){
        cout<<"Ingrese un dia entre 7-11:"<<endl;
        cin>>mounth;
        if(mounth > 6 && mounth < 12){
            condition = false;
        }

    } 


    int hour;

    condition = true;
    while(condition){
        cout<<"Ingrese un dia entre 8:00-16:00:"<<endl;
        cin>>hour;
        if(hour > 7 && hour < 17){
            condition = false;
        }

    }


    cout<<"Ingrese el estado:"<<endl;
    string estado;
    cin>>estado;
    Date * date = new Date(2021,mounth,day);
    
    int indice  = (hour-8)+9*((day-1)+30*(mounth-7));
    Task * task = new Task(Task::identi,newCarnet,name,description,materia,*date,hour,estado,date->getYYMMDD());
    Task::identi = Task::identi + 1;
    tareas->insertWithIndex(indice, *task);
    cout<<"Se agrego Correctamente!!\n\n"<<endl;

    principal();
    
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

#endif