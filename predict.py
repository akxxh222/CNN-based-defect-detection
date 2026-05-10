import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# -----------------------------
# Load trained model
# -----------------------------
model = tf.keras.models.load_model("casting_defect_cnn.keras")

# -----------------------------
# Image path (PERFECT image 14)
# -----------------------------
img_path = "test/def_front/cast_def_0_65.jpeg"

# -----------------------------
# Preprocess image
# -----------------------------
img = image.load_img(
    img_path,
    color_mode="grayscale",
    target_size=(150, 150)
)

img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)  # shape: (1,150,150,1)

# -----------------------------
# Predict
# -----------------------------
prediction = model.predict(img_array)[0][0]

# -----------------------------
# Output result
# -----------------------------
if prediction >= 0.5:
    print(f"Prediction: PERFECT (OK)")
    print(f"Confidence: {prediction:.4f}")
else:
    print(f"Prediction: DEFECTIVE")
    print(f"Confidence: {1 - prediction:.4f}")
