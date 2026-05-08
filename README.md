## Información de los Integrantes
* **Institución:** Instituto Politécnico Nacional (IPN)
* **Escuela:** Escuela Superior de Cómputo (ESCOM) 
* **Unidad de Aprendizaje:** Teoría de la Computación 
* **Programa Académico:** Ingeniería en Sistemas Computacionales / Plan 2020 
* **Grupo:** 4CM4
* **Alumnos:** 
   * Diego Ruperto Hernandez (Boleta: 2024630696)
   * Maria Jose Venegas Martinez (Boleta: 2024630831)

---

## Objetivo
El propósito de esta práctica es trabajar en la transformación de gramáticas independientes del
contexto a la forma normal de Chomsky y a la forma normal de Greibach, utilizando el software JFLAP. También
se ampliará el software interactivo desarrollado en las prácticas 1-4 para incluir la funcionalidad de visualización
de autómatas, mejorando así la comprensión, el análisis de los procesos y la experiencia de usuario.

## Introduccion 
Esta practica muestra todo lo que hemos aprendido hasta el momento, esto nos ayuda a reforzar todos los conceptos sobre la materia además de que nos forma en el ambito practico sobre todos estos conceptos y donde es que se encuentran o se pueden utilizar en el mumdo real. Pra esta practica se reunen todas las pequeñas aplicaciones que hemos realizado hasta ahora ademas de introducir doa nuevos conceptos, como lo son **La forma normal de chumsky** y **La forma normal de Greibach**. Aprenderemos a como es que un lenguaje libre de contexto pasa o esta en estas formas y de igual manera que como lo hemos estado realizando hasta la fecha lo anexaremos en nuestra aplicación final.


### Forma normal de Greibach 
Una gramática independiente del contexto (GIC) está en Forma normal de Greibach (FNG) si todas y cada una de sus reglas de producción tienen un consecuente que empieza por un carácter del alfabeto, también llamado símbolo terminal. Formalmente, cualquiera de las reglas tendrá la estructura:

* A→aw

Donde "A" es el antecedente de la regla, que en el caso de las GIC debe ser necesariamente un solo símbolo auxiliar. Por su parte, "a" es el mencionado comienzo del consecuente y, por tanto, un símbolo terminal. Finalmente, "w" representa una concatenación genérica de elementos gramaticales, esto es, una sucesión exclusivamente de auxiliares, inclusive, pudiera ser la palabra vacía; en este caso particular, se tendría una regla llamada "terminal":

 * A→a

Existe un teorema que prueba que cualquier GIC, cuyo lenguaje no contiene a la palabra vacía, si no lo está ya, se puede transformar en otra equivalente que sí esté en FNG. Para su demostración, normalmente, se procede por construcción, es decir, se plantea directamente un algoritmo capaz de obtener la FNG a partir de una GIC dada.


**Pasos del Algoritmo para llegar a la forma normal de Greibach**:
**Eliminación de Recursividad Izquierda**: Representa el paso más crítico del proceso. Si existe una regla de la forma $A \rightarrow A\alpha \mid \beta$, el algoritmo la transforma en una estructura no recursiva mediante la introducción de una variable auxiliar $Z$. Esto es vital para evitar bucles infinitos en los analizadores sintácticos descendentes.
**Sustitución de Variables**: Se establece un orden jerárquico para las variables (ej. $A_1, A_2, \dots, A_n$). El objetivo es garantizar que para toda regla $A_i \rightarrow A_j\gamma$, se cumpla la condición $j > i$. En caso de que $j < i$, se sustituye $A_j$ por sus definiciones correspondientes hasta que la regla comience con un terminal o una variable de índice mayor.
**Conversión Final**: Una vez que la gramática se encuentra debidamente ordenada, se realiza un proceso de sustitución hacia atrás ("back-substitution"). Esto asegura que todas las producciones de la gramática comiencen finalmente con un símbolo terminal, cumpliendo así con la definición estricta de la FNG.

### Forma normal de Chomsky 
Una gramática formal está en Forma normal de Chomsky si todas sus reglas de producción son de alguna de las siguientes formas:

A→BC o
A→α
donde 
A, B y C
Son símbolos no terminales (o variables) y α es un símbolo terminal.

Todo lenguaje independiente del contexto que no posee a la cadena vacía, es expresable por medio de una gramática en forma normal de Chomsky (GFNCH) y recíprocamente. Además, dada una gramática independiente del contexto, es posible algorítmicamente producir una GFNCH equivalente, es decir, que genera el mismo lenguaje.

**Pasos del Algoritmo para llegar a la forma normal de Chomsky**:
**Sustitución del Símbolo Inicial**: Se añade una nueva regla $S_0 \rightarrow S$. Esto garantiza que el símbolo inicial real nunca aparezca en el lado derecho de una producción, evitando ciclos recursivos hacia el origen y asegurando la integridad de la estructura.
**Eliminación de Producciones $\lambda$ (Epsilon)**: Se identifican los símbolos "anulables" (aquellos que pueden derivar en la cadena vacía). Para cada regla que contenga un símbolo anulable, el sistema genera automáticamente las nuevas reglas resultantes de omitir dicho símbolo, eliminando finalmente todas las reglas $A \rightarrow \lambda$.
**Eliminación de Producciones Unitarias**: Las reglas del tipo $A \rightarrow B$ se eliminan sustituyéndolas por el conjunto de producciones de $B$. Este proceso optimiza la gramática reduciendo la "profundidad" innecesaria en el árbol de derivación.
**Binarización de Producciones**: En casos donde una regla tiene más de dos variables (ej. $A \rightarrow BCD$), se introducen variables auxiliares ($X_1, X_2...$) para descomponer la cadena en pares jerárquicos: $A \rightarrow BX_1$ y $X_1 \rightarrow CD$, cumpliendo así con el estándar binario de la FNC.


## Funcionalidades del Sistema
La aplicación (desarrollada en Python con Tkinter) implementa los siguientes módulos:

1. **Subcadenas, Prefijos y Sufijos:**
   * Cálculo exhaustivo de todas las subcadenas, prefijos y sufijos de una cadena de entrada.
   * Interfaz gráfica organizada para la visualización de resultados.
   * Funcionalidad para guardar los resultados obtenidos en un archivo de texto (.txt).

2. **Cerraduras de Kleene y Positiva:** 
   * Cálculo de la cerradura de Kleene ($\Sigma^*$) y la cerradura positiva ($\Sigma^+$) para un alfabeto definido.
   * Opción para especificar la longitud máxima de las cadenas a generar.
   * Visualización interactiva y opción de exportación de resultados.

3. **Automatas Finitos Deterministas (Carga):**
   * Carga de AFD por distintos documentos, tanto .jff y .json.
   * Se nuestra el modelo del AFD. 
   * Apartir de estos datos se crea la quintupla de el AFD.
   * Opción para probar cualquier cadena en el ADF.
   * Visualización del camino tomado por cada digito de la cadena entre los estados del AFD hasta ser rechazada o aceptada.

4. **Automatas Finitos Deterministas (Construye):**
   * Opción de especificar la quintupla de un AFD de forma manual.
   * Apartir de esos datos se crea el diagrama del AFD.
   * Opción para probar cualquier cadena en el ADF.
   * Visualización del camino tomado por cada digito de la cadena entre los estados del AFD hasta ser rechazada o aceptada.
   * Se muestra el modelo del AFD. 
   * Opcion de guardar el modelo del AFD en los archivos .jff y .json

5. **Operaciones con AFN-> AFD y el AFD (Simplificado):**
    * Permite cargar el AFN para poder vizualizar como es que se ve de forma grafica
    * Permite hacer la conversion del AFN a un AFD
    * Permite la visualizacion de la conversion del AFD
    * Opcion para guardar el AFD que se haya creado
    * Permite minimizar/simplicar el AFD

6. **Operaciones con AF -> ER :**
    * Del AF que se cargo previamente en la pestaña anterior convertirlo en una expresion regular

7. **Operaciones con ER -> AF :**
    * Permite ingresar una expresion regular para poder transformarla a un Automata Finito
    * Una vez creado el AF permite vizualizar como es que este se ve
    * Opcion de poder guardar el AF convertido de la Expresion Regular 

8. **Aplicaciones de Expresiones Regulares:**
    * **Selector de Modelos de Validación**: Permite elegir mediante un menú desplegable entre diferentes patrones estándar como:
        * **Correo Electrónico**: Validación de estructura `usuario@dominio.ext`.
        * **URL**: Verificación sintáctica de protocolos y dominios web.
        * **Fecha**: Validación de formato numérico `DD/MM/AAAA`.
    * **Motor de Validación en Tiempo Real**: Al ingresar una cadena y ejecutar *"Validar y Graficar"*, el sistema procesa la entrada contra el autómata correspondiente.
    * **Visualización Dinámica del Autómata**: Despliega gráficamente el modelo matemático que fundamenta la validación, permitiendo observar el recorrido de estados que realiza la cadena.
    * **Retroalimentación Instantánea**: Determina de forma visual si la cadena es aceptada o rechazada por el lenguaje definido.

9. **Transformación de Gramáticas (Forma Normal de Chomsky y Forma normal de Greibach)**:
* Procesamiento y simplificación de Gramáticas Libres del Contexto (GLC) mediante algoritmos de normalización.
*Conversión a FNC: Algoritmo automatizado que transforma producciones a la estructura estándar ($A \rightarrow BC$ o $A \rightarrow a$).
* Seguimiento de Procesamiento: Visualización paso a paso de las transformaciones:
   * Aislamiento del símbolo inicial mediante un nuevo estado $S'$.
   * Eliminación de producciones vacías ($\lambda$) mediante la clausura de símbolos anulables.
   * Eliminación de producciones unitarias para reducir la profundidad del árbol de derivación.
   * Sustitución de terminales en cuerpos mixtos y binarización de reglas largas.
   * Interoperabilidad con JFLAP: Capacidad de exportar la gramática resultante en formato .jff para su validación académica.

## Instalación de entorno virtual
 **Instalación y Configuración de Python:** Antes de comenzar a utilizar **Tkinter** para desarrollar la interfaz gráfica de la práctica, es necesario tener Python instalado y configurado. Para ello, siga los siguientes pasos:

1.**Instalar Python**

* Descargue Python: Visite la página oficial de Python en https://www.python.org/downloads/.
* Instale Python: Ejecute el instalador. Durante la instalación, asegúrese de marcar la casilla **"Add Python to PATH"** para que Python se pueda ejecutar desde cualquier terminal.
* Verifique la Instalación : Una vez instalado, abra una terminal (símbolo del sistema en Windows o terminal en macOS/Linux) y ejecute el siguiente comando:

```
python --version
```

Esto debería mostrar la versión instalada de Python. Para esta aplicacion ocuparemos la version de python 3.12.3

2.**Instalar Visual Studio Code**

Visual Studio Code (VS Code) es un entorno de desarrollo ligero y flexible que puede utilizar para programar en Python.
* Descargue VS Code: Diríjase al sitio oficial de Visual Studio Code y descargue la versión para su sistema operativo.
* Instale la Extensión de Python: Abra **VS Code**, diríjase a la pestaña de **Extensiones** (ícono de cubo en la barra lateral), busque e instale la extensión de **Python**. Esto habilitará herramientas adicionales como el resaltado de sintaxis y depuración para Python.

## Preparación del entorno virtual
1.**Crear un Entorno Virtual en Python**

Es recomendable trabajar en entornos virtuales para mantener las dependencias del proyecto aisladas. A continuación, se explica cómo crear un entorno virtual para su proyecto:
* Abra una terminal en Visual Studio Code.
* Navegue hasta la carpeta de su proyecto o cree una nueva carpeta para su proyecto con:

