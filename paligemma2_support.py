import re

def parse_boxes(output_text, img_w, img_h):
    """
    Parses PaliGemma <locXXXX> tokens and scales them to original image pixels.
    Format is: <locYMIN><locXMIN><locYMAX><locXMAX> label
    """
    # Regex pattern to extract location tokens and the trailing label
    pattern = r"<loc(\d+)><loc(\d+)><loc(\d+)><loc(\d+)>\s*([^<]+)"
    matches = re.findall(pattern, output_text)
    
    results = []
    for match in matches:
        ymin, xmin, ymax, xmax = map(int, match[:4])
        label = match[4].strip().replace("\n", "").rstrip("; ")
        
        # Denormalize from 1024-grid to actual pixel spaces
        pixel_xmin = (xmin / 1024) * img_w
        pixel_ymin = (ymin / 1024) * img_h
        pixel_xmax = (xmax / 1024) * img_w
        pixel_ymax = (ymax / 1024) * img_h
        
        results.append({
            "label": label,
            "box": [pixel_xmin, pixel_ymin, pixel_xmax, pixel_ymax]
        })
    return results
