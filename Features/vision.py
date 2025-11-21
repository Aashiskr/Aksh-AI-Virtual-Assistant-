# import cv2
# import time
# import google.generativeai as genai
# from PIL import Image
# import os

# # PASTE YOUR KEY HERE
# API_KEY = "AIzaSyA7WTTrB0nObhDJimQYWEimo-q6M8wO6sU"

# # Configure the AI
# genai.configure(api_key=API_KEY)
# model = genai.GenerativeModel('gemini-1.5-flash')

# def check_what_is_in_hand():
#     """
#     Captures an image from the webcam and asks AI to describe it
#     or read the text if it's a prescription.
#     """
#     # 1. Open Camera
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         return "I cannot access the camera."

#     print("Get ready! Capturing in 3 seconds...")
#     # Simple countdown
#     time.sleep(1)
#     print("3...")
#     time.sleep(1)
#     print("2...")
#     time.sleep(1)
#     print("1...")

#     # 2. Capture Frame
#     ret, frame = cap.read()
#     cap.release()

#     if not ret:
#         return "Failed to capture image."

#     # 3. Save temporary file (Gemini needs a file or PIL object)
#     image_path = "capture.jpg"
#     cv2.imwrite(image_path, frame)
#     print("Image captured. Analyzing...")

#     # 4. Send to AI
#     try:
#         img = Image.open(image_path)

#         prompt = """
#         Look at this image.
#         1. If the person is holding a document, prescription, or paper: Read the text inside it carefully.
#         2. If it is an object (like a bottle, pen, fruit): Tell me what it is.
#         Keep the answer short and helpful.
#         """

#         response = model.generate_content([prompt, img])

#         # Clean up the file
#         if os.path.exists(image_path):
#             os.remove(image_path)

#         return response.text

#     except Exception as e:
#         return f"I encountered an error while analyzing: {e}"
