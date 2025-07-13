
# Stable Diffusion Image Generator

A Python script that uses the Stable Diffusion model to generate images from text prompts.

## Features

- Text-to-image generation using Stable Diffusion v1.4
- Automatic GPU/CPU detection and usage
- Image saving and display functionality
- Optimized for Jupyter notebooks

## Requirements

Install the required libraries:

```bash
pip install transformers diffusers torch flax jax jaxlib pillow ipython
```

## Usage

1. Run the script to generate an image from the default prompt
2. The generated image will be saved as `generated_image.png`
3. In Jupyter notebooks, the image will be displayed automatically

## Customization

Modify the `prompt` variable to generate different images:

```python
prompt = "your custom text prompt here"
```

## System Requirements

- Python 3.7+
- CUDA-compatible GPU (recommended) or CPU
- Sufficient RAM/VRAM for model loading

## Output

The script generates and saves a PNG image based on the provided text prompt.
