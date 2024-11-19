from tensorflow.keras.models import load_model

model = load_model('outputs/v1/trained_model.h5')
model.save('path_to_save/saved_model', save_format='tf')
