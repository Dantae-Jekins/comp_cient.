"""
#PSEUDOCODIGO

# predição -> p(x,y) onde x=x0 e y=x1
def est(x1, x2, a, b, c):
  # NOSSA ESTIMAÇÃO
  return 1.0 / (math.exp(-(x0*a + x1*b + c)))

def erro(y, estimados):
  # AQUI SERIA O ERRO DE FUNÇÕES NÃO LINEARES
  # estimados é a função cross entropy
  return abs(y - estimados); # PRECISA ALTERAR (ERRADO)

def gradient_descent(y, x0, x1, n=100, limite = 10e-6, alpha = 0.01):
  a = 0.1
  b = 0.1
  c = 0.1
  nosso_erro_medio = 1;
  
  for (_ in n):
    # realizar gradiente para direcionar a, b, c para o valor de menor erro


    if (nosso_erro_medio <= limite)
      return (a, b, c);
    # gradient = ∂L/∂a = 1/N * X * (p(x,y) - z)
    a = a - alpha * gradiente[a]
    b = b - alpha * gradiente[b]
    c = c - alpha * gradiente[c]

    nossos_valores = est (x1, x2, a, b, c);
    nosso_erro_medio = erro(y, nossos_valores);

    Continua com outras coisas
    -> registrar os erros
    -> registrar os coeficientes (a, b, c)

"""
import numpy as np;
import pandas as pd;

def sigmoidal(a1, a2, a3, x1, x2): 
    e = np.exp(-a1*x1 -a2*x2 - a3, dtype=np.float128);
    return 1 / (1 + e);

def perda(y: np.array, p: np.array):
    N = len(y);
    values = - (y * np.log(p) + (1 - y) * np.log(1 - p));
    return np.sum(values)/N;

def gradiente(a1, a2, a3, x1, x2, y):
    N = len(y);
    grada1 = np.sum(x1 * (sigmoidal(a1, a2, a3, x1, x2) - y)) / N
    grada2 = np.sum(x2 * (sigmoidal(a1, a2, a3, x1, x2) - y)) / N
    grada3 = np.sum(sigmoidal(a1, a2, a3, x1, x2) - y)/N
    return grada1, grada2, grada3;

def classificador(y, x1, x2, iters = 10000, alpha = 1e-4, lim = 1e-4):
    N = len(y);
    count = 0;
    a1 = 0.1;
    a2 = 0.1;
    a3 = 1; 
    err_atual = 0;
    err_anter = float('inf');
    erros = []
    for i in range(1,iters):
        estimados = sigmoidal(a1, a2, a3, x1, x2);
        print(estimados)
        err_atual = perda(y, estimados); 
        count+= 1;
        if (abs(err_atual - err_anter) <= lim): 
            print("Coeficientes encontrados {} iterações".format(count));
            print(" a1 = {}\n a2 = {}\n a3 = {}".format(a1, a2, a3));
            return a1, a2, a3, erros;
        erros.append(err_atual);
        
        #recálculo
        err_anter = err_atual;
        grad1, grad2, grad3 = gradiente(a1, a2, a3, x1, x2, y);       
        a1 -= alpha * grad1;
        a2 -= alpha * grad2;
        a3 -= alpha * grad3;

    print("Coeficientes não encontrados");
    print(" a1 = {}\n a2 = {}\n a3 = {}".format(a1, a2, a3));
    return a1, a2, a3, erros, count;


#Código
notas = pd.read_csv('https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/notas-estudantes.csv');
x1 = notas.nota_1;
x2 = notas.nota_2;
y = notas.resultado;

a, b, c, erro = classificador(y, x1, x2);
