def tabla(ax, df, fs=9, dec=1, bbox=(0.02, 0.15, 0.98, 0.7), ancho_etiq=0.17,
          color_cab="#d9d9d9", color_alt="#f2f2f2"):
    """
    Dibuja un DataFrame como tabla con formato profesional dentro de un axes.

    IMPORTANTE: la tabla reproduce el DataFrame tal cual está:
      - el índice    -> primera columna (nombres de las filas)
      - las columnas -> cabecera
    Por tanto, el DataFrame hay que prepararlo antes con la forma deseada

    Argumentos:
      ax         -> el axes (hueco de la figura) donde se dibuja la tabla
      df         -> el DataFrame con los datos
      fs         -> tamaño de letra (font size)
      dec        -> número de decimales que se muestran
      bbox       -> caja donde va la tabla: (x, y, ancho, alto), en proporción del axes (de 0 a 1)
      ancho_etiq -> proporción del ancho de la tabla reservada a la columna de nombres
      color_cab  -> color de fondo de la cabecera
      color_alt  -> color de fondo de las filas alternas
    """

    # Ocultamos los ejes, las marcas y el marco: en este axes solo queremos ver la tabla
    ax.axis("off")

    # Preparamos el contenido de las celdas como una lista de filas.
    # Cada fila empieza con el nombre (índice del DataFrame) y sigue con los valores
    # convertidos a texto con 'dec' decimales (p. ej., 2.9134 -> "2.9").
    celdas = []
    for i, fila in zip(df.index, df.values):
        textos = [f"{v:.{dec}f}" for v in fila]
        celdas.append([i] + textos)

    # Anchura de cada columna, en proporción del ancho de la tabla:
    # la primera (nombres) mide 'ancho_etiq' y el resto se reparte a partes iguales
    k = df.shape[1]                             # número de columnas de datos
    anchos = [ancho_etiq] + [(1 - ancho_etiq) / k] * k

    # Creamos la tabla: contenido, cabecera (hueco vacío sobre los nombres +
    # nombres de las columnas), anchuras y caja donde se coloca
    tb = ax.table(cellText=celdas, colLabels=[""] + list(df.columns),
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

        # Elegimos el color de fondo según la fila
        if r == 0:                      # cabecera (fila 0): gris medio y negrita
            fondo = color_cab
            cell.set_text_props(size=fs-1) # Si queremos negrita: weight="bold"
        elif r % 2 == 0:                # filas pares: gris claro (r % 2 es el resto de dividir entre 2)
            fondo = color_alt
        else:                           # filas impares: blanco
            fondo = "white"

        cell.set_facecolor(fondo)       # color de relleno de la celda
        cell.set_edgecolor(fondo)       # borde del mismo color, para que no se vea la rejilla

    # Líneas horizontales (arriba, bajo la cabecera y al cierre), dibujadas aparte
        # porque los bordes de celda no son compatibles con el relleno
        x0, y0, ancho, alto = bbox
        alto_fila = alto / (len(df) + 1)
        for y in [y0 + alto, y0 + alto - alto_fila, y0]:
            ax.plot([x0, x0 + ancho], [y, y], color="black", lw=0.5, transform=ax.transAxes)

    # Devolvemos la tabla por si queremos retocarla después fuera de la función
    return tb
