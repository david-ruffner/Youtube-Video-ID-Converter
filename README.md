# Youtube-Video-ID-Converter
#### Script that takes youtube video IDs and creates a spreadsheet of video titles and their authors using the Youtube Data API.

# Instructions
---
### Setup
- You will first need Python installed on your computer (https://www.python.org/)
- Next you will need to install pip via python (https://www.makeuseof.com/tag/install-pip-for-python/)
- You will need to run the following commands in a terminal  
&nbsp;&nbsp;&nbsp;&nbsp;pip install pandas  
&nbsp;&nbsp;&nbsp;&nbsp;pip install openpyxl  
&nbsp;&nbsp;&nbsp;&nbsp;pip install xlwt  
&nbsp;&nbsp;&nbsp;&nbsp;pip install requests  
&nbsp;&nbsp;&nbsp;&nbsp;pip install beautifulsoup4  

### Google API Setup
- You will first need a Google API key. These are free and can be created in the google cloud dashboard with a free Google account (https://console.cloud.google.com/apis/dashboard, https://cloud.google.com/docs/authentication/api-keys).
- Paste the API key that you're given into the script where it says "Your Google API Key Here"

### Google Takeout
- Get a list of video ids in all of your playlists by using Google Takeout and following their instructions. This will give you a zip file with CSV files for each of your playlists. Unfortunately for some strange reason Google can't give you the titles and channel names themselves leading to the need for this script (https://takeout.google.com/settings/takeout).

### Running The Script And Notes
- The script was written to expect a CSV file of only video IDs, no other columns or headers. You may want to modify the script to suit your needs.
- Note that "./" used in the script's file path's means the directory that the script is run from. If you run the script from your documents folder, "./list.csv" would be looking for list.csv within your documents folder. This can be changed to any absolute path ("C:\Users\Me\Documents\playlist.csv") to fit your needs.
- Each API request will respond back with a JSON object. If for some reason the specific properties aren't in the response object (like if the video was removed or set to private), that row in the output file will be Title: [video id] | Channel: Invalid.
---
# Disclaimer And Legal Junk
This program comes as is with no warantee. The developer, David Ruffner, is not responsible for any damage this script may cause to your computer. If you're having trouble you can always open a bug on the github page, but to be honest I probably won't be checking it, if very little. If you understand Python it won't be too hard to debug and figure out what's going wrong. If you don't understand it this is a good way to learn :).
