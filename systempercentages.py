import pickle
import glob

path = '/home/nerve/Documents/UW/gdrive/DMREF/MD/Rc_database/TEMP/*/*'

# Loop for each path
compositions = {}
for item in glob.glob(path):
    items = item.split('/')
    system = items[-2]
    composition = items[-1]

    if system in compositions:
        compositions[system].append(composition)

    else:
        compositions[system] = []
        compositions[system].append(composition)

with open('compositions.pkl', 'wb') as outfile:
    pickle.dump(compositions, outfile, pickle.HIGHEST_PROTOCOL)

print(glob.glob(path))
