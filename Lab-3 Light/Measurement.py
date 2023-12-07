from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.brightness = 40

#Camera warm-up time - Отображение входных данных камеры в ральном времени
camera.start_preview()

camera.resolution = (2000, 2000) #- задание разрешения снимка
camera.contrast = 15
brightness = str(camera.brightness)
resolution = str(camera.resolution)
contrast = str(camera.contrast)
print('Яркость камеры: ' + brightness + '%')
print('Разрешение снимков камеры: ' + resolution + 'пикселей')
print('Контрастность снимков камеры: ' + contrast + ' единиц')

sleep(7)
camera.capture('/home/guest/Desktop/B03-301/red_spec.jpg')  # Take a picture - и сохранение фото

camera.stop_preview() #- остановка предварительного просмотра

#- задание контраста снимка

camera.close() #-   метод для освобождения ресурсов камеры