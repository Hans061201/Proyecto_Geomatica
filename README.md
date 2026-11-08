# Puntos críticos de residuos sólidos en el distrito de Ate (Lima, Perú)

Análisis espacial en Python de los reportes ciudadanos de acumulación de residuos del aplicativo **Reporta Residuos** (OEFA) y su relación con la red de **contenedores soterrados** de la Municipalidad de Ate.

**Pregunta de investigación:** ¿dónde se concentran los reportes ciudadanos de acumulación de residuos en Ate y qué relación espacial guardan con la red de contenedores municipales?

> Proyecto del curso **Geomática Ambiental** · E.P. de Ingeniería Ambiental · Universidad Nacional Mayor de San Marcos

![Puntos calientes Getis-Ord Gi*](resultados/F6_gi_star.png)

## Resultados principales

| Indicador                               | Resultado                                                                                         |
| --------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Datos analizados                        | 37 reportes ciudadanos (15/06/2026 – 02/10/2026) y 52 contenedores soterrados                    |
| Patrón de los reportes (Clark y Evans) | Agrupado: R = 0.408, z = −6.89                                                                   |
| Autocorrelación global (I de Moran)    | Reportes: I = 0.115, p = 0.003 · Bivariado contenedores–reportes: p = 0.073 (no significativo)  |
| Puntos críticos (DBSCAN, eps = 200 m)  | 6 puntos críticos que reúnen 26 de los 37 reportes (70.3 %)                                     |
| Puntos calientes (Getis-Ord Gi\*)       | 39 celdas calientes en tres zonas; la más intensa, en Huaycán (z hasta 8.56)                    |
| Cobertura de contenedores               | Mediana de 570 m al contenedor más cercano; solo el 5.4 % de los reportes está a menos de 300 m |

Los reportes se concentran en el este del distrito (Huaycán) y los contenedores en el oeste: hay un desacople espacial entre los lugares donde se reporta acumulación de residuos y la infraestructura de almacenamiento.

## Métodos

| Técnica                                       | Para qué se usa                                      | Librería                      |
| ---------------------------------------------- | ----------------------------------------------------- | ------------------------------ |
| Índice de vecino más cercano (Clark y Evans) | Saber si el patrón es agrupado, aleatorio o disperso | NumPy                          |
| Buffers y distancias                           | Medir la cobertura de los contenedores                | GeoPandas                      |
| Densidad kernel (KDE)                          | Superficie continua de concentración                 | scikit-learn                   |
| DBSCAN                                         | Delimitar los puntos críticos                        | scikit-learn                   |
| I de Moran global y bivariado                  | Autocorrelación espacial en una grilla de 500 m      | PySAL (`esda`, `libpysal`) |
| Getis-Ord Gi\*                                 | Puntos calientes estadísticamente significativos     | PySAL (`esda`)               |

Todos los cálculos de distancias y áreas se hacen en **WGS 84 / UTM 18S (EPSG:32718)**.

## Contenido del repositorio

