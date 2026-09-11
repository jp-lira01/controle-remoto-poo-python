import os

from rich import print
from rich.panel import Panel
from time import sleep


class ControleRemoto:
    """Representa um controle remoto de televisão.

    Permite ligar e desligar a TV, mudar o canal e aumentar
    ou diminuir o volume.
    """
    
    def __init__(self, marca, can_min, can_max, vol_min, vol_max):
        """Inicializa o controle remoto com a quantidade de canais disponível."""
        
        self.marca = marca
        self.ligada = False
        self.canal_max = can_max
        self.canal_min = can_min
        self.canal_atual = can_min
        self.volume_max = vol_max
        self.volume_min = vol_min
        # Liga a TV em um volume médio
        self.volume_atual = vol_min + (vol_max // 2)

    def aperta_botao(self, botao):
        """Executa uma ação segundo o botão pressionado."""

        match botao:
            case "@":
                self.liga_desliga()
            case "<":
                self.diminui_canal()
            case ">":
                self.aumenta_canal()
            case "-":
                self.diminui_volume()
            case "+":
                self.aumenta_volume()
            case _:
                print(f"[red]Botão inexistente[/]")
                sleep(2)

    def liga_desliga(self):
        """Liga ou desliga a televisão."""

        self.ligada = not self.ligada

    def aumenta_canal(self):
        """Avança para o próximo canal da televisão."""

        if not self.ligada:
            return

        if self.canal_atual >= self.canal_max:
            self.canal_atual = self.canal_min
        else:
            self.canal_atual += 1

    def diminui_canal(self):
        """Volta para o canal anterior da televisão."""

        if not self.ligada:
            return

        if self.canal_atual <= self.canal_min:
            self.canal_atual = self.canal_max
        else:
            self.canal_atual -= 1

    def aumenta_volume(self):
        """Aumenta o volume da televisão até o limite máximo."""

        if not self.ligada:
            return

        if self.volume_atual < self.volume_max:
            self.volume_atual += 1

    def diminui_volume(self):
        """Diminui o volume da televisão até o limite mínimo."""
        
        if not self.ligada:
            return

        if self.volume_atual > self.volume_min:
            self.volume_atual -= 1

    def televisao(self):
        """Cria e retorna um painel com o estado atual da televisão."""

        if not self.ligada:
            conteudo = f"[red]:prohibited: A tv está desligada[/]"
            caixa = Panel(conteudo, title=self.marca, expand=False)
            return caixa

        conteudo = f"Canal:\t = "
        for i in range(self.canal_min, self.canal_max + 1):
            if i == self.canal_atual:
                conteudo += f"[black on yellow] {i} [/]"
            else:
                conteudo += f" {i} "

        barra_vol = "[cyan on cyan] [/]" * self.volume_atual + "[white on white] [/]" * (
                self.volume_max - self.volume_atual)
        conteudo += f"\n\nVolume\t = [blue]{barra_vol}[/] ({self.volume_atual})"
        caixa = Panel(conteudo, title=f"{self.marca}", expand=False)
        return caixa


# ========== Objetos ==========

c1 = ControleRemoto("Samsung", 1, 10, 0, 5)

while True:
    os.system("cls")
    print(c1.televisao())

    opcao = input("0 - Sair    < CH >    - VOL +    PWR - @:    ")
    if opcao == "0":
        break

    c1.aperta_botao(opcao)
