#explicação da entrega em sumário.txt

def sis_Conversao(valor: float, flag: int) -> float:

    #trata valores inválidos
    if type(valor) is not float and type(valor) is not int:
        try: 
            valor = float(valor);
        except ValueError as err:
            flag = -1
            print(err);
    
    if type(flag) is not int:
        try: 
            flag = int(flag);
        except ValueError as err:
            print(err);


    #flag == 1 metro -> pé
    if flag == 1:
        return valor * 3.281;

    #flag == 2 pé -> metro
    elif flag == 2:
        return valor * 0.3048;

    #inválido
    else:
        print("Entrada inválida\nsis_Conversao");



# teste
if __name__ == "__main__":
    print("\nInsira um input para o teste:");
    valor = input("(float/int): ")
    print("\nInsira o método de conversão:");
    flag = input("[1 = metro->pé]\n[2 = pé->metro]: ");
    print("\n");
    print("\noutput: {}", sis_Conversao(valor, flag));
