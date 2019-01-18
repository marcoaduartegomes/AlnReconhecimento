COPIE A BASE DE FOTOS NOVAMENTE, POIS TEM FOTOS NOVAS, UMA DA UERJ E OUTRA COM QUANTIDADE DIFERENTES
FOI ALTERADO TAMBEM UM ARQUIVO DENTRO DE ALGUMAS PASTAS, POIS O MESMO TINHA EM SEU NOME A PALAVRA CHAVE "-", QUE É UTILIZADA COMO SEPARADOR PELO ALGORITMO.
O codigo é dividido em dois para facilitar o entendimento.
O algoritmo bruto funciona da seguinte forma:
No final do código, são chamadas funções teste, que recebem como argumentos as seguintes coisas:
teste(mapeamento para treino(diretorio),mapeamento a ser comparado(diretorio),diretorio do treino,diretorio a ser comparado, exibir as fotos ou não, quantidade de vezes a ser executado,extensão)
exemplo: teste(jsons('very-easy'),jsons('comparar'),"very-easy","comparar",1,1,'.jpg'). a função jsons faz o mapeamento das imagens do diretorio dado.

É recomendado apenas chamar uma função por vez, comentando o resto do código, pois pode demorar para executar todos de uma vez so, e para o console não encher de informações.

O algoritmo PCA funciona de forma analoga, apenas mudando sua estrutura. Tomar cuidado pois o codigo pode demorar bastante para rodar, principalmente na base de dados medium.

Um arquivo separado esta no mesmo diretorio contendo os dados retornados ao rodar todo o código.