import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

EXAMPLE_TEXT = "texto_de_ejemplo"
MODEL_PATH = "hate_type_model"
TOKENIZER = 'pysentimiento/robertuito-base-uncased'
LABEL_MAPPING = {
        0: 'general',
        1: 'político',
        2: 'misoginia',
        3: 'xenofobia',
        4: 'sexual'
    }

def _model_prediction(model, tokenizer, text):
    # Tokenize example text
    tokens = tokenizer(text, return_tensors="pt")

    # Predict
    with torch.no_grad():
        outputs = model(**tokens)

    # Obtain each class probability
    probabilidades = torch.softmax(outputs.logits, dim=1).squeeze()

    # Obtain the higher class
    clase_predicha = torch.argmax(probabilidades).item()

    # Return prediction
    return LABEL_MAPPING[clase_predicha]


# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER)

# Predict
prediction = _model_prediction(model, tokenizer, EXAMPLE_TEXT)

# Show prediction
print(f'El comentario:\n"{EXAMPLE_TEXT}"\n\nContiene odio del tipo: {prediction}')