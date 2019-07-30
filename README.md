# qualtrics-creator
This script can help you generate a text file to generate Qualtrics questions given a list of videos.

See the Import Survey Functions of Qualtrics to see how you can create surveys using text files: https://www.qualtrics.com/support/edit-survey/survey-tools/general-tools/import-and-export-surveys/#PreparingAnAdvancedFormatTXTFile

# Instructions
1. Create a list of video links in `videos.txt` (note: videos must be served from a publicly accessible server)
2. Run `python generate_qualtrics.py >> survey.txt`
3. Use the Qualtrics import survey tool to import the text file.

