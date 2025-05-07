import os
import re

def build_dashboard(base_directory):
    readme_path = os.path.join(base_directory, "README.md")
    dashboard_rows = []

    for root, _, files in os.walk(base_directory):
        if "Table.md" in files:
            table_path = os.path.join(root, "Table.md")
            relative_path = os.path.relpath(root, base_directory).replace("\\", "/")
            path_parts = relative_path.split("/")

            with open(table_path, "r", encoding="utf-8") as f:
                table_content = f.read()

            section_col = format_section_column(path_parts)
            questions_col = extract_questions(table_content, relative_path)

            dashboard_rows.append((section_col, questions_col))

    md = "# 📘 DSA Summary Dashboard\n\nAll categorized questions across all directories.\n\n"
    md += "| Section | Total Questions | Questions Details |\n"
    md += "|---------|----------------|-------------------|\n"
    for section, questions in dashboard_rows:
        total_questions = questions.count('•')  # Count the number of bullet points
        md += f"| {section} | {total_questions} | {questions} |\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(md)

def format_section_column(path_parts):
    full_path = "/".join(path_parts)
    label = " > ".join(path_parts)
    return f"📂 [{label}]({full_path}/Table.md)"

def extract_questions(table_md, rel_dir):
    categories = re.findall(r'<h3.*?>(.*?)</h3>', table_md)
    lists = re.findall(r'<ul.*?>(.*?)</ul>', table_md, re.DOTALL)

    markdown_lines = []

    for cat, ul_html in zip(categories, lists):
        markdown_lines.append(f"**{cat.strip()}**")
        items = re.findall(r'href="(.*?)".*?>(.*?)</a>', ul_html)
        for href, label in items:
            full_path = os.path.join(rel_dir, href).replace("\\", "/")
            markdown_lines.append(f"&nbsp;&nbsp;&nbsp;&nbsp;• [{label}]({full_path})")
        markdown_lines.append("")  # Line break between categories

    return "<br>".join(markdown_lines).strip() if markdown_lines else "_No questions_"

if __name__ == "__main__":
    base_directory = os.path.dirname(os.path.abspath(__file__))
    build_dashboard(base_directory)
