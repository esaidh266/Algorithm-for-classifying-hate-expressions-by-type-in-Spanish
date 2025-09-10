# Modelo de Clasificación de Tipos de Discurso de Odio

Este código implementa un sistema de clasificación de tipos de discurso de odio utilizando el modelo RoBERTuito (una versión en español de RoBERTa) para detectar y categorizar diferentes tipos de discurso de odio en textos.

## Arquitectura del Modelo

El modelo se basa en `pysentimiento/robertuito-base-uncased` con las siguientes modificaciones:
- Se añadió una capa de clasificación densa sobre el modelo base
- Utiliza IDs de entrada y máscaras de atención como entradas
- Genera una clasificación multi-clase con 5 categorías de odio

## Dataset

**Conjunto de Datos HATEMEDIA**: Conjunto de datos personalizado de discurso de odio con categorización por tipos:
- **Etiquetas**: 5 categorías de tipos de odio (0-4)
- **Preprocesamiento**: 
  - Eliminación de valores nulos en texto y etiquetas
  - Reindexación y reetiquetado (las etiquetas originales se ajustan restando 1)
  - Exclusión de la categoría 2 durante el entrenamiento
  - Conversión de la categoría 5 a categoría 2

## Proceso de Entrenamiento

### Configuración
- **Batch size**: 128
- **Épocas**: 5
- **Learning rate**: 2e-5 con warmup steps del 10%
- **Early stopping** con paciencia=2
- **Pesos de clase**: Balanceados para manejar desequilibrio de clases

### Métricas Personalizadas
- Recall para clases específicas (focus en clase 2)
- Precision para clases específicas (focus en clase 3)
- F1-score (weighted)
- AUC-PR
- Recall at precision=0.6 (clase 3)
- Precision at recall=0.6 (clase 2)

## Métricas de Evaluación

El modelo se evalúa utilizando:
- Macro recall, precision, and F1-score
- One-vs-Rest AUC
- Accuracy
- Métricas por clase
- Matriz de confusión
- Classification report completo

## Características Técnicas

### Preprocesamiento de Datos
- **Tokenización**: Máxima longitud de 128 tokens (truncamiento y padding)
- **Codificación de etiquetas**: One-hot encoding para clasificación multi-clase
- **División de datos**: 80% entrenamiento, 10% validación, 10% prueba

### Optimización
- **Optimizador**: Adam con schedule de warmup lineal
- **Función de pérdida**: Categorical Crossentropy (from_logits=True)
- **Manejo de desbalance**: Class weights computados automáticamente

## Requerimientos

Se requieren los siguientes paquetes de Python:
- TensorFlow
- Transformers
- scikit-learn
- pandas
- datasets
- matplotlib
- seaborn
- numpy

## Uso

1. **Formato de datos**:
- Archivo CSV o DataFrame de Pandas
- Nombre de columna obligatorio: `text` (tipo cadena)
  - Nombre de columna obligatorio: Etiqueta de tipo de odio (tipo entero, 0-4) - ppcional para evaluación

2. **Preprocesamiento de texto**:
- Tokenización automática con longitud máxima de 128 tokens
- Los textos largos se truncarán automáticamente
- Manejo de caracteres especiales, URLs y emojis incluido

3. **Codificación de etiquetas**:
- El modelo clasifica en 5 categorías de tipos de discurso de odio (0-4)
    -   `0`: Odio político: Expresiones contra individuos o colectivos por motivos de orientación política.
    -   `1`: Odio general o indiferenciado: Expresiones de odio, sin un claro dominio de uno de los tipos específicos considerados en este monitor, pudiendo contener en este tipo de mensajes más de un tipo de odio.
    -   `2`: Odio sexual: Expresiones dirigidas contra personas o colectivos por su orientación sexual.
    -   `3`: Odio xenófono: Expresiones dirigidas contra personas o colectivos, por motivo de origen (e.j. extranjero e inmigrante).
    -   `4`: Odio misógino: Expresiones dirigidas contra mujeres o rasgos asociados a ellas.
      
**Estructura de Archivos**

El código genera y guarda:
- Pesos del modelo entrenado (.h5)
- Tokenizer configurado
- Historial de entrenamiento en CSV
- Archivo de requirements

**Notas Importantes**

- El modelo excluye la categoría 2 durante el entrenamiento
- Implementa transfer learning desde un modelo preentrenado en detección binaria de odio
- Incluye callbacks de early stopping para prevenir overfitting
- Utiliza class weighting para manejar desbalance en las categorías
- Para hacer uso correcto de este algoritmo es necesario pasar los mensajes en los que se desean detectar expresiones de odio a través del algoritmo de clasificación de odio/no odio, desarrollado también por los autores: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish. Una vez identificados los mensajes con odio, este algoritmo clasificará estos según los tipos de odio asociados a este desarrollo.

El proceso de creación de este algoritmo se expone en el informe técnico localizado en: Blanco-Valencia, X., De Gregorio-Vicente, O., Ruiz Iniesta, A., & Said-Hung, E. (2025). Algoritmos de detección de odio/no odio, tipo e intensidad – Hatemedia V.2.0 (Version 2). Hatemedia Project. https://doi.org/10.5281/zenodo.16996080

Autores: 
- Daniel Pérez Palau
- Xiomara Blanco
- Almudena Ruiz
- Oscar De Gregorio
- Juan José Cubillas
- Elias Said-Hung
- Julio Montero-Díaz 

Financiado por: 
MCIN/AEI /10.13039/501100011033

Como citar: Pérez Palau, D., Blanco Valencia, X., Ruiz-Iniesta, A., De Gregorio Vicente, O., José Cubillas, J., Said-Hung, E. y Montero-Diaz, J. (2023). Algoritmo de clasificación de expresiones de odio por tipos en español [Algorithm for classifying hate expressions by type in Spanish]. https://doi.org/10.6084/m9.figshare.25669038.

