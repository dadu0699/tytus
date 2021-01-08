import sys, os.path
import math

dir_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\EXPRESION\\EXPRESION\\')
sys.path.append(dir_nodo)

ent_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(ent_nodo)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\C3D\\')
sys.path.append(c3d_dir)

from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion
from Label import *
from Temporal import *

class Function_Sign(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):
        op1 = self.hijos[0]
        res = op1.execute(enviroment)

        if op1.tipo.data_type == Data_Type.numeric :

            self.tipo = Type_Expresion(Data_Type.numeric)

            if res > 0 :
                self.valorExpresion = 1
                return self.valorExpresion
            
            elif res == 0 :

                self.valorExpresion = 0
                return self.valorExpresion
            
            elif res < 0 :

                self.valorExpresion = -1
                return self.valorExpresion
        
        else :

            self.tipo = Type_Expresion(Data_Type.error)
            self.valorExpresion = None
            return self.valorExpresion

    def compile(self, enviroment):
        op1 = self.hijos[0]
        res = op1.compile(enviroment)

        if op1.tipo.data_type == Data_Type.numeric :

            self.tipo = Type_Expresion(Data_Type.numeric)
            self.dir = instanceTemporal.getTemporal()
            self.cod = res
            self.cod += self.dir + ' = 0\n'
            self.cod += 'if ' + op1.dir + ' > 0 :\n'
            self.cod += '\t' + self.dir + ' = 1\n'
            self.cod += 'elif ' + op1.dir + ' == 0 :\n'
            self.cod += '\t' + self.dir + ' = 0\n'
            self.cod += 'else :\n'
            self.cod += '\t' + self.dir + ' = -1\n'
            return self.cod
        
        else :

            self.tipo = Type_Expresion(Data_Type.error)
            self.dir = ''
            self.cod = ''
            return self.cod
    
    def getText(self):
        exp = self.hijos[0]
        stringReturn = 'sign('+ exp.getText() +')'
        return stringReturn