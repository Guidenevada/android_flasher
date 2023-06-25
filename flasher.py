import os
from art import *
from termcolor import colored
import time

def detect_images(): #function to detect images in the current directory
    
    if os.listdir(os.getcwd()) == "images.txt":
        images = ["1"]
        with open("images.txt", "r") as f:
            for line in f:
                images.append(line)
    else:
        images = ["0"]    
        for file in os.listdir(os.getcwd()):
            if file.endswith(".img"):
                images.append(file)
    return images

def flash(): #function to flash an android devices with every possible image in fastboot mode
    images = detect_images()
    if images[0] == "1":
        print(colored("Detected images: ", "green"))
        for image in images[1:]:

            print(colored(image,"blue"))
        for image in images:

            print(colored("Flashing " + image.split(".")[0] + "...", "blue"))
            os.system("fastboot flash " + image.split(".")[0] + " " + image)
            print(colored("Done!", "green"))
        print(colored("Ereasing storage", "blue"))
        os.system("fastboot -w")
        time.sleep(5)
        os.system("fastboot reboot")
    if images[0] == "0":
        print(colored("Using images from images.txt", "green"))
        print(colored("images ares", "blue"))
        # print every image in images.txt exept the first line
        for image in images[1:]:
            image = image.split("/")    
            print(colored(image[0]+ "in" + image[1],"blue"))
        for image in images[1:]:
            image = image.split("/")
            print(colored("Flashing " + image[0] + "...", "blue"))
            os.system("fastboot flash " + image[1] + " " + image[0])
            print(colored("Done!", "green"))

def main():
    flash()

if __name__ == "__main__":
    print(colored(text2art("ULTIMATE_ANDROID_FLASHER"), "red"))
    print(colored("Pour ma Maëlle adorée", "green"))
    main()