Más información:

- https://www.hatemedia.es/ o contactar con:  elias.said@unir.net
- Este algoritmo está relacionado con el algoritmo de clasificación de odio/no odio, desarrollado también por los autores: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish
- Este algoritmo está relacionado con el algoritmo de clasificación de expresiones de odio por intensidades en español, desarrollado también por los autores: https://github.com/esaidh266/Algorithm-for-classifying-hate-expressions-by-intensities-in-Spanish

---------

# Hate Speech Type Classification Model

This code implements a hate speech type classification system using the RoBERTuito model (a Spanish version of RoBERTa) to detect and categorize different types of hate speech in texts.

## Model Architecture

The model is based on `pysentimiento/robertuito-base-uncased` with the following modifications:
- A dense classification layer was added over the base model
- Uses input IDs and attention masks as inputs
- Generates a multi-class classification with 5 hate categories

## Dataset

**HATEMEDIA Dataset**: Custom hate speech dataset with categorization by type:
- **Labels**: 5 hate type categories (0-4)
- **Preprocessing**:
- Null values ​​removed from text and labels
- Reindexing and relabeling (original labels are adjusted by subtracting 1)
- Exclusion of category 2 during training
- Conversion of category 5 to category 2

## Training Process

### Configuration
- **Batch size**: 128
- **Epoches**: 5
- **Learning rate**: 2e-5 with 10% warmup steps
- **Early stopping** with patience=2
- **Class weights**: Balanced to handle class imbalance

### Custom Metrics
- Recall for specific classes (focus on class 2)
- Precision for specific classes (focus on class 3)
- F1-score (weighted)
- AUC-PR
- Recall at precision=0.6 (class 3)
- Precision at recall=0.6 (class 2)

## Evaluation Metrics

The model is evaluated using:
- Macro recall, precision, and F1-score
- One-vs-Rest AUC
- Accuracy
- Per-class metrics
- Confusion matrix
- Full classification report

## Technical Features

### Data Preprocessing
- **Tokenization**: Maximum length of 128 tokens (truncation and padding)
- **Encoding of labels**: One-hot encoding for multi-class classification
- **Data split**: 80% training, 10% validation, 10% testing

### Optimization
- **Optimizer**: Adam with linear warmup scheduling
- **Loss function**: Categorical Crossentropy (from_logits=True)
- **Imbalance handling**: Class weights computed automatically

## Requirements

The following Python packages are required:
- TensorFlow
- Transformers
- scikit-learn
- pandas
- datasets
- matplotlib
- seaborn
- numpy

## Usage

1. **Data format**:
- CSV file or Pandas DataFrame
- Required column name: `text` (string type)
- Required column name: Data type label (integer type, 0-4) - optional for evaluation

2. **Text preprocessing**:
- Automatic tokenization with a maximum length of 128 tokens
- Long texts will be automatically truncated
- Handling of special characters, URLs, and emojis included

3. **Label encoding**:
- The model classifies hate speech into 5 categories (0-4)
- `0`: Political hatred: Expressions directed against individuals or groups based on political orientation.
- `1`: General or undifferentiated hatred: Expressions of hatred without a clear dominance of one of the specific types considered in this monitor, and these types of messages may contain more than one type of hatred.
- `2`: Sexual hatred: Expressions directed against individuals or groups based on their sexual orientation.
- `3`: Xenophonic hatred: Expressions directed against individuals or groups based on their origin (e.g., foreigners and immigrants).
- `4`: Misogynistic hate: Expressions directed against women or traits associated with them.

**File Structure**

The code generates and saves:
- Weights of the trained model (.h5)
- Configured tokenizer
- Training history in CSV
- Requirements file

**Important Notes**

- The model excludes category 2 during training
- Implements transfer learning from a pre-trained model for binary hate detection
- Includes early stopping callbacks to prevent overfitting
- Uses class weighting to handle category imbalances
- To correctly use this algorithm, you must pass the messages in which you want to detect hate speech through the hate/non-hate classification algorithm, also developed by the authors: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish. Once the hate messages are identified, this algorithm will classify them according to the types of hate associated with this development.

The process of creating this algorithm is explained in the technical report located at: Blanco-Valencia, X., De Gregorio-Vicente, O., Ruiz Iniesta, A., & Said-Hung, E. (2025). Algoritmos de detección de odio/no odio, tipo e intensidad – Hatemedia V.2.0 (Version 2). Hatemedia Project. https://doi.org/10.5281/zenodo.16996080

Authors:
- Daniel Pérez Palau
- Xiomara Blanco
- Almudena Ruiz
- Oscar De Gregorio
- Juan José Cubillas
- Elias Said-Hung
- Julio Montero-Díaz 

Funded by:
MCIN/AEI/10.13039/501100011033

How to cites: Pérez Palau, D., Blanco Valencia, X., Ruiz-Iniesta, A., De Gregorio Vicente, O., José Cubillas, J., Said-Hung, E. and Montero-Diaz, J. (2023). Algoritmo de clasificación de expresiones de odio por tipos en español [Algorithm for classifying hate expressions by types in Spanish]. https://doi.org/10.6084/m9.figshare.25669038.

More information:

- https://www.hatemedia.es/ or contact: elias.said@unir.net
- This algorithm is related to the hate/non-hate classification algorithm, also developed by the authors: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish
- This algorithm is related to the algorithm for classifying hate expressions by intensities in Spanish, also developed by the authors: https://github.com/esaidh266/Algorithm-for-classifying-hate-expressions-by-intensities-in-Spanish


