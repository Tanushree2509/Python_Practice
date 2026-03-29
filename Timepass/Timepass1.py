from super_image import EdsrModel, ImageLoader
from PIL import Image

# Load your blurry/low-res image
image = Image.open('blurry_image.jpg')

# Load a pre-trained EDSR model for 2x or 4x upscaling
model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=2)

# Upscale the image
inputs = ImageLoader.load_image(image)
preds = model(inputs)

# Save the result
ImageLoader.save_image(preds, './hd_result.png')




import cv2
from cv2 import dnn_superres

# Load image
img = cv2.imread('blurry.jpg')

# Initialize SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read the model (download models like ESRGAN_x4.pb first)
model_path = "ESRGAN_x4.pb"
sr.readModel(model_path)
sr.setModel("esrgan", 4) # Scale 4x

# Upscale
result = sr.upsample(img)
cv2.imwrite('high_res.png', result)
