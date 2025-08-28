import markdown

# Read the markdown file
with open("README.md", "r", encoding="utf-8") as f:
    md_text = f.read()

# Convert to HTML
html = markdown.markdown(md_text)

# Save to an HTML file
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)