| Archivo                                                     | Descripción                                                                                                                                             |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Analisis_ATE_Version_Final.py`                           | Limpieza de datos y todos los cálculos. Exporta tablas (`.xlsx`) y capas (`.geojson`) a `resultados/`                                             |
| `Figuras_ATE.py`                                          | Genera las 7 figuras del informe en `figuras/`. Los datos ya calculados están incluidos en el propio script, así que no necesita archivos de entrada |
| `Alertas_Reporta_Residuos.json`                           | Alertas ciudadanas del OEFA (GeoJSON, EPSG:4326)                                                                                                         |
| `Lista de ubicacion de contenedores actualizado (1).xlsx` | Inventario de contenedores de la Municipalidad de Ate                                                                                                    |
| `1a Dataset Generacion de RRSS_V2.0 (2).csv`              | Generación de residuos sólidos municipales (MINAM)                                                                                                     |
| `62_5.xlsx`, `64_4.xlsx`                                | Cuadros 2.62 y 2.64: residuos generados y dispuestos en rellenos sanitarios, Lima 2018–2024                                                             |

## Cómo ejecutarlo

### En Google Colab

Cuaderno: [Geomatica.ipynb](https://colab.research.google.com/drive/133IY3O2gIuiyFVStd1M2WORHTEh54Is_?usp=sharing)

1. Instala las dependencias en la primera celda:

   ```python
   !pip install geopandas esda libpysal osmnx contextily openpyxl
   ```
2. Sube los cinco archivos de datos al panel de archivos de Colab.
3. Ejecuta `Analisis_ATE_Version_Final.py` para obtener las tablas y capas.
4. Ejecuta `Figuras_ATE.py` para obtener las figuras.

### En tu computadora

Requiere Python 3.11 o superior.

```bash
pip install geopandas esda libpysal osmnx scikit-learn openpyxl matplotlib contextily
python Analisis_ATE_Version_Final.py
python Figuras_ATE.py
```

Notas:

- El límite distrital se descarga de OpenStreetMap con `osmnx`. Para usar el límite oficial del INEI, coloca `limite_ate.geojson` o `limite_ate.shp` en la misma carpeta y el script lo usará en su lugar.
- Las Figuras 1, 4, 5 y 7 descargan un mapa base de Esri, por lo que necesitan conexión a Internet.

## Salidas

**`resultados/`** (generado por `Analisis_ATE_Version_Final.py`)

| Archivo                                                                       | Contenido                          |
| ----------------------------------------------------------------------------- | ---------------------------------- |
| `T1_limpieza.xlsx`, `T1b_contenedores_descartados.xlsx`                   | Depuración de las capas           |
| `T2_reportes_por_fecha.xlsx`, `T3_contenedores_zona_estado.xlsx`          | Análisis exploratorio             |
| `T4_vecino_mas_cercano.xlsx`                                                | Índice de Clark y Evans           |
| `T5_distancia_reporte_contenedor.xlsx`, `T6_buffers_cobertura.xlsx`       | Distancias y cobertura por buffers |
| `T7_dbscan_sensibilidad.xlsx`, `T8_puntos_criticos_dbscan.xlsx`           | DBSCAN                             |
| `T9_moran.xlsx`                                                             | I de Moran                         |
| `T10_gi_resumen.xlsx`, `T11_gi_celdas_calientes.xlsx`                     | Getis-Ord Gi\*                     |
| `T12_minam_generacion_ate.xlsx` a `T14_indicadores.xlsx`                  | Contexto distrital                 |
| `T15_kde_resumen.xlsx`                                                      | Densidad kernel                    |
| `reportes_ate.geojson`, `contenedores_ate.geojson`, `grilla_gi.geojson` | Capas para ArcGIS o QGIS           |

**`figuras/`** (generado por `Figuras_ATE.py`): distribución de reportes y contenedores, reportes por fecha, densidad kernel, Getis-Ord Gi\*, buffers, residuos 2018–2024 y puntos críticos DBSCAN.

## Limitaciones

- **Sesgo de participación:** los reportes dependen de quién usa el aplicativo; la ausencia de reportes no implica ausencia de residuos.
- **Muestra pequeña:** con 37 reportes, los resultados son sensibles a los parámetros; por eso se evaluó la sensibilidad de DBSCAN.
- **Límite de OpenStreetMap:** puede diferir del límite oficial del INEI.
- **Solo contenedores soterrados:** la cobertura no incluye la recolección puerta a puerta.

## Fuentes de datos

- Organismo de Evaluación y Fiscalización Ambiental (OEFA). *Alertas Reporta Residuos*.
- Municipalidad Distrital de Ate. *Lista de ubicación de contenedores (actualizado)*.
- Ministerio del Ambiente (MINAM). *Generación de residuos sólidos municipales*. Plataforma Nacional de Datos Abiertos.
- Municipalidad Metropolitana de Lima. *Cuadros 2.62 y 2.64: residuos sólidos municipales, 2018–2024*.
- OpenStreetMap contributors. *Límite del distrito de Ate (relación 1944683)*.
