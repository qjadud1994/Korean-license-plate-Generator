# Korean-license-plate-Generator

Generate Synthetic Korea License Plate.

### Types of Korean license plates

![Type of license plate](https://github.com/qjadud1994/CRNN-Keras/blob/master/photo/license%20plate.jpg)

You can create synthetic license plate pictures by selecting the plate of the desired type.


### Labeling

The name of the photo shows the letters and numbers on the license plate.

Hangul in the plate was translated into English with the following rules.

Region : 서울 -> A, 인천 -> B ... <br/>
Hangul : 나 -> sk, 너 -> sj, 다 -> ek, 도 -> eh ... <br/>


### File Description

os : Ubuntu 16.04.4 LTS
Python : 3.5.2


|       File         |Description                                       |
|--------------------|--------------------------------------------------|
|Model .py           |Network using CNN (VGG) + Bidirectional LSTM      |
|Model_GRU. py       |Network using CNN (VGG) + Bidirectional GRU       |
|Image_Generator. py |Image batch generator for training                |
|parameter. py       |Parameters used in CRNN                           |
|training. py        |CRNN training                                     |
|Prediction. py      |CRNN prediction                                   |
