# Números Romanos

## Quiero construir un nuevo tipo de número en Pytho, nº romano.
### 2ª kata, es importante.

Tenemos que crear una función que coja un número entero de entrada y lo transforme a número romano.

1984
El algoritmo de Jhon lo que hace es restarle cifras romanas M, D, C, L, X, V, I

Por tanto lo primero que restamos es M, luego D, 
Habrá problema con los 4 y con los 9, pues el orden de las figuras en número romanos no resulta en mostrar IV si no IIII.

Auto observarnos resolviendo el problema. Divide y vencerás.

Lo suyo es dividir por unidad, esto es: 1, 9, 6, 9. Dependiendo de la posición equivaldrá a un valor especificado tal cual.

Primero lo que tenemos que hacer es separar el número en sus distintos componentes: millar, centena, decena, etc. 
Aunque el paso previo, tenemos que acotar el alcance de la función.

Lo segundo sería traducir por orden de magnitud.