COPIE A BASE DE FOTOS NOVAMENTE, POIS TEM FOTOS NOVAS, UMA DA UERJ E OUTRA COM QUANTIDADE DIFERENTES
FOI ALTERADO TAMBEM UM ARQUIVO DENTRO DE ALGUMAS PASTAS, POIS O MESMO TINHA EM SEU NOME A PALAVRA CHAVE "-", QUE � UTILIZADA COMO SEPARADOR PELO ALGORITMO.
O codigo � dividido em dois para facilitar o entendimento.
O algoritmo bruto funciona da seguinte forma:
No final do c�digo, s�o chamadas fun��es teste, que recebem como argumentos as seguintes coisas:
teste(mapeamento para treino(diretorio),mapeamento a ser comparado(diretorio),diretorio do treino,diretorio a ser comparado, exibir as fotos ou n�o, quantidade de vezes a ser executado,extens�o)
exemplo: teste(jsons('very-easy'),jsons('comparar'),"very-easy","comparar",1,1,'.jpg'). a fun��o jsons faz o mapeamento das imagens do diretorio dado.

� recomendado apenas chamar uma fun��o por vez, comentando o resto do c�digo, pois pode demorar para executar todos de uma vez so, e para o console n�o encher de informa��es.

O algoritmo PCA funciona de forma analoga, apenas mudando sua estrutura. Tomar cuidado pois o codigo pode demorar bastante para rodar, principalmente na base de dados medium.

Um arquivo separado esta no mesmo diretorio contendo os dados retornados ao rodar todo o c�digo.