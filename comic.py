from PIL import Image, ImageDraw
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_comic_page(page_num, page_width=800, page_height=1200):
    """
    Generate a single comic book page with structured panel layouts.
    
    Args:
        page_num (int): Page number to include on the page.
        page_width (int): Width of the page in pixels.
        page_height (int): Height of the page in pixels.

    Returns:
        Image: PIL Image object representing the comic page.
    """
    # Create a blank white page
    page = Image.new("RGB", (page_width, page_height), "white")
    draw = ImageDraw.Draw(page)

    # Number of rows and columns for panels
    rows = random.randint(2, 4)
    cols = random.randint(2, 4)

    # Calculate panel dimensions and margins
    margin = 20
    panel_width = (page_width - (cols + 1) * margin) // cols
    panel_height = (page_height - (rows + 1) * margin) // rows

    for row in range(rows):
        for col in range(cols):
            x1 = margin + col * (panel_width + margin)
            y1 = margin + row * (panel_height + margin)
            x2 = x1 + panel_width
            y2 = y1 + panel_height

            # Draw a rectangle to represent the panel
            draw.rectangle([x1, y1, x2, y2], outline="black", width=3)

            # Add a placeholder for text inside the panel
            text_x = x1 + 10
            text_y = y1 + 10
            draw.text((text_x, text_y), "Text Placeholder", fill="black")

    # Add a page number
    draw.text((page_width - 100, page_height - 50), f"Page {page_num}", fill="black")

    return page

def save_comic_as_pdf(num_pages, output_filename="comic_book.pdf"):
    """
    Generate a comic book with the specified number of pages and save as a PDF.
    
    Args:
        num_pages (int): Number of pages to generate.
        output_filename (str): Name of the output PDF file.
    """
    # Create a PDF canvas
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter

    for page_num in range(1, num_pages + 1):
        # Generate a comic page
        page_image = generate_comic_page(page_num)

        # Save the page as a temporary image
        temp_filename = f"temp_page_{page_num}.png"
        page_image.save(temp_filename)

        # Draw the image onto the PDF
        c.drawImage(temp_filename, 0, 0, width, height)

        # Add a new page for the PDF
        c.showPage()

    # Save the PDF
    c.save()
    print(f"Comic book saved as {output_filename}")

# Example usage
if __name__ == "__main__":
    num_pages = 5  # Specify the number of pages
    save_comic_as_pdf(num_pages)