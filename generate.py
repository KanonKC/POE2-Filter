import os
import shutil

generalSounds = os.listdir('src/general')
variantSounds = [soundDir for soundDir in os.listdir('sounds') if soundDir != 'general']

filterFile = open('src/Vaal888.filter', 'r')
filterData = filterFile.read()

for vsound in variantSounds:
    os.makedirs(f'dist/vaal888-{vsound}-soundpack', exist_ok=True)
    for sound in generalSounds:
        shutil.copy(f'src/general/{sound}', f'dist/vaal888-{vsound}-soundpack')
    for sound in os.listdir(f'sounds/{vsound}'):
        shutil.copy(f'sounds/{vsound}/{sound}', f'dist/vaal888-{vsound}-soundpack')

    newFilterDataLine = filterData.replace('general/', f'vaal888-{vsound}-soundpack/')
        # newFilterData = 

    with open(f'dist/Vaal888-{vsound}.filter', 'w') as newFilterFile:
        newFilterFile.write(newFilterDataLine)