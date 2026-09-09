# -*- coding: utf-8 -*-
"""Proyecto final .ipynb

import pandas as pd
import numpy as np
# Descargar el archivo directamente al entorno de Google Colab
!curl -O https://raw.githubusercontent.com/reisanar/datasets/master/HollywoodMovies.csv



df = pd.read_csv("HollywoodMovies.csv")

# 2. Seleccionar únicamente las 8 columnas requeridas
columnas_deseadas = [
    "Movie", "LeadStudio", "Genre", "RottenTomatoes",
    "AudienceScore", "WorldGross", "Budget", "Year"
]
df = df[columnas_deseadas]

# Checkpoint 1: Diagnóstico inicial
print("--- ETAPA 1: DIAGNÓSTICO INICIAL ---")
print(f"Forma del dataset: {df.shape}")
print("Valores nulos por columna:")
print(df.isnull().sum())
print("-" * 40)


# ==========================================
# ETAPA 2: Limpiar
# ==========================================
# 1. Columnas de texto: Rellenar nulos con categoría de reemplazo ("Desconocido")
df["Genre"] = df["Genre"].fillna("Desconocido")
df["LeadStudio"] = df["LeadStudio"].fillna("Desconocido")

# 2. Columnas numéricas de calificación: Rellenar con la mediana (medida que no se altera por extremos)
mediana_rotten = df["RottenTomatoes"].median()
mediana_audience = df["AudienceScore"].median()

df["RottenTomatoes"] = df["RottenTomatoes"].fillna(mediana_rotten)
df["AudienceScore"] = df["AudienceScore"].fillna(mediana_audience)

# 3. Columnas numéricas financieras (pocas filas afectadas): Eliminar filas
df = df.dropna(subset=["WorldGross", "Budget"])

# Checkpoint 2: Confirmar 0 nulos en total y 897 filas
print("--- ETAPA 2: LIMPIEZA COMPLETADA ---")
print(f"Forma del dataset tras limpieza: {df.shape}")
print(f"Total nulos en el dataset: {df.isnull().sum().sum()}")
print("-" * 40)


# ==========================================
# ETAPA 3: Crear columnas nuevas
# ==========================================
# 1. Columna Ganancia (WorldGross - Budget)
df["Ganancia"] = df["WorldGross"] - df["Budget"]

# 2. Columna Exitosa (True si Rotten Tomatoes >= 60, False en otro caso)
df["Exitosa"] = df["RottenTomatoes"] >= 60

# Checkpoint 3: Validar conteo de la columna Exitosa
print("--- ETAPA 3: NUEVAS COLUMNAS ---")
print("Conteo de la columna Exitosa:")
print(df["Exitosa"].value_counts())
print("-" * 40)


# ==========================================
# ETAPA 4: Tipos de datos y ordenar
# ==========================================
# 1. Confirmar dtypes (Exitosa debe ser bool)
print("--- ETAPA 4: TIPOS DE DATOS Y TOP 3 RENTABLES ---")
print(f"Tipo de dato de Exitosa: {df['Exitosa'].dtype}")

# 2. Ordenar por Ganancia de mayor a menor y mostrar las 3 películas más rentables
df_ordenado = df.sort_values(by="Ganancia", ascending=False)
print("\nTop 3 películas más rentables:")
print(df_ordenado[["Movie", "Ganancia"]].head(3))
print("-" * 40)


# ==========================================
# ETAPA 5: Agrupar y analizar
# ==========================================
print("--- ETAPA 5: AGRUPACIÓN Y ANÁLISIS ---")
# 1. Promedio de Rotten Tomatoes por Género (redondeado a 1 decimal)
promedio_genero = df.groupby("Genre")["RottenTomatoes"].mean().round(1)
print("Promedio de Rotten Tomatoes por género:")
print(promedio_genero)

print("\n" + "="*20 + "\n")

# 2. Promedio de Ganancia por Estudio (redondeado a 1 decimal)
promedio_estudio = df.groupby("LeadStudio")["Ganancia"].mean().round(1)
print("Promedio de Ganancia por estudio:")
print(promedio_estudio)
print("-" * 40)


# ==========================================
# ETAPA 6: Guardar el resultado
# ==========================================
# Guardar dataset sin la columna extra de índice
df.to_csv("hollywood_limpio.csv", index=False)

# Checkpoint Final
df_verificacion = pd.read_csv("hollywood_limpio.csv")
print("--- ETAPA 6: VERIFICACIÓN ARCHIVO FINAL ---")
print(f"Forma del archivo final: {df_verificacion.shape}")
print(f"Total de nulos: {df_verificacion.isnull().sum().sum()}")
