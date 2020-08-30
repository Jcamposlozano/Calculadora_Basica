

class Calculadora:

    def operacion(self,a:float, b:float, entrada:str):
        if entrada.upper() == 'SUMA':
            return self.suma(a,b)
        elif entrada.upper() == 'RESTA':
            return self.resta(a,b)
        elif entrada.upper() == 'MULTIPLICA':
            return self.multiplica(a,b)
        elif entrada.upper() == 'DIVIDE':
            return self.divide(a,b)
        else:
            return 'Error'

    def suma(self, a:float, b:float):
        resultado = a + b
        return (resultado)
    
    def resta(self,a:float, b:float):
        resultado = a - b
        return (resultado)

    def multiplica(self, a:float, b:float):
        resultado = a * b
        return (resultado)

    def divide(self,a:float, b:float):
        if b != 0:
            resultado = a / b 
            return (resultado)
        else:
            return 0



