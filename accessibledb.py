from gtts import gTTS
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pyqrcode

text = ""
with open("test_text.txt", "r") as file:
    for line in file:
        text = text + line

speech = gTTS(text, 'en')
speech.save("test_audio.mp3")

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

audio_upload = drive.CreateFile()
audio_upload.SetContentFile('test_audio.mp3')
audio_upload.Upload()

permission = audio_upload.InsertPermission({
    'type': 'anyone',
    'role': 'reader'})

url = pyqrcode.create(audio_upload['alternateLink'])
url.svg('qrcode.svg', scale=10)

urlfile = drive.CreateFile()
urlfile.SetContentFile('qrcode.svg')
urlfile.Upload()

print("Done!!")