         JUEGO DE LA SERPIENTE
         Evaluación en Contacto con el Docente 
         Universidad Internacional Del Ecuador


INTEGRANTE

Juan Brayson Gomez Zuñiga


Introducción

La tecnología ha transformado la manera en que las personas interactúan con el mundo digital, y la programación es una de las herramientas fundamentales que hace posible ese cambio. En el ámbito educativo, el desarrollo de software permite a los estudiantes aplicar de forma práctica los conocimientos teóricos adquiridos en el aula, fortaleciendo habilidades como el pensamiento lógico, la resolución de problemas y la organización del trabajo.
El presente proyecto consiste en el desarrollo de un videojuego funcional basado en el clásico juego de la serpiente, implementado en el lenguaje de programación Python utilizando la librería gráfica Tkinter. Este juego, ampliamente reconocido por su sencillez y lógica clara, representa un escenario ideal para aplicar conceptos de programación como estructuras condicionales, bucles repetitivos, funciones y organización modular del código.


OBJETIVO DEL SISTEMA

Desarrollar un videojuego funcional de la serpiente (Snake)
utilizando Python y la librería Tkinter, aplicando los
fundamentos de programación aprendidos durante la asignatura:
estructuras lógicas, condicionales, bucles, funciones y
organización del código.


DESCRIPCION DEL PROBLEMA

El juego de la serpiente es un clásico donde el jugador
controla una serpiente que debe comer alimentos para crecer,
evitando chocar con las paredes o con su propio cuerpo.
Este proyecto resuelve el reto de implementar la lógica de
un juego en tiempo real usando únicamente herramientas base
de Python, sin librerías externas.


FUNCIONALIDADES DEL SISTEMA

1. Iniciar partida         -> Presionar Enter para comenzar
2. Controlar la serpiente  -> Teclas de flecha arriba/abajo/izquierda/derecha
3. Comer alimentos         -> La serpiente crece al consumir comida aleatoria
4. Detectar colisiones     -> Game Over si choca con paredes o consigo misma
5. Puntaje en tiempo real  -> Se actualiza en pantalla con cada alimento
6. Aumento de velocidad    -> Cada 5 puntos la serpiente acelera
7. Pausar juego            -> Tecla P pausa y reanuda
8. Reiniciar partida       -> Enter después del Game Over
9. Finalizar juego         -> Tecla Esc cierra el programa
10. Pantalla Game Over     -> Muestra puntaje final y opciones


ARQUITECTURA DEL SISTEMA


       CAPA DE PRESENTACION          
   Interfaz grafica con Tkinter      
   Canvas, Labels, Ventana           

       CAPA LOGICA DEL JUEGO        
   Gameloop, Gestor Movimiento      
   Detector Colisiones, Puntaje     
          
       CAPA DE DATOS Y ESTADO       
   Posiciones, Dirección            
   Velocidad, Puntaje, Comida       


RELACION CON CONTENIDOS DE LA ASIGNATURA


Unidad 1 - Fundamentos de programación
  Aplicación: Variables, tipos de datos y constantes del juego

Unidad 2 - Estructuras condicionales
  Aplicación: if para colisiones, dirección opuesta, comer comida

Unidad 3 - Estructuras repetitivas
  Aplicación: while en generador de comida, for en renderizado

Unidad 4 - Funciones y modularidad
  Aplicación: Código dividido en funciones por responsabilidad


TECNOLOGIAS UTILIZADAS

- Lenguaje       : Python
- Motor Grafico  : Tkinter


CONTROLES DEL JUEGO

  Flechas (arriba/abajo/izq/der) -> Mover la serpiente
  Enter                          -> Iniciar / Reiniciar partida
  P                              -> Pausar / Reanudar
  Esc                            -> Salir del juego


CRONOGRAMA DE ACTIVIDADES

Semana 1 -> Definicion del problema y alcance del proyecto

Semana 2 -> Planificacion y cronograma de actividades

Semana 3 -> Elaboracion del diagrama de casos de uso

Semana 4 -> Elaboracion del diagrama de flujo

Semana 5 -> Diseno de la arquitectura del sistema

Semana 6 -> Desarrollo del codigo

Semana 7 -> Desarrollo completo, pruebas, correcciones y entrega


REFLEXION

El desarrollo de este proyecto demuestra como la programación
puede recrear experiencias de entretenimiento que durante
décadas han acompañado a generaciones de usuarios. El juego
Snake, popularizado en los teléfonos Nokia en los anos 90,
es hoy un ejercicio clásico de programación que permite
aplicar conceptos fundamentales como bucles, condicionales
y manejo de eventos.


FECHA DE ENTREGA

26/06/2026
