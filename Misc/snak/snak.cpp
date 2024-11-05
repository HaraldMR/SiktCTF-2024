#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <csignal>  // Required for signal handling
#include <unistd.h> // For alarm()

// Game settings
const int BoardSize = 16;
const char BorderChar = '#';
const char SnakeChar = 'o';
const char AppleChar = 'g';
const int MaxApples = 100;
const int GameTimeout = 300; // Set a timeout for 5 minutes (300 seconds)

// Function to clear the console (platform dependent)
void clearConsole() {
#ifdef _WIN32
    system("cls");  // Windows
#else
    system("clear");  // Linux/macOS
#endif
}

// Function to print the game board
void printBoard(int score, int snakeX, int snakeY, int appleX, int appleY) {
    clearConsole();
    
    std::cout << "Score: " << score << std::endl;
    for (int i = 0; i < BoardSize + 2; ++i) {
        std::cout << BorderChar;
    }
    std::cout << std::endl;

    for (int i = 0; i < BoardSize; ++i) {
        std::cout << BorderChar;
        for (int j = 0; j < BoardSize; ++j) {
            if (i == snakeY && j == snakeX) {
                std::cout << SnakeChar;
            } else if (i == appleY && j == appleX) {
                std::cout << AppleChar;
            } else {
                std::cout << " ";
            }
        }
        std::cout << BorderChar << std::endl;
    }

    for (int i = 0; i < BoardSize + 2; ++i) {
        std::cout << BorderChar;
    }
    std::cout << std::endl;
}

// Signal handler for SIGALRM (timeout)
void handleTimeout(int sig) {
    std::cout << "\nGame timed out due to inactivity." << std::endl;
    exit(0);
}

int main() {
    // Seed the random number generator
    srand(time(NULL));

    // Set the alarm for a timeout (300 seconds)
    signal(SIGALRM, handleTimeout);  // Set the signal handler
    alarm(GameTimeout);  // Start the timer

    std::cout << "SNAK" << std::endl;
    std::cout << "Start game? [Y/n]: ";
    char choice;
    std::cin >> choice;

    if (choice == 'Y' || choice == 'y') {
        int score = 0;
        int snakeX = BoardSize / 2;
        int snakeY = BoardSize / 2;
        int appleX = rand() % BoardSize;
        int appleY = rand() % BoardSize;

        // Main game loop
        while (score < MaxApples && !std::cin.eof()) {
            // Reset the alarm for each iteration (in case of activity)
            alarm(GameTimeout);

            // Print the game board
            printBoard(score, snakeX, snakeY, appleX, appleY);

            // Get player input
            std::cout << "Enter direction (1=Up, 2=Down, 3=Left, 4=Right): ";
            int direction;
            std::cin >> direction;

            // Handle input and update snake position
            if (direction == 1) {
                snakeY--;  // Move up
            } else if (direction == 2) {
                snakeY++;  // Move down
            } else if (direction == 3) {
                snakeX--;  // Move left
            } else if (direction == 4) {
                snakeX++;  // Move right
            } else {
                std::cout << "Invalid direction. Please try again." << std::endl;
                continue;
            }

            // Check for collisions with the walls
            if (snakeX < 0 || snakeX >= BoardSize || snakeY < 0 || snakeY >= BoardSize) {
                std::cout << "Game over! You hit the wall." << std::endl;
                break;
            }

            // Check if the snake has reached the apple
            if (snakeX == appleX && snakeY == appleY) {
                // Increment the score
                score++;

                // Generate a new random apple
                appleX = rand() % BoardSize;
                appleY = rand() % BoardSize;
            }

            // Check for the game-over condition
            if (score >= MaxApples) {
                std::cout << "Congratulations! You won the game." << std::endl;
                std::ifstream flagFile("flag.txt");
                if (flagFile.is_open()) {
                    std::string flag;
                    flagFile >> flag;
                    std::cout << "Here's the flag: " << flag << std::endl;
                    flagFile.close();
                } else {
                    std::cout << "Flag file not found." << std::endl;
                }
                break;
            }
        }
    } else {
        std::cout << "Game stopped." << std::endl;
    }

    return 0;
}
