# Teoría y Fundamentos del Generador de Contraseñas

Este documento expone la base teórica y los requerimientos funcionales detrás de la construcción de un generador de contraseñas seguro.

## 1. Teoría: Entropía y Fuerza Bruta
La seguridad de una contraseña depende directamente de su **entropía**, la cual es una medida matemática de qué tan impredecible es la clave. Un atacante utiliza métodos de "fuerza bruta" (probar todas las combinaciones posibles) para vulnerarla.

La resistencia matemática ante estos ataques se logra mediante dos factores:
1.  **Espacio de Caracteres (Diversidad):** Al combinar mayúsculas, minúsculas, números y símbolos, el número de posibilidades para un solo carácter se amplía significativamente.
2.  **Longitud:** Es el factor más crítico. La dificultad para adivinar una contraseña crece de forma exponencial por cada carácter adicional que se agrega a la longitud total.
3.  **CSPRNG (Generador de Números Pseudoaleatorios Criptográficamente Seguro):** Los algoritmos básicos (`random`) son predecibles si se conoce la "semilla" del sistema. Un generador seguro utiliza librerías especiales (como `secrets` en Python) para recolectar aleatoriedad del hardware del sistema operativo, volviéndola verdaderamente impredecible.

## 2. Funcionalidades Requeridas del Programa

Para que el programa sea considerado robusto y seguro, debe cumplir con los siguientes hitos funcionales:

*   **Validación de Entrada (Input Validation):** El programa no debe colapsar ante entradas incorrectas (ej. escribir letras cuando se pide un número).
*   **Longitud Mínima Forzosa:** Debe prohibir la generación de claves menores a 8 caracteres, ya que cualquier longitud inferior es matemáticamente vulnerable hoy en día.
*   **Selección Dinámica:** Debe permitir al usuario decidir qué conjuntos de caracteres (criterios) desea incluir.
*   **Inclusión Garantizada:** Debe existir una lógica que garantice que, si el usuario pidió un símbolo, la contraseña final contenga obligatoriamente al menos un símbolo (evitando que el azar puro excluya un criterio solicitado).
*   **Ciclo de Uso:** Debe funcionar de manera iterativa, permitiendo generar múltiples contraseñas sin necesidad de reiniciar la aplicación de consola.
