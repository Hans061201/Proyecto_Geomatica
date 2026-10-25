import geopandas as gpd
import pandas as pd

# Cargar el archivo GeoJSON con la ruta corregida
data = gpd.read_file("C:/Carrera/Ambiental/Ciclo 6/Geomatica/Proyecto/archive/Alertas_Reporta_Residuos.json")

# Mostrar las primeras filas y la geometría (puntos con coordenadas)
pd.set_option('display.max_columns', None)


#data = data[data["Provincia"]=="LIMA"]
#Ate = data[data["Distrito"] == "ATE"]

#print(Ate.head())
#Ate.to_file("C:/Carrera/Ambiental/Ciclo 6/Geomatica/Proyecto/archive/Ate_Residuos.shp", driver="ESRI Shapefile")

data1 = pd.read_excel("C:/Carrera/Ambiental/Ciclo 6/Geomatica/Proyecto/archive/Contenedores/Lista de ubicacion de contenedores actualizado (1).xlsx")
data1[["Latitud", "Longitud"]] = data1["COORDENADAS"].str.split(',', expand = True)
data1['Latitud'] = pd.to_numeric(data1['Latitud'], errors='coerce')
data1['Longitud'] = pd.to_numeric(data1['Longitud'], errors='coerce')
data1 = data1.drop(columns=["COORDENADAS"])
#gdf = gpd.GeoDataFrame(
 #   data1, 
 #   geometry=gpd.points_from_xy(data1['Longitud'], data1['Latitud']),
 #   crs="EPSG:4326"  
#)

# 5. Exportar a un archivo Shapefile (.shp) para abrirlo en ArcGIS
#ruta_salida = "C:/Carrera/Ambiental/Ciclo 6/Geomatica/Proyecto/archive/Contenedores/contenedores.shp"
#gdf.to_file(ruta_salida, driver="ESRI Shapefile")

print("¡Exportación completada exitosamente!")
print(data1)