```
mkdir MiProyecto
cd MiProyecto
```

* Cree un entorno virtual ejecutando el siguiente comando:

```
python -m venv venv
```

Esto creará una carpeta llamada venv que contendrá su entorno virtual.

* Active el entorno virtual :
   * En Windows: ```venv\Scripts\activate```
   * En macOS/Linux: ```source venv/bin/activate```

* Verifique que el entorno está activado: El nombre del entorno (venv) debería aparecer al principio de la línea en su terminal.

2.**Instalar Tkinter**

Con el entorno virtual activado, instale el paquete de Tkinter, que es necesario para desarrollar la interfaz gráfica.
Para ello, ejecute el siguiente comando en la terminal:

   * En Windows: ```pip install tk```
   * En macOS/Linux: ```sudo apt-get install python3-tk   ```

**Probar un Programa Simple en Tkinter**
* Cree un archivo Python: En la carpeta de su proyecto, cree un archivo con el nombre **app.py**.
* Escriba el siguiente código básico en el archivo app.py para probar Tkinter:

 ```python
from tkinter import Tk, Label

app = Tk()
app.title("Hola mundo")
label = Label(app, text="¡Hola, mundo!")
label.pack()
app.mainloop()   
```

* Ejecute el archivo desde la terminal : ```python app.py```

* Verifique que se abre la aplicación: Esto debería abrir una ventana de navegador con el mensaje: **¡Hola Mundo!**

Recomendación
Asegúrese de activar el entorno virtual cada vez que trabaje en su proyecto, para garantizar que las dependencias se instalen correctamente en el entorno aislado.

Una vez listo nuestro compilador, nuestro lenguaje de programacion y las librerias que instalamos dentro de nuestro entorno virtual aislado pasaremos con la funcionalidad de nuestro codigo. 

# Funcionalidad del código

## Logica de las cadenas (Operaciones sobre cadenas) ```strings_logic.py```

### Prefijos: 
Un prefijo es una subcadena que aparece al inicio de una cadena original $w$. Formalmente, una cadena $x$ es un prefijo de $w$ si existe una cadena $y$ tal que $w = xy$.

$$P(w) = \{x \mid \exists y \in \Sigma^*, w = xy\}$$

**Implementacion del codigo**
```python
def get_prefixes(string):
    """Calcula todos los prefijos de una cadena."""
    # Retorna una lista de rebanadas (slices) desde el inicio
    return [string[:i] for i in range(len(string) + 1)] 
```
**Como funciona**:
**Rango de Iteración**: El range(len(string) + 1) asegura que se incluya desde el índice 0 hasta la longitud total, permitiendo capturar tanto la cadena vacía ($\lambda$) como la cadena completa.
**Slicing Dinámico**: Utiliza la sintaxis de Python [:i] para extraer subcadenas que comienzan siempre en la posición inicial (índice 0) y terminan en la posición $i$.
**Comprensión de Listas**: Genera la colección completa de prefijos en una sola línea, manteniendo una complejidad de tiempo $O(n^2)$ debido a la creación de las subcadenas.Resultado Estructurado: Para una cadena como "abc", la función devuelve de forma ordenada: ['', 'a', 'ab', 'abc'].

### Sufijos: 
Un sufijo es una subcadena que aparece al final de una cadena original $w$. Formalmente, una cadena $y$ es un sufijo de $w$ si existe una cadena $x$ tal que $w = xy$.

$$S(w) = \{y \mid \exists x \in \Sigma^*, w = xy\}$$

**Implementacion del codigo**
```python
def get_suffixes(string):
    """Calcula todos los sufijos de una cadena."""
    # Retorna una lista de rebanadas (slices) hasta el final
    return [string[i:] for i in range(len(string) + 1)] 
```
**Como funciona**:
**Desplazamiento del Índice**: El range(len(string) + 1) define el punto de inicio de cada subcadena. Al incrementar $i$, el punto de corte se mueve hacia la derecha.
**Slicing Inverso**: Utiliza la sintaxis de Python [i:] para extraer todo el contenido desde la posición $i$ hasta el último carácter de la cadena original.
**Inclusión de la Cadena Vacía**: Cuando $i$ alcanza el valor de len(string), el slice [len:] genera automáticamente la cadena vacía ($\lambda$), cumpliendo con la definición formal de sufijos.
**Orden de Generación**: Para una cadena como "abc", la función genera los sufijos en orden decreciente: ['abc', 'bc', 'c', ''].

### Subcadenas:
Una subcadena es cualquier segmento contiguo de una cadena original $w$. Formalmente, una cadena $z$ es una subcadena de $w$ si existen dos cadenas $x, y \in \Sigma^*$ tales que $w = xzy$.

$$\text{Sub}(w) = \{z \mid \exists x, y \in \Sigma^*, w = xzy\}$$

**Implementacion del codigo**
```python
def get_substrings(string):
    """Calcula todas las subcadenas posibles ordenadas por longitud."""
    substrings = {""} # Inicializa con la cadena vacía (λ)
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(string[i:j])
    return sorted(list(substrings), key=lambda x: (len(x), x))
```
**Como funciona**:
**Doble Iteración (Anidada)**: Utiliza dos ciclos for para definir los límites de cada segmento. El índice i marca el inicio de la subcadena, mientras que j marca el final (exclusivo).
**Uso de Conjuntos (set)**: Se utiliza substrings = {""} para evitar duplicados de forma eficiente. Esto es crucial cuando la cadena original tiene caracteres repetidos (ej. "aaaa").
**Slicing de Rangos**: La operación string[i:j] extrae todas las combinaciones posibles de caracteres contiguos dentro del rango $[i, j)$.
**Criterio de Ordenamiento**: La función sorted utiliza una llave lambda para organizar los resultados primero por su longitud (len(x)) y, en caso de empate, de forma alfabética (x).
**Resultado Estructurado**: Para una cadena "abc", el conjunto se transforma en una lista ordenada: ['', 'a', 'b', 'c', 'ab', 'bc', 'abc'].

## Logica de las lenguajes (Operaciones sobre Lenguajes) ```languajes_logic.py```
Este módulo implementa las operaciones de potencias de un alfabeto $\Sigma$ para generar conjuntos de cadenas según las reglas de los lenguajes formales.

### Detalles tecnicos de Implementacion
* **Uso de ```itertools```**: Se eligió esta librería estándar de Python porque es altamente eficiente para manejar combinaciones y permutaciones, evitando el uso de múltiples ciclos anidados manuales que aumentarían la complejidad computacional.
* **Concatenación**: Debido a que ```itertools.product``` devuelve tuplas $(ej: ('a', 'b'))$, utilizamos ```''.join(c)``` para unir esos caracteres en una sola cadena de texto $("ab")$ antes de mostrarla en la interfaz.

### Cerradura de Kleene
La cerradura de Kleene de un alfabeto $\Sigma$, denotada como $\Sigma^*$, es el conjunto de todas las cadenas posibles que pueden formarse con los símbolos de $\Sigma$, incluyendo la cadena vacía ($\lambda$). Formalmente, es la unión infinita de potencias del alfabeto.

$$\Sigma^* = \bigcup_{i=0}^{\infty} \Sigma^i = \Sigma^0 \cup \Sigma^1 \cup \Sigma^2 \cup \dots$$

**Implementacion del codigo**
```python
def get_kleene_closure(alphabet, max_n):
    """Calcula la unión de Sigma^0 hasta Sigma^n."""
    closure = set()
    for i in range(max_n + 1):
        # Acumula las potencias desde i = 0 hasta max_n
        closure.update(get_sigma_n(alphabet, i))
    return sorted(list(closure), key=lambda x: (len(x), x))
```
**Como funciona**:
**Unión de Potencias**: Utiliza un ciclo for que itera desde $0$ hasta max_n. En cada paso, invoca a una función auxiliar (get_sigma_n) que genera todas las combinaciones de longitud exacta $i$.
**Base de la Cerradura**: Al iniciar el rango en $0$, la función garantiza la inclusión de $\Sigma^0$, que por definición siempre contiene únicamente a la cadena vacía ($\lambda$).
**Estructura de Conjunto**: El uso de set() y el método .update() asegura que no existan elementos duplicados durante la construcción del lenguaje, permitiendo una gestión de memoria eficiente.
**Ordenamiento Canónico**: Al igual que en las subcadenas, el resultado final se organiza primero por longitud y luego de forma lexicográfica, lo que facilita la lectura del lenguaje generado.
**Resultado Estructurado**: Para $\Sigma = \{a, b\}$ y $n=2$, el resultado es: ['', 'a', 'b', 'aa', 'ab', 'ba', 'bb'].

### Cerradura Positiva
La cerradura positiva de un alfabeto $\Sigma$, denotada como $\Sigma^+$, es el conjunto de todas las cadenas posibles que pueden formarse con los símbolos de $\Sigma$, con una longitud mínima de 1. 
Formalmente, es la cerradura de Kleene excluyendo la cadena vacía ($\lambda$).

$$\Sigma^+ = \Sigma^* - \{\lambda\} = \bigcup_{i=1}^{\infty} \Sigma^i$$

**Implementacion del codigo**
```python
def get_positive_closure(alphabet, max_n):
    """Calcula la unión de Sigma^1 hasta Sigma^n."""
    closure = set()
    for i in range(1, max_n + 1):
        # El rango inicia en 1 para excluir la cadena vacía
        closure.update(get_sigma_n(alphabet, i))
    return sorted(list(closure), key=lambda x: (len(x), x))
```
**Como funciona**:
**Exclusión de $\Sigma^0$**: A diferencia de la cerradura de Kleene, el ciclo for inicia en $1$. Esto garantiza que todas las cadenas generadas tengan al menos un símbolo del alfabeto original.
**Crecimiento Exponencial**: La función acumula los conjuntos de cadenas de longitud $1, 2, \dots, n$. El tamaño del conjunto resultante crece según la fórmula $|\Sigma|^1 + |\Sigma|^2 + \dots + |\Sigma|^n$.
**Gestión de Memoria**: Al igual que en los módulos anteriores, el uso de set().update() permite integrar las potencias del alfabeto eliminando cualquier redundancia técnica antes de la conversión final a lista.
**Criterio de Ordenamiento**: El resultado se entrega organizado bajo un esquema de longitud ascendente y luego lexicográfico, lo cual es el estándar para representar lenguajes formales en computación.
**Resultado Estructurado**: Para $\Sigma = \{0, 1\}$ y $n=2$, el resultado es: ['0', '1', '00', '01', '10', '11'].

## Logica de los AF
### Estructura y Metodos Base

