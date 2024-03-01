# sidebar_style.py

import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def sidebar_background_css(file_path):
    img = get_img_as_base64(file_path)
    css = f"""
    <style>
    [data-testid="stSidebar"] {{
        background-image: url('data:image/jpg;base64,{img}');
        background-size: cover;
    }}
    .sidebar-content {{
        color: white; /* Set text color to black */
    }}
    .sidebar .sidebar-content .element-container .markdown-text-container a {{
        color: white; /* Set page names text color to black */
        font-size: 18px; /* Set font size of page names */
    }}
    </style>
    """
    return css
