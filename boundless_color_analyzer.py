#!/usr/bin/env python
from gimpfu import *
import csv
import math
import os

# Define the Boundless Color Palette as a list of (code, name, r, g, b, hex) tuples
BOUNDLESS_PALETTE = [
    (1, "Black", 27, 27, 27, "#1b1b1b"),
    (2, "Night Azure", 17, 29, 37, "#111d25"),
    (3, "Shadow Cerulean", 5, 29, 50, "#051d32"),
    (4, "Dark Cerulean", 46, 56, 71, "#2e3847"),
    (5, "Dark Cobalt", 54, 54, 77, "#36364d"),
    (6, "Dark Berry", 65, 52, 65, "#413441"),
    (7, "Dark Violet", 73, 47, 73, "#492f49"),
    (8, "Dark Lilac", 76, 42, 91, "#4c2a5b"),
    (9, "Strong Violet", 99, 16, 99, "#631063"),
    (10, "Strong Magenta", 95, 30, 77, "#5f1e4d"),
    (11, "Strong Fuchsia", 110, 13, 54, "#6e0d36"),
    (12, "Strong Cherry", 105, 26, 35, "#691a23"),
    (13, "Dark Red", 90, 41, 35, "#5a2923"),
    (14, "Dark Orange", 79, 48, 35, "#4f3023"),
    (15, "Dark Rose", 73, 50, 50, "#493232"),
    (16, "Dark Fuchsia", 82, 44, 55, "#522c37"),
    (17, "Shadow Fuchsia", 60, 4, 27, "#3c041b"),
    (18, "Night Berry", 46, 17, 38, "#2e1126"),
    (19, "Night Fuchsia", 43, 21, 27, "#2b151b"),
    (20, "Night Orange", 37, 25, 20, "#251914"),
    (21, "Shadow Orange", 47, 20, 3, "#2f1403"),
    (22, "Shadow Red", 63, 3, 3, "#3f0303"),
    (23, "Strong Red", 115, 12, 12, "#730c0c"),
    (24, "Deep Red", 171, 23, 23, "#ab1717"),
    (25, "Hot Cherry", 158, 44, 57, "#9e2c39"),
    (26, "Silk Cherry", 131, 68, 68, "#834444"),
    (27, "Oxide Rose", 110, 78, 82, "#6e4e52"),
    (28, "Silk Orange", 110, 79, 67, "#6e4f43"),
    (29, "Silk Mustard", 100, 83, 67, "#645343"),
    (30, "Hot Sepia", 117, 78, 42, "#754e2a"),
    (31, "Deep Mustard", 112, 81, 22, "#705116"),
    (32, "Hot Tan", 99, 85, 42, "#63552a"),
    (33, "Silk Yellow", 88, 88, 56, "#585838"),
    (34, "Deep Yellow", 89, 89, 22, "#595916"),
    (35, "Hot Moss", 64, 95, 42, "#405f2a"),
    (36, "Deep Green", 22, 100, 22, "#166416"),
    (37, "Strong Green", 11, 65, 11, "#0b410b"),
    (38, "Dark Green", 44, 60, 34, "#2c3c22"),
    (39, "Dark Yellow", 57, 57, 34, "#393922"),
    (40, "Strong Yellow", 58, 58, 11, "#3a3a0b"),
    (41, "Strong Mustard", 73, 52, 11, "#49340b"),
    (42, "Dark Mustard", 65, 54, 35, "#413623"),
    (43, "Shadow Mustard", 36, 26, 3, "#241a03"),
    (44, "Shadow Yellow", 29, 29, 3, "#1d1d03"),
    (45, "Night Green", 19, 30, 19, "#131e13"),
    (46, "Shadow Turquoise", 4, 31, 31, "#041f1f"),
    (47, "Dark Turquoise", 44, 58, 58, "#2c3a3a"),
    (48, "Dark Grey", 62, 62, 62, "#3e3e3e"),
    (49, "Oxide Azure", 79, 87, 93, "#4f575d"),
    (50, "Oxide Grey", 99, 99, 99, "#636363"),
    (51, "Oxide Yellow", 87, 87, 77, "#57574d"),
    (52, "Oxide Green", 77, 90, 77, "#4d5a4d"),
    (53, "Silk Mint", 67, 93, 67, "#435d43"),
    (54, "Silk Teal", 58, 93, 83, "#3a5d53"),
    (55, "Deep Turquoise", 25, 96, 96, "#196060"),
    (56, "Deep Slate", 26, 94, 110, "#1a5e6e"),
    (57, "Deep Azure", 27, 92, 125, "#1b5c7d"),
    (58, "Deep Cerulean", 30, 87, 154, "#1e579a"),
    (59, "Silk Cobalt", 67, 83, 143, "#43538f"),
    (60, "Silk Cerulean", 73, 87, 111, "#49576f"),
    (61, "Oxide Blue", 84, 84, 114, "#545472"),
    (62, "Oxide Violet", 99, 80, 99, "#635063"),
    (63, "Silk Berry", 111, 73, 111, "#6f496f"),
    (64, "Silk Lilac", 115, 66, 136, "#734288"),
    (65, "Silk Lavender", 93, 70, 162, "#5d46a2"),
    (66, "Deep Lavender", 109, 37, 213, "#6d25d5"),
    (67, "Deep Lilac", 134, 33, 179, "#8621b3"),
    (68, "Deep Violet", 148, 30, 148, "#941e94"),
    (69, "Hot Magenta", 143, 49, 118, "#8f3176"),
    (70, "Silk Magenta", 136, 60, 97, "#883c61"),
    (71, "Deep Fuchsia", 165, 25, 84, "#a51954"),
    (72, "Warm Fuchsia", 190, 83, 117, "#be5375"),
    (73, "Warm Magenta", 202, 67, 138, "#ca438a"),
    (74, "Fuchsia", 224, 38, 116, "#e02674"),
    (75, "Rose", 227, 36, 90, "#e3245a"),
    (76, "Warm Cherry", 197, 81, 92, "#c5515c"),
    (77, "Cherry", 230, 35, 64, "#e62340"),
    (78, "Red", 232, 35, 35, "#e82323"),
    (79, "Warm Red", 200, 81, 61, "#c8513d"),
    (80, "Stale Red", 168, 101, 94, "#a8655e"),
    (81, "Warm Orange", 163, 105, 79, "#a3694f"),
    (82, "Stale Sepia", 144, 113, 94, "#90715e"),
    (83, "Warm Mustard", 141, 115, 79, "#8d734f"),
    (84, "Stale Tan", 127, 119, 94, "#7f775e"),
    (85, "Warm Yellow", 121, 121, 79, "#79794f"),
    (86, "Stale Moss", 105, 125, 93, "#697d5d"),
    (87, "Warm Viridian", 81, 129, 107, "#51816b"),
    (88, "Teal", 37, 133, 117, "#258575"),
    (89, "Viridian", 36, 134, 98, "#248662"),
    (90, "Mint", 34, 136, 73, "#228849"),
    (91, "Green", 34, 137, 33, "#228921"),
    (92, "Warm Moss", 90, 130, 60, "#5a823c"),
    (93, "Yellow", 123, 123, 34, "#7b7b22"),
    (94, "Tan", 139, 117, 34, "#8b7522"),
    (95, "Mustard", 153, 112, 34, "#997022"),
    (96, "Sepia", 168, 105, 34, "#a86922"),
    (97, "Orange", 183, 95, 34, "#b75f22"),
    (98, "Vivid Orange", 234, 123, 47, "#ea7b2f"),
    (99, "Light Sepia", 208, 137, 80, "#d08950"),
    (100, "Light Orange", 209, 135, 103, "#d18767"),
    (101, "Pale Sepia", 184, 145, 122, "#b8917a"),
    (102, "Ashen Taupe", 166, 151, 138, "#a6978a"),
    (103, "Ashen Yellow", 154, 154, 138, "#9a9a8a"),
    (104, "Pale Tan", 163, 153, 121, "#a39979"),
    (105, "Light Mustard", 177, 150, 103, "#b19667"),
    (106, "Light Tan", 171, 153, 80, "#ab9950"),
    (107, "Light Yellow", 156, 156, 102, "#9c9c66"),
    (108, "Pale Moss", 136, 161, 121, "#88a179"),
    (109, "Ashen Mint", 139, 158, 144, "#8b9e90"),
    (110, "Ashen Turquoise", 140, 157, 157, "#8c9d9d"),
    (111, "Ashen Grey", 139, 139, 139, "#8b8b8b"),
    (112, "Rust Slate", 109, 121, 126, "#6d797e"),
    (113, "Stale Turquoise", 97, 124, 124, "#617c7c"),
    (114, "Rust Lime", 116, 121, 107, "#74796b"),
    (115, "Rust Taupe", 129, 117, 107, "#81756b"),
    (116, "Rust Fuchsia", 147, 109, 118, "#936d76"),
    (117, "Rust Violet", 136, 111, 136, "#886f88"),
    (118, "Stale Berry", 159, 100, 141, "#9f648d"),
    (119, "Warm Violet", 168, 89, 168, "#a859a8"),
    (120, "Stale Lilac", 143, 104, 166, "#8f68a6"),
    (121, "Warm Blue", 111, 111, 191, "#6f6fbf"),
    (122, "Blue", 101, 101, 240, "#6565f0"),
    (123, "Lavender", 139, 86, 240, "#8b56f0"),
    (124, "Lilac", 178, 54, 240, "#b236f0"),
    (125, "Violet", 201, 44, 201, "#c92cc9"),
    (126, "Vivid Violet", 245, 82, 245, "#f552f5"),
    (127, "Vivid Lilac", 204, 116, 245, "#cc74f5"),
    (128, "Vivid Lavender", 172, 133, 245, "#ac85f5"),
    (129, "Vivid Blue", 143, 143, 245, "#8f8ff5"),
    (130, "Light Blue", 148, 148, 209, "#9494d1"),
    (131, "Pale Lilac", 168, 144, 191, "#a890bf"),
    (132, "Light Lilac", 185, 134, 209, "#b986d1"),
    (133, "Pale Berry", 193, 135, 177, "#c187b1"),
    (134, "Ashen Berry", 174, 145, 165, "#ae91a5"),
    (135, "Ashen Red", 179, 145, 145, "#b39191"),
    (136, "Cool Red", 216, 181, 181, "#d8b5b5"),
    (137, "Stark Orange", 229, 178, 160, "#e5b2a0"),
    (138, "Bright Orange", 250, 170, 138, "#faaa8a"),
    (139, "Bright Sepia", 250, 172, 113, "#faac71"),
    (140, "Bright Taupe", 250, 174, 78, "#faae4e"),
    (141, "Bright Mustard", 236, 180, 59, "#ecb43b"),
    (142, "Bright Tan", 217, 188, 59, "#d9bc3b"),
    (143, "Bright Yellow", 195, 195, 59, "#c3c33b"),
    (144, "Bright Lime", 170, 202, 59, "#aaca3b"),
    (145, "Bright Moss", 133, 209, 59, "#85d13b"),
    (146, "Bright Green", 59, 217, 59, "#3bd93b"),
    (147, "Stark Green", 127, 208, 127, "#7fd07f"),
    (148, "Bright Viridian", 61, 214, 146, "#3dd692"),
    (149, "Stark Viridian", 104, 208, 176, "#68d0b0"),
    (150, "Cool Mint", 151, 201, 163, "#97c9a3"),
    (151, "Cool Teal", 154, 199, 183, "#9ac7b7"),
    (152, "Stark Turquoise", 134, 201, 201, "#86c9c9"),
    (153, "Bright Turquoise", 65, 208, 208, "#41d0d0"),
    (154, "Bright Slate", 66, 206, 228, "#42cee4"),
    (155, "Bright Azure", 79, 203, 249, "#4fcbf9"),
    (156, "Stark Azure", 130, 196, 249, "#82c4f9"),
    (157, "Bright Cerulean", 159, 190, 249, "#9fbef9"),
    (158, "Bright Blue", 183, 183, 249, "#b7b7f9"),
    (159, "Stark Lavender", 197, 183, 226, "#c5b7e2"),
    (160, "Cool Blue", 187, 187, 214, "#bbbbd6"),
    (161, "Weary Violet", 202, 184, 202, "#cab8ca"),
    (162, "Cool Violet", 214, 178, 214, "#d6b2d6"),
    (163, "Bright Lilac", 217, 174, 237, "#d9aeed"),
    (164, "Bright Magenta", 238, 167, 219, "#eea7db"),
    (165, "Bright Violet", 249, 157, 249, "#f99df9"),
    (166, "Light Berry", 229, 111, 197, "#e56fc5"),
    (167, "Vivid Fuchsia", 247, 104, 151, "#f76897"),
    (168, "Light Fuchsia", 216, 127, 152, "#d87f98"),
    (169, "Light Red", 218, 129, 129, "#da8181"),
    (170, "Vivid Cherry", 248, 109, 109, "#f86d6d"),
    (171, "Vivid Red", 248, 111, 87, "#f86f57"),
    (172, "Bright Red", 250, 168, 168, "#faa8a8"),
    (173, "Bright Fuchsia", 249, 166, 188, "#f9a6bc"),
    (174, "Luminous Violet", 252, 215, 252, "#fcd7fc"),
    (175, "Cold Berry", 237, 222, 237, "#eddeed"),
    (176, "Luminous Blue", 224, 224, 252, "#e0e0fc"),
    (177, "Luminous Azure", 204, 230, 252, "#cce6fc"),
    (178, "Cold Slate", 205, 231, 237, "#cde7ed"),
    (179, "Luminous Slate", 169, 237, 252, "#a9edfc"),
    (180, "Cool Slate", 157, 196, 206, "#9dc4ce"),
    (181, "Weary Teal", 173, 194, 190, "#adc2be"),
    (182, "Cool Grey", 182, 182, 182, "#b6b6b6"),
    (183, "Weary Mustard", 203, 187, 171, "#cbbbab"),
    (184, "Cool Taupe", 218, 183, 152, "#dab798"),
    (185, "Stark Mustard", 218, 184, 128, "#dab880"),
    (186, "Cool Tan", 199, 189, 150, "#c7bd96"),
    (187, "Weary Yellow", 190, 191, 171, "#bebfab"),
    (188, "Cool Lime", 181, 195, 150, "#b5c396"),
    (189, "Stark Lime", 168, 200, 127, "#a8c87f"),
    (190, "Stark Yellow", 193, 193, 127, "#c1c17f"),
    (191, "Crisp Yellow", 231, 231, 153, "#e7e799"),
    (192, "Crisp Lime", 214, 237, 120, "#d6ed78"),
    (193, "Luminous Moss", 181, 246, 72, "#b5f648"),
    (194, "Luminous Green", 129, 253, 129, "#81fd81"),
    (195, "Crisp Green", 174, 243, 174, "#aef3ae"),
    (196, "Cold Lime", 210, 235, 180, "#d2ebb4"),
    (197, "Cold Viridian", 187, 238, 213, "#bbeed5"),
    (198, "Cold Teal", 160, 241, 230, "#a0f1e6"),
    (199, "Crisp Teal", 126, 248, 217, "#7ef8d9"),
    (200, "Luminous Viridian", 98, 252, 191, "#62fcbf"),
    (201, "Luminous Turquoise", 79, 249, 249, "#4ff9f9"),
    (202, "Vivid Turquoise", 51, 169, 169, "#33a9a9"),
    (203, "Light Turquoise", 108, 163, 163, "#6ca3a3"),
    (204, "Vivid Slate", 52, 167, 189, "#34a7bd"),
    (205, "Vivid Azure", 54, 164, 211, "#36a4d3"),
    (206, "Light Azure", 111, 160, 186, "#6fa0ba"),
    (207, "Pale Cerulean", 129, 156, 187, "#819cbb"),
    (208, "Vivid Cobalt", 109, 151, 245, "#6d97f5"),
    (209, "Vivid Cerulean", 57, 158, 244, "#399ef4"),
    (210, "Cerulean", 42, 123, 193, "#2a7bc1"),
    (211, "Azure", 40, 127, 166, "#287fa6"),
    (212, "Slate", 39, 130, 148, "#278294"),
    (213, "Turquoise", 37, 131, 132, "#258384"),
    (214, "Vivid Teal", 50, 171, 151, "#32ab97"),
    (215, "Light Viridian", 105, 166, 139, "#69a68b"),
    (216, "Vivid Viridian", 48, 173, 128, "#30ad80"),
    (217, "Vivid Mint", 47, 175, 96, "#2faf60"),
    (218, "Vivid Green", 46, 176, 46, "#2eb02e"),
    (219, "Vivid Moss", 117, 167, 79, "#75a74f"),
    (220, "Vivid Lime", 137, 164, 46, "#89a42e"),
    (221, "Vivid Yellow", 158, 158, 46, "#9e9e2e"),
    (222, "Vivid Mustard", 189, 147, 46, "#bd932e"),
    (223, "Luminous Tan", 253, 225, 127, "#fde17f"),
    (224, "Crisp Tan", 248, 224, 174, "#f8e0ae"),
    (225, "Cold Tan", 238, 225, 200, "#eee1c8"),
    (226, "Luminous Taupe", 252, 221, 197, "#fcddc5"),
    (227, "Luminous Red", 252, 219, 219, "#fcdbdb"),
    (228, "White", 226, 226, 226, "#e2e2e2"),
    (229, "Cool Azure", 170, 192, 214, "#aac0d6"),
    (230, "Ashen Blue", 152, 152, 173, "#9898ad"),
    (231, "Rust Blue", 117, 117, 144, "#757590"),
    (232, "Stale Cerulean", 100, 121, 147, "#647993"),
    (233, "Cobalt", 48, 112, 240, "#3070f0"),
    (234, "Deep Cobalt", 34, 75, 195, "#224bc3"),
    (235, "Deep Blue", 55, 55, 232, "#3737e8"),
    (236, "Strong Blue", 25, 25, 172, "#1919ac"),
    (237, "Strong Cobalt", 20, 46, 138, "#142e8a"),
    (238, "Strong Cerulean", 17, 55, 105, "#113769"),
    (239, "Strong Azure", 15, 59, 84, "#0f3b54"),
    (240, "Strong Slate", 14, 61, 73, "#0e3d49"),
    (241, "Strong Turquoise", 13, 62, 62, "#0d3e3e"),
    (242, "Strong Viridian", 12, 64, 43, "#0c402b"),
    (243, "Shadow Green", 3, 33, 3, "#032103"),
    (244, "Deep Viridian", 23, 98, 70, "#176246"),
    (245, "Silk Turquoise", 70, 90, 90, "#465a5a"),
    (246, "Dark Blue", 51, 51, 97, "#333361"),
    (247, "Night Blue", 22, 22, 65, "#161641"),
    (248, "Shadow Blue", 9, 9, 97, "#090961"),
    (249, "Strong Lavender", 66, 36, 124, "#42247c"),
    (250, "Shadow Violet", 53, 5, 53, "#350535"),
    (251, "Night Lilac", 34, 23, 43, "#22172b"),
    (252, "Strong Orange", 89, 43, 11, "#592b0b"),
    (253, "Deep Orange", 135, 68, 22, "#874416"),
    (254, "Hot Orange", 137, 66, 43, "#89422b"),
    (255, "Luminous Yellow", 233, 233, 72, "#e9e948"),
]

