#include <iostream>
#include <cmath>
#include <string>
using namespace std;
int main() {
	string type;
	double answer = 0.0;{}
	double number_1 = 0.0;{}
	double number_2 = 0.0;{}
	cout << "Select your calculation type \nAddition\nSubtraction\nMultiplication\nDivision\n";
	cin >> type;
	if (type == "Addition") {
		answer = (number_1 + number_2);
	}
	else if (type == "Subtraction") {
		answer = (number_1 - number_2);
	}
	else if (type == "Multiplication") {
		answer = (number_1 * number_2);
	}
	else if (type == "Division") {
		answer = (number_1 / number_2);
	}
	else
		cout << "Please enter a valid calculation type.\n";

}