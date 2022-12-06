from pdf2image import convert_from_path
import os
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import tempfile

poppler_path = r"Release-22.12.0-0/poppler-22.12.0/Library/bin"
# pdf_path = r"pdf_files/2.pdf"
output_folder = r"output_files"
#
# pages = convert_from_path(pdf_path=pdf_path,
#                           poppler_path=poppler_path,
#                           grayscale=True,
#                           size=(1700, 2400),
#                           dpi=300
#                           )
#
#
# for index, page in enumerate(pages):
#     page.save(os.path.join(output_folder, f"{index}.jpg"), "JPEG")

# for subdir, dirs, files in os.walk('pdf_files'):
#     if files:
#         for file in files:
#             pdf_path = f'{subdir}/{file}'
#             pages = convert_from_path(pdf_path=pdf_path,
#                                       poppler_path=poppler_path,
#                                       grayscale=True,
#                                       size=(1700, 2400),
#                                       dpi=300
#                                       )
#             if not os.path.exists(f'{output_folder}/{file}'):
#                 os.makedirs(f'{output_folder}/{file}'[:-4])
#                 for index, page in enumerate(pages):
#                     page.save(os.path.join(f'{output_folder}/{file}'[:-4], f"{index}.jpg"), "JPEG")
for subdir, dirs, files in os.walk('pdf_files'):
    print(subdir, dirs, files)
    if files:
        for file in files:
            pdf_path = f'{subdir}/{file}'
            with tempfile.TemporaryDirectory() as path:
                images_from_path = convert_from_path(pdf_path=pdf_path,
                                                     poppler_path=poppler_path,
                                                     grayscale=True,
                                                     size=(1700, 2400),
                                                     dpi=300
                                                     )
                if not os.path.exists(f'{output_folder}/{file}'):
                    os.makedirs(f'{output_folder}/{file}'[:-4])
                    for index, page in enumerate(images_from_path):
                        page.save(os.path.join(f'{output_folder}/{file}'[:-4], f"{index}.jpg"), "JPEG")
#
# convert_from_path(pdf_path, dpi=200, output_folder=None, first_page=None,
#                   last_page=None, fmt='ppm', jpegopt=None, thread_count=1,
#                   userpw=None, use_cropbox=False, strict=False, transparent=False,
#                   single_file=False, output_file=str(uuid.uuid4()), poppler_path=None,
#                   grayscale=False, size=None, paths_only=False, use_pdftocairo=False, timeout=600)

