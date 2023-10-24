<img src="https://i.ibb.co/1XYjgQy/compymaker.png" alt="compymaker" style="margin-left: auto; margin-right: auto; display: block;">


# Installation
Run this in terminal:
`git clone https://github.com/qvthc/compymaker`

# Guide
## 1. Load your YouTube URLs
To get started, open the **./assets/links.txt** text file, and enter your YouTube Shorts links separated with a newline. Example:
```
https://youtube.com/shorts/mylink
https://youtube.com/shorts/mylink2
https://youtube.com/shorts/mylink3
```

## 2. Download the videos
After loading in your YouTube URLs to the text file, go back to the root directory and run this command:
`python Step1.py`
This will download the YouTube videos into the **./videos** folder.

## 3. Pick the random videos
Make sure you are still in the same folder. Next, run the command:
`python Step2.py`
Nice, now you have 3 random videos in the root folder that are named **video1,video2,video3**. 

## 4. Compile the videos!
Now you can run:
`python Step3.py`
To start compiling the final video. The final video should be exported as **output.mp4**. Congratulations!
You have successfully used this tool.

# Extras
## How to do everything at once
`DISCLAIMER: YOU WILL HAVE TO RUN STEP 2 AND STEP 3 SEPERATELY AFTER RUNNING THIS ONCE, SINCE DUPLICATES WOULD APPEAR.`

Simply run the following command:
`sudo python3 Automated.py`
