import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Image settings
IMG_SIZE = (150, 150)
BATCH_SIZE = 16

# Training data generator (with augmentation)
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255.0,
    rotation_range=10,
    zoom_range=0.1,
    horizontal_flip=True
)

# Test data generator (NO augmentation)
test_datagen = ImageDataGenerator(
    rescale=1.0 / 255.0
)

# Load training data
train_generator = train_datagen.flow_from_directory(
    directory="train",
    target_size=IMG_SIZE,
    color_mode="grayscale",
    batch_size=BATCH_SIZE,
    class_mode="binary"
)

# Load test data
test_generator = test_datagen.flow_from_directory(
    directory="test",
    target_size=IMG_SIZE,
    color_mode="grayscale",
    batch_size=BATCH_SIZE,
    class_mode="binary",
    shuffle=False
)

print("Preprocessing setup completed successfully.")