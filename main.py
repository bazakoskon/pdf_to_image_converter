from pdf2image import convert_from_path
import os

import tempfile
poppler_path = r"Release-22.12.0-0/poppler-22.12.0/Library/bin"
output_folder = r"output_files"


for subdir, dirs, files in os.walk('pdf_files'):
    # print(subdir, dirs, files)
    if files:
        for file in files:
            pdf_path = f'{subdir}/{file}'
            with tempfile.TemporaryDirectory() as path:
                images_from_path = convert_from_path(pdf_path=pdf_path,
                                                     poppler_path=poppler_path,
                                                     grayscale=True,
                                                     size=(1700, 2400),
                                                     dpi=300,
                                                     fmt="jpeg",
                                                     jpegopt={
                                                         "quality": 100,
                                                         "progressive": False,
                                                         "optimize": False
                                                     }
                                                     )
                if not os.path.exists(f'{output_folder}/{file}'):
                    os.makedirs(f'{output_folder}/{file}'[:-4])
                    for index, page in enumerate(images_from_path):
                        page.save(os.path.join(f'{output_folder}/{file}'[:-4], f"{index}.jpg"), "JPEG", dpi=(300, 300))

# https://github.com/Belval/pdf2image