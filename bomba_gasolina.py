from bomba_combustivel import BombaCombustivel

class BombaGasolina(BombaCombustivel):
    ADITIVO_VALOR= 0.05
    
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)
        
    def abastecer_por_valor_com_aditivo(self, valor):
        litros = valor / super().get_valor_litro()
        
        if litros > super().get_quantidade_disponivel():
            return -1
        
        def retirar_litros(litros):
            self.get_quantidade_disponivel = self.__quantidade_disponivel-litros
        
        return litros
    
    def abastecer_por_litro_com_aditivo(self, litros):
        self.__quantidade_disponivel = self.abastecer_por_litro
            

# Testing Area
bomba = BombaGasolina(2, 200)
litros = bomba.abastecer_por_valor_com_aditivo(20)
print(litros)