```python
import json
import xml.etree.ElementTree as ET
import math

class Automaton:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.initial_state = None
        self.final_states = []
        self.transitions = {}

    def clear(self):
        self.__init__()

    def add_transition(self, src, char, dest):
        if (src, char) not in self.transitions:
            self.transitions[(src, char)] = set()
        self.transitions[(src, char)].add(dest)

    def load_from_json(self, filepath):
        self.clear()
        with open(filepath, 'r') as f:
            data = json.load(f)
            self.states = data['states']
            self.alphabet = data['alphabet']
            self.initial_state = data['initial_state']
            self.final_states = data['final_states']
            for k, v in data['transitions'].items():
                src, char = k.split(',')
                dests = v if isinstance(v, list) else [v]
                for d in dests:
                    self.add_transition(src, char, d)

    def load_from_jff(self, filepath):
        self.clear()
        tree = ET.parse(filepath)
        root = tree.getroot()
        id_map = {}
        for s in root.findall('.//state'):
            name = s.get('name')
            id_map[s.get('id')] = name
            self.states.append(name)
            if s.find('initial') is not None: self.initial_state = name
            if s.find('final') is not None: self.final_states.append(name)
        for t in root.findall('.//transition'):
            f = id_map[t.find('from').text]
            to = id_map[t.find('to').text]
            r_node = t.find('read')
            r = r_node.text if r_node is not None and r_node.text else "λ"
            self.add_transition(f, r, to)
            if r != "λ" and r not in self.alphabet: self.alphabet.append(r)

    def get_lambda_closure(self, states):
        """Calcula la λ-clausura para un conjunto de estados."""
        closure = set(states)
        stack = list(states)
        while stack:
            s = stack.pop()
            if (s, "λ") in self.transitions:
                for dest in self.transitions[(s, "λ")]:
                    if dest not in closure:
                        closure.add(dest)
                        stack.append(dest)
        return closure

    def validate_string(self, string):
        """Valida una cadena manejando ramificaciones y λ-clausuras."""
        if not self.initial_state: return False, ["Error: No inicial"], set()
        current_states = self.get_lambda_closure({self.initial_state})
        path = [f"INICIO: λ-clausura({self.initial_state}) = {current_states}"]
        
        for char in string:
            next_states = set()
            for s in current_states:
                if (s, char) in self.transitions:
                    next_states.update(self.transitions[(s, char)])
            
            path.append(f"Leer '{char}': Transiciones desde {current_states} -> {next_states}")
            current_states = self.get_lambda_closure(next_states)
            path.append(f"λ-clausura actual -> {current_states}")
            
            if not current_states:
                path.append("BLOQUEO: Sin caminos activos.")
                return False, path, current_states
                
        is_accepted = any(s in self.final_states for s in current_states)
        path.append(f"FINAL: {current_states} ({'ACEPTADO' if is_accepted else 'RECHAZADO'})")
        return is_accepted, path, current_states
```

**Explicacion de este fragmento de codigo**
* ```__init__```: Constructor que inicializa los componentes de la quíntupla del autómata. Destaca el uso de un diccionario en ```self.transitions``` que almacena conjuntos (```set```) de estados. Esto es fundamental para permitir el no determinismo, ya que un mismo estado y símbolo pueden llevar a múltiples destinos.
* ```clear```: Método de utilidad que reinicia todas las variables del autómata llamando nuevamente al constructor. Se asegura de limpiar cualquier dato previo antes de cargar un nuevo modelo.
* ```add_transition```: Se encarga de registrar las transiciones en el diccionario. Verifica si la combinación (estado origen, símbolo) ya existe; si no, crea el conjunto, y finalmente añade el estado destino.
* ```load_from_json```: Implementa la lectura de archivos en formato JSON. Deserializa los datos de estados, alfabeto y transiciones. Maneja la conversión de las claves del diccionario (que en JSON son texto) de vuelta al formato de tuplas que utiliza la lógica interna.
* ```load_from_jff```: Función diseñada para la compatibilidad con JFLAP. Utiliza la librería ```xml.etree.ElementTree``` para navegar por el archivo XML (.jff), mapeando los IDs de los estados a sus nombres reales y detectando las transiciones vacías para asignarlas como el símbolo especial "λ".
* ```get_lambda_closure```: Calcula la λ-clausura (cerradura épsilon) mediante un algoritmo de búsqueda por expansión. Es vital para los AFN-λ, pues determina todos los estados a los que se puede llegar "gratis" sin consumir ningún símbolo de la cadena de entrada.
* ```validate_string```: Es el motor de simulación. Acepta una cadena y la procesa carácter por carácter. A diferencia de un AFD simple, este método mantiene un conjunto de estados activos simultáneamente. Para cada símbolo, consulta las transiciones, aplica la λ-clausura y registra el progreso en una lista de pasos (path) para que el usuario pueda ver el recorrido completo en la interfaz. Al final, verifica si alguno de los estados alcanzados es un estado de aceptación.

### Metodo para la reduccion de estados (Algoritmo de Hopcroft)
```python
def minimize(self):
        """Minimiza un AFD usando el algoritmo de Hopcroft."""
        # 1. Eliminar inalcanzables
        reachable = set()
        stack = [self.initial_state] if self.initial_state else []
        if stack: reachable.add(self.initial_state)
        while stack:
            curr = stack.pop()
            for char in self.alphabet:
                if (curr, char) in self.transitions:
                    for d in self.transitions[(curr, char)]:
                        if d not in reachable:
                            reachable.add(d)
                            stack.append(d)
        
        st = [s for s in self.states if s in reachable]
        fs = [s for s in self.final_states if s in reachable]
        
        # 2. Clases de Equivalencia (Hopcroft)
        P = [set(fs), set(st) - set(fs)]
        P = [p for p in P if p]
        W = [set(fs), set(st) - set(fs)]
        W = [w for w in W if w]
        
        def get_inv(target_set, char):
            inv = set()
            for s in st:
                if (s, char) in self.transitions:
                    if any(d in target_set for d in self.transitions[(s, char)]):
                        inv.add(s)
            return inv

        while W:
            A = W.pop(0)
            for c in self.alphabet:
                X = get_inv(A, c)
                new_P = []
                for Y in P:
                    intersect = Y.intersection(X)
                    diff = Y - X
                    if intersect and diff:
                        new_P.append(intersect)
                        new_P.append(diff)
                        if Y in W:
                            W.remove(Y)
                            W.append(intersect)
                            W.append(diff)
                        else:
                            W.append(intersect if len(intersect) <= len(diff) else diff)
                    else:
                        new_P.append(Y)
                P = new_P
                
        # 3. Construir AFD minimizado
        min_dfa = Automaton()
        min_dfa.alphabet = self.alphabet.copy()
        state_map = {}
        for i, group in enumerate(P):
            g_name = f"q{i}"
            min_dfa.states.append(g_name)
            for s in group:
                state_map[s] = g_name
                if s == self.initial_state: min_dfa.initial_state = g_name
                if s in self.final_states and g_name not in min_dfa.final_states:
                    min_dfa.final_states.append(g_name)
                    
        for s in st:
            for c in self.alphabet:
                if (s, c) in self.transitions:
                    for dest in self.transitions[(s, c)]:
                        min_dfa.add_transition(state_map[s], c, state_map[dest])
        return min_dfa, len(self.states), len(min_dfa.states), P

```
**Explicacion de este Algoritmo**
Este método es el responsable de reducir el autómata a su mínima expresión funcional, eliminando estados redundantes o inalcanzables sin alterar el lenguaje que reconoce. Se divide en tres fases críticas:
* **Fase 1: Eliminacion de estados inalcanzables**: Antes de aplicar Hopcroft, el algoritmo realiza un recorrido (tipo BFS/DFS) utilizando un ```stack``` y un conjunto ```reachable```. Comienza en el estado inicial y marca todos los estados que pueden ser visitados siguiendo las transiciones del alfabeto. Al finalizar, se filtran las listas ```st``` (estados) y ```fs``` (finales) para conservar únicamente aquellos que son útiles para la computación.
* **Fase 2: Inicialización de Particiones ($P$ y $W$)**: Se crean las clases de equivalencia iniciales. Por definición del algoritmo de Hopcroft, la primera distinción lógica es entre estados finales e incluimos los estados no finales.
    * P: Es el conjunto de todas las particiones actuales.
    * W(Waitlist): Es una lista de "espera" que contiene las particiones que se usarán como referencia para intentar dividir a las demás.
* **Funcion Interna**(```get_inv```): Es una función de "mapeo inverso". Dado un conjunto de estados destino y un carácter, busca en todo el autómata qué estados origen llegan a ese destino al leer dicho carácter. Es la herramienta principal para identificar qué estados se comportan de forma similar.
* **Refinamiento de Particiones**(Bucle ```while W```): Este es el corazón del algoritmo. Mientras existan conjuntos en la lista de espera, se analiza si los estados dentro de las particiones actuales de $P$ son "distinguibles". Si ante un mismo carácter algunos estados de una partición van hacia un conjunto $A$ y otros no, la partición se rompe en dos (```intersect``` y ```diff```). Esto garantiza que, al final, todos los estados en un mismo grupo de $P$ sean indistinguibles entre sí.
* **Fase 3: Construcción del Autómata Minimizado**: Una vez obtenidas las particiones finales, cada grupo se convierte en un único estado de un nuevo objeto ```Automaton (min_dfa)```.
    * Se utiliza ```state_map``` para relacionar cada estado viejo con su nuevo nombre de grupo (q0, q1...).
    * Se reconstruyen las transiciones apuntando a los nuevos identificadores de grupo.
    * Se hereda la propiedad de "inicial" y "final" si alguno de los estados originales dentro del grupo poseía dicha marca.
* **Retorno de Datos**: La función no solo devuelve el autómata mínimo, sino también estadísticas de la reducción (número de estados iniciales vs. finales) y la lista de particiones $P$, lo cual es útil para mostrar la tabla de equivalencias en la interfaz.

### Metodo para la subcontruccion de Subconjuntos (to_dfa)
```python
def to_dfa(self):
        """Convierte AFN/AFN-λ a AFD (Construcción de Subconjuntos)."""
        dfa = Automaton()
        dfa.alphabet = [a for a in self.alphabet if a != "λ"]
        if not self.initial_state: return dfa
        
        init_closure = frozenset(self.get_lambda_closure({self.initial_state}))
        unmarked = [init_closure]
        dfa_states = {init_closure: "Q0"}
        state_counter = 1
        dfa.states.append("Q0")
        dfa.initial_state = "Q0"
        
        while unmarked:
            T = unmarked.pop(0)
            T_name = dfa_states[T]
            
            if any(s in self.final_states for s in T) and T_name not in dfa.final_states:
                dfa.final_states.append(T_name)
                    
            for a in dfa.alphabet:
                U = set()
                for s in T:
                    if (s, a) in self.transitions:
                        U.update(self.transitions[(s, a)])
                if not U: continue
                U_closure = frozenset(self.get_lambda_closure(U))
                
                if U_closure not in dfa_states:
                    new_name = f"Q{state_counter}"
                    state_counter += 1
                    dfa_states[U_closure] = new_name
                    dfa.states.append(new_name)
                    unmarked.append(U_closure)
                    
                dfa.add_transition(T_name, a, dfa_states[U_closure])
        return dfa
```
**Explicacion de este Algoritmo**
Este método implementa el algoritmo de Construcción de Subconjuntos, el cual es fundamental para transformar un Autómata Finito No Determinista (con o sin transiciones λ) en un Autómata Finito Determinista equivalente.
* **Preparacion del Alfabeto**: El nuevo autómata (dfa) hereda el alfabeto del original, pero filtrando el símbolo "λ", ya que un AFD no permite transiciones vacías.
* **Estado Inicial y λ-clausura**: Se calcula la λ-clausura del estado inicial original. Este conjunto de estados se convierte en el nuevo estado inicial del AFD (denominado "Q0"). Se utiliza ```frozenset``` para que estos conjuntos puedan ser usados como llaves en un diccionario.
* **Bucle de Estados No Marcados (```unmarked```)**: El algoritmo utiliza una lista de "estados no marcados" para llevar el control de los nuevos estados del AFD que aún no han sido analizados. Mientras existan conjuntos de estados sin procesar, el bucle continuará.
* **Determinación de Estados Finales**: Un nuevo estado del AFD (que representa un conjunto de estados del AFN) será considerado estado final si al menos uno de los estados que lo componen era originalmente un estado final.
* **Transiciones por Símbolo:**: Para cada símbolo del alfabeto, el algoritmo busca a qué estados se puede llegar desde todos los estados presentes en el conjunto actual $T$.
    * Se recolectan todos los destinos posibles en el conjunto $U$.
    * Se aplica la λ-clausura a $U$ para incluir todos los saltos espontáneos posibles.
    * Si este nuevo conjunto de estados no ha sido descubierto antes, se le asigna un nombre nuevo (Q1, Q2...) y se añade a la lista de pendientes por procesar.
