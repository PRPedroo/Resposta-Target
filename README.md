# Resposta-Target
Resposta ao desafio da vaga de estágio da target sistemas

1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

   Resposta:
   código "fib.py" anexado a esse repositório
   
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

   Resposta:
   código "str.py" anexado a esse repositório
   
3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
  Ao final do processamento, qual será o valor da variável SOMA? 

  Resposta:
  2+3+4+5+6+7+8+9+10+11+12 = 77

4) Descubra a lógica e complete o próximo elemento: 
  a) 1, 3, 5, 7, ___ 
  b) 2, 4, 8, 16, 32, 64, ____ 
  c) 0, 1, 4, 9, 16, 25, 36, ____ 
  d) 4, 16, 36, 64, ____ 
  e) 1, 1, 2, 3, 5, 8, ____ 
  f) 2,10, 12, 16, 17, 18, 19, ____

  Resposta:
  a) 9
  b) 128
  c) 49
  d) 100
  e) 13
  f) 20

5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

   Resposta:
   Supondo os interruptores A, B e C. Ligue o interruptor A e deixe a lâmpada ligada por um certo período de tempo. Depois de deixar a lampada A esquentar, desligue o interruptor A e ligue o B. Fazendo isso as lampadas se distinguem dessa forma:
   A - quente e desligada
   B - fria e ligada
   C - fria e desligada
   Entrando em apenas 2 quartos é possivel saber qual interruptor liga qual lâmpada
