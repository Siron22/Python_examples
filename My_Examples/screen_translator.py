from googletrans import Translator  # перевод текста через гугл-транслейт
import pyscreenshot  # захват изображения с экрана
import easyocr  # распознавание текста с изображения
from PIL import ImageGrab  # для захвата изображения из буфера обмена
import keyboard  # для захвата нажатий клавиш в фоне

########### Здесь настройка параметров утилиты ########################################
src_lang = 'en'  # исходный язык текста
dst_lang = 'ru'  # целевой язык для перевода
key_for_clipboard = 'f9'  # кнопка для перевода картинки из буфера обмена
key_for_screencapture = 'f12'  # кнопка для перевода области экрана
screen_region = (150, 850, 1400, 1000)  # область экрана, координаты границ окна захвата (Left, Top, Right, Bottom)
translator = Translator()
ocrreader = easyocr.Reader([src_lang])


def image_translate():
    """Перевод уже сохраненного изображения image_to_translate.png"""
    global ocrreader
    print('')
    # Распознавание текста на изображении
    result = ocrreader.readtext('image_to_translate.png', detail=0)
    resulttext = ' '.join(result)
    print('\033[92m' + resulttext + '\033[0m')
    # Перевод и вывод результата
    translated = translator.translate(resulttext, src=src_lang, dest=dst_lang)
    print(translated.text)


def capture_translate():
    """Скриншот и перевод"""
    try:
        screenshot = pyscreenshot.grab(bbox=screen_region)
        screenshot.save('image_to_translate.png', format='png')
        image_translate()
    except Exception:
        print('Ошибка')


def clipboard_translate():
    """Перевод изображения в буфере обмена"""
    im = ImageGrab.grabclipboard()
    if im is None:
        print('Вначале скопируйте в буфер обмена изображение')
    else:
        try:
            im.save('image_to_translate.png', 'png')
            image_translate()
        except Exception:
            print('Ошибка')


keyboard.add_hotkey(key_for_screencapture, capture_translate)
keyboard.add_hotkey(key_for_clipboard, clipboard_translate)
print(f'Для захвата области экрана нажимайте {key_for_screencapture}')
print(f'Для перевода картинки из буфера обмена нажимайте {key_for_clipboard}')
keyboard.wait()


"""
>>>>>>>>>> INSTALLATION <<<<<<<<<<
Запускаем консоль.
Выполняем команды:
chmod +x ./translator.py
sudo mkdir /usr/share/pyshared/translator
sudo cp ./translator.py /usr/share/pyshared/translator/translator.py

Создаем файл translator.desktop со следующим содержимым:

[Desktop Entry]
Type=Application
Version=1.0
Name=translator
#Icon=/usr/share/pyshared/translator/images/icon.png
Exec=/usr/share/pyshared/translator/translator.py
Terminal=false
Categories=Utilities;
Encoding=UTF-8


Выполняем команду:
sudo cp ./translator.desktop /usr/share/applications/translator.desktop
"""