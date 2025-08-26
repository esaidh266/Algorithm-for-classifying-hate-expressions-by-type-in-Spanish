# Modelo de clasificación de tipos de discurso de odio

Este código implementa un sistema de clasificación de discurso de odio utilizando el modelo RoBERTuito (una versión en español de RoBERTa) para detectar diferentes tipos de discurso de odio en tuits.

## Arquitectura del Modelo

El modelo se basa en `pysentimiento/robertuito-base-uncased` con las siguientes modificaciones:
- Se añadió una capa de clasificación densa con 5 salidas sobre el modelo base.
- Utiliza IDs de entrada y máscaras de atención como entradas.
- Genera una clasificación multiclase con 5 categorías.

## Datasets

1.  **Conjunto de Datos de Tipos de Odio**: Este modelo utiliza un conjunto de datos personalizado para la clasificación de tipos de discurso de odio, que incluye una columna `label` con etiquetas enteras del 0 al 5.
    -   Las etiquetas numéricas corresponden a 6 clases distintas de discurso de odio. Las definiciones específicas de cada etiqueta (1-5) no se detallan en el código.

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
    -   Nombre de columna opcional: `label` (tipo entero, 1 a 5) si está disponible para la evaluación

2.  **Preprocesamiento de texto**:
    -   El texto se tokenizará automáticamente a minúsculas durante el procesamiento.
    -   Longitud máxima: 128 tokens (los textos más largos se truncarán).
    -   Los caracteres especiales, las URL y los emojis deben permanecer en el texto (el tokenizador los gestiona).

3.  **Codificación de etiquetas**:

-   El modelo clasifica los textos en 5 clases distintas, representadas por los enteros:
    -   `1`: Odio general o indiferenciado: Expresiones de odio, sin un claro dominio de uno de los tipos específicos considerados en este monitor, pudiendo contener en este tipo de mensajes más de un tipo de odio.
    -   `2`: Odio político: Expresiones contra individuos o colectivos por motivos de orientación política.
    -   `3`: Odio sexual: Expresiones dirigidas contra personas o colectivos por su orientación sexual.
    -   `4`: Odio misógino: Expresiones dirigidas contra mujeres o rasgos asociados a ellas.
    -   `5`: Odio xenófono: Expresiones dirigidas contra personas o colectivos, por motivo de origen (e.j. extranjero e inmigrante).

El proceso de creación de este algoritmo se expone en el informe técnico localizado en: 

Autores: 
- Elias Said-Hung
- Julio Montero-Díaz
- Oscar De Gregorio
- Almudena Ruiz
- Xiomara Blanco
- Juan José Cubillas
- Daniel Pérez Palau 

Financiado por: 
MCIN/AEI /10.13039/501100011033

Como citar: Pérez Palau, D., Blanco Valencia, X., Ruiz-Iniesta, A., De Gregorio Vicente, O., José Cubillas, J., Said-Hung, E. y Montero-Diaz, J. (2023). Algoritmo de clasificación de expresiones de odio por tipos en español [Algorithm for classifying hate expressions by type in Spanish]. https://doi.org/10.6084/m9.figshare.25892815.v1.

Más información:

- https://www.hatemedia.es/ o contactar con:  elias.said@unir.net
- Este algoritmo está relacionado con el algoritmo de clasificación de odio/no odio, desarrollado también por los autores: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish
- Este algoritmo está relacionado con el algoritmo de clasificación de expresiones de odio por intensidades en español, desarrollado también por los autores: https://github.com/esaidh266/Algorithm-for-classifying-hate-expressions-by-intensities-in-Spanish

---------

# Hate Speech Type Classification Model

This code implements a hate speech classification system using the RoBERTuito model (a Spanish version of RoBERTa) to detect different types of hate speech in tweets.

##Model Architecture

The model is based on `pysentimiento/robertuito-base-uncased` with the following modifications:
- A dense classification layer with 5 outputs has been added over the base model.
- It uses input IDs and attention masks as inputs.
- It generates a multiclass classification with 5 categories.

##Datasets

1. **Hate Speech Types Dataset**: This model uses a custom dataset for hate speech type classification, which includes a `label` column with integer labels from 0 to 5.
- The numerical labels correspond to 6 distinct classes of hate speech. The specific definitions of each label (1-5) are not detailed in the code.

## Training Process

### Pre-training
- Group size: 16
- Epochs: 5
- Learning rate: 2e-5 with 10% warm-up steps
- Early stopping with patience = 2

### Fine-tuning
- Group size: 128
- Epochs: 5
- Learning rate: 2e-5 with 10% warm-up steps
- Early stopping with patience = 2
- Custom metrics (e.g., recall, precision, class-weighted F1 score, multi-class AUC).

## Evaluation Metrics

The model is evaluated using:
- Macro recall, precision, and F1 score
- One-versus-rest AUC
- Accuracy
- Per-class metrics
- Confusion matrix

##Requirements

The following Python packages are required (see requirements.txt for the full list):
- TensorFlow
- Transformers
- scikit-learn
- pandas
- datasets
- matplotlib
- seaborn

##Usage
The model expects input data with the following specifications:

1. **Data Format**:
- CSV file or Pandas DataFrame
- Required column name: `text` (string type)
- Optional column name: `label` (integer type, 1 to 5) if available for evaluation

2. **Text Preprocessing**:
- Text will be automatically tokenized to lowercase during processing.
- Maximum length: 128 tokens (longer texts will be truncated).
- Special characters, URLs, and emojis must remain in the text (the tokenizer handles them).

3. **Tag Encoding**:

- The model classifies texts into 5 distinct classes, represented by integers:
    - `1`: General or undifferentiated hate: Expressions of hate, without a clear dominance of one of the specific types considered in this monitor, and these types of messages may contain more than one type of hate.
    - `2`: Political hate: Expressions against individuals or groups for reasons of political orientation.
    - `3`: Sexual hate: Expressions directed against individuals or groups for their sexual orientation.
    - `4`: Misogynistic hate: Expressions directed against women or traits associated with them.
    - `5`: Xenophonous hatred: Expressions directed against people or groups, due to their origin (e.g. foreigner and immigrant).

The process of creating this algorithm is explained in the technical report located at:XXXX

Authors:
- Elias Said-Hung
- Julio Montero-Díaz
- Oscar De Gregorio
- Almudena Ruiz
- Xiomara Blanco
- Juan José Cubillas
- Daniel Pérez Palau

Funded by:
MCIN/AEI/10.13039/501100011033

How to cites: Pérez Palau, D., Blanco Valencia, X., Ruiz-Iniesta, A., De Gregorio Vicente, O., José Cubillas, J., Said-Hung, E. and Montero-Diaz, J. (2023). Algoritmo de clasificación de expresiones de odio por tipos en español [Algorithm for classifying hate expressions by types in Spanish]. https://doi.org/10.6084/m9.figshare.25892815.v1.

More information:

- https://www.hatemedia.es/ or contact: elias.said@unir.net
- This algorithm is related to the hate/non-hate classification algorithm, also developed by the authors: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish
- This algorithm is related to the algorithm for classifying hate expressions by intensities in Spanish, also developed by the authors: https://github.com/esaidh266/Algorithm-for-classifying-hate-expressions-by-intensities-in-Spanish




