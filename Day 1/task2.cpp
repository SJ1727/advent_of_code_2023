#include <iostream> 
#include <fstream>
#include <string>

using namespace std; 

std::string numStrings[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

int left_right_sum(std::string s) {
    int string_length = s.length();
    int sum = 0;
    int left = 0;
    char right = string_length - 1;
    std::string numString;
    bool found = false;

    for (int left = 0; left < string_length; left++) {
        for (int i = 0; i < sizeof(numStrings) / sizeof(numStrings[0]); i++) {
            numString = numStrings[i];

            if (s.substr(left, numString.length()) == numString) {
                sum += (i + 1) * 10;
                found = true;
            }

            if (found) { break; }
        }

        if (found) { break; }

        if (isdigit(s[left])) {
            sum += int(s[left] - '0') * 10;
            break;
        }
    }

    found = false;

    for (int right = string_length - 1; right >= 0; right--) {
        for (int i = 0; i < sizeof(numStrings) / sizeof(numStrings[0]); i++) {
            numString = numStrings[i];
            if (s.substr(right, numString.length()) == numString) {
                sum += (i + 1);
                found = true;
            }

            if (found) { break; }
        }

        if (found) { break; }

        if (isdigit(s[right])) {
            sum += int(s[right] - '0');
            break;
        }
    }

    return sum;

}

int main() 
{ 
    int total = 0;
    std::string currentString;
    std::ifstream file ("codes.txt");

    while (std::getline(file, currentString)) {
        //cout << left_right_sum(currentString) << " : " << currentString  << endl;
        total += left_right_sum(currentString);
    }

    cout << total;

    return 0; 
} 