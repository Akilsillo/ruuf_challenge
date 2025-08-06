# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

```bash
cd ruuf_challenge
python3 main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

Explica acá
#### Lógica del algoritmo

La solución implementada es un algoritmo heurístico basado en la partición recursiva del espacio, este método sigue una estrategia "greedy" que busca maximizar el empaquetado en cada paso.

El proceso está implementado en la función `calculate_panels` y se puede desglosar de la siguiente manera:

1. Considerar Ambas Orientaciones: El algoritmo evalúa dos escenarios principales de forma independiente:

    Escenario A: Colocar los paneles en su orientación original (vertical).

    Escenario B: Colocar los paneles rotados 90 grados (horizontal).

2. Llenado Inicial: En cada escenario, el algoritmo primero llena el área del techo con la mayor cantidad posible de paneles en la orientación correspondiente.

3. Partición del Espacio Sobrante: Una vez colocada la cuadrícula principal, se llama nuevamente la función `calculate_panels` para así comprobar cuantos paneles caben en los dos rectángulos que se pueden formar con el espacio sobrante.

4. Resultado Final: El número total de paneles para el Escenario A es la suma de los paneles de la cuadrícula inicial más los obtenidos en las llamadas recursivas. Se realiza el mismo cálculo para el Escenario B. El resultado final de la función es el valor máximo entre el total del Escenario A y el total del Escenario B.

---

## 💰 Bonus (Opcional)

Si completaste alguno de los ejercicios bonus, explica tu solución aquí:

### Bonus Implementado
*[Indica cuál bonus implementaste: Opción 1 (techo triangular) o Opción 2 (rectángulos superpuestos)]*




### Explicación del Bonus
*[Explica cómo adaptaste tu algoritmo para resolver el bonus]*




---

## 🤔 Supuestos y Decisiones

Una decisión que considero importante, es la de limitar la rotación de los rectángulos pequeños a solo 90°. A pesar de que se puede modificar la formula para considerar casos donde utilizando diagonales se pueden empaquetar rectángulos pequeños que aparentemente no caben en el contenedor, decidí no tomar en cuenta estos, ya que no me hacen sentido teniendo en cuenta el el contexto real al que se aplicaría esta solución(la instalación de paneles solares).