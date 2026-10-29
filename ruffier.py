''' Módulo para calcular los resultados de las pruebas de Ruffier.
 
La suma de los tres intentos de medición del pulso (antes del esfuerzo, justo después del esfuerzo y después de un breve descanso)
idealmente no debería superar los 200 latidos por minuto.
Se propone que los niños midan su pulso durante 15 segundos,
y encuentren el resultado en latidos por minuto multiplicando por 4:
   S = 4 * (P1 + P2 + P3)
Cuanto más se aleje el resultado del ideal de 200 latidos, peor será.
Tradicionalmente, se presentan tablas con los valores divididos por 10.
 
Índice de Ruffier  
   IR = (S - 200) / 10
se evalúa según la edad de acuerdo con la tabla:
        7-8             9-10                11-12               13-14               15+ (solo para adolescentes!)

perfecto     < 6.5           < 5                 < 3.5               < 2                 < 0.5  
bueno    >= 6.5 y < 12   >= 5 y < 10.5       >= 3.5 y < 9        >= 2 y < 7.5        >= 0.5 y < 6
satisfactorio  >= 12 y < 17    >= 10.5 y < 15.5    >= 9 y < 14         >= 7.5 y < 12.5     >= 6 y < 11
débil  >= 17 y < 21    >= 15.5 y < 19.5    >= 14 y < 18        >= 12.5 y < 16.5    >= 11 y < 15
insatisfactorio   >= 21           >= 19.5             >= 18               >= 16.5             >= 15

El resultado “insatisfactorio” está 4 puntos por encima del resultado “débil” para todas las edades,
“débil” se separa de “satisfactorio” por 5, y “bueno” se separa de “satisfactorio” por 5.5.
 
Por lo tanto, escribiremos una función ruffier_result(r_index, level) que producirá
el índice de Ruffier calculado y el nivel “insatisfactorio” para la edad evaluada, y producirá un resultado.
 
'''
# aquí se dan las líneas que producen el resultado
txt_index = "Tu índice de Ruffier: "
txt_workheart = "Eficiencia cardíaca: "
txt_nodata = '''
No hay datos para esa edad'''
txt_res = []
txt_res.append('''bajo.
¡Ve a ver a tu médico lo antes posible!''')
txt_res.append('''satisfactorio.
¡Ve a ver a tu médico!''')
txt_res.append('''promedio.
Podría valer la pena realizar pruebas adicionales con el médico.''')
txt_res.append('''
superior al promedio''')
txt_res.append('''
alto''')

def ruffier_index(pulso_1:int, pulso_2:int, pulso_3:int) -> float:
   index = (4 * (pulso_1 + pulso_2 + pulso_3) - 200) / 10
   
   return index 

def neud_level(age):
   ''' las opciones con una edad menor de 7 años y con adultos deben procesarse por separado,
   aquí seleccionamos el nivel “insatisfactorio” solo dentro de la tabla:
   para la edad de 7 años, “insatisfactorio” es un índice de 21, luego, cada 2 años, disminuye en 1.5 hasta el nivel de 15 a los 15–16 años '''
    pass
    
def ruffier_result(r_index, level):
   ''' la función obtiene un índice de Ruffier e lo interpreta,
   devolvemos el nivel de preparación: un número del 0 al 4
   (cuanto mayor sea el nivel de preparación, mejor). '''
    pass

def test(P1, P2, P3, age):
   ''' esta función puede usarse desde fuera del módulo para calcular el índice de Ruffier.
   Devolvemos los textos listos que solo necesitan escribirse en el lugar necesario.
   Usamos las constantes definidas al inicio de este módulo para los textos. '''
    pass

