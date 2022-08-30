import numpy as np

if __name__ == "__main__":
    file_altu = None;
    file_anos = None;

    ## <tratamento de erro  (ignora)>
    try:
        file_altu = open("altura.txt", "r");
    except IOError as e:
        print("Erro open()", e );
        file_altu = None;
    try:
        file_anos = open("anos.txt", "r");

    except IOError as e:
        print("Erro open()", e);
        file_anos = None;   
    ## </tratamento de erro>

    if ( file_altu == None or file_anos == None):
        print("Encerrando programa");

    else:
        ## next para menor consumo de memória
        line_altu = next(file_altu);
        line_anos = next(file_anos);
        altu_array = np.empty(0, dtype=np.float64);
        
        while 1:
           
            ## filtração dos dados 
            ano = float(line_anos);
            
            ## não foi definido se o intervalo é inclusivo ou não, pela semântica assume-se que não
            if (ano >= 1.998e+3 and ano <= 2.005e+3):
                altu_array = np.append(altu_array, float(line_altu));
            
            ## condições de break
            try:line_altu = next(file_altu);
            except: break;
            try:line_anos = next(file_anos);
            except: break;

        ## conclusão dos dados
        media = np.average(altu_array);
        print("Média das alturas dos atletas nascidos entre 1998 e 2005.");
        print(media);
