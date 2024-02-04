#include <iostream>
#include <string.h>

using namespace std;

float sum(float vector[4]);
void displayNotes(float notes[4]);
float average(float number, int spaces);

int main() {
    
    int number_tests = 0;
    float notes_for_test[4];

    cout << "Quantos periodos avaliativos:\n";
    cin >> number_tests;

    for (int idc = 0; idc < number_tests; idc++) {
        cout << "Entre com sua nota, utilize '.' no lugar de virgula:\n:";
        cin >> notes_for_test[idc];
    }

    //estudar ponteiros para melhorar essa parte 

    if(number_tests >= 4){

        float big_number = sum(notes_for_test);
        float your_arvarege = average(big_number, number_tests);
        cout <<"media: " << your_arvarege <<"\n";
            if(your_arvarege < 7){
                cout << "pegou exame!!";
            }
            displayNotes(notes_for_test); 
    }

    else{
        int rest_of_periods = 4 - number_tests;
        float imcomplet_big_number = sum(notes_for_test);
        float rest = 28 - imcomplet_big_number;
        float imcomple_arverage = average(rest, rest_of_periods );
        cout << "vc precissa de: " << imcomple_arverage <<" em "<< rest_of_periods <<" periodos\n";
            if(imcomple_arverage > 10){
                cout << "pegou exame!!"; 
            }
            displayNotes(notes_for_test);
    }
    system("pause");
    return 0;
}

float sum(float vector[4]) {
    float result = 0.0;

    for (int i = 0; i < 4; i++) {
        result += vector[i];
    }

    return result; 
}

void displayNotes(float notes[4]) {
    cout << "Notas inseridas:\n ";
    for (int i = 0; i < 4; i++) {
        cout << "[" << notes[i] << "]\n";
    }
}

float average(float number, int spaces){
    float average = number / spaces; 

    return average;
}