from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load model ONCE
model = tf.keras.models.load_model("casting_defect_cnn.keras")

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def preprocess_image(img_path):
    img = image.load_img(
        img_path,
        color_mode="grayscale",
        target_size=(150, 150)
    )
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    status_code = None
    confidence = None
    confidence_ratio = 0
    image_path = None

    if request.method == "POST":
        file = request.files["image"]

        if file and file.filename:
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(image_path)

            img = preprocess_image(image_path)
            pred = model.predict(img)[0][0]

            if pred >= 0.5:
                prediction = "PASS - OK"
                status_code = "ok"
                confidence = round(pred * 100, 2)
            else:
                prediction = "DEFECTIVE"
                status_code = "defective"
                confidence = round((1 - pred) * 100, 2)

            confidence_ratio = confidence / 100

    return render_template(
        "index.html",
        prediction=prediction,
        status_code=status_code,
        confidence=confidence,
        confidence_ratio=confidence_ratio,
        image_path=image_path
    )


if __name__ == "__main__":
    app.run(debug=True)
