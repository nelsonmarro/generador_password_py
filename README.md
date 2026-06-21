# Generador de Contraseñas Seguro en Python

Un programa de consola en Python diseñado para generar contraseñas criptográficamente seguras. Este proyecto fue construido con un enfoque estructurado (sin funciones complejas), ideal para principiantes en la lógica de programación.

## Requisitos

- Python 3.6 o superior.
- No requiere instalación de librerías externas (solo usa `string` y `secrets` nativas).

## Cómo Usarlo

1. Abre tu terminal o consola de comandos.
2. Clona o descarga este repositorio en tu máquina local.
3. Navega hasta la carpeta del proyecto.
4. Ejecuta el archivo principal:

```bash
python generador_password_v1.py
```

1. Sigue las instrucciones en pantalla para definir la longitud y los criterios de tu contraseña.

## Estructura Lógica y Diagramas de Flujo

1. **`diagrama-principal.png`**: Muestra el bucle principal de ejecución y la validación de la longitud. Llama internamente a los dos sub-procesos siguientes.
2. **`diagrama-sub1.png`**: Detalla el "Sub-proceso 1", donde se validan los 4 criterios lógicos (mayúsculas, minúsculas, números y símbolos) y se rellena la contraseña garantizando la diversidad.
3. **`diagrama-sub2.png`**: Detalla el "Sub-proceso 2", que se encarga de barajar aleatoriamente los caracteres generados y mostrarlos en pantalla.
