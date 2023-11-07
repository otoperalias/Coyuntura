```

# Procesamos datos
    # Columnas relevantes
ss=ss[["Datos totales de afiliados Medios en alta por Regímenes","Unnamed: 13"]]
    # Filas con datos
ss=ss.iloc[2:-10] #
    # Cambiamos nombres a columnas:
ss.columns=["fecha","afiliados"]
    # Preparar columna para fecha
meses={"Ene":"01","Feb":"02","Mar":"03","Abr":"04",
       "May":"05","Jun":"06","Jul":"07","Ago":"08",
       "Sep":"09","Oct":"10","Nov":"11","Dic":"12"}
ss["periodo"]=ss.fecha.str[-4:]+"-"+ss.fecha.str[:3].map(meses)
    # Convertimos to date times
ss.periodo=pd.to_datetime(ss.periodo)
ss.set_index(ss.periodo, inplace=True)
    # Me quedo con las columnas relevantes
ss=ss[['afiliados']]
ss
```
