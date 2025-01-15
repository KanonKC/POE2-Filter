import os
import shutil

generalSounds = os.listdir('sounds/general')
variantSounds = [soundDir for soundDir in os.listdir('sounds') if soundDir != 'general']

filterFile = open('src/Vaal888.filter', 'r')
filterData = filterFile.readlines()

for vsound in variantSounds:
    os.makedirs(f'dist/vaal888-{vsound}-soundpack', exist_ok=True)
    for sound in generalSounds:
        shutil.copy(f'sounds/general/{sound}', f'dist/vaal888-{vsound}-soundpack')
    for sound in os.listdir(f'sounds/{vsound}'):
        shutil.copy(f'sounds/{vsound}/{sound}', f'dist/vaal888-{vsound}-soundpack')

    newFilterDataLine = []
    for data in filterData:
        if "CustomAlertSound" in data:
            insertIndex = data.find('"')+1
            data = data[:insertIndex] + f"vaal888-{vsound}-soundpack/" + data[insertIndex:]
        newFilterDataLine.append(data)
        # newFilterData = 

    with open(f'dist/Vaal888-{vsound}.filter', 'w') as newFilterFile:
        newFilterFile.write("".join(newFilterDataLine))