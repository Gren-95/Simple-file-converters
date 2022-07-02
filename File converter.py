from fileinput import filename
import os
import glob
import PIL
import os.path

print("Efe's file converters")

# Change directory/folder to your desired location
print("Current working directory: {0}".format(os.getcwd()))
print("Choose your directory.")
location = input()
os.chdir(location)

# Show options
print("\n 0) exit \n\n Picture converters \n*-----------------*\n| 1) JPG  to png  |\n| 2) PNG  to JPG  |\n| 3) JPG  to WEBP |\n| 4) WEBP to JPG  |\n| 5) PNG  to WEBP |\n| 6) WEBP to PNG  |\n*-----------------*\n\n Video converters \n*-----------------*\n| 7) WEBM to MP4  |\n*-----------------*")
answer = input("\nWhat is your choice?\n")

# Exit option
if answer == "0":
    print("exiting")
    exit()

# JPG to PNG option
elif answer == "1":
        from PIL import Image
        from os import listdir
        from os.path import splitext

# Input picture
        target_directory = '.'
        target = '.jpg'
        for file in listdir(target_directory):
            filename, extension = splitext(file)
            try:
                if extension not in ['.py', target]:
# Output picture
                    im = Image.open(filename + extension)
                    im.save(filename + target, "png")
# Progress
                    print("Completed converting - " + filename + ".jpg" + " --> " + filename + ".png")
            except OSError:
                print('Cannot convert %s' % file)

# PNG to JPG option
elif answer == "2":
        from PIL import Image
        from os import listdir
        from os.path import splitext

        target_directory = '.'
        target = '.png'
        for file in listdir(target_directory):
            filename, extension = splitext(file)
            try:
                if extension not in ['.py', target]:
                    im = Image.open(filename + extension)
                    im.save(filename + target, "png")
                    print("Completed converting - " + filename + ".png" + " --> " + filename + ".jpg")
            except OSError:
                print('Cannot convert %s' % file)

# JPG to WEBP option
elif answer == "3":
        from PIL import Image
        from os import listdir
        from os.path import splitext

        target_directory = '.'
        target = '.jpg'
        for file in listdir(target_directory):
            filename, extension = splitext(file)
            try:
                if extension not in ['.py', target]:
                    im = Image.open(filename + extension)
                    im.save(str(filename)+".webp", "webp")
                    print("Completed converting - " + filename + ".jpg" + " --> " + filename + ".webp")
            except OSError:
                print('Cannot convert %s' % file)

# WEBP to JPG option
elif answer == "4":
        from PIL import Image
        from os import listdir
        from os.path import splitext

        target_directory = '.'
        target = '.webp'
        for file in listdir(target_directory):
            filename, extension = splitext(file)
            try:
                if extension not in ['.py', target]:
                    im = Image.open(filename + extension)
                    im.save(str(filename)+".jpg", "jpeg")
                    print("Completed converting - " + filename + ".webp" + " --> " + filename + ".jpg")
            except OSError:
                print('Cannot convert %s' % file)

# PNG to WEBP option
elif answer == "5":
        from PIL import Image
        from os import listdir
        from os.path import splitext

        target_directory = '.'
        target = '.png'
        for file in listdir(target_directory):
            filename, extension = splitext(file)
            try:
                if extension not in ['.py', target]:
                    im = Image.open(filename + extension)
                    im.save(str(filename)+".webp", "webp")
                    print("Completed converting - " + filename + ".png" + " --> " + filename + ".webp")
            except OSError:
                print('Cannot convert %s' % file)

# WEBP to PNG option
elif answer == "6":
        from PIL import Image
        from os import listdir
        from os.path import splitext

        target_directory = '.'
        target = '.webp'
        for file in listdir(target_directory):
            filename, extension = splitext(file)
            try:
                if extension not in ['.py', target]:
                    im = Image.open(filename + extension)
                    im.save(str(filename)+".png", "png")
                    print("Completed converting - " + filename + ".webp" + " --> " + filename + ".png")
            except OSError:
                print('Cannot convert %s' % file)

# WEBM to MP4 option
elif answer == "7":
	from os import path
	#parallel = print("Parallel installed: " + str(path.exists('/usr/bin/parallel')))
	if str(path.exists('/usr/bin/parallel')) == "True":
		os.system('parallel ffmpeg -i {} {.}.mp4 ::: *.webm')
		print("done")
	else:
		print("Please install GNU Parallel")
else:
	print("invalid option")
