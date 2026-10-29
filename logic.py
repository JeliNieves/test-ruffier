def ruffier_index(pulso_1:int, pulso_2:int, pulso_3:int) -> float:
    index = (4 * (pulso_1 + pulso_2 + pulso_3) - 200) / 10
    
    return index



def check_int(val):
    try:
        return int(val)
    except ValueError:
        return False


def ruffier_index(r, edad):
    # --- CATEGORÍA: 15 AÑOS O MAYOR ---
    if edad >= 15:
        if r >= 15.0:
            return "Bajo"
        elif 11.0 <= r <= 14.9:
            return "Satisfactorio"
        elif 6.0 <= r <= 10.9:
            return "Promedio"
        elif 0.5 <= r <= 5.9:
            return "Más alto del promedio"
        else: # 0.4 e inferior
            return "Alto"
            
    # --- CATEGORÍA: DE 13 A 14 AÑOS ---
    elif 13 <= edad <= 14:
        if r >= 16.5:
            return "Bajo"
        elif 12.5 <= r <= 16.4:
            return "Satisfactorio"
        elif 7.5 <= r <= 12.4:
            return "Promedio"
        elif 2.0 <= r <= 7.4:
            return "Más alto del promedio"
        else: # 1.9 e inferior
            return "Alto"
            
    # --- CATEGORÍA: DE 11 A 12 AÑOS ---
    elif 11 <= edad <= 12:
        if r >= 18.0:
            return "Bajo"
        elif 14.0 <= r <= 17.9:
            return "Satisfactorio"
        elif 9.0 <= r <= 13.9:
            return "Promedio"
        elif 3.5 <= r <= 8.9:
            return "Más alto del promedio"
        else: # 3.4 e inferior
            return "Alto"
            
    # --- CATEGORÍA: DE 9 A 10 AÑOS ---
    elif 9 <= edad <= 10:
        if r >= 19.5:
            return "Bajo"
        elif 15.5 <= r <= 19.4:
            return "Satisfactorio"
        elif 10.5 <= r <= 15.4:
            return "Promedio"
        elif 5.0 <= r <= 10.4:
            return "Más alto del promedio"
        else: # 4.9 e inferior
            return "Alto"
            
    # --- CATEGORÍA: DE 7 A 8 AÑOS ---
    elif 7 <= edad <= 8:
        if r >= 21.0:
            return "Bajo"
        elif 17.0 <= r <= 20.9:
            return "Satisfactorio"
        elif 12.0 <= r <= 16.9:
            return "Promedio"
        elif 6.5 <= r <= 11.9:
            return "Más alto del promedio"
        else: # 6.4 e inferior
            return "Alto"
            
    # --- CASO DE SEGURIDAD (Menores de 7 años) ---
    else:
        return "Edad no apta para el test (Mínimo 7 años)"