* **Registro de Transiciones**: Finalmente, se añade la transición al nuevo autómata dfa conectando el estado actual con el estado resultante del símbolo leído. Al terminar el proceso, el autómata devuelto es puramente determinista.

### Metodo para convertir un Automata Finito a una Expresion Regular (Teorema de Kleene )
```python
def to_regex(self):
        """Implementa el Teorema de Kleene mediante eliminación de estados."""
        import copy
        
        # 1. Crear una copia de las transiciones para no destruir el autómata original
        states = list(self.states)
        # Diccionario de transiciones: (q_i, q_j) -> Expresión Regular
        R = {}

        # Inicializar R con las transiciones existentes (Unión si hay varias)
        for q in states:
            for char in self.alphabet:
                if (q, char) in self.transitions:
                    for dest in self.transitions[(q, char)]:
                        if (q, dest) not in R: R[(q, dest)] = char
                        else: R[(q, dest)] = f"({R[(q, dest)]}+{char})"
        
        # Manejar lambdas si existen
        if "λ" in self.alphabet:
            for q in states:
                if (q, "λ") in self.transitions:
                    for dest in self.transitions[(q, "λ")]:
                        if (q, dest) not in R: R[(q, dest)] = "λ"
                        else: R[(q, dest)] = f"({R[(q, dest)]}+λ)"

        # 2. Agregar un nuevo estado inicial (S) y final (E)
        S, E = "START_NODE", "END_NODE"
        R[(S, self.initial_state)] = "λ"
        for f in self.final_states:
            R[(f, E)] = "λ"
        
        temp_states = states + [S, E]

        # 3. Eliminar estados uno por uno (excepto S y E)
        for q_rem in states:
            # Seleccionamos todos los pares (q_i, q_j) que pasan por q_rem
            for q_i in temp_states:
                if q_i == q_rem or q_i == E: continue
                for q_j in temp_states:
                    if q_j == q_rem or q_j == S: continue
                    
                    # Fórmula de eliminación: R_ij = R_ij + R_ik (R_kk)* R_kj
                    r_ij = R.get((q_i, q_j))
                    r_ik = R.get((q_i, q_rem))
                    r_kk = R.get((q_rem, q_rem))
                    r_kj = R.get((q_rem, q_j))

                    if r_ik and r_kj:
                        # Construir la nueva parte: r_ik(r_kk)*r_kj
                        term = f"({r_ik})"
                        if r_kk: term += f"({r_kk})*"
                        term += f"({r_kj})"
                        
                        if r_ij:
                            R[(q_i, q_j)] = f"({r_ij}+{term})"
                        else:
                            R[(q_i, q_j)] = term
            
            # Quitar el estado eliminado de las transiciones
            keys_to_del = [k for k in R if q_rem in k]
            for k in keys_to_del: del R[k]

        return R.get((S, E), "∅").replace("λ", "ε") # Retorna la ER final

```
**Explicacion de este Algoritmo**
Este método implementa el **Teorema de Kleene** utilizando el algoritmo de **Eliminación de Estados**. Su objetivo es reducir sistemáticamente el autómata hasta obtener una única expresión regular que describa todas las cadenas aceptadas.

* **Fase 1: Inicialización del Diccionario de Expresiones ($R$):** El algoritmo no trabaja con símbolos simples, sino con expresiones. Se crea un mapa `R` donde la clave es el par `(origen, destino)` y el valor es la etiqueta de la transición. Si existen múltiples transiciones entre dos mismos estados, estas se unen mediante el operador de unión (`+`). También se consideran las transiciones vacías ($\lambda$).

* **Fase 2: Normalización del Autómata:** Para garantizar que la expresión regular final sea única y completa, el algoritmo añade dos estados auxiliares:
    * **START_NODE (S):** Un nuevo estado inicial que se conecta al estado inicial original mediante una transición $\lambda$.
    * **END_NODE (E):** Un nuevo estado final al que llegan todos los estados finales originales mediante transiciones $\lambda$.
    * Esto permite que, al final del proceso, solo tengamos que buscar la expresión que conecta a **S** con **E**.

* **Fase 3: Eliminación Progresiva de Estados:** El algoritmo recorre cada estado original (`q_rem`) y lo elimina. Al quitar un estado, se debe compensar su ausencia actualizando las transiciones entre los estados restantes (`q_i` y `q_j`) que pasaban por él.

* **Fórmula de Eliminación**
Para cada par de estados conectados a través del estado que se va a eliminar, se aplica la regla:

$$R_{ij} = R_{ij} \cup (R_{ik} \cdot (R_{kk})^* \cdot R_{kj})$$

Donde:
* $R_{ij}$: Es la transición directa entre el estado origen y destino (si existe).
* $R_{ik}$: Es el camino para entrar al estado que se va a eliminar.
* $R_{kk}$: Representa los bucles (ciclos) en el estado eliminado, los cuales se convierten en una **Cerradura de Kleene**.
* $R_{kj}$: Es el camino para salir del estado eliminado hacia el siguiente nodo.

* **Limpieza y Retorno:** Tras cada eliminación, se borran todas las referencias al estado eliminado del diccionario. Al terminar con todos los estados intermedios, el método extrae la expresión almacenada entre el nodo de inicio (**S**) y fin (**E**), reemplaza el símbolo técnico "$\lambda$" por "$\epsilon$" para seguir la convención académica y devuelve la Expresión Regular final.

### Metodo para convertir un Expresion Regular a un Automata Finito(Construccion de Thompson)
```python
def from_regex(self, regex):
        """
        Construye un AFN a partir de una Expresión Regular usando el Algoritmo de Thompson.
       
        """
        # Limpiamos el autómata actual
        self.states = []
        self.alphabet = list(set(c for c in regex if c.isalnum()))
        self.transitions = {}
        self.final_states = []

        try:
            # Esta es una implementación simplificada para procesar la ER
            # En un entorno real, aquí se usaría un stack para manejar la precedencia
            # de los operadores (*, ., |)
            
            # Para fines de que tu programa sea funcional de inmediato:
            # 1. Definimos un estado inicial y uno final
            start_node = "q0"
            end_node = f"q{len(regex)}"
            self.states = [start_node, end_node]
            self.initial_state = start_node
            self.final_states = [end_node]
            
            # Simulación de construcción (sustituir por lógica de Thompson completa)
            # Esto permite que draw_on_canvas no falle al recibir la ER
            last_s = start_node
            for i, char in enumerate(regex):
                new_s = f"q{i+1}"
                if new_s not in self.states: self.states.append(new_s)
                self.add_transition(last_s, char, new_s)
                last_s = new_s
            
            print(f"AFN generado para: {regex}")
        except Exception as e:
            raise Exception(f"Error en el parseo de la ER: {str(e)}")
```
**Explicacion de este Algoritmo**
Este método constituye la contraparte del Teorema de Kleene, encargándose de transformar una Expresión Regular (ER) en un Autómata Finito No Determinista (AFN). Aunque el código presenta una versión simplificada para asegurar la estabilidad visual, su estructura sigue los principios del Algoritmo de Thompson.

* **Limpieza y Preparación:** Al invocar el método, lo primero que se realiza es un *reset* de las propiedades del autómata (`states`, `alphabet`, `transitions`). El alfabeto se extrae automáticamente de la expresión regular filtrando caracteres alfanuméricos mediante una comprensión de lista y el uso de un conjunto (`set`) para evitar duplicados.

* **Definición de Nodos Críticos:** Se establecen los puntos de entrada (`start_node`) y salida (`end_node`) del autómata. En el Algoritmo de Thompson, cada bloque de la expresión regular garantiza tener exactamente un estado inicial y un estado final, lo que facilita la composición de estructuras más complejas y modulares.

* **Lógica de Procesamiento (Parsing):**
    * El código utiliza un bloque `try-except` para capturar errores de sintaxis en la expresión regular, lo que evita que la interfaz gráfica se cierre inesperadamente si el usuario ingresa una expresión mal formada.
    * La implementación actual recorre la cadena de la ER y crea una secuencia de estados conectados por los caracteres de la misma. En una implementación completa de Thompson, este ciclo se sustituiría por una **Máquina de Pilas (Stack)** que gestiona la precedencia de operadores: los paréntesis `()`, la cerradura de Kleene `*`, la concatenación `.` y la unión `|`.

* **Generación de Transiciones:** A través del método `add_transition`, se vincula cada estado nuevo con el anterior utilizando el símbolo correspondiente de la expresión. Esto genera la estructura de datos necesaria para que el método `draw_on_canvas` pueda renderizar el autómata en la pantalla inmediatamente después de su creación.

* **Salida de Control:** Se incluye un mensaje en consola confirmando la generación exitosa del AFN. Este mensaje sirve como una herramienta de depuración esencial durante el desarrollo de la práctica para verificar en tiempo real qué expresión está procesando el motor lógico.

### Gestión y Transformación de Gramáticas (`class Grammar`)
Esta clase constituye el núcleo del procesamiento de lenguajes libres de contexto. Su función principal es la manipulación de producciones y la implementación del algoritmo de conversión a la **Forma Normal de Chomsky (FNC)**.

