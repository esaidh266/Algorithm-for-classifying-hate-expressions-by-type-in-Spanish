# Algorithm-for-classifying-hate-expressions-by-type-in-Spanish
Algoritmo de clasificación de expresiones de odio por tipos en español. Este algoritmo fue desarrollado en el marco del proyecto Hatemedia (PID2020-114584GB-I00), financiado por MCIN/AEI /10.13039/501100011033, con la colaboración de Possible Inc.

Por favor lea el documento README IN SPANISH, en el que se expone todos los pasos a seguir para el uso del algoritmo desarrollado en el marco del proyecto Hatemedia (PID2020-114584GB-I00), financiado por MCIN/ AEI /10.13039/501100011033

El algoritmo permite la clasificación de expresiones de odio, de acuerdo a 5 tipos de odio: 

- Odio general o indiferenciado: Expresiones de odio, sin un claro dominio de uno de los tipos específicos considerados en este monitor.
- Odio político: Expresiones contra individuos o colectivos por motivos de orientación política. 
- Odio Sexual: Expresiones dirigidas contra personas o colectivos por su orientación sexual.
- Odio misógino: Expresiones dirgidas contra mujeres o rasgos asociados a ellas.
- Odio xenófobo. Expresiones dirigidas contra personas o colectivos, por motivo de origen (e.j. extranjero e inmigrante)

