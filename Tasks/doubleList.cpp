#ifndef doubleList_H
#define doubleList_H
#include "Nodo.cpp"
class doubleList
{
    private:
    /* data */
    public:
        NodoT * first;
        NodoT * last;
        doubleList(/* args */);
        void insert(Casilla casilla);
        void print();
        static doubleList * getList();
        Task &searchForIndex(int id);
        Task &getTask(int carnet);
        void insertWithIndex(int index, Task task);
        
    
};

doubleList::doubleList(/* args */){
    this->first  = NULL;
    this->last = NULL;
}
Task &doubleList::searchForIndex(int id){
    NodoT * aux = this->first;
    Task * task;
    while(aux != NULL){
        if(aux->casilla.id == id){
            task = &(aux->casilla.task);
            break;
        }
        aux = aux->next;
    }
    return *task;
}
void doubleList::insertWithIndex(int index, Task task){
    NodoT * aux = this->first;
    while (aux != NULL){
        if(aux->casilla.id == index){
            aux->casilla.task = task;
        }
        aux = aux->next;
    }
    
}
Task &doubleList::getTask(int carnet){
    NodoT * aux = this->first;
    while(aux != NULL){
        if(aux->casilla.task.getCarnet() == carnet){

            break;     

        }
        aux = aux->next;
    }
    return aux->casilla.task;
}
void doubleList::insert(Casilla casilla){
    NodoT * newNodo = new NodoT(casilla);
    if(this->first == NULL){
        this->first = newNodo;
        this->last = newNodo;
        this->first->back = NULL;
        this->last->next = NULL;
    }else{
        NodoT * aux = this->last;

        aux->next = newNodo;
        newNodo->next = NULL;
        newNodo->back = aux;
        this->last = newNodo;
        this->last->next = NULL;
    }

}

void doubleList::print(){
    NodoT * aux = this->first;

    while(aux != NULL){
        cout<<"id task: "<<aux->casilla.task.getId()<<endl;
        aux = aux->next;

    }
}




doubleList * doubleList::getList(){
    static doubleList list;
    return &list;
}





#endif