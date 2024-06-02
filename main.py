#Create a desktop application with a Graphical User Interface (GUI) where you can upload an image and use Python to add a watermark logo/text.

# Create Tkinter Graphic Box.
from tkinter import *
window = Tk()
window.title("Watermark Your Photos")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)
window.config(background = "Light Blue")

from PIL import Image, ImageTk, ImageDraw

# Create Global Parameter to store photo path
global photo_path
photo_path = None

# Function to show image in the main window
def submit_image(path, *args):
    # Make sure that the my_pass_img PhotoImage object is accessible outside the submit_image() function
    global my_pass_img
    canvas = Canvas(window, width=400, height=400, highlightthickness=0)
    img = Image.open(path)

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Check if text argument passed to assess if a watermark is to be added to the image or a logo:
    if args:
        image_width, image_height = img.size
        if 'yes' not in str(args):
            txt = str(args)
            print(txt)
            for i in range(5):
                for x in range(0,image_width, 100):
                    for y in range (0, image_height, 100):
                        draw.text((x,y), txt, fill=(0,0,0))
        else:
            img2 = Image.open('output_image.png')
            for i in range(5):
                for x in range(0,image_width, 100):
                    for y in range (0, image_height, 100):
                        img.paste(img2, (x,y), mask=img2)



    # Calculate scaling factor to fit the image into the canvas
    img_width, img_height = img.size
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()
    scale_factor = min(canvas_width / img_width, canvas_height / img_height)

    # Resize the image with the calculated scaling factor
    img = img.resize((int(img_width * scale_factor), int(img_height * scale_factor)))

    # Load Image to main window
    my_pass_img = ImageTk.PhotoImage(img)  # Convert PIL Image to Tkinter PhotoImage
    canvas.create_image(canvas_width / 2, canvas_height / 2, image=my_pass_img)
    canvas.grid(column=1, row=2, columnspan=4)

# Function to upload an Image when the 'Add Image' Button is selected
def image_clicked():
    top = Toplevel(window)
    top.minsize(width=200, height=200)

    my_label = Label(top, text="Add the Image Path", font=("Arial", 18, "bold"))
    my_label.pack(padx=20, pady=20)

    # Create an Entry Widget in the Toplevel window for photo path
    entry = Entry(top, width=25)
    entry.pack(padx=20, pady=40)

    def submit_and_close():
        global photo_path
        photo_path = entry.get()

        # Call the submit_image function with the entry text
        submit_image(photo_path)

        # Close the Toplevel window
        top.destroy()

    # Create button to submit entry and close the window
    button = Button(top, text='Submit', command=submit_and_close)
    button.pack(padx=20, pady=60)

# Function to add watermark to Image
def watermark_clicked():

    # Create a pop up window for user to add text to image
    text_box = Toplevel(window)
    text_box.minsize(width=200, height=200)

    my_label = Label(text_box, text="Type text to add to image", font=("Arial", 18, "bold"))
    my_label.pack(padx=20, pady=20)

    # Create an Entry Widget in the text_box window for users text
    entry = Entry(text_box, width=25)
    entry.pack(padx=20, pady=40)

    def submit_and_close():
        global photo_path
        # Call the submit_image function with the entry text
        submit_image(photo_path, entry.get())

        # Close the Toplevel window
        text_box.destroy()

    # Create button to submit entry and close the window
    button = Button(text_box, text='Submit', command=submit_and_close)
    button.pack(padx=20, pady=60)

# Function to remove watermark when 'Remove Watermark' button is selected
def remove_watermark_button():
    global photo_path
    submit_image(photo_path)

#Function to add logo as watermark when 'Add Logo' button is selected
def add_logo_button():
    global photo_path
    submit_image(photo_path, 'yes')


# Below are components used to build the main Tkinter window

# Add Image Button
image_button = Button()
image_button = Button(text="Add Image", command=image_clicked)
image_button.grid(column=1, row=0, padx=30, pady=5)

# Add Watermark Button
add_watermark = Button()
add_watermark = Button(text='Add Watermark', command=watermark_clicked)
add_watermark.grid(column=2, row=0, padx=30, pady=5)

# Add Logo Button
add_logo = Button()
add_watermark = Button(text='Add Logo', command=add_logo_button)
add_watermark.grid(column=3, row=0, padx=30, pady=5)

# Remove Watermark
remove_watermark = Button()
remove_watermark = Button(text='Remove Watermark', command=remove_watermark_button)
remove_watermark.grid(column=4, row=0, padx=30, pady=5)

# Used to keep tkinter window open until user clicks exit
window.mainloop()