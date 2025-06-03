#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void simulate_amplified_flood(char* target, int seconds) {
    printf("[!] Beginning pseudo flood on %s for %d seconds\n", target, seconds);
    for (int i = 0; i < seconds; i++) {
        printf("[.] Tick %d: spoofed UDP burst\n", i);
        sleep(1);
    }
    printf("[+] Flood simulation complete\n");
}

int main(int argc, char *argv[]) {
    if (argc < 3) return 1;
    simulate_amplified_flood(argv[1], atoi(argv[2]));
    return 0;
}
