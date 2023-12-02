#include <iostream> 
#include <fstream>
#include <string>
#include <regex>

using namespace std;

const int RED_LIMIT = 12;
const int GREEN_LIMIT = 13;
const int BLUE_LIMIT = 14;

bool stringNumberAboveLimit(string s, int limit) {
    smatch number;
    regex numberRegex("\\d+");

    if (regex_search(s, number, numberRegex)) {
        if (stoi(number.str(0)) > limit) {
            return true;
        }
    }

    return false;
}

bool validColorAmounts(string game) {
    regex redRegex("\\d+ red");
    regex greenRegex("\\d+ green");
    regex blueRegex("\\d+ blue");

    smatch match;
    string numberAndColor;

    if (regex_search(game, match, redRegex)) {
        numberAndColor = match.str(0);

        if (stringNumberAboveLimit(numberAndColor, RED_LIMIT)) { return false; }
    }

    if (regex_search(game, match, greenRegex)) {
        numberAndColor = match.str(0);

        if (stringNumberAboveLimit(numberAndColor, GREEN_LIMIT)) { return false; }
    }

    if (regex_search(game, match, blueRegex)) {
        numberAndColor = match.str(0);

        if (stringNumberAboveLimit(numberAndColor, BLUE_LIMIT)) { return false; }
    }

    return true;
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

    while (std::getline(file, currentLine)) {
        index++;
        currentLine = regex_replace(currentLine, gameRegex, "");

        int pos;
        std::string game;
        while ((pos = currentLine.find(DELIMINATOR)) != std::string::npos) {
            game = currentLine.substr(0, pos);

            if (!validColorAmounts(game)) { validGame = false; }

            currentLine.erase(0, pos + DELIMINATOR.length());
        }

        if (!validColorAmounts(currentLine)) { validGame = false; }

        if (validGame) { total += index; }
        validGame = true;
    }

    cout << total;

    return 0; 
} 