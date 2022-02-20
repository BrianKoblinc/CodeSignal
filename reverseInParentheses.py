# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 20:52:50 2022

@author: Brian
"""

a = "foo(bar)baz"
b = "(ba(bar)r)"
c = "foo(bar(baz))blim"
d = "foo(bar)blabla(baz)jeje"

#Esta funcion vuelve a dar vuelta los parentesis interiores
def revpar(str):
  a = str.copy()
  for i in range(len(a)):
    if a[i] == ")":
      a[i] = "("
    elif a[i] == "(":
      a[i] = ")"
  return a

#Esta funcion da vuelta todo lo que esta entre los parentesis mas exteriores
def rev(str):
  par = []
  count = 0
  for j in range(len(str)):
    if str[j] == "(":
      count += 1
    elif str[j] == ")":
      count -= 1 
    if (count != 1 or str[j] != "(") and (count != 0 or str[j] == ")"):
      par.append(str[j])
    if count == 0:
      break
  par.pop()
  par.reverse()
  parfin = revpar(par)
  return parfin

#Esta funcion va enlistando todos los caracteres que no estan dentro de
#parentesis hasta encontrar la apertura de parentesis externos
def sol(a):
  fin=[]
  salt = 0
  for i in range(len(a)):
    if salt != 0:
      salt -=1
      continue
    if a[i] == "(":
      fin += rev(a[i:])
      salt += len(rev(a[i:]))+1
      #print(rev(a[i:]))
    else:
      fin.append(a[i])
  listToStr = ''.join([elem for elem in fin])
  solution(listToStr)

#Esta funcion busca si aun hay pares de parentesis restantes y si no
#deberia devolver el resultado final
#aca esta el problema porque puedo imprimir(print) el resultado pero
#no devolverlo (return)  
def solution(s):
  count1 = 0
  count2 = 0
  for i in s:
    if i == "(":
      count1 += 1
    if i == ")":
      count2 += 1
  if count1 == 0 or count2 == 0:
    return s #si lo cambio por print(s) se puede ver que funciona
  else:
    return sol(s)