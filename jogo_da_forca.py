from random import randint

palco = ['', 'O', 'O-', 'O-|', 'O-|-', 'O-|-<']


class Forca:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_certas = []
        self.letras_erradas = []

    def adivinha(self, letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    def forca_acabou(self):
        if self.forca_venceu() or len(self.letras_erradas) >= 5:
            return True
        return False

    def forca_venceu(self):
        if '_' not in self.palavra_escondida():
            return True
        return False

    def palavra_escondida(self):
        status = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                status += '_'
            else:
                status += letra
        return status

    def mostra_status_jogo(self):
        print('\n======== Jogo da Forca ========')
        print(palco[len(self.letras_erradas)])
        print(f'\n {self.palavra_escondida()}')
        print('\nLetras Erradas:')
        for letra in self.letras_erradas:
            print(letra,)
        print('\nLetras Corretas:')
        for letra in self.letras_certas:
            print(letra,)
        print('==================')


def palavra_aleatoria():
    with open('palavras.txt', 'rt') as f:
        banco = f.readlines()
    return banco[randint(0, len(banco))].strip()


def main():
    jogo = Forca(palavra_aleatoria())

    while not jogo.forca_acabou():
        jogo.mostra_status_jogo()
        letra = input('Digite uma letra: ')
        jogo.adivinha(letra)
        continue

    if jogo.forca_venceu():
        print('\nParabéns! Você ganhou!')
    else:
        print('\nFinal do Jogo! Você perdeu!')
        print(f'A palavra era {jogo.palavra}')

    print('\nFoi bom jogar com você!\n')


if __name__ == '__main__':
    main()
