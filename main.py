def traducir_pseudocodigo(expresion):
    # reemplazar pseudocodigo por expresiones
    # que python interprete
    reemplazos = {
        "div": "//",
        "mod": "%",
        "=": "==",  # tal vez tener cuidado con ambigüedad en asignacion vs comparacion
        "V": "True",
        "F": "False"
    }

    # el word (o el que lo escribio) puede haber colocado guion largo en vez del normal
    # que usa py para restar
    expresion = expresion.replace("–", "-")

    for pseudo, real in reemplazos.items():
        expresion = expresion.replace(f" {pseudo}", f" {real} ")

    return expresion

def main():
    print("Evaluador de pseudocodigo - METPROG Edition")
    while True:
        entrada = input("\nYa te la sabes manito, pon la expresion: ")
        if entrada.lower() == "exit()":
            break
            
        try:
            traducida = traducir_pseudocodigo(entrada)
            print(f" Traduccion a python: {traducida}")
            resultado = eval(traducida)
            print(f" Resultado: {resultado}")
        except Exception as e:
            print(f" Algo hiciste mal pai: {e}")
    
if __name__ == "__main__":
    main()