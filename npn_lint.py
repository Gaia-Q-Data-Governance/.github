
```
Este script, llamado `npn_lint.py`, valida nombres de archivo según una expresión regular definida. Aquí hay una explicación detallada de cómo funciona y qué hace:

---

### **Descripción del Script**
1. **Propósito**  
   El objetivo del script es comprobar si los nombres de archivo proporcionados cumplen con un formato canónico predefinido, utilizando una expresión regular.

2. **Cómo Usarlo**  
   El script se ejecuta desde la línea de comandos con la siguiente sintaxis:  
   ```bash
   python npn_lint.py <archivo1> [archivo2 ...]
   ```
   - `<archivo1>` y `[archivo2 ...]` son los nombres de archivo a validar.
   - Devuelve **0** si todos los nombres son válidos, o **1** si alguno es inválido.

3. **Salida**  
   - Para cada archivo, imprime:
     - `✔ <nombre> : OK` si el nombre cumple con la expresión regular.
     - `✖ <nombre> : INVALID` si no cumple.
   - Finaliza con un código de salida:
     - **0** si todos los nombres son válidos.
     - **1** si alguno es inválido.
     - **2** si no se proporcionaron argumentos.

---

### **Explicación de la Expresión Regular**

```python
REGEX = re.compile(
    r"^(?P<NPN>[A-Z0-9]{2,5}-[0-9]{2}-[0-9]{3}-[0-9]{4})-"
    r"(?P<TipoDoc>[A-Z]{2,6})"
    r"(?:-(?P<Seq>[0-9]{3}))?"
    r"-(?P<Ver>v[0-9]+\.[0-9]+|r[0-9][1-9]|r[1-9][0-9])\."
    r"(?P<ext>[a-z0-9]{1,5})$"
)
```

#### **Partes de la Expresión Regular**
1. **NPN (Número de Parte o Identificador)**  
   ```regex
   (?P<NPN>[A-Z0-9]{2,5}-[0-9]{2}-[0-9]{3}-[0-9]{4})
   ```
   - Debe comenzar con 2 a 5 caracteres alfanuméricos en mayúscula (`A-Z0-9`).
   - Seguido de un guion `-`, 2 dígitos (`[0-9]{2}`), otro guion, 3 dígitos, y otro guion.
   - Finalmente, debe terminar con 4 dígitos.

2. **Tipo de Documento**  
   ```regex
   (?P<TipoDoc>[A-Z]{2,6})
   ```
   - Una cadena de 2 a 6 letras mayúsculas (`[A-Z]`).

3. **Secuencia Opcional**  
   ```regex
   (?:-(?P<Seq>[0-9]{3}))?
   ```
   - Tres dígitos (`[0-9]{3}`), precedidos de un guion.  
   - Es opcional debido a `(?: ... )?`.

4. **Versión o Revisión**  
   ```regex
   (?P<Ver>v[0-9]+\.[0-9]+|r[0-9][1-9]|r[1-9][0-9])
   ```
   - Puede ser:
     - `vX.Y` (con `X` e `Y` como uno o más números).
     - `rXY` o `rYY` (donde `X` es 1 dígito y `Y` es 1 o 2 dígitos).

5. **Extensión del Archivo**  
   ```regex
   (?P<ext>[a-z0-9]{1,5})
   ```
   - Una extensión de 1 a 5 caracteres en minúscula o dígitos (`[a-z0-9]`).

6. **Estructura Completa**  
   ```regex
   ^ ... $  
   ```
   - El nombre del archivo debe coincidir **exactamente** con el patrón (de principio a fin).

---

### **Ejemplo de Nombres Válidos**
- `AB12-34-567-8901-DOC-v1.0.txt`
- `XYZ-12-345-6789-REP-001-v2.5.pdf`
- `A1-23-456-7890-TXT-r11.doc`

### **Ejemplo de Nombres Inválidos**
- `AB1234-567-8901-DOC-v1.0.txt` (Error en el NPN, falta un guion).
- `XYZ-12-345-6789-DOC-v1.0` (Falta la extensión).
- `XYZ-12-345-6789-REP-v1.txt` (Versión inválida, falta `.0`).

---

### **Mejoras Posibles**
1. **Documentación Extendida**  
   Agrega comentarios en el código para explicar cada parte de la expresión regular.

2. **Validación de Extensiones Permitidas**  
   Si solo se aceptan ciertas extensiones (e.g., `txt`, `pdf`), limita la validación:
   ```regex
   (?P<ext>txt|pdf|doc)
   ```

3. **Soporte Multiplataforma**  
   Valida rutas completas (`pathlib.Path`) para manejar nombres de archivo correctamente en diferentes sistemas operativos.

4. **Pruebas Automáticas**  
   Agrega un conjunto de pruebas unitarias con `unittest` o `pytest` para garantizar la funcionalidad.

---

¿Te gustaría que implemente alguna mejora o personalización adicional para este script?
Valida que los nombres de archivo cumplan la expresión
canónica definida en el SOP.
Uso:  python npn_lint.py <archivo1> [archivo2 ...]
Devuelve 0 si todos los nombres son válidos; 1 en caso contrario.
"""
import re, sys, pathlib

REGEX = re.compile(
    r"^(?P<NPN>[A-Z0-9]{2,5}-[0-9]{2}-[0-9]{3}-[0-9]{4})-"
    r"(?P<TipoDoc>[A-Z]{2,6})"
    r"(?:-(?P<Seq>[0-9]{3}))?"
    r"-(?P<Ver>v[0-9]+\.[0-9]+|r[0-9][1-9]|r[1-9][0-9])\."
    r"(?P<ext>[a-z0-9]{1,5})$"
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python npn_lint.py <file1> [file2 ...]")
        sys.exit(2)

    exit_code = 0
    for fname in sys.argv[1:]:
        name = pathlib.Path(fname).name
        if REGEX.match(name):
            print(f"✔ {name} : OK")
        else:
            print(f"✖ {name} : INVALID")
            exit_code = 1
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
