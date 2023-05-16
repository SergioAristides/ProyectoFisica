
import math
class Particula:
  def calcular_distancia(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
  def centro_imagen(particula,imagenAncho,imagenAlto):
    return ((particula.x+(imagenAncho+particula.x))/2,(particula.y+(imagenAlto+particula.y))/2)
  def __init__(self, carga,valor,url,x,y,centro):
    self.carga = carga
    self.valor = valor
    self.url=url
    self.x=x
    self.y=y
    self.centro=centro


