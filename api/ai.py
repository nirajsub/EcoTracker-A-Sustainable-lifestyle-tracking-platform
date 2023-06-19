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

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc, service_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

YOUR_CLARIFAI_API_KEY = "1024f3c9ba6545b0bd868f54f7952504"
YOUR_MODEL_ID = "my-first-application-00l6ao"

def classify_image(image_url):
    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    request = service_pb2.PostModelOutputsRequest(
        model_id=YOUR_MODEL_ID,
        inputs=[
            service_pb2.Input(data=service_pb2.Data(image=service_pb2.Image(url=image_url)))
        ],
    )

    metadata = (("authorization", f"Key {YOUR_CLARIFAI_API_KEY}"),)
    response = stub.PostModelOutputs(request, metadata=metadata)

    if response.status.code != status_code_pb2.SUCCESS:
        print(response)
        raise Exception(f"Request failed, status code: {response.status}")

    predicted_labels = [
        concept.name for concept in response.outputs[0].data.concepts
    ]

    return predicted_labels
