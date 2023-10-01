# LinuxAI
A new BASH Linux command created in python that will use chat gpt's API to allow for simple AI use in linux.
TUTORIAL FOR UBUNTU 20.04

sudo apt update
sudo apt install python

sudo nano <location>/LinuxAI/ai.py
<replace OPENAI_API_KEY = "YOUR_API_KEY_HERE" with your api key>


chmod +x ai.py


nano ~/.bashrc # or source ~/.bash_aliases
<Add this to end of file>
alias ai="<location>/LinuxAI/ai.py"


source ~/.bashrc  # or source ~/.bash_aliases if you edited that file


ai "Your Prompt Here."
