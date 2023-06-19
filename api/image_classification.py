from PIL import Image
import torch
from transformers import CLIPModel, CLIPTokenizer

def classify_image(image_path):
    # Load the CLIP model and tokenizer
    model = CLIPModel.from_pretrained('openai/clip-vit-base-patch32')
    tokenizer = CLIPTokenizer.from_pretrained('openai/clip-vit-base-patch32')

    # Preprocess the image and convert it to a tensor
    image = Image.open(image_path)
    image_tensor = tokenizer.images_to_tensor([image])

    # Perform image classification using the CLIP model
    with torch.no_grad():
        logits_per_image, _ = model(image_tensor)
        predicted_labels = torch.argmax(logits_per_image, dim=1)

    # Return the predicted labels
    return predicted_labels
