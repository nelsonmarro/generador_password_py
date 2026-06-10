# Proyecto: Generador Seguro de Contraseñas

---

## 1. Análisis del Problema

### Definición y Entendimiento

El problema radica en la vulnerabilidad de las cuentas digitales debido al uso de contraseñas débiles o repetidas. Se requiere una herramienta que genere cadenas de caracteres aleatorias con alta entropía y seguridad que le permitirá a los usuarios crear contraseñas seguras y robustas.

### Variables de Entrada

- **Longitud (L)**: Número total de caracteres (mínimo recomendado: 12).
- **Criterios (C)**: Mayúsculas, minúsculas, números y símbolos especiales.

### Procesos (Lógica del Sistema)

1. **Validación**: Verificar que la longitud sea un entero positivo (L > 8) y se haya seleccionado al menos un criterio.
2. **Construcción del Conjunto de Caracteres**: Unión de conjuntos según los criterios.
3. **Generación Criptográfica**: Utilizar un generador de números aleatorios seguro (CSPRNG - Cryptographically Secure Pseudo-Random Number Generator).
4. **Garantía de Diversidad**: Asegurar la inclusión de al menos un carácter por cada tipo elegido.
5. **Cálculo de Fortaleza**: Evaluación de la dificultad de descifrar el resultado.
6. **Garantía de Aleatoriedad**: Asegurar que una misma contraseña no se repita.

### Variables de Salida

- **Contraseña**: Cadena de texto generada.
- **Estado**: Confirmación de fortaleza y copiado al portapapeles.

---

## 2. Diseño de la Solución

### Técnicas de Representación

Para representar visualmente la solución y asegurar su correcto diseño, se seleccionaron las siguientes herramientas de diagramación:

- **Diagrama de Secuencia (UML)**:
  - **Por qué se usó**: Es la mejor opción para mostrar paso a paso la interacción temporal entre el usuario, la interfaz de usuario (UI) y el motor de generación en memoria. Permite modelar el ciclo de vida de una solicitud de contraseña, visualizando con precisión el flujo de mensajes, las llamadas a funciones de validación y la entrega del resultado de manera secuencial.
- **Modelo C4 (Nivel de Contenedores)**:
  - **Por qué se usó**: Se eligió este estándar moderno para representar la estructura arquitectónica del sistema. Permite ilustrar la separación de responsabilidades entre la capa de presentación (Frontend) y la capa de lógica (Web Crypto API), dejando claro que la aplicación opera completamente en el dispositivo del usuario sin enviar datos a servidores externos, reforzando el diseño de seguridad.

## 3. Implementación (Referencia de la Interfaz)

Para la futura construcción del aplicativo, se propone el desarrollo de una interfaz gráfica de usuario interactiva que actúe como puente entre los parámetros seleccionados (longitud y tipo de caracteres) y el proceso lógico del generador. El diseño preliminar planteado se presenta como referencia visual en el informe técnico.

---

## 4. Revisión

### Verificación de Correctitud

- **Pruebas de Límite**: Validación de rangos de longitud (8-64 caracteres).
- **Validación Lógica**: Uso de expresiones regulares para confirmar que la salida cumple con los tipos seleccionados.
- **Auditoría de Seguridad**: Verificación del uso de funciones criptográficas resistentes al análisis.
- **Verificar Aleatoriedad**: Verificar que la salida no se repite en varias ejecuciones.

### Análisis de Fortaleza (Nivel de Seguridad)

Para entender la seguridad de la contraseña generada, imaginemos a una supercomputadora intentando adivinarla probando todas las combinaciones posibles. Una contraseña de 12 caracteres creada con esta herramienta es tan compleja que le tomaría a esa computadora **miles de años** descifrarla. Esto garantiza que la información del usuario esté protegida incluso ante los ataques más potentes.
