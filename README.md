# Korean-license-plate-Generator

## Origin
- https://github.com/qjadud1994/Korean-license-plate-Generator

## Update
- electric vehicle license plate
- 8 digit license plate

Generate Synthetic Korea License Plate.

- You can use this generator when there is insufficient data on the license plate.

- This image generator may be used in a [character recognition model like 'CRNN'](https://github.com/qjadud1994/CRNN-Keras.git)

- I recommend pre-training with synthetic images and fine-tune with real data.

## Types of Korean license plates

- You can create synthetic license plate pictures by selecting the plate of the desired type.

![Type of license plate](https://github.com/qjadud1994/CRNN-Keras/blob/master/photo/license%20plate.jpg)

### Type 6

![112ah0833](https://user-images.githubusercontent.com/49277505/137438935-63c4bfde-c867-4901-b635-71498d131cc2.jpg)


### Type 7 (electric vehicle license plate)

![X63en1384](https://user-images.githubusercontent.com/49277505/137438943-4ca6024d-1189-4f0b-8acd-c481c5e965fe.jpg)

## Labeling

- The name of the photo shows the letters and numbers on the license plate.

- Hangul in the plate was translated into English with the following rules.

- Region : 서울 -> A, 인천 -> B ... <br/>
- Hangul : 나 -> sk, 너 -> sj, 다 -> ek, 도 -> eh ... <br/>

## Brightness control part
    def random_bright(img):
        img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        img = np.array(img, dtype=np.float64)
        random_bright = .5 + np.random.uniform()
        img[:, :, 2] = img[:, :, 2] * random_bright
        img[:, :, 2][img[:, :, 2] > 255] = 255
        img = np.array(img, dtype=np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
        return img


Ex)   
Type 1 : Z13wn0965   
Type 2 : Z22aj0246   
Type 3 : B16an7086   
Type 4 : A48sk2287   
Type 5 : Z19tn7921   
Type 6 : 112ah0833   
Type 7 : X50fk9747

## File Description

- os : Ubuntu 16.04.4 LTS or Windows 10
- Python : 3.5.2


|       File         |Description                                       |
|--------------------|--------------------------------------------------|
|Generator_original.py           |  generate images without any image distortion/augmentation.     |
|Generator_augmentation.py       |  generate images with image augmentations such as random brightness.   |
|Generator_perspective.py |   generate images with perspective transform.     |
