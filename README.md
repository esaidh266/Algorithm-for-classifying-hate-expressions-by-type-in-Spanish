# Modelo de clasificación de tipos de discurso de odio

Este código implementa un sistema de clasificación de discurso de odio utilizando el modelo RoBERTuito (una versión en español de RoBERTa) para detectar diferentes tipos de discurso de odio en tuits.

## Arquitectura del Modelo

El modelo se basa en `pysentimiento/robertuito-base-uncased` con las siguientes modificaciones:
- Se añadió una capa de clasificación densa con 6 salidas sobre el modelo base.
- Utiliza IDs de entrada y máscaras de atención como entradas.
- Genera una clasificación multiclase con 6 categorías.

## Datasets

1.  **Conjunto de Datos de Tipos de Odio**: Este modelo utiliza un conjunto de datos personalizado para la clasificación de tipos de discurso de odio, que incluye una columna `label` con etiquetas enteras del 0 al 5.
    -   Las etiquetas numéricas corresponden a 6 clases distintas de discurso de odio. Las definiciones específicas de cada etiqueta (0-5) no se detallan en el código.

## Proceso de Entrenamiento

### Pre-entrenamiento
- Batch size: 16
- Epochs: 5
- Learning rate: 2e-5 with 10% warmup steps
- Early stopping with patience=2

### Fine-tuning
- Batch size: 128
- Epochs: 5
- Learning rate: 2e-5 with 10% warmup steps
- Early stopping with patience=2
- Métricas personalizadas (ej., recall, precision, F1-score ponderados por clase, AUC multiclase).

## Métricas de Evaluación

El modelo se evalúa utilizando:
- Macro recall, precision, and F1-score
- One-vs-Rest AUC
- Accuracy
- Métricas por clase
- Matriz de confusión

## Requerimientos

Se requiere los siguientes paquetes de Python (consulte requirements.txt para ver la lista completa):
- TensorFlow
- Transformers
- scikit-learn
- pandas
- datasets
- matplotlib
- seaborn

## Uso
El modelo espera datos de entrada con las siguientes especificaciones:

1.  **Formato de datos**:
    -   Archivo CSV o DataFrame de Pandas
    -   Nombre de columna obligatorio: `text` (tipo cadena)
    -   Nombre de columna opcional: `label` (tipo entero, 0 a 5) si está disponible para la evaluación

2.  **Preprocesamiento de texto**:
    -   El texto se tokenizará automáticamente a minúsculas durante el procesamiento.
    -   Longitud máxima: 128 tokens (los textos más largos se truncarán).
    -   Los caracteres especiales, las URL y los emojis deben permanecer en el texto (el tokenizador los gestiona).

3.  **Codificación de etiquetas**:
    -   El modelo clasifica los textos en 6 clases distintas, representadas por los enteros `0`, `1`, `2`, `3`, `4`, `5`. Las definiciones específicas de lo que representa cada etiqueta deben ser proporcionadas por el usuario.