import sys
import os
import exifread

if len(sys.argv) == 2:
	folder_name = sys.argv[1]
	print("Entering {:s} folder...".format(folder_name))
	os.chdir(folder_name)
	print("List of all files:")
	with os.scandir() as i:
		for entry in i:
			if entry.is_file():
				extension = os.path.splitext(entry)[1][1:].strip().lower()
				if(extension == 'jpg' or extension == 'nef'):
					f = open(entry.path, 'rb')
					tags = exifread.process_file(f)
					dateTimeIm = str(tags.get('Image DateTime'))
					dateTimeEx = str(tags.get('EXIF DateTime'))
					dateTimeOrgIm = str(tags.get('Image DateTimeOriginal'))
					dateTimeOrgEx = str(tags.get('EXIF DateTimeOriginal'))
					f.close()
					if(dateTimeOrgEx is not None):
						dateTimeFinal = dateTimeOrgEx
					elif(dateTimeOrgIm is not None):
						dateTimeFinal = dateTimeOrgIm
					elif(dateTimeEx is not None):
						dateTimeFinal = dateTimeEx
					elif(dateTimeIm is not None):
						dateTimeFinal = dateTimeIm
					else:
						dateTimeFinal = None
					#print("{:s}\t\t{:s}\t{:s}\t{:s}\t{:s}".format(entry.path,dateTimeIm,dateTimeOrgIm,dateTimeEx,dateTimeOrgEx))
					if(dateTimeFinal is not None):
						dateTimeFinal = dateTimeFinal.split(' ')
						fileName = ""
						dateTimeFinalName = str(dateTimeFinal[0]).replace(":",".")+"_"+"Ula_"+fileName+"_"+dateTimeFinal[1].replace(":","")+"."+extension
						print("{:s}\t{:s}\t{:s}".format(entry.path,extension,dateTimeFinalName))
						os.rename(entry,dateTimeFinalName)
	#list_of_files = [os.path.join(folder_name,fn) for fn in next(os.walk(folder_name,".jpg"))[2]]
	#print(list_of_files)
else:
	print("Unknown number of arguments. Shall be 1.")