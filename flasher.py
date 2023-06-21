import os
from art import *
from termcolor import colored

def detect_images(): #function to detect images in the current directory
    images = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".img"):
            images.append(file)
    return images

def flash(): #function to flash an android devices with every possible image in fastboot mode
    images = detect_images()
    print(colored("Detected images: ", "green"))
    for image in images:
        
        print(colored(image,"blue"))
    for image in images:
        
        print(colored("Flashing " + image.split(".")[0] + "...", "green"))
        os.system("fastboot flash " + image.split(".")[0] + " " + image)
        print(colored("Done!", "blue"))

def main():
    flash()

if __name__ == "__main__":
    print(colored(text2art("ULTIMATE_ANDROID_FLASHER"), "red"))
    print(colored("Pour ma Maëlle adorée", "green"))
    main()
