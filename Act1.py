import numpy as np

#excepción 
class ErrorMatrizSingular(Exception):
    pass

def resolver_sistema_gauss(A_input, b_input):
    """
    Eliminación Gaussiana simple.
    A_input: Matriz de coeficientes
    b_input: Vector de resultados
    """
    try:
        # Convertimos a float para evitar problemas de división entera
        A = np.array(A_input, dtype=float)
        b = np.array(b_input, dtype=float)
        
        n = len(b) # Número de ecuaciones
        
        #ELIMINACIÓN HACIA ADELANTE 
        
        for k in range(n-1):
            
            #Si el pivote es casi 0 no podemos dividir 
            if abs(A[k, k]) < 1e-10:
                raise ErrorMatrizSingular(f"El pivote en la fila {k} es cero")
            
            # Hacemos ceros debajo del pivote
            for i in range(k+1, n):
                # Calculamos el factor
                factor = A[i, k] / A[k, k]
                
                # Restamos a la fila actual la fila del pivote multiplicada por el factor
                # En numpy esto resta toda la fila de golpe 
                A[i, k:] = A[i, k:] - factor * A[k, k:]
                b[i] = b[i] - factor * b[k]

        # SUSTITUCIÓN HACIA ATRÁS
        
        # Verificamos el último elemento antes de empezar
        if abs(A[n-1, n-1]) < 1e-10:
             raise ErrorMatrizSingular("Fallo en el último paso: matriz singular.")

        x = np.zeros(n) # Vector vacío para las soluciones
        
        # Vamos desde la última fila hacia arriba (range inverso)
        for i in range(n-1, -1, -1):
            suma = np.dot(A[i, i+1:], x[i+1:])
            x[i] = (b[i] - suma) / A[i, i]
            
        return x

    except ErrorMatrizSingular as e:
        print("ERROR La matriz es singular")
        return None
        
    except Exception as e:
        print(f"ERROR DE CÓDIGO O DATOS: {e}")
        return None


# CASO 1: Un sistema no singular
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3
matriz_bien = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
vector_bien = [8, -11, -3]

print("Sistema funcionañ")
resultado = resolver_sistema_gauss(matriz_bien, vector_bien)
if resultado is not None:
    print("La solución es:", resultado)


# matriz singular 
matriz_mal = [[1, 1, 1], [2, 2, 2], [3, 1, 4]]
vector_mal = [1, 2, 5]

print("\nSistema Singular")
resolver_sistema_gauss(matriz_mal, vector_mal)