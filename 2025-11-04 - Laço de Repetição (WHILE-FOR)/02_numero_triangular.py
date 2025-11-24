'''
   Faça um programa que solicite ao usuário um número inteiro e
   informe se ele é um número triangular ou não.

   Um número triangular é um número que pode ser representado na forma 
   de um triângulo equilátero.

   Os primeiros números triangulares são: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
'''
import sys

try:
   intNumero = int(input('Digite um número inteiro: '))
except ValueError:
   sys.exit('ERRO: Informe um número inteiro válido...')
except KeyboardInterrupt:
   sys.exit('AVISO: Programa interrompido pelo usuário...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   # Números triangulares são positivos
   if intNumero < 1:
      sys.exit(f'O número {intNumero} não é triangular.')

   # Inicializa variáveis para calcular números triangulares
   intTriangular = 0 # Valor do número triangular atual
   intIncremento = 1 # Incremento para o próximo número triangular

   # Calcula números triangulares até encontrar ou ultrapassar o número
   while intTriangular < intNumero:
      intTriangular += intIncremento
      intIncremento += 1 

   # Verifica se o número é triangular
   if intTriangular == intNumero:
      print(f'O número {intNumero} é triangular.')
   else:
      print(f'O número {intNumero} não é triangular.')