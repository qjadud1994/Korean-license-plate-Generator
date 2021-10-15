import os, random
import cv2, argparse
import numpy as np

edf random_bright(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    img = np.array(img, dtype=np.float64)
    random_bright = .5 + np.random.uniform()
    img[:, :, 2] = img[:, :, 2] * random_bright
    img[:, :, 2][img[:, :, 2] > 255] = 255
    img = np.array(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    return img

class ImageGenerator:
    def __init__(self, save_path):
        self.save_path = save_path
        # Plate
        self.plate = cv2.imread("plate.jpg")
        self.plate2 = cv2.imread("plate_y.jpg")
        self.plate3 = cv2.imread("plate_g.jpg")
        self.plate4 = cv2.imread("plate_e.jpg")

        # loading Number
        file_path = "./num/"
        file_list = os.listdir(file_path)
        self.Number = list()
        self.number_list = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Number.append(img)
            self.number_list.append(file[0:-4])

        # loading Char
        file_path = "./char1/"
        file_list = os.listdir(file_path)
        self.char_list = list()
        self.Char1 = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Char1.append(img)
            self.char_list.append(file[0:-4])

        # loading Number ====================  blue-one-line  ==========================
        file_path = "./num_e/"
        file_list = os.listdir(file_path)
        self.Number_e = list()
        self.number_list_e = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Number_e.append(img)
            self.number_list_e.append(file[0:-4])

        # loading Char
        file_path = "./char1_e/"
        file_list = os.listdir(file_path)
        self.char_list_e = list()
        self.Char1_e = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Char1_e.append(img)
            self.char_list_e.append(file[0:-4])
        # =========================================================================

        # loading Number ====================  yellow-two-line  ==========================
        file_path = "./num_y/"
        file_list = os.listdir(file_path)
        self.Number_y = list()
        self.number_list_y = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Number_y.append(img)
            self.number_list_y.append(file[0:-4])

        # loading Char
        file_path = "./char1_y/"
        file_list = os.listdir(file_path)
        self.char_list_y = list()
        self.Char1_y = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Char1_y.append(img)
            self.char_list_y.append(file[0:-4])

        # loading Resion
        file_path = "./region_y/"
        file_list = os.listdir(file_path)
        self.Resion_y = list()
        self.resion_list_y = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Resion_y.append(img)
            self.resion_list_y.append(file[0:-4])
        #=========================================================================

        # loading Number ====================  green-two-line  ==========================
        file_path = "./num_g/"
        file_list = os.listdir(file_path)
        self.Number_g = list()
        self.number_list_g = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Number_g.append(img)
            self.number_list_g.append(file[0:-4])

        # loading Char
        file_path = "./char1_g/"
        file_list = os.listdir(file_path)
        self.char_list_g = list()
        self.Char1_g = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Char1_g.append(img)
            self.char_list_g.append(file[0:-4])

        # loading Resion
        file_path = "./region_g/"
        file_list = os.listdir(file_path)
        self.Resion_g = list()
        self.resion_list_g = list()
        for file in file_list:
            img_path = os.path.join(file_path, file)
            img = cv2.imread(img_path)
            self.Resion_g.append(img)
            self.resion_list_g.append(file[0:-4])
        #=========================================================================


    def Type_1(self, num, save=False):
        number = [cv2.resize(number, (56, 83)) for number in self.Number]
        char = [cv2.resize(char1, (60, 83)) for char1 in self.Char1]
        Plate = cv2.resize(self.plate, (520, 110))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate, (520, 110))
            label = "Z"
            # row -> y , col -> x
            row, col = 13, 35  # row + 83, col + 56
            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # character 3
            label += self.char_list[i%37]
            Plate[row:row + 83, col:col + 60, :] = char[i%37]
            col += (60 + 36)

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    def Type_2(self, num, save=False):
        number = [cv2.resize(number, (45, 83)) for number in self.Number]
        char = [cv2.resize(char1, (49, 70)) for char1 in self.Char1]
        Plate = cv2.resize(self.plate, (355, 155))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate, (355, 155))
            label = "Z"
            row, col = 46, 10  # row + 83, col + 56

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 3
            label += self.char_list[i%37]
            Plate[row + 12:row + 82, col + 2:col + 49 + 2, :] = char[i%37]
            col += 49 + 2

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col + 2:col + 45 + 2, :] = number[rand_int]
            col += 45 + 2

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 45, :] = number[rand_int]
            col += 45
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    def Type_3(self, num, save=False):
        number1 = [cv2.resize(number, (44, 60)) for number in self.Number_y]
        number2 = [cv2.resize(number, (64, 90)) for number in self.Number_y]
        resion = [cv2.resize(resion, (88, 60)) for resion in self.Resion_y]
        char = [cv2.resize(char1, (64, 62)) for char1 in self.Char1_y]

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate2, (336, 170))

            label = str()
            # row -> y , col -> x
            row, col = 8, 76

            # resion
            label += self.resion_list_y[i % 16]
            Plate[row:row + 60, col:col + 88, :] = resion[i % 16]
            col += 88 + 8

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]
            col += 44

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]

            row, col = 72, 8

            # character 3
            label += self.char_list_y[i % 37]
            Plate[row:row + 62, col:col + 64, :] = char[i % 37]
            col += 64

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_y[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    def Type_4(self, num, save=False):
        number1 = [cv2.resize(number, (44, 60)) for number in self.Number_g]
        number2 = [cv2.resize(number, (64, 90)) for number in self.Number_g]
        resion = [cv2.resize(resion, (88, 60)) for resion in self.Resion_g]
        char = [cv2.resize(char1, (64, 62)) for char1 in self.Char1_g]

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate3, (336, 170))

            label = str()
            # row -> y , col -> x
            row, col = 8, 76

            # resion
            label += self.resion_list_g[i % 16]
            Plate[row:row + 60, col:col + 88, :] = resion[i % 16]
            col += 88 + 8

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]
            col += 44

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 60, col:col + 44, :] = number1[rand_int]

            row, col = 72, 8

            # character 3
            label += self.char_list_g[i % 37]
            Plate[row:row + 62, col:col + 64, :] = char[i % 37]
            col += 64

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            col += 64

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 64, :] = number2[rand_int]
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    def Type_5(self, num, save=False):
        number1 = [cv2.resize(number, (60, 65)) for number in self.Number_g]
        number2 = [cv2.resize(number, (80, 90)) for number in self.Number_g]
        char = [cv2.resize(char1, (60, 65)) for char1 in self.Char1_g]

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate3, (336, 170))
            random_width, random_height = 336, 170
            label = "Z"

            # row -> y , col -> x
            row, col = 8, 78

            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 65, col:col + 60, :] = number1[rand_int]
            col += 60

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 65, col:col + 60, :] = number1[rand_int]
            col += 60

            # character 3
            label += self.char_list_g[i%37]
            Plate[row:row + 65, col:col + 60, :] = char[i%37]
            row, col = 75, 8

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]
            col += 80


            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]
            col += 80

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]
            col += 80

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_g[rand_int]
            Plate[row:row + 90, col:col + 80, :] = number2[rand_int]

            Plate = random_bright(Plate)

            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
    def Type_6(self, num, save=False):
        number = [cv2.resize(number, (55, 83)) for number in self.Number]
        char = [cv2.resize(char1, (60, 83)) for char1 in self.Char1]
        Plate = cv2.resize(self.plate, (520, 110))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate, (520, 110))
         
            label = ""
            # row -> y , col -> x
            row, col = 13, 30  # row + 83, col + 56

            # number 0
            rand_int = random.randint(1, 6)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 55, :] = number[rand_int]
            col += 55
            
            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 55, :] = number[rand_int]
            col += 55

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 55, :] = number[rand_int]
            col += 55

            # character 3
            label += self.char_list[i%37]
            Plate[row:row + 83, col:col + 60, :] = char[i%37]
            col += (60 + 15)

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 55, :] = number[rand_int]
            col += 55

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 55, :] = number[rand_int]
            col += 55

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 55, :] = number[rand_int]
            col += 55

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list[rand_int]
            Plate[row:row + 83, col:col + 55, :] = number[rand_int]
            col += 55
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

    def Type_7(self, num, save=False):
        number = [cv2.resize(number_e, (56, 83)) for number_e in self.Number_e]
        char = [cv2.resize(char1_e, (60, 83)) for char1_e in self.Char1_e]
        Plate = cv2.resize(self.plate4, (520, 110))

        for i, Iter in enumerate(range(num)):
            Plate = cv2.resize(self.plate4, (520, 110))
            label = "X"
            # row -> y , col -> x
            row, col = 13, 44  # row + 83, col + 56
            # number 1
            rand_int = random.randint(0, 9)
            label += self.number_list_e[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 2
            rand_int = random.randint(0, 9)
            label += self.number_list_e[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # character 3
            label += self.char_list_e[i%37]
            Plate[row:row + 83, col:col + 60, :] = char[i%37]
            col += (60 + 36)

            # number 4
            rand_int = random.randint(0, 9)
            label += self.number_list_e[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 5
            rand_int = random.randint(0, 9)
            label += self.number_list_e[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 6
            rand_int = random.randint(0, 9)
            label += self.number_list_e[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56

            # number 7
            rand_int = random.randint(0, 9)
            label += self.number_list_e[rand_int]
            Plate[row:row + 83, col:col + 56, :] = number[rand_int]
            col += 56
            Plate = random_bright(Plate)
            if save:
                cv2.imwrite(self.save_path + label + ".jpg", Plate)
            else:
                cv2.imshow(label, Plate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--img_dir", help="save image directory",
                    type=str, default="../DB/test/")
parser.add_argument("-n", "--num", help="number of image",
                    type=int, default=50)
parser.add_argument("-s", "--save", help="save or imshow",
                    type=bool, default=True)
args = parser.parse_args()


img_dir = args.img_dir
A = ImageGenerator(img_dir)
img_dir2 = "../DB/train/"
B = ImageGenerator(img_dir2)

num_img = args.num
Save = args.save

print("test")
A.Type_1(num_img, save=Save)
print("Type 1 finish")
A.Type_2(num_img, save=Save)
print("Type 2 finish")
A.Type_3(num_img, save=Save)
print("Type 3 finish")
A.Type_4(num_img, save=Save)
print("Type 4 finish")
A.Type_5(num_img, save=Save)
print("Type 5 finish")
A.Type_6(num_img, save=Save)
print("Type 6 finish")
A.Type_7(num_img, save=Save)
print("Type 7 finish")

print("train")
B.Type_1(num_img, save=Save)
print("Type 1 finish")
B.Type_2(num_img, save=Save)
print("Type 2 finish")
B.Type_3(num_img, save=Save)
print("Type 3 finish")
B.Type_4(num_img, save=Save)
print("Type 4 finish")
B.Type_5(num_img, save=Save)
print("Type 5 finish")
B.Type_6(num_img, save=Save)
print("Type 6 finish")
B.Type_7(num_img, save=Save)
print("Type 7 finish")