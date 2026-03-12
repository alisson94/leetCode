#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _investor{

    int id;
    char name[10];
    
    } Investor;

Investor *create(int id, char *name){
    Investor *_investor = (Investor*) malloc(sizeof(Investor));
    _investor->id = id;
    strcpy(_investor->name, name);

    return _investor;
}

int main(){

}