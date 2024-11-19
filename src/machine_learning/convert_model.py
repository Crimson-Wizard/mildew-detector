from tensorflow.keras.models import load_model

# Load the existing model
model = load_model("/workspace/mildew-detector/outputs/v1/trained_model.h5")

# Re-save the model to ensure compatibility with TensorFlow 2.6.0
model.save("trained_model.h5", include_optimizer=False)

print("Model successfully re-saved for compatibility.")