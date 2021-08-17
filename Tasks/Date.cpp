#ifndef DATE_H
#define DATE_H

class Date
{
    private:
        int day;
        int mounth;
        int year;
        /* data */
    public:
        Date();
        Date(int year, int mounth, int day);
        int getDay();
        int getYear();
        int getMounth();    
};

Date::Date(int year, int mounth, int day){
    this->year= year;
    this->mounth = mounth;
    this->day = day;
}
Date::Date(){
    this->year=2021;
    this->mounth = 8;
    this->day = 17;
}

int Date::getDay(){return this->day;}
int Date::getMounth(){return this->mounth;}
int Date::getYear(){return this->year;}






#endif