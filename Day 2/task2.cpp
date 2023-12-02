#include <iostream> 
#include <fstream>
#include <string>
#include <regex>

using namespace std;

int stringNumber(string s) {
    smatch number;
    regex numberRegex("\\d+");

    if (regex_search(s, number, numberRegex)) {
        return stoi(number.str(0));
    }

    return 0;
}

void minimumColorAmounts(string game, int &red, int &green, int &blue) {
    regex redRegex("\\d+ red");
    regex greenRegex("\\d+ green");
    regex blueRegex("\\d+ blue");

    smatch match;
    string numberAndColor;

    if (regex_search(game, match, redRegex)) {
        numberAndColor = match.str(0);

        red = max(red, stringNumber(numberAndColor));
    }

    if (regex_search(game, match, greenRegex)) {
        numberAndColor = match.str(0);

        green = max(green, stringNumber(numberAndColor));
    }

    if (regex_search(game, match, blueRegex)) {
        numberAndColor = match.str(0);

        blue = max(blue, stringNumber(numberAndColor));
    }
}

int main() 
{ 
    int total = 0;
    std::string currentLine;
    std::ifstream file ("data.txt");

    const string DELIMINATOR = ";";

    regex gameRegex("Game \\d*: ");

    int index = 0;
    bool validGame = true;
    string numberAndColor;

    int minimum_red = 0;
    int minimum_green = 0;
    int minimum_blue = 0;

    while (std::getline(file, currentLine)) {
        index++;
        currentLine = regex_replace(currentLine, gameRegex, "");

        minimum_red = 0;
        minimum_green = 0;
        minimum_blue = 0;

        int pos;
        std::string game;
        while ((pos = currentLine.find(DELIMINATOR)) != std::string::npos) {
            game = currentLine.substr(0, pos);

            minimumColorAmounts(game, minimum_red, minimum_green, minimum_blue);

            currentLine.erase(0, pos + DELIMINATOR.length());
        }

        minimumColorAmounts(currentLine, minimum_red, minimum_green, minimum_blue);

        if (validGame) { total += minimum_red * minimum_green * minimum_blue; }
        validGame = true;
    }

    cout << total;

    return total; 
} 