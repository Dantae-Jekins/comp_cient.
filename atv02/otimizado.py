#no numpy
file_altu = open("altura.txt");
file_anos = open("anos.txt");

num = 0;
soma = 0;
line_altu = next(file_altu);
line_anos = next(file_anos);

while 1:
    ano = float(line_anos)
    if (ano >= 1998 and ano <= 2005):
         num+= 1;
         soma += float(line_altu);

    try:line_altu = next(file_altu);
    except: break;
    try:line_anos = next(file_anos);
    except: break;

print(soma/num);
