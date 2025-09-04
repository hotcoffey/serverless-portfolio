import markdown
import os

def generate_index_html():
    with open("content.md", "r") as md_file:
        md_content = md_file.read()
    html_content = markdown.markdown(md_content)
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Joshua Coffey - Portfolio</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #333; }}
            a {{ color: #007bff; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        {html_content}
        <p>Built by Joshua Coffey, Senior DevOps Engineer</p>
    </body>
    </html>
    """
    os.makedirs("../site", exist_ok=True)
    with open("../site/index.html", "w") as html_file:
        html_file.write(html_template)

if __name__ == "__main__":
    generate_index_html()