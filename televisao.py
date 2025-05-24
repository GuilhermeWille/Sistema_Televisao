class Televisao:
    def __init__(self, canal, canal_minimo, canal_maximo, volume):
        self.canal = canal
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo
        self.volume = volume
        self.volume_maximo = 100
        self.volume_minimo = 0
        self.volume_mudo = False
        self.saida_de_som = True
        self.tv_ligada = False

    def botao_power(self):
        self.tv_ligada = not self.tv_ligada
        estado = "ligada" if self.tv_ligada else "desligada"
        print(f"Televisao {estado}")

    def _verificar_tv_ligada(self):
        if not self.tv_ligada:
            print("A TV esta desligada")
            return False
        return True

    def mais_canal(self):
        if not self._verificar_tv_ligada():
            return
        
        if self.canal < self.canal_maximo:
            self.canal += 1
        

    def menos_canal(self):
        if not self._verificar_tv_ligada():
            return
        
        if self.canal > self.canal_minimo:
            self.canal -= 1
        

    def mudar_canal(self, canal_destino):

        if not self._verificar_tv_ligada():
            return
    
        if canal_destino < self.canal_minimo:
            print(f"valor invalido: {canal_destino}. Limite minimo atingido{self.canal_minimo}")
            return False
        elif canal_destino > self.canal_maximo:
            print(f"valor invalido: {canal_destino}. Limite maximo atingido {self.canal_maximo}")
            return False
        else:
            self.canal = canal_destino
            print(f"canal atual: {canal_destino}")
            return True

    def mostrar_canal(self):
        print(f"canal: {self.canal} ")


    def aumentar_volume(self):
        if not self._verificar_tv_ligada():
            return
        
        if self.volume < self.volume_maximo:
            self.volume += 1
            print(f"Volume atual: {self.volume}")
        else:
            print(f"Volume: {self.volume_maximo}")

    def abaixar_volume(self):
        if not self._verificar_tv_ligada():
            return
        
        if self.volume > self.volume_minimo:
            self.volume -= 1
            print(f"Volume atual: {self.volume}")
        else:
            print(f"Volume: {self.volume_minimo}")

    def mudo(self):
        if not self._verificar_tv_ligada():
            return
        
        self.volume_mudo = not self.volume_mudo
        estado = "Ativado" if self.volume_mudo else "Desativado"
        print(f"Mudo {estado}")
        return True


    def som(self): #Emula saida de som, sem finalidade no codigo pratica
        if not self._verificar_tv_ligada():
            return

        if self.volume == 0:
            self.saida_de_som = False
        elif self.volume_mudo:
            self.saida_de_som = False
        
    def exibir_status(self):
        if self.tv_ligada:
            print(f"canal: {self.canal} | Volume: {self.volume} | Mudo: {'Sim' if self.volume_mudo else 'Não'}")
        else:
            print("A TV está desligada.")


def main():
    tv = Televisao(57, 0, 150, 20)

    opcoes_TV = [
        "1 - Ligar TV",
        "2 - Desligar TV",
        "3 - Mudar canal",
        "4 - canal +",
        "5 - canal -",
        "6 - Aumentar volume",
        "7 - Diminuir volume",
        "8 - Ativar mudo",
        "9 - Desativar mudo",
        "10 - Mostrar status da TV",
        "0 - Sair"
    ]

    for i in opcoes_TV:
       print(i) 
    status = -1

    while status != 0:
        try:
            status = int(input("Digite um numero: "))
        except ValueError:
            print("Entrada invalida. Digite um numero.")
            continue

        if status == 1:
            tv.botao_power()
        elif status == 2:
            if not tv.tv_ligada: 
                print("A TV ja esta desligada")
            else:
                tv.botao_power()
        elif status == 10:
            tv.exibir_status()
        elif status == 0:
            print("Volte sempre!")
            break
        else:
            print("Opção inválida. Digite um número da lista.")
            
        if not tv._verificar_tv_ligada():
            continue
        else:
            if status == 3:
                try:
                    cn = int(input("Digite o canal: "))
                    tv.mudar_canal(cn)
                    tv.mostrar_canal()
                except ValueError:
                    print("canal invalido. Digite um numero")
            elif status == 4: 
                tv.mais_canal()
                tv.mostrar_canal()
            elif status == 5:
                tv.menos_canal()
                tv.mostrar_canal()
            elif status == 6:
                tv.aumentar_volume()
            elif status == 7:  
                tv.abaixar_volume()
            elif status == 8:
                if tv.volume_mudo:
                    print("TV ja esta no mudo")
                else:
                    tv.mudo()
            elif status == 9:
                if not tv.volume_mudo:
                    print("A tv ja esta com som")
                else:
                    tv.mudo()
       
        
    

if __name__ == "__main__":
    main()