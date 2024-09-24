class BombaCombustivel:
    def __init__(self, __valor_litro, quantidade_disponivel):
        self.__valor_litro = __valor_litro
        self.__quantidade_disponivel = quantidade_disponivel
        
    def get_quantidade_disponivel(self):
        return self.__quantidade_disponivel
    
    def get_valor_litro(self):
        return self.__valor_litro
        
    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.__valor_litro
        if litros_abastecidos <= self.__quantidade_disponivel:
            self.__quantidade_disponivel -= litros_abastecidos
            print(f"Abastecidos {litros_abastecidos:.2f} litros.")
        else:
            print("Quantidade insuficiente.")

    def abastecer_por_litro(self, litros):
        if litros <= self.__quantidade_disponivel:
            self.__quantidade_disponivel -= litros
            print(f"Abastecidos {litros} litros.")
        else:
            print("Quantidade insuficiente.")

