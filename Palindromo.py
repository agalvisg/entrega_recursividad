import unicodedata

class Palindromo():
    
    
    
    def __init__(self,texto_usuario):
        self.texto_usuario = texto_usuario

    def get_palabra(self):
        return self.texto_usuario
    
    def EsPalindromo(self,texto_usuario):
        
        #Filtrar caracteres alfanuméricos
        texto_sin_espacios= ''.join(c for c in texto_usuario if c.isalnum())

        #Sustituir caracteres acentuados por su equivalente sin acento
        texto_sin_acentos = unicodedata.normalize('NFKD',texto_sin_espacios).encode('ASCII', 'ignore').decode('ASCII')

        #Convertir todas las letras a minúsculas
        texto_minusculas = texto_sin_acentos.lower()

        #Verificar si el texto filtrado es igual a su imagen reflejada
        return texto_minusculas == texto_minusculas[::-1]

    
def main():
    # Pedir al usuario que ingrese un texto
    texto_usuario = input("Ingrese un texto: ")

    # Verificar si el texto ingresado es un palíndromo
    palindromo = Palindromo(texto_usuario)
    if palindromo.EsPalindromo(texto_usuario):
        print("El texto ingresado es un palíndromo.")
    else:
        print("El texto ingresado no es un palíndromo.")


if __name__ == "__main__":
    main()