import markdown

# --- Settings ---
input_md_file = "README.md"
output_html_file = "output.html"

# --- Read Markdown File ---
with open(input_md_file, "r", encoding="utf-8") as f:
    md_content = f.read()

# --- Convert Markdown to HTML ---
html_content = markdown.markdown(md_content)

# --- Wrap in HTML Template ---
full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Converted Markdown</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      max-width: 800px;
      margin: 2rem auto;
      padding: 1rem;
      line-height: 1.6;
      background-color: #f9f9f9;
      color: #333;
    }}
    h1, h2, h3 {{
      color: #222;
    }}
    pre {{
      background: #eee;
      padding: 1em;
      overflow-x: auto;
    }}
    code {{
      background: #f4f4f4;
      padding: 2px 4px;
      border-radius: 4px;
    }}
    a {{
      color: #0366d6;
    }}
  </style>
</head>
<body>
{html_content}
</body>
</html>
"""

# --- Write to HTML File ---
with open(output_html_file, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"✅ Converted '{input_md_file}' to '{output_html_file}' successfully.")
