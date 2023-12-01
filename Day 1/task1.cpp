#include <iostream> 
#include <fstream>
#include <string>

using namespace std; 

int left_right_sum(std::string s) {
    int string_length = s.length();
    int sum = 0;
    int left = 0;
    char right = string_length - 1;

    while (!isdigit(s[left])) {
        left++;
    }

    sum += int(s[left] - '0') * 10;

    while (!isdigit(s[right])) {
        right--;
    }

    sum += int(s[right] - '0');

    return sum;

}

int main() 
{ 
    int total = 0;
    std::string currentString;
    std::ifstream file ("codes.txt");

    while (std::getline(file, currentString)) {
        total += left_right_sum(currentString);
    }

    cout << total;

    return 0; 
} 