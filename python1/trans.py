import googletrans
from googletrans import Translator
#print('Google Trans. lang code')
#print(googletrans.LANGUAGES)
with open('sampleText.txt', 'r') as file:
    data = file.read().rstrip()
trans = Translator()
t = trans.translate(data, dest="de")
print(t)
