#ifndef DATE_H
#define DATE_H
#include <iostream>
using namespace std;

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
        string getYYMMDD();    
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
string Date::getYYMMDD(){
    string d;
    string m;
    if(this->day < 10){
        d = "0"+to_string(this->day);
    }else{
        d = to_string(this->day);
    }
    if(this->mounth < 10){
        m = "0"+to_string(this->mounth);
    }else{
        m = to_string(this->mounth);
    }
    return to_string(this->year)+"/"+m+"/"+d;
}

int Date::getDay(){return this->day;}
int Date::getMounth(){return this->mounth;}
int Date::getYear(){return this->year;}






#endif