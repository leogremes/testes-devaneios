#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int joguinho(int muda_de_porta) {
    /*Atribuir premio, escolha de porta e porta de revelação*/
    int premio = rand() % 3;
    int escolha = rand() % 3;
    int reveal = rand() % 3;
    while (reveal == premio | reveal == escolha) {
        reveal = rand() % 3;
    }
    /*Escolha se vai mudar de porta*/
    /*ATOI = Ascii to int*/
    if (muda_de_porta == 1) {
        escolha = 3 - escolha - reveal;
    }
    /*Ver se ganhou*/
    if (escolha == premio) {
        return 1;
    }
    else {
        return 0;
    }
}

int main (int num_args, char *args[]) {    
    /*srand >  seed random*/
    srand(time(NULL));
    int qtd = atoi(args[1]);
    int muda_porta = atoi(args[2]);
    int contador = 0;
    for (int i = 0; i < qtd; i++) {
        contador += joguinho(muda_porta);
    }
    printf("De %i partidas, ele ganhou %i Vezes (%.2f %%)", qtd, contador, (float) contador / qtd * 100);
    scanf("coisa dentro");
    return 0;
}