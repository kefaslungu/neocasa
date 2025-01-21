import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import logging
import speech
def analyze_image(image_path):
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Set up Azure credentials
    endpoint = os.getenv("neovisionendpoint")
    key = os.getenv("neovisionkey")
    if not endpoint or not key:
        logging.error("Azure endpoint or key is missing.")
        return None

    # Check if the image file exists
    if not os.path.exists(image_path):
        logging.error(f"Image file not found: {image_path}")
        return None

    # Read image data
    with open(image_path, "rb") as img_file:
        image_data = img_file.read()

    # Create the Image Analysis client
    client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    try:
        # Analyze the image
        result = client.analyze(
            image_data=image_data,
            visual_features=[
                VisualFeatures.TAGS,
                VisualFeatures.OBJECTS,
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS,
                VisualFeatures.READ,
                VisualFeatures.SMART_CROPS,
                VisualFeatures.PEOPLE,
            ],
            language="en",
        )
        parse_full_image_analysis_result_to_text(result)

    except Exception as e:
        logging.error(f"An error occurred during image analysis: {e}")
        return None

def parse_full_image_analysis_result_to_text(data):
    # Extract the main caption
    caption = data.get("captionResult", {}).get("text", "").strip()

    # Extract dense captions
    dense_captions = [
        item["text"].strip() for item in data.get("denseCaptionsResult", {}).get("values", []) if item["text"].strip()
    ]

    # Extract tags
    tags = [
        tag["name"].strip() for tag in data.get("tagsResult", {}).get("values", []) if tag["name"].strip()
    ]

    # Extract people (if identified by bounding boxes)
    people = [
        f"Person {idx + 1}" for idx, _ in enumerate(data.get("peopleResult", {}).get("values", []))
    ]

    # Extract text from OCR results
    detected_text = []
    ocr_blocks = data.get("readResult", {}).get("blocks", [])
    for block in ocr_blocks:
        for line in block.get("lines", []):
            line_text = line.get("text", "").strip()
            if line_text:
                detected_text.append(line_text)

    # Construct a clean, single-string output
    global output
    output = []

    # Add caption
    if caption:
        output.append(f"Summary: {caption}")

    # Add dense captions
    #if dense_captions:
    #observations = " ".join(dense_captions)
    #output.append(f"\nDetailed Observations: {observations}")

    # Add tags
    #if tags:
    #tags_text = ", ".join(tags)
    #output.append(f"\nTags: {tags_text}")

    # Add people
    #if people:
    #people_text = ", ".join(people)
    #output.append(f"\nPeople Detected: {people_text}")

    # Add OCR text
    if detected_text:
        text_content = " ".join(detected_text)
        output.append(f"\nText: {text_content}")

    # Join everything into one clean string
    #return " ".join(output).strip()
    image_result = " ".join(output).strip()
    speech.speak(image_result)

