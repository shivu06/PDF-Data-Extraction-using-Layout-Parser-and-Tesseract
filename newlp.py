import cv2
import pytesseract
import matplotlib.pyplot as plt
import layoutparser as lp
import pandas as pd

# Load the image from the given path
image = cv2.imread(r"C:\Users\Shivashanmuga\Downloads\invoice_2001665 1_page-0001.jpg")
TesseractAgent = pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Shivashanmuga\Downloads\Tesseract-OCR 1\Tesseract-OCR\tesseract.exe'

# Create an instance of the Tesseract OCR agent
ocr_agent = lp.TesseractAgent()
print(ocr_agent)

# Detect text in the image with the OCR agent
res = ocr_agent.detect(image, return_response=True)

# Get the text, bounding boxes, and confidence scores
layout = ocr_agent.gather_data(res, agg_level= lp.TesseractFeatureType.WORD)
print(layout)

# Initialize an empty layout
empty_layout = lp.Layout()

# Display the empty layout
empty_draw_bb = lp.draw_text(image, empty_layout, font_size=15,with_box_on_text=True,
             text_box_width=5)
plt.figure(figsize=(300, 300))
plt.imshow(empty_draw_bb)
plt.title("Empty Layout")
plt.show()

# Draw the final layout
draw_bb = lp.draw_text(image, layout, font_size=15,with_box_on_text=True,
             text_box_width=5)
plt.figure(figsize=(300,300))
plt.imshow(draw_bb)
plt.title("Layout Created")
plt.show()

# Draw the final layout
draw_bb = lp.draw_text(image, layout, font_size=15,with_box_on_text=False,
             text_box_width=5)
plt.figure(figsize=(300,300))
plt.imshow(draw_bb)
plt.title("Layout Contents Ploted")
plt.show()



# "DATA COMING LINE BY LINE"
# Iterate through the layout line by line and save each line in separate lists
# lines = []
# current_line = []
#
# for element in layout:
#     if isinstance(element, lp.TextBlock):
#         if current_line:
#             lines.append(current_line)
#             current_line = []
#         current_line.append(element.text)
#     elif isinstance(element, lp.TextLine):
#         current_line.append(element.text)
#
# if current_line:
#     lines.append(current_line)
#     print(lines)
#
# # Print the lines
# for i, line in enumerate(lines):
#     print(f"Line {i+1}: {line}")
#
#
# # # Iterate through the layout line by line and save each line in separate lists
# lines = []
# current_line = []
# line_positions = []
#
# for i, element in enumerate(layout):
#     if isinstance(element, lp.TextBlock):
#         if current_line:
#             lines.append(current_line)
#             line_positions.append(layout[i-1].coordinates)
#             current_line = []
#         current_line.append(element.text)
#     elif isinstance(element, lp.TextLine):
#         current_line.append(element.text)
#
# if current_line:
#     lines.append(current_line)
#     line_positions.append(layout[i].coordinates)
#
# # Flatten the lists to a single list of strings
# flattened_lines = [text for line in lines for text in line]
# flattened_positions = [(pos[0], pos[1]) for pos in line_positions]
#
# # Create a pandas DataFrame
# df = pd.DataFrame({
#     'text': flattened_lines,
#     'x': [pos[0] for pos in flattened_positions],
#     'y': [pos[1] for pos in flattened_positions]
# })
#
# # # Save the DataFrame to a CSV file
# dft = df.transpose()
# print(df)
# dft.to_csv('layout_positions.csv', index=False)






# "THIS TO GET ENTIRE DATA INTO CSV"
# # Iterate through the layout line by line and save each line in separate lists
# lines = []
# current_line = []
# line_positions = []
#
# for i, element in enumerate(layout):
#     if isinstance(element, lp.TextBlock):
#         if current_line:
#             lines.append(current_line)
#             line_positions.append(layout[i-1].coordinates)
#             current_line = []
#         current_line.append(element.text)
#     elif isinstance(element, lp.TextLine):
#         current_line.append(element.text)
#
# if current_line:
#     lines.append(current_line)
#     line_positions.append(layout[i].coordinates)
#
# # Flatten the lists to a single list of strings
# flattened_lines = [text for line in lines for text in line]
# flattened_positions = [(pos[0], pos[1]) for pos in line_positions]
#
# # Calculate the number of columns and rows based on the positions
# x_values = [pos[0] for pos in flattened_positions]
# y_values = [pos[1] for pos in flattened_positions]
# num_columns = max(x_values) - min(x_values) + 1
# num_rows = max(y_values) - min(y_values) + 1
#
# # Create a pandas DataFrame with the calculated number of columns and rows
# df = pd.DataFrame(index=range(num_rows), columns=range(num_columns))
# print(df)
#
# # Add the text values to the DataFrame using chained indexing
# for text, pos in zip(flattened_lines, flattened_positions):
#     try:
#         df.loc[pos[1] - min(y_values), pos[0] - min(x_values)] = text
#     except KeyError:
#         print(f"Coordinates {pos} are outside the range of the DataFrame.")
#
# # # Save the DataFrame to a CSV file
# df.transpose().to_csv('layout_positions.csv', index=False)
#
#
# # Print the DataFrame as a table of values
# print(df.to_string(index=False, header=False))




# # # # # # Code for displaying the detected text
filtered_residence = layout.filter_by(
    lp.Rectangle(x_1=83, y_1=504, x_2=1156, y_2=692)
)
ddt = lp.draw_text(image, filtered_residence, font_size=16)
plt.figure(figsize=(50, 50))
plt.imshow(ddt)
plt.title("Table Detected")
plt.show()
#
# # # Extract text from the filtered layout
# # text = "\n".join(filtered_residence.get_texts())
# #
# # # Print the extracted text
# # print("Extracted Text:")
# # print(text)
#
#
# # Filter the layout for the "BillTo" section
bill_to_section = layout.filter_by(
    lp.Rectangle(x_1=84, y_1=344, x_2=141, y_2=358)
)
ddt = lp.draw_text(image, bill_to_section, font_size=16)
plt.figure(figsize=(50, 50))
plt.imshow(ddt)
plt.title("Table Detected")
plt.show()