def find_closest_color(r, g, b):
    """Find the closest Boundless color match using Euclidean distance."""
    min_distance = float('inf')
    closest_color = None
    
    for color in BOUNDLESS_PALETTE:
        code, name, pr, pg, pb, hex_code = color
        distance = math.sqrt((r - pr) ** 2 + (g - pg) ** 2 + (b - pb) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_color = color
    
    return closest_color

def get_chunk(row, col, image_width):
    """Determine which 8x8 chunk the pixel belongs to."""
    chunk_row = (row - 1) // 8  # 0-based chunk row index
    chunk_col = (col - 1) // 8  # 0-based chunk col index
    chunks_per_row = image_width // 8  # Number of chunks per row
    chunk = (chunk_row * chunks_per_row) + chunk_col + 1  # 1-based chunk number
    return chunk

def get_chunk_position(row, col):
    """Get the row and column position within the chunk (1-8)."""
    chunk_row_pos = ((row - 1) % 8) + 1  # 1-8 position within chunk
    chunk_col_pos = ((col - 1) % 8) + 1  # 1-8 position within chunk
    return chunk_row_pos, chunk_col_pos

def process_image(image, drawable, file_path):
    """Main function to process the image and generate the CSV outputs."""
    # Verify image dimensions are multiples of 8
    if image.width % 8 != 0 or image.height % 8 != 0:
        gimp.message("Error: Image dimensions must be multiples of 8x8 pixels!")
        return
    
    # Check if file path is provided, otherwise use default
    if not file_path or file_path.strip() == "":
        file_path = os.path.join(os.path.expanduser("~"), "pixel_colors.csv")
        gimp.message("No file path provided. Saving to default location: " + file_path)
    
    # Ensure .csv extension for pixel_colors.csv
    if not file_path.lower().endswith('.csv'):
        file_path += '.csv'
    
    # Derive pixel_sign_data.csv path from file_path
    base_path = os.path.splitext(file_path)[0]
    sign_data_path = base_path + "_sign_data.csv"
    
    # Initialize variables
    pixel_data = []
    color_counts = {}  # Total counts for each color code
    chunk_color_counts = {}  # Counts of colors within each chunk
    
    # Process each pixel
    for row in range(1, image.height + 1):
        for col in range(1, image.width + 1):
            # Get pixel color
            pixel_region = drawable.get_pixel_rgn(col - 1, row - 1, 1, 1)
            pixel = pixel_region[col - 1, row - 1]  # Returns a byte string
            
            # Convert byte string to integers for RGB
            if len(pixel) >= 3:  # Ensure at least 3 channels (RGB)
                r = ord(pixel[0])  # Red
                g = ord(pixel[1])  # Green
                b = ord(pixel[2])  # Blue
            else:
                gimp.message("Error: Image must be in RGB format with at least 3 channels!")
                return
            
            # Find closest Boundless color
            color = find_closest_color(r, g, b)
            code, name, _, _, _, hex_code = color
            
            # Determine chunk
            chunk = get_chunk(row, col, image.width)
            
            # Get chunk row and column positions
            chunk_row_pos, chunk_col_pos = get_chunk_position(row, col)
            
            # Update total color count
            color_counts[code] = color_counts.get(code, 0) + 1
            
            # Update chunk-specific color count
            chunk_key = (chunk, code)
            chunk_color_counts[chunk_key] = chunk_color_counts.get(chunk_key, 0) + 1
            
            # Store pixel data
            pixel_data.append({
                'row': row,
                'col': col,
                'code': code,
                'color': name,
                'chunk': chunk,
                'chunk_row': chunk_row_pos,
                'chunk_col': chunk_col_pos
            })
    
    # Write to pixel_colors.csv
    try:
        with open(file_path, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            writer.writerow(['Row', 'Column', 'Code', 'Color', 'Count', 'Chunk', 'C Row', 'C Column', 'C Count'])
            
            # Write pixel data
            for data in pixel_data:
                code = data['code']
                chunk = data['chunk']
                chunk_key = (chunk, code)
                writer.writerow([
                    data['row'],
                    data['col'],
                    code,
                    data['color'],
                    color_counts[code],  # Total count in image
                    chunk,
                    data['chunk_row'],
                    data['chunk_col'],  # Fixed typo from original (was data['col'])
                    chunk_color_counts[chunk_key]  # Count in chunk
                ])
        
        gimp.message("Processing complete. Output saved to " + file_path)
    
    except IOError as e:
        gimp.message("Error saving file (pixel_colors.csv): " + str(e))
        return
    
    # Write to pixel_sign_data.csv
    try:
        with open(sign_data_path, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            writer.writerow(['Sign Data'])
            
            # Calculate number of sections (based on height)
            sections = image.height // 8
            chunks_per_row = image.width // 8
            
            # Prepare data for each chunk (8x8 block)
            sign_sections = []
            for chunk in range(1, (sections * chunks_per_row) + 1):
                # Find all pixels in this chunk
                chunk_pixels = [p for p in pixel_data if p['chunk'] == chunk]
                text_lines = []
                # Process each position in the 8x8 chunk
                for chunk_row in range(1, 9):
                    for chunk_col in range(1, 9):
                        # Find the pixel at this chunk position
                        pixel = next((p for p in chunk_pixels 
                                    if p['chunk_row'] == chunk_row and p['chunk_col'] == chunk_col), None)
                        if pixel:
                            # Calculate absolute row and column in image
                            abs_row = ((chunk - 1) // chunks_per_row) * 8 + chunk_row
                            abs_col = ((chunk - 1) % chunks_per_row) * 8 + chunk_col
                            text_lines.append("%d,%d" % (abs_row, abs_col))
                            text_lines.append(str(pixel['code']))
                            # Add two blank lines unless it's the last position
                            if chunk_row < 8 or chunk_col < 8:
                                text_lines.append('')
                                text_lines.append('')
                # Join all lines for this chunk into a single cell
                section_data = '\n'.join(text_lines)
                sign_sections.append([section_data])
            
            # Write each chunk's data as a row in the single column
            writer.writerows(sign_sections)
        
        gimp.message("Sign data output saved to " + sign_data_path)
    
    except IOError as e:
        gimp.message("Error saving file (pixel_sign_data.csv): " + str(e))
        return

# Register the plug-in
register(
    "python_fu_boundless_color_analyzer",
    "Analyze image for Boundless color palette matches",
    "Processes images with dimensions that are multiples of 8x8 pixels, matches pixels to Boundless colors, and outputs to CSV",
    "Your Name",
    "Your Name",
    "2025",
    "<Image>/Filters/Boundless Color Analyzer...",
    "RGB*",
    [
        (PF_STRING, "file_path", "Save file path (e.g., C:\\Users\\yates\\pixel_colors.csv)", ""),
    ],
    [],
    process_image
)

main()