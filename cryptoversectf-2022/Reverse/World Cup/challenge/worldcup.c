#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

const char* TITLE =
"          ___          \n"
"      _.-'___'-._   \n"
"    .'--.`   `.--'.   \n"
"   /.'   \\   /   `.\\   \n"
"  | /'-._/```\\_.-'\\ |   \n"
"  |/    |     |    \\|   \n"
"  | \\ .''-._.-''. / |   \n"
"   \\ |     |     | /   \n"
"    '.'._.-'-._.'.'   \n"
"      '-:_____;-'   \n";

void readFlag() {
    int c;
    FILE *file;
    file = fopen("flag.txt", "r");
    if (file) {
        while ((c = getc(file)) != EOF)
            putchar(c);
        fclose(file);
        printf("\n");
    } else {
        printf("cvctf{real_flag_is_on_remote_DON'T_SUBMIT_THIS}\n");
    }
}

// 32 world cup 2022 teams
const char* TEAMS[32] = {
    "Qatar","Ecuador","Senegal","Netherlands",
    "England","Iran","USA","Wales",
    "Argentina","Saudi Arabia","Mexico","Poland",
    "France","Australia","Denmark","Tunisia",
    "Spain","Costa Rica","Germany","Japan",
    "Belgium","Canada","Morocco","Croatia",
    "Brazil","Serbia","Switzerland","Cameroon",
    "Portugal","Ghana","Uruguay","South Korea"
};

int isWorldCupTeam(char* team) {
    // remove trailing newline
    team[strlen(team)-1] = '\0';
    for (int i = 0; i < 32; i++) {
        if (strcmp(team, TEAMS[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("%s\n", TITLE);
    printf("Welcome to the World Cup Predictor!\n");
    printf("[+] Stage 1: Predict the first place in each group.\n");
    int score = 0;
    char buf[8][32];
    for (int i = 0; i < 8; i++) {
        printf("Group %c: ", 'A' + i);
        // read a line terminated by newline
        fgets(buf[i], 32, stdin);
        if (!isWorldCupTeam(buf[i])) {
            score--;
        }
    }
    for (int i = 0; i < 8; i++) {
        if (strlen(buf[i]) <= 2) {
            score--;
        } else {
            int res = (i == 0 && buf[i][0] == 'N') + (i == 1 && buf[i][1] == 'n') + (i == 2 && buf[i][0] == 'A') + (i == 3 && buf[i][1] == 'e') + \
            (i == 4 && buf[i][0] == 'J') + (i == 5 && buf[i][0] == 'B') + (i == 6 && buf[i][2] == 'a') + (i == 7 && buf[i][0] == 'U');
            score += res;
        }
    }

    if (score < 8) {
        printf("You failed.\n");
        return 0;
    }
    
    printf("[+] Stage 2: Predict the winner!\n");
    char winner[32];
    fgets(winner, 32, stdin);
    if (!isWorldCupTeam(winner)) {
        printf("You failed.\n");
        return 0;
    }
    if (strlen(winner) <= 2) {
        printf("You failed.\n");
        return 0;
    }
    if (winner[0] != 'A' || winner[1] != 'r' || winner[2] != 'g') {
        printf("You failed.\n");
        return 0;
    }
    printf("Congrats! Here is your flag: ");
    readFlag();
    return 0;
}