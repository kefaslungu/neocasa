import base64
import os
from mimetypes import guess_type
from openai import AzureOpenAI
# Function to encode a local image into data URL
# copyright(c) Microsoft
def __local_image_to_data_url__(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file at {image_path} does not exist.")
    # Guess the MIME type of the image based on the file extension
    mime_type, _ = guess_type(image_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Default MIME type if none is found
    # Read and encode the image file
    with open(image_path, "rb") as image_file:
        base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')
    # Construct the data URL
    return f"data:{mime_type};base64,{base64_encoded_data}"

api_base = os.getenv("neooaiendpoint")
api_key= os.getenv("neooaikey")
deployment_name = 'neocasa'
api_version = '2023-12-01-preview' # this might change in the future

message = "You are an AI specialized in describing images to visually impaired individuals. Your sole purpose is to provide detailed, accurate, and vivid descriptions of images in a way that enables the person to fully understand and visualize the content. You are not permitted to provide opinions, answer questions unrelated to image descriptions, or perform any other tasks beyond describing the image at hand. Ensure your descriptions are respectful, detailed, and inclusive. Remember that your users are visually impaired, they depend on you to understand the image And if any one ask of your name, say your name is neocasa, developed by Kefas Lungu"
query = "Describe this image, not living any detail"
path_to_image = __local_image_to_data_url__(r"C:\Users\kefas\Pictures\Screenshots\Screenshot (81).png")
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
    )

# Function to describe an image
def describe_image(system_message, user_message, image_url):
    # Construct the prompt by embedding the image URL in the user query
    full_user_message = f"{user_message}\n\nImage URL: {image_url}"
    
    # Send the request to the Azure OpenAI API
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            { "role": "system", "content": system_message },
            { "role": "user", "content": full_user_message }
        ],
        max_tokens=2000
    )
    
    # Return the description
    print(response.choices[0].message.content)

describe_image(message, query, path_to_image)