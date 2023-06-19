# import openai
# openai.api_key = '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'
# def classify_image(image_path):
#     # Read the image file
#     with open(image_path, 'rb') as f:
#         image_data = f.read()
#     # Call the OpenAI API for image classification
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt="Is this item recyclable, garbage, or compostable?\n\nImage:",
#         examples=[
#             ["Recyclable", "This item is recyclable."],
#             ["Garbage", "This item is garbage."],
#             ["Compost", "This item is compostable."],
#         ],
#         documents=[image_data.decode("latin1")],
#         max_tokens=5,
#         n=1,
#         stop=None,
#     )
#     # Retrieve the predicted label from the API response
#     predicted_label = response.choices[0].text.strip()
#     return predicted_label
# 1024f3c9ba6545b0bd868f54f7952504

from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.grpc.api import service_pb2_grpc, service_pb2
from clarifai.rest import Image as ClImage, ClarifaiApp

app = ClarifaiApp(api_key='1024f3c9ba6545b0bd868f54f7952504')

def classify_image(image_path):
    image = ClImage(file_obj=open(image_path, 'rb'))
    model = app.public_models.general_model
    response = model.predict([image])
    predictions = response['outputs'][0]['data']['concepts']
    predicted_labels = [prediction['name'] for prediction in predictions]

    return predicted_labels
