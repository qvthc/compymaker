# compymaker
Open-source creator for meme compilation channels. (YouTube shorts)

# Installation
Run this in terminal:
`git clone https://github.com/qvthc/compymaker`

# Guide
## 1. Load your YouTube URL's
To get started, please go to the **./assets/links.txt** text file and edit it to have short links. An example of the format is like this:

`https://youtube.com/shorts/videolink`
`https://youtube.com/shorts/videolink`
`https://youtube.com/shorts/videolink`

## 2. Download the videos
Congrats! Now what you have to do, is go back to the root folder and run the following:
`sudo python3 Step1.py`
This will download the YouTube videos into the **./videos** folder.




## 3. Pick the random videos
Make sure you are still in the same folder. Next, run the command:
`sudo python3 Step2.py`
Nice, now you have 3 random videos in the root folder that are named **video1,video2,video3**. 



## 4. Compile the videos!
Now you can run:
`sudo python3 Step3.py`
To start compiling the final video. The final video should be exported as **output.mp4**. Congratulations!
You have successfully used this tool.


# EXTRAS
## How to do everything at once
`DISCLAIMER: YOU WILL HAVE TO RUN STEP 2 AND STEP 3 SEPERATELY AFTER RUNNING THIS ONCE, SINCE DUPLICATES WOULD APPEAR.`

Simply run the following command:
`sudo python3 Automated.py`
