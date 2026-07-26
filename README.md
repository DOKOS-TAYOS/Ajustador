# Ajustador

Conjunto de programas Python para ajustar datos experimentales a distintas funciones (incluidas funciones arbitrarias si se configuran bien), con interfaz útil en escritorio y en Android.

**Autor:** Alejandro Mata Ali (DOKOS TAYOS)

Repositorio: [github.com/DOKOS-TAYOS/Ajustador](https://github.com/DOKOS-TAYOS/Ajustador)

## Contenido

| Carpeta | Descripción |
| --- | --- |
| `Ajustes/` | Versión de escritorio (Tkinter): carga de datos, ajuste y gráficas |
| `Ajustes movil/` | Variante orientada a uso en Android / entorno móvil |
| `*/Datos/` | Ejemplos de datos (CSV/Excel) |
| `Ajustes/Graficas/` | Salidas gráficas de ejemplo |

## Dependencias

- Python 3.x
- NumPy, SciPy, Matplotlib, pandas
- Tkinter (interfaz)
- Lectura Excel vía pandas (puede requerir `openpyxl` u otro motor Excel)

Instalación típica:

```bash
pip install numpy scipy matplotlib pandas openpyxl
```

## Uso rápido

1. Coloca o usa los archivos de `Datos/`.
2. Ejecuta el script principal de la carpeta deseada (`Exper_ajus_1.py` o `Ajustador_movil.py`).
3. Selecciona el conjunto de datos y la función de ajuste desde la interfaz.

Este código es un prototipo antiguo; úsalo como base o referencia, no como producto empaquetado.

## Licencia

Este proyecto está licenciado bajo la **Apache License 2.0**. Ver [`LICENSE`](LICENSE).

Avisos de dependencias de terceros: [`NOTICE`](NOTICE).

## Contacto

Alejandro Mata Ali — alejandro.mata.ali@gmail.com
