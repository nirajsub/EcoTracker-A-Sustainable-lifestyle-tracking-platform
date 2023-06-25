import openai
openai.api_key = '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'
def classify_image(image_path):
    # Read the image file
    with open(image_path, 'rb') as f:
        image_data = f.read()
    # Call the OpenAI API for image classification
    response = openai.Completion.create(
        engine="davinci",
        prompt="Is this item recyclable, garbage, or compostable?\n\nImage:",
        examples=[
            ["Recyclable", "This item is recyclable."],
            ["Garbage", "This item is garbage."],
            ["Compost", "This item is compostable."],
        ],
        documents=[image_data.decode("latin1")],
        max_tokens=5,
        n=1,
        stop=None,
    )
    # Retrieve the predicted label from the API response
    predicted_label = response.choices[0].text.strip()
    return predicted_label
  