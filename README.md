# Korean-license-plate-Generator

Generate Synthetic Korea License Plate.

- You can use this generator when there is insufficient data on the license plate.

- This image generator may be used in a [character recognition model like 'CRNN'](https://github.com/qjadud1994/CRNN-Keras.git)

- I recommend pre-training with synthetic images and fine-tune with real data.

## Types of Korean license plates

- You can create synthetic license plate pictures by selecting the plate of the desired type.

![Type of license plate](https://github.com/qjadud1994/CRNN-Keras/blob/master/photo/license%20plate.jpg)




## Labeling

- The name of the photo shows the letters and numbers on the license plate.

- Hangul in the plate was translated into English with the following rules.

- Region : 서울 -> A, 인천 -> B ... <br/>
- Hangul : 나 -> sk, 너 -> sj, 다 -> ek, 도 -> eh ... <br/>


## File Description

- os : Ubuntu 16.04.4 LTS
- Python : 3.5.2


|       File         |Description                                       |
|--------------------|--------------------------------------------------|
|Generator_original.py           |  generate images without any image distortion/augmentation.     |
|Generator_augmentation.py       |  generate images with image augmentations such as random brightness.   |
|Generator_perspective.py |   generate images with perspective transform.     |
