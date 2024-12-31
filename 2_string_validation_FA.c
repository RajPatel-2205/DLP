#include <stdio.h>
#include <string.h>

// Function to determine the next state based on the current state and input symbol
int getNextState(int currentState, char input) {
    // Transition table based on the given problem
    switch (currentState) {
        case 1:
            if (input == 'a') return 2;
            if (input == 'b') return 3;
            break;
        case 2:
            if (input == 'a') return 1;
            if (input == 'b') return 4;
            break;
        case 3:
            if (input == 'a') return 4;
            if (input == 'b') return 1;
            break;
        case 4:
            if (input == 'a') return 3;
            if (input == 'b') return 2;
            break;
    }
    return -1; // Invalid state
}

int main() {
    char testString[] = "abbabab"; // Test string
    int currentState = 1;         // Initial state
    int i;

    // Process each character in the test string
    for (i = 0; i < strlen(testString); i++) {
        char input = testString[i];
        currentState = getNextState(currentState, input);
        if (currentState == -1) {
            printf("Rejected: Invalid transition encountered.\n");
            return 0;
        }
    }

    // Define acceptable final states (example: state 1 is the accepting state)
    int acceptingStates[] = {1}; // Add any other accepting states if necessary
    int numAcceptingStates = sizeof(acceptingStates) / sizeof(acceptingStates[0]);

    // Check if the final state is one of the accepting states
    int isAccepted = 0;
    for (i = 0; i < numAcceptingStates; i++) {
        if (currentState == acceptingStates[i]) {
            isAccepted = 1;
            break;
        }
    }

    if (isAccepted) {
        printf("Accepted: The test string is accepted by the finite automaton.\n");
    } else {
        printf("Rejected: The test string is not accepted by the finite automaton.\n");
    }

    return 0;
}
