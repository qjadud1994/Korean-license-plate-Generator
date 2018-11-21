# Korea-license-plate-Generator

Generate Synthetic Korea License Plate

## license plate recognition using CRNN

I used CRNN to recognize license plates in Korea.

![Type of license plate](https://github.com/qjadud1994/CRNN-Keras/blob/master/photo/license%20plate.jpg)

I learned the following kinds of Korean license plates.


### How to Training

First, you need a lot of cropped license plate images. <br/>
And in my case I expressed the number of the license plate with the image file name. <br/>
(The license plate number 1234 is indicated as "1234.jpg"). <br/>
(You can also define labeling with txt or csv files if you want. [(ex)0001.jpg "1234" \n 0002.jpg "0000" ...)

Since I used Korean license plates, I expressed the Korean language on the license plate in English.

![Example](https://github.com/qjadud1994/CRNN-Keras/blob/master/DB/train/A18sk6897.jpg)
<br/>
(exmaple) A18sk6897 <br/>
A : 서울 <br/>
sk : 나 <br/>

After creating training data in this way, put it in 'DB/train' directory and run [training.py](https://github.com/qjadud1994/CRNN-Keras/blob/master/training.py).

## File Description

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
