import gdown
PytorchURL   = 'https://drive.google.com/uc?id=1P9r7pCc-5eTmW4krT4GZ1F6w_miTtxJA'
TfLiteURL    = 'https://drive.google.com/uc?id=1WbZD6PMETHIH6oMj0bzyG3BoDUlyO2Ll'
PytorchModel = 'model_ft.pth'
TfLiteModel  = 'model.tflite'
gdown.download(PytorchURL, PytorchModel, quiet=False)
gdown.download(TfLiteURL, TfLiteModel, quiet=False)
from distracted_driver_detection import DistractedDriverDetection_Utils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
