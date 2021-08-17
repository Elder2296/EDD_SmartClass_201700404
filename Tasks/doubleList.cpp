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
        void insert(Task task);
        void print();
        static doubleList * getList();
    
};

doubleList::doubleList(/* args */){
    this->first  = NULL;
    this->last = NULL;
}
void doubleList::insert(Task task){
    NodoT * newNodo = new NodoT(task);
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
        cout<<"id task: "<<aux->task.getId()<<endl;
        aux = aux->next;

    }
}




doubleList * doubleList::getList(){
    static doubleList list;
    return &list;
}





#endif