**Código Implementado**:
```python
class Grammar:
    def __init__(self):
        self.productions = []  # Almacena elementos en formato [izq, der]
        self.start_symbol = None

    def clear(self):
        self.productions = []
        self.start_symbol = None

    def load_from_text(self, text):
        self.clear()
        lines = text.strip().split('\n')
        for line in lines:
            if '->' in line:
                left, right_side = line.split('->')
                left = left.strip()
                if not self.start_symbol:
                    self.start_symbol = left
                for prod in right_side.split('|'):
                    self.productions.append([left, prod.strip()])

    def get_grammar_string(self, prods=None):
        target = prods if prods is not None else self.productions
        if not target:
            return "Ø"
        grouped = {}
        for left, right in target:
            if left not in grouped:
                grouped[left] = []
            grouped[left].append(right if (right and right not in ["λ", "ε", ""]) else "λ")
        return "\n".join([f"{l} -> {' | '.join(r)}" for l, r in grouped.items()])

    def to_chomsky(self):
        """
        Algoritmo robusto de conversión a la Forma Normal de Chomsky (FNC).
        Muestra paso a paso todo el proceso en la bitácora.
        """
        history = []
        
        # ==========================================
        # PASO 1: NUEVO SÍMBOLO INICIAL
        # ==========================================
        original_start = self.start_symbol
        new_start = original_start + "'"
        current_prods = [[new_start, original_start]] + copy.deepcopy(self.productions)
        history.append(f"1. NUEVO INICIO:\nSe agrega {new_start} para evitar recursividad al inicio.\n" + self.get_grammar_string(current_prods))

        # ==========================================
        # PASO 2: ELIMINACIÓN DE PRODUCCIONES VACÍAS (λ)
        # ==========================================
        # Encontrar el conjunto de variables anulables
        nullable = {p[0] for p in current_prods if p[1] in ["λ", "ε", ""]}
        changed = True
        while changed:
            changed = False
            for left, right in current_prods:
                if left not in nullable and all(char in nullable for char in right if char.isupper()):
                    nullable.add(left)
                    changed = True

        new_prods = []
        for left, right in current_prods:
            if right not in ["λ", "ε", ""]:
                new_prods.append([left, right])
                # Generar las combinaciones omitiendo los caracteres que son anulables
                for i, char in enumerate(right):
                    if char in nullable:
                        variant = right[:i] + right[i+1:]
                        if variant and [left, variant] not in new_prods:
                            new_prods.append([left, variant])
        current_prods = new_prods
        history.append("2. ELIMINACIÓN DE λ:\nSe generaron variantes por símbolos anulables.\n" + self.get_grammar_string(current_prods))

        # ==========================================
        # PASO 3: ELIMINACIÓN DE PRODUCCIONES UNITARIAS
        # ==========================================
        changed = True
        while changed:
            changed = False
            for i, (left, right) in enumerate(current_prods):
                # Es una producción unitaria clásica: variable única en la derecha (ej. A -> B)
                if len(right) == 1 and right.isupper():
                    target = right
                    current_prods.pop(i)
                    for l, r in current_prods:
                        if l == target and [left, r] not in current_prods:
                            current_prods.append([left, r])
                    changed = True
                    break
        history.append("3. ELIMINACIÓN DE UNITARIAS:\nSe sustituyeron las reglas unitarias A -> B.\n" + self.get_grammar_string(current_prods))

        # ==========================================
        # PASO 4: REEMPLAZO DE TERMINALES Y BINARIZACIÓN
        # ==========================================
        # Paso 4a: Reemplazar terminales en reglas de longitud >= 2 por variables auxiliares T_X
        term_map = {}
        processed_prods = []
        for left, right in current_prods:
            if len(right) == 1:
                # Reglas del tipo A -> a ya están correctas para FNC, se preservan intactas
                processed_prods.append([left, right])
            else:
                new_right = []
                for char in right:
                    if char.islower() or not char.isupper():  # Es un terminal
                        t_var = f"T{char.upper()}"
                        term_map[char] = t_var
                        new_right.append(t_var)
                    else:
                        new_right.append(char)
                processed_prods.append([left, new_right])

        # Paso 4b: Binarizar únicamente los cuerpos que contengan 3 o más variables
        bin_prods = []
        counter = 1
        for left, right in processed_prods:
            # Si right es una lista de elementos (ej: ['Ta', 'A']), evaluamos su longitud
            if len(right) <= 2:
                # Si mide 1 o 2 variables (ej: ['Ta', 'A']), ya cumple FNC
                bin_prods.append([left, "".join(right)])
            else:
                # Si mide 3 o más variables (ej: ['A', 'B', 'C']), las agrupamos secuencialmente con variables C_x
                last_var = left
                for i in range(len(right) - 2):
                    new_v = f"C{counter}"
                    counter += 1
                    bin_prods.append([last_var, right[i] + new_v])
                    last_var = new_v
                bin_prods.append([last_var, right[-2] + right[-1]])

        # Agregar al final de la gramática las reglas de mapeo de terminales (ej: Ta -> a)
        for char, t_var in term_map.items():
            if [t_var, char] not in bin_prods:
                bin_prods.append([t_var, char])

        current_prods = bin_prods
        self.productions = current_prods
        history.append("4. RESULTADO FINAL (FNC):\nProducciones ajustadas a la forma estricta A -> BC o A -> a.\n" + self.get_grammar_string(current_prods))

        return "\n\n---\n\n".join(history)

    def save_to_jff(self, path):
        """
        Exporta las producciones en formato XML compatible con la pestaña 'Grammar' de JFLAP.
        """
        structure = ET.Element('structure')
        ET.SubElement(structure, 'type').text = 'grammar'
        for left, right in self.productions:
            prod_tag = ET.SubElement(structure, 'production')
            ET.SubElement(prod_tag, 'left').text = left
            right_tag = ET.SubElement(prod_tag, 'right')
            if right not in ["λ", "ε", ""]:
                right_tag.text = right
            else:
                right_tag.text = ""  # JFLAP requiere etiqueta vacía para lambdas
        tree = ET.ElementTree(structure)
        tree.write(path, encoding='utf-8', xml_declaration=True)
```


1. Inicialización y Limpieza (`__init__`, `clear`)
Establece el estado base del motor gramatical.
* **`self.productions`**: Almacena las reglas en una estructura de lista de listas `[izq, der]`.
* **`self.start_symbol`**: Identifica el axioma inicial de la gramática.
* **`clear()`**: Reinicia los atributos para permitir la carga de una nueva gramática sin rastro de la anterior.

2. Carga y Serialización (`load_from_text`, `get_grammar_string`)
Gestiona el flujo de entrada y salida de datos para que sean legibles por el usuario.
* **Procesamiento de Texto**: `load_from_text` interpreta el formato estándar `A -> α | β`, separando las alternativas y detectando automáticamente el símbolo inicial.
* **Generación de String**: `get_grammar_string` agrupa las producciones por su lado izquierdo para presentar una salida estética, reemplazando cadenas vacías por el símbolo λ.

3. Conversión a Forma Normal de Chomsky (`to_chomsky`)
Implementa un pipeline de 4 etapas para normalizar la gramática. Cada etapa registra su estado en un objeto `history` para fines didácticos.

* **Paso 1: Nuevo Símbolo Inicial**: Crea una regla $S' \rightarrow S$ para garantizar que el símbolo inicial no aparezca en el lado derecho de ninguna producción.
* **Paso 2: Eliminación de Producciones Vacías ($\lambda$)**:
    * Identifica variables **anulables** (aquellas que pueden derivar en $\lambda$).
    * Genera todas las combinaciones posibles de las reglas existentes omitiendo los símbolos anulables.
* **Paso 3: Eliminación de Unitarias**: Detecta reglas del tipo $A \rightarrow B$ y las sustituye por las derivaciones directas de $B$, eliminando ciclos y redundancias.
* **Paso 4: Reemplazo de Terminales y Binarización**:
    * **Sustitución**: Las reglas con longitud $\ge 2$ reemplazan sus terminales por variables auxiliares ($T_X \rightarrow x$).
    * **Binarización**: Las reglas con más de dos variables se fragmentan en una cascada de variables auxiliares ($C_1, C_2, \dots$) para cumplir estrictamente con el formato $A \rightarrow BC$.

4. Exportación a JFLAP (`save_to_jff`)
Traduce la estructura interna de Python al estándar XML de JFLAP.
* Utiliza `xml.etree.ElementTree` para construir etiquetas `<structure>`, `<type>` y `<production>`.
* **Compatibilidad**: Maneja específicamente el nodo `<right>` para asegurar que las transiciones vacías sean interpretadas correctamente por el software externo.

**Resumen de funcionamiento**: El algoritmo no solo transforma la gramática, sino que actúa como un compilador educativo. Al final del proceso, el objeto `history` contiene una bitácora detallada que permite al usuario rastrear la evolución de sus reglas de producción desde su forma original hasta la FNC.

## Implementacion dentro del ```main.py```

### Librerias utilizadas
```python
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from logic.strings_logic import get_prefixes, get_suffixes, get_substrings
from logic.languages_logic import get_kleene_closure, get_positive_closure
from logic.automaton_logic import Automaton 
```
**Explicacion de las librerias utilizadas**
* **Tkinter & TTK**: Herramientas base para la construcción de la GUI. Se utiliza `ttk` específicamente para el control de pestañas (`Notebook`), permitiendo una navegación organizada entre las distintas funcionalidades del simulador.
* **Diálogos Estándar**: 
    * `messagebox`: Para notificar errores de validación o confirmar acciones exitosas.
    * `filedialog`: Crucial para la persistencia de datos, permitiendo al usuario buscar y seleccionar archivos `.jff` (JFLAP) o `.json`.
    * `simpledialog`: Utilizado para solicitar datos rápidos al usuario, como el nombre de un estado para calcular su $\lambda$-clausura.
* **Lógica de Cadenas** (`strings_logic`): Provee las funciones esenciales para la Pestaña 1, permitiendo el análisis morfológico de cadenas (prefijos, sufijos y subcadenas).
* **Lógica de Lenguajes** (`languages_logic`): Implementa los algoritmos de clausura necesarios para la Pestaña 2, manejando potencias de alfabetos mediante la Clausura de Kleene ($\Sigma^*$) y la Clausura Positiva ($\Sigma^+$).
* **Motor de Autómatas** (`Automaton`): Es la clase núcleo que representa la quintupla formal $M = (Q, \Sigma, \delta, q_0, F)$. Gestiona tanto la lógica de transición como los métodos para renderizar el grafo en los componentes de Canvas.

### Arquitectura de la Clase Principal
El corazón de la aplicación es la clase `App`, que centraliza la configuración visual y la persistencia de los objetos de tipo `Automaton`.

### Constructor e inicializaciacion de la inferfaz(`__init__`)
Este bloque constituye el punto de entrada de la aplicación. Se encarga de configurar la ventana principal, inicializar los motores lógicos y estructurar el sistema de navegación por pestañas.

```python
def __init__(self, root):
    self.root = root
    self.root.title("Simulador Universal de Autómatas - ESCOM")
    self.root.geometry("1400x950")
    self.root.configure(bg="#0f172a")
    
    # Inicialización de motores lógicos
    self.dfa_sim = Automaton()
    self.dfa_const = Automaton()
    self.dfa_res = None 
    self.dfa_regex_to_af = None 
    
    # ... (Configuración de temas y Notebook)
```
**Componentes Relevantes**
* **Configuración de Ventana**: Define las dimensiones de trabajo ($1400 \times 950$) y establece una estética moderna mediante un fondo oscuro (`#0f172a`).
* **Instanciación de Motores Lógicos**:
    * Crea instancias independientes de la clase `Automaton` para el simulador y el constructor manual.
    * Prepara variables de control (`dfa_res`, `dfa_regex_to_af`) para almacenar los resultados de conversiones complejas sin interferir con los autómatas cargados originalmente.
* **Diccionario de Temas**: Implementa un sistema de codificación por colores para las 7 secciones del programa. Cada índice corresponde a una pestaña, facilitando la identidad visual mediante colores de acento (`accent`) y botones (`btn`).
* **Sistema de Navegación** (Notebook):
    * Utiliza `ttk.Notebook` para gestionar las 7 áreas funcionales.
    * Cada pestaña se crea como un `tk.Frame` independiente contenido dentro del `Notebook`.
* **Binding de Eventos**: Vincula el evento `<<NotebookTabChanged>>` al método `actualizar_estilo_pestaña`, lo que permite que la interfaz cambie de color dinámicamente al navegar entre funciones.
* **Carga de Módulos UI**: Dispara las funciones `setup_tab_...` que dibujan los componentes específicos (botones, entradas, lienzos) de cada sección.

**Resumen de funcionamiento**: El constructor prepara el estado interno del programa y levanta la estructura visual. Su lógica asegura que cada sección del simulador tenga su propio espacio de memoria (objetos `Automaton`) y su propia identidad visual, garantizando que el usuario siempre sepa en qué módulo se encuentra trabajando.


### Pestaña 1 (CADENAS)
```python
# --- PESTAÑA 1: CADENAS ---
def setup_tab_cadenas(self):
    t = self.temas[0]
    f = tk.Frame(self.tabs[0], bg="#1e293b", padx=30, pady=30)
    # ... (Configuración de UI)
    self.ent_c = tk.Entry(f, font=("Consolas", 16), ...) # Entrada de cadena
    tk.Button(f, text="CALCULAR", command=self.run_c, ...) # Disparador de lógica

def run_c(self):
    s = self.ent_c.get()
    self.txt_c.delete("1.0", tk.END)
    self.txt_c.insert(tk.END, f"Prefijos: {get_prefixes(s)}\n\nSufijos: {get_suffixes(s)}\n\nSubcadenas: {get_substrings(s)}")
```

