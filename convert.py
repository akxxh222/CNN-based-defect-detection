from tensorflow.keras.models import load_model

model = load_model("casting_defect_cnn.h5")
model.save("casting_defect_cnn.keras")

print("Model converted to .keras format successfully")
