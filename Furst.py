from PIL import Image
import numpy as np
import os

counter = 0
for photo in os.listdir("First"):

    img = Image.open(os.path.join("First", photo))
    data = np.array(img)

    updated_data = (data - np.min(data)) * (255 / (np.max(data) - np.min(data)))
    print(updated_data)

    res_img = Image.fromarray(updated_data).convert('L')
    res_img.save(str(counter)+'.jpg')
    counter += 1
