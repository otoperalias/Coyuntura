import pandas as pd


def tabla(ax, df, fs=9, bbox=(0.02, 0.15, 0.98, 0.7), ancho_etiq=0.17,
          filas_color="alternas", color_cab="#d9d9d9", color_fila="#f2f2f2",
          titulos_negrita=True):
    """
    Dibuja un DataFrame como tabla con formato profesional dentro de un axes.

    IMPORTANTE: la tabla reproduce el DataFrame tal cual está:
      - el índice    -> primera columna (nombres de las filas)
      - las columnas -> cabecera
      - los valores  -> se escriben tal cual, sin redondear
    Por tanto, el DataFrame hay que prepararlo antes con la forma y los decimales
    deseados (p. ej., con .round(1)).

    Las filas sin datos (todo NaN o texto vacío) se muestran como filas de título:
    solo aparece su nombre (en negrita, si titulos_negrita=True).

    Argumentos:
      ax              -> el axes (hueco de la figura) donde se dibuja la tabla
      df              -> el DataFrame con los datos
      fs              -> tamaño de letra (font size)
      bbox            -> caja donde va la tabla: (x, y, ancho, alto), en proporción del axes (de 0 a 1)
      ancho_etiq      -> proporción del ancho de la tabla reservada a la columna de nombres
      filas_color     -> filas con fondo de color:
                           "alternas"           -> una sí y otra no
                           lista de nombres     -> esas filas, p. ej. ["España", "Italia"]
                           None                 -> ninguna
      color_cab       -> color de fondo de la cabecera
      color_fila      -> color de fondo de las filas coloreadas
      titulos_negrita -> si True, las filas sin datos (títulos) van en negrita
    """

    # Ocultamos los ejes, las marcas y el marco: en este axes solo queremos ver la tabla
    ax.axis("off")

    # Función auxiliar: ¿está vacía esta celda? (NaN, None o texto vacío)
    def vacia(v):
        return pd.isna(v) or v == ""

    # Preparamos el contenido de las celdas como una lista de filas.
    # Cada fila empieza con el nombre (índice del DataFrame) y sigue con los valores
    # convertidos a texto TAL CUAL (sin redondear). Las celdas vacías quedan en blanco.
    # Usamos astype(object) para que cada valor conserve su tipo (enteros, decimales, texto).
    celdas = []
    filas_titulo = []                           # posiciones de las filas sin datos
    for pos, (nombre, fila) in enumerate(zip(df.index, df.astype(object).values)):
        textos = ["" if vacia(v) else str(v) for v in fila]
        celdas.append([str(nombre)] + textos)
        if all(vacia(v) for v in fila):
            filas_titulo.append(pos + 1)        # +1 porque la fila 0 de la tabla es la cabecera

    # Decidimos qué filas de la tabla llevan fondo de color (la fila 1 es la primera de datos)
    if filas_color == "alternas":
        coloreadas = [r for r in range(1, len(df) + 1) if r % 2 == 0]
    elif filas_color is None:
        coloreadas = []
    else:
        # Buscamos la posición de cada nombre indicado en el índice del DataFrame
        coloreadas = [pos + 1 for pos, nombre in enumerate(df.index) if nombre in filas_color]

    # Anchura de cada columna, en proporción del ancho de la tabla:
    # la primera (nombres) mide 'ancho_etiq' y el resto se reparte a partes iguales
    k = df.shape[1]                             # número de columnas de datos
    anchos = [ancho_etiq] + [(1 - ancho_etiq) / k] * k

    # Creamos la tabla: contenido, cabecera (hueco vacío sobre los nombres +
    # nombres de las columnas), anchuras y caja donde se coloca
    tb = ax.table(cellText=celdas, colLabels=[""] + [str(c) for c in df.columns],
                  colWidths=anchos, bbox=bbox)

    # Fijamos nosotros el tamaño de letra (si no, matplotlib lo ajusta a su gusto)
    tb.auto_set_font_size(False)
    tb.set_fontsize(fs)

    # Recorremos todas las celdas para darles formato.
    # get_celld() devuelve un diccionario: la clave es (fila, columna) y el valor es la celda.
    for (r, c), cell in tb.get_celld().items():

        # Margen interior de la celda (espacio entre el texto y el borde)
        cell.PAD = 0.04

        # Nombres (columna 0) a la izquierda; números a la derecha, para alinear las cifras
        cell.set_text_props(ha="left" if c == 0 else "right")

        # Filas de título: borramos el texto de la celda (la celda de al lado lo taparía
        # si es largo); lo escribimos después, por encima de la tabla
        if r in filas_titulo:
            cell.get_text().set_text("")

        # Elegimos el color de fondo según la fila
        if r == 0:                      # cabecera
            fondo = color_cab
            cell.set_text_props(size=fs-1)   # Si queremos negrita: weight="bold"
        elif r in coloreadas:           # filas elegidas para colorear
            fondo = color_fila
        else:                           # resto de filas: blanco
            fondo = "white"

        cell.set_facecolor(fondo)       # color de relleno de la celda
        cell.set_edgecolor(fondo)       # borde del mismo color, para que no se vea la rejilla

    # Líneas horizontales (arriba, bajo la cabecera y al cierre), dibujadas aparte
    # porque los bordes de celda no son compatibles con el relleno
    x0, y0, ancho, alto = bbox
    alto_fila = alto / (len(df) + 1)
    for y in [y0 + alto, y0 + alto - alto_fila, y0]:
        ax.plot([x0, x0 + ancho], [y, y], color="black", lw=0.5, transform=ax.transAxes)

    # Escribimos los títulos encima de la tabla, para que puedan ocupar todo el ancho.
    # Posición: mismo margen izquierdo que el resto de nombres y centrados en su fila.
    margen = 0.04 * ancho_etiq * ancho          # el mismo PAD que las celdas
    for r in filas_titulo:
        y = y0 + alto - (r + 0.5) * alto_fila    # centro vertical de la fila r
        ax.text(x0 + margen, y, str(df.index[r - 1]), transform=ax.transAxes,
                ha="left", va="center", fontsize=fs,
                weight="bold" if titulos_negrita else "normal")

    # Devolvemos la tabla por si queremos retocarla después fuera de la función
    return tb