La estructura de carpetas con la documentación de Github es la presentada a continuación:

        02 Documentación Github
         └── 02_Tipos
             ├── hate_type_model
             │   ├── config.json
	     │	 └── pytorch_mode.bin (https://acortar.link/rbCxiy)
             ├── DOCUMENTACIÓN GITHUB.docx
             └── ejemplo.py

Se detalla a continuación el contenido de cada fichero:

- DOCUMENTACIÓN GITHUB.docx: Informe en el que se presenta el uso de los scripts ejemplo (1).py y obtener_caracteristicas (1).py para emplear los modelos.

- ejemplo (1).py: Script Python que muestra el uso de los modelos para realizar predicciones.

- hate_type_model: En esta carpeta encontramos los archivos necesarios para la construcción del modelo:
  - config.json: Archivo JSON con la configuración del modelo entrenado.
  - pytorch_model.bin: Este archivo contiene los pesos de la red neuronal del modelo en formato binario compatible con PyTorch. Este archivo debe descargarse desde https://acortar.link/rbCxiy y pegarse en la carpeta hate_type_model.

El dataset que se ha utilizado para el entrenamiento de los modelos:
- Said-Hung, Elias; Montero-Diaz, julio; Blanco, Xiomara; Ruiz-Iniesta, Almudena; Pérez Palau, Daniel; De Gregorio Vicente, Oscar; et al. (2024). Dataset usado para entrenamientos de modelos de algoritmos de clasificación de odio, por tipos e intensidades (Dataset used to train hate classification algorithm models by types and intensities). figshare. Dataset. https://doi.org/10.6084/m9.figshare.26085700.v1

El Algoritmo fue desarrollado a partir de las pruebas de los modelos aplicados que se muestran en la carpeta MODELOS (https://acortar.link/d8WQ0P). En esta carpeta se encuentran todos los resultados de los modelos utilizados durante el proceso de desarrollo de este algoritmo, con los respectivos porcentajes de entrenamiento y prueba.

El procedimiento seguido para entrenar los modelos queda reflejado en el Informe técnico Desarrollo del algoritmo de clasificación del odio por tipos en medios digitales españoles en X (Twitter), Facebook y portales web (https://doi.org/10.6084/m9.figshare.26314360.v1).

Autores: 
- Daniel Pérez Palau
- Xiomara Blanco
- Almudena Ruiz
- Oscar De Gregorio
- Juan José Cubillas
- Elias Said-Hung
- Julio Montero-Díaz
  
Financiado por: 
Agencia Estatal de Investigación – Ministerio de Ciencia e Innovación

Con el apoyo de:
- POSSIBLE S.L.

Como citar: Pérez Palau, D., Blanco Valencia, X., Ruiz-Iniesta, A., De Gregorio Vicente, O., José Cubillas, J., Said-Hung, E. y Montero-Diaz, J. (2023). Algoritmo de clasificación de expresiones de odio por tipos en español [Algorithm for classifying hate expressions by type in Spanish]. https://doi.org/10.6084/m9.figshare.25892815.v1.

Más información:
- https://www.hatemedia.es/ o contactar con:  elias.said@unir.net
- Este algoritmo está relacionado con el algoritmo de clasificación de odio/no odio, desarrollado también por los autores: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish
- Este algoritmo está relacionado con el algoritmo de clasificación de expresiones de odio por intensidades en español, desarrollado también por los autores: https://github.com/esaidh266/Algorithm-for-classifying-hate-expressions-by-intensities-in-Spanish
  
---

Algorithm for classifying hate expressions by types in Spanish. This algorithm was developed within the framework of the Hatemedia project (PID2020-114584GB-I00), funded by MCIN/AEI/10.13039/501100011033, with the collaboration of Possible Inc.

Please read README IN SPANISH, which outlines all the steps to follow to use the algorithm developed within the framework of the Hatemedia project (PID2020-114584GB-I00), funded by MCIN/AEI/10.13039/501100011033

The algorithm allows the classification of hate expressions according to 5 types of hate: 

- General or undifferentiated hatred: Expressions of hate without a clear predominance of any specific types considered in this monitor.
- Political hatred: Expressions against people or groups for political orientation. 
- Sexual Hate: Expressions directed against people or groups because of their sexual orientation.
- Misogynistic hatred: Expressions directed against women or traits associated with them.
- Xenophobic Hate. Expressions directed against people or groups due to their origin (e.g. foreigners and immigrants)

The folder structure with the GitHub documentation is presented below:

        02 Documentación Github
         └── 02_Tipos
             ├── hate_type_model
             │   ├── config.json
	     │	 └── pytorch_mode.bin (https://acortar.link/rbCxiy)
             ├── DOCUMENTACIÓN GITHUB.docx
             └── ejemplo.py

The content of each file is detailed below:

- DOCUMENTACIÓN GITHUB.docx: Report that presents the example of the script (1).py and get_characteristics (1).py to use the models.

- ejemplo (1).py: Python script showing the use of models to make predictions.

- hate_type_model: In this folder, we find the files necessary to build the model:
   - config.json: JSON file with the configuration of the trained model.
   - pytorch_model.bin: This file contains the model's neural network weights in PyTorch-compatible binary format. This file should be downloaded from https://acortar.link/rbCxiy and pasted into the hate_type_model folder.

The dataset that has been used to build this library:
- Said-Hung, Elias; Montero-Diaz, julio; Blanco, Xiomara; Ruiz-Iniesta, Almudena; Pérez Palau, Daniel; De Gregorio Vicente, Oscar; et al. (2024). Dataset usado para entrenamientos de modelos de algoritmos de clasificación de odio, por tipos e intensidades (Dataset used to train hate classification algorithm models by types and intensities). figshare. Dataset. https://doi.org/10.6084/m9.figshare.26085700.v1

Results and comparisons generated during the training and validation process of the final model used for the development of the algorithm are shared in the MODELOS folder (https://acortar.link/d8WQ0P). This folder contains all the results of the models used during the algorithm's development process, with the respective training and testing.

The procedure followed to train the models is reflected in the technical report: The development of the hate classification algorithm by type in Spanish digital media in X (Twitter), Facebook, and web portals (https://doi.org/10.6084/m9.figshare.26314360.v1).

Authors:
- Daniel Pérez Palau
- Xiomara Blanco
- Almudena Ruiz
- Oscar De Gregorio
- Juan José Cubillas
- Elias Said-Hung
- Julio Montero-Díaz

Funded by:
State Research Agency – Ministry of Science and Innovation

With the support of:
- POSSIBLE S.L.

How to cites: Pérez Palau, D., Blanco Valencia, X., Ruiz-Iniesta, A., De Gregorio Vicente, O., José Cubillas, J., Said-Hung, E. and Montero-Diaz, J. (2023). Algoritmo de clasificación de expresiones de odio por tipos en español [Algorithm for classifying hate expressions by types in Spanish]. https://doi.org/10.6084/m9.figshare.25892815.v1.

More information:
- https://www.hatemedia.es/ or contact: elias.said@unir.net
- This algorithm is related to the hate/non-hate classification algorithm, also developed by the authors: https://github.com/esaidh266/Algorithm-for-detection-of-hate-speech-in-Spanish
- This algorithm is related to the algorithm for classifying hate expressions by intensities in Spanish, also developed by the authors: https://github.com/esaidh266/Algorithm-for-classifying-hate-expressions-by-intensities-in-Spanish
