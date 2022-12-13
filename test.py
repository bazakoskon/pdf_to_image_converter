from PIL import Image
import os

# Path to the PDF files
pdf_path = r"pdf_files"

# Loop through all PDF files in the given directory
for filename in os.listdir(pdf_path):
    if filename.endswith(".pdf"):
        # Open the PDF file
        with Image.open(os.path.join(pdf_path, filename)) as pdf:
            # Get the number of pages
            num_pages = pdf.get_page_count()

            # Loop through all pages
            for page_num in range(num_pages):
                # Get the current page
                page = pdf.get_page(page_num)

                # Check the orientation of the page
                orientation = page.get_orientation()

                # Create a new image with the correct orientation
                if orientation == "portrait":
                    img = Image.new("L", (1700, 2400), "white")
                elif orientation == "landscape":
                    img = Image.new("L", (2400, 1700), "white")
                else:
                    # Handle other orientations as needed
                    pass

                # Paste the page onto the image
                img.paste(page)

                # Save the image to file
                img.save(f"{filename}_page_{page_num}.png", "PNG", dpi=(300, 300))
