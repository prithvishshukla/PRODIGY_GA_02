# Install required libraries (uncomment and run if needed)
# !pip install diffusers torch pillow ipython

# Import necessary libraries
from diffusers import StableDiffusionPipeline  # For loading the Stable Diffusion model pipeline
import torch                                   # For checking GPU availability
from PIL import Image                          # For image processing and saving
from IPython.display import display            # For displaying images in Jupyter notebooks

# Specify the model ID for Stable Diffusion
model_id = "CompVis/stable-diffusion-v1-4"

# Select device: use GPU if available, otherwise fallback to CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Stable Diffusion pipeline from the pretrained model
pipe = StableDiffusionPipeline.from_pretrained(model_id)

# Move the pipeline to the selected device (GPU or CPU)
pipe = pipe.to(device)

# Define the text prompt for image generation
prompt = "indian celebrating festival with Holi colors, vibrant atmosphere, joyful expressions, traditional attire"

# Generate an image based on the prompt
image = pipe(prompt).images[0]

# Save the generated image to a file
image.save("generated_image.png")

# Display the generated image (works in Jupyter notebooks)
display(image)