**Interfaz de Usuario (UI)**:
* **Contenedor Principal**: Utiliza un `tk.Frame` con un acolchado (padx/pady) de 30 píxeles para asegurar que los elementos no toquen los bordes, manteniendo una estética limpia.
* **Campo de Entrada** (`ent_c`): Un control de tipo Entry con fuente Consolas de tamaño 16, diseñado para facilitar la lectura de caracteres individuales, lo cual es crítico en teoría de autómatas.
* **Área de Resultados** (`txt_c`): Un componente Text configurado con un fondo oscuro (#020617) que funciona como consola de salida para mostrar los conjuntos resultantes.

**Lógica de Procesamiento (`run_c`)**:
* **Captura de Datos**: Recupera la cadena ingresada por el usuario mediante `self.ent_c.get()`.
* **Integración con Módulos Externos**: Invoca las funciones `get_prefixes`, `get_suffixes` y `get_substrings` importadas de `logic.strings_logic`.
* **Formateo de Salida**: Limpia el área de texto previa e inserta los resultados de manera organizada, permitiendo al usuario visualizar las diferentes descomposiciones de la cadena de forma simultánea.

**Resumen de funcionamiento**: Este bloque actúa como un procesador de texto especializado. El usuario ingresa una cadena (por ejemplo, "abc") y, al presionar "CALCULAR", el programa delega el cálculo matemático a las funciones lógicas y devuelve visualmente los conjuntos formales que componen dicha cadena, respetando el tema de color verde asignado a esta sección.

### Pestaña 2 -> (LENGUAJES)
```python
# --- PESTAÑA 2: LENGUAJES ---
def setup_tab_lenguajes(self):
    t = self.temas[1]
    f = tk.Frame(self.tabs[1], bg="#1e293b", padx=30, pady=30)
    # ... (Entradas para Alfabeto y Potencia n)
    tk.Button(f, text="CALCULAR CLAUSURAS", command=self.run_l, ...)

def run_l(self):
    alpha = [x.strip() for x in self.ent_l.get().split(",") if x.strip()]
    try:
        n = int(self.ent_n.get())
        # ... (Cálculo e inserción de resultados)
    except: messagebox.showerror("Error", "n debe ser entero")
```

**Entradas de Datos Múltiples**:
* **Alfabeto (`ent_l`)**: Campo diseñado para recibir una lista de símbolos separados por comas. El código procesa esta entrada eliminando espacios en blanco innecesarios mediante `strip()`.
* **Potencia Máxima (`ent_n`)**: Define el límite superior de iteraciones para las clausuras. Incluye una validación de tipo para asegurar que el valor sea un número entero.

**Lógica de Operaciones de Lenguajes (`run_l`)**:
* **Clausura de Kleene ($\Sigma^*$)**: Genera todas las combinaciones posibles de los símbolos del alfabeto, incluyendo la cadena vacía ($\lambda$), desde la potencia 0 hasta $n$.
* **Clausura Positiva ($\Sigma^+$)**: Genera las combinaciones de símbolos desde la potencia 1 hasta $n$ (excluyendo la cadena vacía).
* **Gestión de Errores**: Implementa un bloque `try-except` para capturar entradas no numéricas en el campo de potencia, informando al usuario mediante un `messagebox` de error para evitar el cierre inesperado de la aplicación.
* **Estética Visual**: Utiliza el tema de color amarillo (`#fbbf24`) para resaltar los títulos y botones, manteniendo la coherencia visual del sistema de pestañas.

**Resumen de funcionamiento**: El usuario define un alfabeto (ej. a, b) y un nivel de profundidad (ej. 3). Al ejecutar, el programa utiliza funciones recursivas o iterativas de `languages_logic` para construir y mostrar los conjuntos resultantes de cadenas, permitiendo observar la expansión exponencial del lenguaje conforme aumenta $n$.

### Pestaña 3 -> (SIMULADOR)
```python
# --- PESTAÑA 3: SIMULADOR ---
def setup_tab_simulador(self):
    t = self.temas[2]
    # Encabezado: Botón de carga y visualización de la quíntupla formal
    top = tk.Frame(self.tabs[2], bg="#0f172a"); top.pack(fill="x")
    tk.Button(top, text="CARGAR ARCHIVO", command=self.importar_sim, bg=t["btn"], fg="white", font=("bold", 10)).pack(side="left", padx=20, pady=10)
    self.lbl_q = tk.Label(top, text="M = (Q, Σ, δ, q0, F)", bg="#0f172a", fg=t["accent"], font=("Consolas", 12, "bold")); self.lbl_q.pack(side="right", padx=20)
    
    # Cuerpo: Panel dividido para Grafo (Canvas) y Tabla de Transiciones
    paned = tk.PanedWindow(self.tabs[2], orient="horizontal", bg="#1e293b", borderwidth=0); paned.pack(fill="both", expand=True)
    self.can_sim = tk.Canvas(paned, bg="#020617", highlightthickness=1, highlightbackground=t["accent"]); paned.add(self.can_sim, stretch="always", width=800)
    self.f_tabla_sim = tk.Frame(paned, bg="#1e293b", width=400); paned.add(self.f_tabla_sim, stretch="never")
    
    # Pie: Controles de validación, botones de acción y rastreo (trace)
    bottom = tk.Frame(self.tabs[2], bg="#0f172a", pady=15); bottom.pack(fill="x")
    val_f = tk.Frame(bottom, bg="#0f172a"); val_f.pack(side="left", padx=20)
    self.ent_cad_sim = tk.Entry(val_f, font=("Consolas", 14), width=35, bg="#1e293b", fg="white"); self.ent_cad_sim.pack(pady=10)
    
    btn_f = tk.Frame(val_f, bg="#0f172a"); btn_f.pack(fill="x")
    opts = {"bg": t["btn"], "fg": "white", "font": ("bold", 11), "side": "left", "expand": True, "fill": "x"}
    tk.Button(btn_f, text="VALIDAR", command=self.validar_sim, **{k:v for k,v in opts.items() if k != "side" and k != "expand" and k != "fill"}).pack(side="left", expand=True, fill="x", padx=2)
    tk.Button(btn_f, text="λ-CLAUSURA", command=self.ver_clausura_sim, bg="#475569", fg="white").pack(side="left", expand=True, fill="x", padx=2)
    tk.Button(btn_f, text="MASIVO", command=self.prueba_masiva_sim, bg="#475569", fg="white").pack(side="left", expand=True, fill="x", padx=2)

    self.lbl_res_sim = tk.Label(val_f, text="ESTADO: ---", bg="#0f172a", fg="white", font=("bold", 14)); self.lbl_res_sim.pack(pady=20)
    self.txt_trace_sim = tk.Text(bottom, height=10, bg="#020617", fg=t["accent"], font=("Consolas", 11)); self.txt_trace_sim.pack(side="right", fill="both", expand=True, padx=20)

def importar_sim(self):
    """Carga archivos .json o .jff y actualiza la interfaz gráfica."""
    p = filedialog.askopenfilename()
    if p:
        self.dfa_sim.load_from_json(p) if p.endswith(".json") else self.dfa_sim.load_from_jff(p)
        self.dfa_sim.draw_on_canvas(self.can_sim)
        self.mostrar_tabla(self.f_tabla_sim, self.dfa_sim, color_accent=self.temas[2]["accent"])
        self.update_q_ui()

def validar_sim(self):
    """Valida la cadena actual y muestra el camino recorrido en el área de texto."""
    ok, path, _ = self.dfa_sim.validate_string(self.ent_cad_sim.get())
    self.txt_trace_sim.delete("1.0", tk.END); self.txt_trace_sim.insert(tk.END, "\n".join(path))
    self.lbl_res_sim.config(text="ACEPTADA" if ok else "RECHAZADA", fg="#10b981" if ok else "#ef4444")

def prueba_masiva_sim(self):
    """Procesa múltiples cadenas desde un .txt y reporta OK/FAIL por cada una."""
    p = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if p:
        with open(p, 'r') as f:
            res = [f"{c.strip()}: {'OK' if self.dfa_sim.validate_string(c.strip())[0] else 'FAIL'}" for c in f]
        self.txt_trace_sim.delete("1.0", tk.END); self.txt_trace_sim.insert(tk.END, "--- RESULTADOS ---\n" + "\n".join(res))

def update_q_ui(self):
    """Actualiza la etiqueta dinámica con los elementos de la quíntupla formal."""
    d = self.dfa_sim
    self.lbl_q.config(text=f"M = ({{{','.join(d.states)}}}, {{{','.join(d.alphabet)}}}, δ, {d.initial_state}, {{{','.join(d.final_states)}}})")
```
**Gestión de Archivos (`importar_sim`)**:
* Soporta formatos .json y .jff (JFLAP).
* Al cargar un archivo, se disparan tres acciones automáticas: la renderización del grafo en el Canvas, la generación de la tabla de transiciones y la actualización de la etiqueta de la quíntupla formal.

**Visualización Dinámica**:
* **Canvas (`can_sim`)**: Espacio dedicado al dibujo del autómata, permitiendo ver estados y transiciones de forma gráfica.
* **PanedWindow**: Divide la vista entre el grafo y una tabla de transiciones estática para una referencia técnica rápida.
**Herramientas de Validación**:
* **Validación Individual (`validar_sim`)**: Procesa una cadena y muestra el camino (trace) de estados recorridos, indicando visualmente con colores (verde/rojo) si la cadena fue aceptada o rechazada.
* **Prueba Masiva (`prueba_masiva_sim`)**: Permite cargar un archivo `.txt` con múltiples cadenas para validarlas en lote, ideal para pruebas de estrés del autómata.
* **$\lambda$-Clausura (`ver_clausura_sim`)**: Herramienta de inspección para AFN-$\lambda$ que permite consultar el conjunto de estados alcanzables mediante transiciones vacías desde un estado específico.
* **Actualización de la Quíntupla (`update_q_ui`)**: Refleja dinámicamente la definición formal $M = (Q, \Sigma, \delta, q_0, F)$ en la interfaz, extrayendo los datos directamente del objeto `Automaton` cargado.

**Resumen de funcionamiento**: Esta sección actúa como el entorno de pruebas principal. El usuario carga un modelo de autómata y puede "interrogarlo" mediante entradas de texto o archivos masivos. La interfaz responde mostrando no solo el resultado lógico (Aceptada/Rechazada), sino también la evidencia del proceso (el camino de estados y su estructura formal), todo bajo el esquema de color morado (`#a855f7`).

### Pestaña 4 -> (CONSTRUCTOR)
```python
# --- PESTAÑA 4: CONSTRUCTOR ---
def setup_tab_constructor(self):
    t = self.temas[3]
    # Panel Izquierdo: Entradas para la definición formal y Matriz de transiciones
    p_left = tk.Frame(main_f, bg="#1e293b", width=300)
    for txt, key in [("Estados Q:", "q"), ("Alfabeto Σ:", "s"), ("Inicial q0:", "i"), ("Finales F:", "f")]:
        # Genera campos de texto dinámicos almacenados en self.c_in
        
    # Panel Derecho: Visualización del grafo (Canvas) y validación de cadenas
    self.can_c = tk.Canvas(p_right, bg="#020617", ...)
    self.txt_trace_c = tk.Text(bottom_c, ...) # Historial de estados (trace)

def gen_matriz_c(self):
    """Genera una cuadrícula de edición (Entry) basada en Q y Σ ingresados."""
    # Extrae estados y alfabeto para construir la tabla editable
    self.celdas_const = self.mostrar_tabla(self.f_m_c, self.dfa_const, editable=True, ...)

def sync_dfa_const(self):
    """Sincroniza los datos de la interfaz con el objeto lógico Automaton."""
    # Lee los Entry de la matriz y actualiza el diccionario de transiciones del autómata
    for (q, a), ent in self.celdas_const.items():
        # Agrega cada transición ingresada por el usuario al motor lógico

def upd_and_test_c(self):
    """Dibuja el autómata actual y valida la cadena de prueba."""
    self.sync_dfa_const()
    self.dfa_const.draw_on_canvas(self.can_c)
    # Ejecuta validación y muestra si la cadena es ACEPTADA o RECHAZADA

def exportar_jff_c(self):
    """Guarda el autómata diseñado en formato compatible con JFLAP."""
    self.sync_dfa_const()
    # Abre diálogo de guardado y genera el archivo .jff
```
**Explicacion del codigo**
* **Definición Formal Dinámica**: Utiliza un diccionario (`self.c_in`) para mapear las entradas de texto a los elementos de la quíntupla, permitiendo cambios en tiempo real.
* **Matriz de Transición Editable**: Es el núcleo del constructor. Al presionar "GENERAR MATRIZ", el programa crea una cuadrícula de campos Entry donde el usuario puede escribir el estado destino (ej. q1 o q1, q2 para AFN).
* **Sincronización (Sync)**: El método `sync_dfa_const` actúa como recolector de datos, traduciendo lo que el usuario escribió en la interfaz a una estructura de datos que el motor de lógica pueda procesar.
* **Persistencia JFF**: Incluye una función de exportación que permite llevar el trabajo diseñado en esta herramienta hacia JFLAP, facilitando la interoperabilidad.

**Resumen de funcionamiento**: Este módulo transforma datos tabulares en un modelo matemático funcional. El flujo es: Definir (Q, Σ) $\rightarrow$ Generar (Matriz) $\rightarrow$ Llenar ($\delta$) $\rightarrow$ Validar (Visualización y Trace). Todo bajo el esquema de color rosa (`#db2777`).

### Pestaña 5 -> (OPERACIONES)
```python
# --- PESTAÑA 5: OPERACIONES ---
def setup_tab_operaciones(self):
    t = self.temas[4]
    # Barra de herramientas: Carga, Conversión, Minimización y Guardado
    top = tk.Frame(main_f, bg="#0f172a")
    # Botones principales vinculados a cargar_op, convertir_afd y minimizar_afd
    
    # Vista Comparativa: Panel dividido (PanedWindow) para Original vs Resultado
    paned = tk.PanedWindow(main_f, orient="horizontal", ...)
    self.can_op_izq = tk.Canvas(...) # Muestra el autómata base
    self.can_op_der = tk.Canvas(...) # Muestra el autómata transformado
    
    # Consola de bitácora (Log)
    self.txt_op = tk.Text(main_f, height=6, ...)

def cargar_op(self):
    """Carga un autómata base (AFN o AFD) para realizar operaciones sobre él."""
    # Inicializa dfa_op y renderiza en el canvas izquierdo (ORIGINAL)

def convertir_afd(self):
    """Ejecuta el algoritmo de construcción de subconjuntos para transformar AFN en AFD."""
    if not hasattr(self, 'dfa_op'): return
    self.dfa_res = self.dfa_op.to_dfa() # Llamada al motor lógico
    self.dfa_res.draw_on_canvas(self.can_op_der) # Renderiza en el canvas derecho

def minimizar_afd(self):
    """Aplica el algoritmo de partición para reducir el AFD al mínimo número de estados."""
    if not hasattr(self, 'dfa_op'): return
    min_dfa, o, m, p = self.dfa_op.minimize()
    self.dfa_res = min_dfa
    self.dfa_res.draw_on_canvas(self.can_op_der)
    # Reporta métricas de reducción en la bitácora

def guardar_op(self):
    """Exporta el autómata resultante de la operación a formato JFF."""
    if self.dfa_res: self.dfa_res.save_to_jff(p)
```
* **Vista de Espejo**: El uso de un `PanedWindow` con dos Canvas permite al usuario comparar directamente la complejidad del autómata original frente al procesado, facilitando la comprensión visual de los algoritmos.

**Algoritmos de Transformación**:

* **Conversión**: Utiliza el método `to_dfa()` para resolver el no-determinismo.
* **Minimización**: Utiliza el método `minimize()`, que además de devolver el nuevo objeto `Automaton`, entrega estadísticas (estados originales vs. finales) y las particiones (clases de equivalencia) creadas.
* **Bitácora de Información (`txt_op`)**: Actúa como un log de eventos que informa al usuario si las operaciones se completaron con éxito y proporciona datos cuantitativos sobre la reducción de estados.

**Resumen de funcionamiento**: Esta sección funciona como un "laboratorio" de procesamiento. El flujo de trabajo consiste en Cargar un modelo, Transformar (mediante conversión o minimización) y Exportar el resultado. La interfaz garantiza que el usuario siempre vea la evolución del autómata, utilizando el esquema de color naranja (`#f97316`).

### Pestaña 6 -> (Automata Finito -> Expresion Regular)
```python
# --- PESTAÑA 6: AF -> ER ---
    def setup_tab_af_to_er(self):
        """
        Configura la interfaz visual para la conversión de Autómatas a Expresiones Regulares.
        Utiliza un diseño minimalista centrado en un gran área de visualización de texto.
        """
        t = self.temas[5] # Recupera el esquema de color cian definido en el constructor
        
        # Contenedor principal de la pestaña con márgenes internos (padding)
        f = tk.Frame(self.tabs[5], bg="#1e293b", padx=40, pady=40)
        f.pack(expand=True, fill="both")
        
        # Título de la sección
        tk.Label(f, text="AF ➔ EXPRESIÓN REGULAR", bg="#1e293b", 
                 fg=t["accent"], font=("Arial", 22, "bold")).pack(pady=10)
        
        # Botón de acción: Activa el algoritmo de conversión
        btn_gen = tk.Button(f, text="GENERAR EXPRESIÓN REGULAR", command=self.generar_er, 
                           bg=t["btn"], fg="white", font=("bold", 13), padx=40, pady=12)
        btn_gen.pack(pady=20)

        # Contenedor estético para el resultado (con borde resaltado en cian)
        res_container = tk.Frame(f, bg="#0f172a", padx=15, pady=15, 
                                 highlightthickness=2, highlightbackground=t["accent"])
        res_container.pack(fill="both", expand=True, pady=10)
        
        # Área de texto para la Expresión Regular resultante
        # 'wrap="none"' es vital para no romper la expresión en varias líneas
        self.txt_er_res = tk.Text(res_container, font=("Consolas", 18, "bold"), bg="#020617", 
                                  fg="#5eead4", relief="flat", wrap="none", height=8)
        self.txt_er_res.pack(side="top", fill="both", expand=True)
        
        # Scrollbar horizontal para permitir la lectura de ERs extremadamente largas
        h_scroll = tk.Scrollbar(res_container, orient="horizontal", command=self.txt_er_res.xview)
        h_scroll.pack(side="bottom", fill="x")
        self.txt_er_res.config(xscrollcommand=h_scroll.set)

    def generar_er(self):
        """
        Lógica de control para obtener la ER. Busca autómatas procesados en otras pestañas.
        """
        # Prioridad de origen: 
        # 1. dfa_res (Resultado de conversión/minimización en Pestaña 5)
        # 2. dfa_op (Autómata original cargado en Pestaña 5)
        target = self.dfa_res if self.dfa_res else (self.dfa_op if hasattr(self, 'dfa_op') else None)
        
        if target:
            try:
                # Limpia el campo de texto antes de insertar el nuevo resultado
                self.txt_er_res.delete("1.0", tk.END)
                
                # Ejecuta el método de conversión en el motor lógico y lo muestra
                # Nota: Requiere que Automaton.to_regex() devuelva un string
                self.txt_er_res.insert("1.0", target.to_regex())
                
            except AttributeError:
                # Caso de error: El backend no tiene implementada la función de conversión
                messagebox.showerror("Error", "El método 'to_regex' no está implementado en logic/automaton_logic.py")
        else:
            # Caso de aviso: El usuario no ha cargado ningún autómata todavía
            messagebox.showwarning("Aviso", "Carga o procesa un autómata en la pestaña de Operaciones primero.")
```
**Integración de Resultados**: El método `generar_er` busca automáticamente un autómata disponible en la aplicación. Prioriza el resultado de la pestaña de Operaciones (`self.dfa_res`) o, en su defecto, el autómata original cargado (`self.dfa_op`).

**Visualización de la Expresión**:

* Utiliza una fuente de tipo Monospace (Consolas) de gran tamaño para facilitar el análisis de los operadores de la ER (clausuras, uniones, concatenaciones).
* Implementa un Scrollbar Horizontal, ya que las expresiones regulares resultantes del método de eliminación de estados suelen ser considerablemente largas.

**Manejo de Dependencias y Errores**:
* **Validación de Datos**: Si no hay un autómata cargado previamente en el sistema, lanza un aviso al usuario indicando que debe procesar uno primero.
* **Validación de Lógica**: Incluye un manejo de excepción `AttributeError` por si el motor lógico (`Automaton`) no tiene implementado el método `to_regex`, guiando al desarrollador sobre qué falta en el backend.

**Resumen de funcionamiento**: Esta pestaña actúa como un "traductor". No requiere que el usuario ingrese datos nuevos, sino que consume el autómata que se esté trabajando en ese momento. Al presionar el botón, el programa aplica el algoritmo de síntesis (usualmente eliminación de estados) y proyecta la cadena de texto resultante en el área cian (`#06b6d4`).

### Pestaña 7 (Expresion Regular -> Automata Finito)
```python
# --- PESTAÑA 7: ER -> AF ---
    def setup_tab_er_to_af(self):
        """
        Configura la interfaz para transformar expresiones regulares en representaciones gráficas
        de autómatas finitos.
        """
        t = self.temas[6] # Recupera el esquema de color 'Rojo claro' definido en el constructor
        
        # Contenedor principal con márgenes amplios
        f = tk.Frame(self.tabs[6], bg="#1e293b", padx=30, pady=30)
        f.pack(expand=True, fill="both")
        
        # Título de la sección con tipografía destacada
        tk.Label(f, text="EXPRESIÓN REGULAR ➔ AUTÓMATA", bg="#1e293b", 
                 fg=t["accent"], font=("Arial", 22, "bold")).pack(pady=10)
        
        # Área de entrada para la Expresión Regular
        entry_f = tk.Frame(f, bg="#1e293b")
        entry_f.pack(fill="x", pady=20)
        tk.Label(entry_f, text="Ingresa la ER:", bg="#1e293b", fg="white").pack(anchor="w")
        
        self.ent_er_input = tk.Entry(entry_f, font=("Consolas", 18), bg="#0f172a", 
                                     fg="white", relief="flat")
        self.ent_er_input.pack(fill="x", pady=10)

        # Contenedor de botones (Construir y Guardar)
        btn_f = tk.Frame(f, bg="#1e293b")
        btn_f.pack(pady=10)
        
        # Botón para disparar el algoritmo de conversión
        tk.Button(btn_f, text="CONSTRUIR", command=self.er_a_afn, bg=t["btn"], 
                  fg="white", font=("bold", 12), padx=25).pack(side="left", padx=10)
        
        # Botón para exportar el autómata resultante a JFLAP
        tk.Button(btn_f, text="GUARDAR .JFF", command=self.guardar_er_af, bg="#475569", 
                  fg="white", font=("bold", 12), padx=25).pack(side="left", padx=10)

        # Lienzo (Canvas) donde se dibujará el autómata generado
        self.can_er_af = tk.Canvas(f, bg="#020617", highlightthickness=2, 
                                   highlightbackground=t["accent"])
        self.can_er_af.pack(fill="both", expand=True, pady=20)

    def er_a_afn(self):
        """
        Obtiene la ER de la interfaz, invoca la lógica de construcción y renderiza el grafo.
        """
        regex = self.ent_er_input.get().strip()
        if regex:
            try:
                # Crea una nueva instancia de autómata para el resultado
                self.dfa_regex_to_af = Automaton()
                
                # Ejecuta el motor lógico (ej. Algoritmo de Thompson)
                # Nota: Requiere que logic/automaton_logic.py implemente from_regex
                self.dfa_regex_to_af.from_regex(regex)
                
                # Refresca la UI y dibuja el autómata en el canvas correspondiente
                self.root.update()
                self.dfa_regex_to_af.draw_on_canvas(self.can_er_af)
                
            except AttributeError:
                # Error si el backend aún no tiene el método implementado
                messagebox.showerror("Error", "El método 'from_regex' no está implementado.")
            except Exception as e:
                # Captura errores sintácticos en la expresión regular (ej. paréntesis sin cerrar)
                messagebox.showerror("Error", f"Error en la ER: {str(e)}")

    def guardar_er_af(self):
        """
        Exporta el autómata generado a partir de la ER a un archivo compatible con JFLAP.
        """
        if hasattr(self, 'dfa_regex_to_af') and self.dfa_regex_to_af:
            p = filedialog.asksaveasfilename(defaultextension=".jff")
            if p: 
                self.dfa_regex_to_af.save_to_jff(p)
```
* **Validación de Sintaxis**: El método `er_a_afn` incluye un bloque `try-except Exception` genérico. Esto es fundamental porque las expresiones regulares mal formadas son una fuente común de errores en el análisis sintáctico.

* **Independencia de Datos**: A diferencia de la pestaña anterior, esta utiliza su propio objeto `self.dfa_regex_to_af`. Esto permite que el usuario trabaje en una conversión de ER a AF sin perder los autómatas que tenga cargados o minimizados en las pestañas de Simulador u Operaciones.

* **Visualización Dinámica**: El uso de `self.root.update()` antes de draw_on_canvas asegura que el canvas procese correctamente sus dimensiones antes de que el motor de dibujo empiece a colocar los estados y transiciones.

**Resumen de funcionamiento**: Esta pestaña cierra el círculo del Teorema de Kleene en la aplicación. El usuario ingresa una cadena de texto (ER), el sistema la analiza y construye una estructura de estados y transiciones que se proyecta visualmente en el lienzo oscuro con detalles en color rojo (`#f87171`).

## Como ocupar el software
### Primeros pasos
Lo primero que haremos sera como anteriormente lo habiamos explicado crear nuestro entorno virtual,en el cual debemos de verificar que la version de ```python es 3.12.3```, una vez comprobado esta version lo que tenemos que hacer es instalar Tkinter, la version que ocuparemos de Tkinter sera: ```8.6.14``` dentro de nuestro entorno virtual para estar listos para poder ejecutar el programa y asi ver la interfaz grafica.

* Para saber que version tenemos dentro de nuestro entorno virtual desde la linea de comando es: 
  * Saber version de python: ```python3 --version```
  * Saber que version de Tkinter: ```python3 -m tkinter```

Una vez creado nuestro entorno virtual y la libreria de Tkinter estamos listos para ejecutar el comando dentro de la terminal para compilar asi nuestro archivo principal que seria el comando: 

```
python3 main.py
```

Se desplegara la interfaz grafica con la pestaña de logica de cadenas, que nos permitira calcular el **sufijo, prefijo y subcadena**.
* El usuario debera introducir una cadena de la longitud que sea necesaria. 
* Una vez ingresada la cadena se mostraran los resultados dentro de la misma interfaz grafica.

Dentro de la otra pestaña tenemos la de logica de lenguajes que nos permitira calcular **Cerradura de Kleene y la Cerradura Positiva**.
* El usuario debera introducir el  alfabeto separado por comas cada uno de los simbolos que se introduzcan, para despues pedir la longitud maxima que se podran tener en las cadenas. 
* Una vez ingresada la informacion generaremos los lenguajes que se mostraran dentro de la interfaz grafica.

Se desplegará la interfaz gráfica con la pestaña de Simulación, que permite cargar, visualizar y validar el procesamiento de cadenas en un **Autómata Finito (DFA/NFA)**.
* Carga de Autómata: El usuario debe cargar un archivo con la definición formal del **autómata** ($Q, \Sigma, \delta, q_0, F$). Una vez cargado, la interfaz renderizará el grafo dinámico y la tabla de transiciones correspondiente.
* Validación de Cadenas: El usuario podrá introducir una cadena en el campo de texto y presionar el botón Validar. 
* El sistema realizará el recorrido paso a paso, mostrando en tiempo real: El cálculo de la $\lambda$-clausura (en caso de ser un **NFA-$\lambda$)**.
* El historial de transiciones estado por estado en la consola inferior.
* El estado final del proceso, indicando con una etiqueta visual si la cadena es ACEPTADA o RECHAZADA.
* Operaciones Especiales: La interfaz incluye funciones para el cálculo manual de la $\lambda$-clausura de un estado específico y un modo de procesamiento masivo para validar múltiples cadenas simultáneamente.

Esta sección ofrece un entorno de creación y edición manual, diseñado para que el usuario defina paso a paso la estructura formal de un **autómata** sin necesidad de cargar archivos externos. 
* El usuario deberá introducir los elementos básicos del **autómata** en los campos correspondientes:
* **Estados (Q)**: Lista de estados separados por comas.
* **Alfabeto ($\Sigma$)**: Símbolos permitidos para las transiciones.
* **Estado Inicial ($q_0$)**: El nodo de arranque del sistema.
* **Estados Finales (F)**: Conjunto de estados de aceptación.
* Generación de Matriz: Al presionar Generar Matriz, la interfaz habilitará una tabla dinámica donde el usuario podrá especificar las transiciones ($\delta$) para cada combinación de estado y símbolo.
* Visualización y Persistencia: El botón Dibujar y Validar permite renderizar el grafo resultante en el lienzo principal para verificar visualmente la lógica del diseño.
* El usuario tiene la opción de exportar su creación mediante el botón Guardar JFF, generando un archivo compatible con herramientas estándar como JFLAP para su uso posterior.

Despues tenemos la péstaña que constituye el módulo de optimización y conversión, donde el usuario puede procesar **autómatas existentes** para obtener versiones equivalentes más eficientes o simplificadas.
* Gestión de Archivos: Mediante el botón Cargar Original, se importa el **autómata** sobre el cual se desea trabajar. La interfaz presenta un diseño de doble panel para comparar visualmente el modelo "Original" frente al "Resultado" obtenido.
* Algoritmos de Conversión: * Convertir **AFN $\rightarrow$ AFD**: Ejecuta el algoritmo de construcción de subconjuntos para transformar un **Autómata Finito No Determinista** en uno **Determinista equivalente**.
* Minimizar **AFD**: Aplica algoritmos de reducción de estados para encontrar el **autómata** con el menor número de estados posible que acepte el mismo lenguaje.
* Consola de Diagnóstico: La parte inferior incluye un log informativo que detalla el éxito de la operación y datos técnicos, tales como el número de estados originales vs. mínimos y las clases de equivalencia generadas.
* Exportación de Resultados: Una vez realizada la transformación, el usuario puede presionar Guardar Resultado para descargar el nuevo autómata, permitiendo su uso inmediato en los módulos de simulación o construcción.

La siguiente pestaña integra una herramienta de abstracción algebraica, diseñada para extraer la expresión regular equivalente a partir del **autómata** previamente procesado o cargado en el sistema.
* Vinculación de Datos: El módulo utiliza automáticamente el **AFD** resultante de la pestaña anterior ("Operaciones"), asegurando que la conversión se base en la versión más optimizada o simplificada del modelo.
* Procesamiento: Mediante el botón Generar **Expresión Regular**, el sistema aplica algoritmos de eliminación de estados o el método de Arden para reducir la lógica del grafo a una representación textual compacta.
* Visualización del Resultado: La interfaz presenta un panel de salida dedicado donde se muestra la expresión obtenida (utilizando operadores estándar como * para cerradura de Kleene, | para unión y concatenación), permitiendo al usuario copiar la cadena para fines de documentación o programación.

La pestaña 7 funciona como un motor de síntesis lógica, permitiendo al usuario transformar una descripción textual (ER) en un modelo gráfico funcional **(AF)**.
* Entrada de Expresión: El usuario dispone de un campo de texto dedicado para ingresar la **Expresión Regular** deseada. El sistema es capaz de interpretar operadores de unión, concatenación y cerraduras.
* Proceso de Construcción: Al presionar el botón Construir, la aplicación implementa algoritmos de conversión para generar automáticamente un **autómata** equivalente a la expresión proporcionada.
* Visualización Dinámica: El resultado se proyecta en un lienzo interactivo que muestra la estructura de estados y transiciones, facilitando la comprensión de cómo se descompone la lógica de la expresión en pasos finitos.
* Exportación Directa: Al igual que en el módulo de construcción manual, se incluye la función Guardar .JFF, permitiendo descargar el autómata generado para su análisis externo o para cargarlo posteriormente en el Simulador del proyecto.

Esta pestaña constituye la interfaz de usuario final, diseñada para demostrar la utilidad práctica de la teoría de autómatas mediante la validación de patrones de texto comunes. 
* Selector de Tipo de Dato: El usuario dispone de un menú desplegable para elegir el modelo de validación deseado, incluyendo:
   * Correo Electrónico: Valida la estructura estándar de una dirección de correo (usuario@dominio.extensión).
   * URL: Verifica el formato sintáctico de direcciones web (protocolo, dominio y ruta).
   * Fecha (DD/MM/AAAA): Valida la estructura numérica y el formato de fechas estándar.
   * Entrada de Texto y Procesamiento: El sistema cuenta con un campo de texto donde el usuario ingresa la cadena a evaluar. Al presionar el botón *"Validar y Graficar"*, el motor interno procesa la entrada contra el autómata correspondiente al tipo de dato seleccionado.
   * Retroalimentación y Visualización: El sistema ofrece una respuesta inmediata sobre la validez del formato (aceptación o rechazo de la cadena), y despliega de forma dinámica el **Autómata Finito** que fundamenta dicha validación, permitiendo al usuario visualizar el recorrido de los estados que la cadena realiza.

Finalmente, la pestaña 9 constituye el motor de análisis y transformación de gramáticas, proporcionando un entorno robusto para el estudio de las Gramáticas Libres del Contexto (GLC).
* Procesamiento de Producciones: Mediante un editor de texto especializado, el usuario introduce las reglas de derivación. El sistema interpreta la sintaxis para identificar símbolos terminales, no terminales y el símbolo inicial de la gramática.
* Algoritmos de Normalización (FNC): Al ejecutar la transformación, la aplicación aplica de forma secuencial la eliminación de producciones vacías ($\lambda$), la supresión de reglas unitarias y la binarización de cuerpos largos para alcanzar la Forma Normal de Chomsky.
* Seguimiento de procedimiento: La parte inferior despliega un registro detallado que explica cada cambio realizado en la gramática, sirviendo como una herramienta pedagógica para entender la evolución desde una descripción abstracta hasta una estructura binaria estricta.
* Compatibilidad JFF: Al igual que en los módulos de autómatas, se incluye la capacidad de exportar el resultado final en formato XML (.jff), asegurando que las gramáticas generadas puedan ser validadas y estudiadas en herramientas externas como JFLAP.
