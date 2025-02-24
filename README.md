# discordmusicbot

YOU HAVE TO CHANGE BOT TOKEN
Discord auto detects when your token is on github and makes you reset it so I cannot put the string entirely lol 

Things to do to get this to work properly:
1)*********************************************************************
Visit the Download Page:
Open your browser and go to https://www.gyan.dev/ffmpeg/builds/.

Choose a Build:

Scroll down to the "Release Builds" section.
Click on the link for the "ffmpeg-git-full" build (this version includes all features).
Alternatively, if you prefer a stable release, look for a link labeled with a version number.
Download the ZIP File:

Click on the ZIP file link to start the download. The file will typically be named something like ffmpeg-git-full.7z or ffmpeg-<version>-full.zip.
Extract the Files:

Once the download is complete, extract the ZIP (or 7z) archive using a tool like 7-Zip or WinRAR.
Extract it to a folder, for example:
makefile
Copy
C:\ffmpeg
Inside that folder, you should see a subfolder named bin containing ffmpeg.exe and ffprobe.exe.
Add FFmpeg to Your PATH (Optional but Recommended):

Press Win + R, type sysdm.cpl, and press Enter.
Go to the Advanced tab and click Environment Variables…
Under User variables (or System variables), find and select the Path variable, then click Edit.
Click New and enter the path to the bin folder (e.g., C:\ffmpeg\bin).
Click OK to save changes and close all dialogs.
Open a new Command Prompt or VS Code terminal and run ffmpeg -version to verify that it's recognized.

2)************************************************************************
in terminal: 
pip install -U discord.py[voice] yt-dlp

3)****************************************************************************
Like with ffmpeg, Add install location of yt-dlp.exe to your PATH on Windows, follow these steps:

Open Environment Variables:

Press Win + R, type sysdm.cpl, and press Enter.
In the System Properties window, click on the Advanced tab, then click Environment Variables….
Edit Your PATH:

Under User variables (or System variables if you want it available for all users), find the variable named Path and select it.
Click Edit.
In the Edit Environment Variable window, click New and paste the path in the directory
