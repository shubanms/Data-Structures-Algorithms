import os
from rich.console import Console
from rich.progress import track
import matplotlib.pyplot as plt


def capitalize_first_letter(text):
    return text[0].upper() + text[1:] if text else text


def generate_pie_chart(difficulty_counts, output_path):
    labels = list(difficulty_counts.keys())
    sizes = list(difficulty_counts.values())
    colors = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
    ]  # Better contrasting colors for dark mode

    # Create a pie chart
    plt.figure(figsize=(6, 6))  # Reduced size
    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        textprops=dict(color="white"),
    )

    # Add a legend below the chart
    plt.legend(
        wedges,
        labels,
        title="Difficulty Levels",
        loc="upper center",
        bbox_to_anchor=(0.5, -0.1),
        ncol=3,
        frameon=False,
        fontsize=10,
        title_fontsize=12,
        labelcolor="white",
    )
    plt.title("Difficulty Split", color="white")
    plt.gca().set_facecolor("#2e2e2e")  # Dark mode background
    plt.savefig(output_path, facecolor="#2e2e2e", bbox_inches="tight")
    plt.close()


def generate_markdown(directory):
    console = Console()
    console.log(f"[bold green]Starting to process directory:[/bold green] {directory}")

    # Define the markdown file path
    markdown_file_path = os.path.join(directory, "Table.md")

    # Initialize the markdown content
    markdown_content = "# Kanban Board\n\n"
    markdown_content += '<div style="display: flex; justify-content: space-around; gap: 20px; background-color: #2e2e2e; padding: 20px; border-radius: 10px;">\n'

    # Initialize counters for Kanban board and pie chart
    status_counts = {}
    difficulty_counts = {}

    # Iterate through all files in the directory
    for file_name in track(os.listdir(directory), description="Processing files..."):
        # Check if the file matches the format Question-<number>.py
        if file_name.startswith("Question-") and file_name.endswith(".py"):
            file_path = os.path.join(directory, file_name)

            # Read the first few lines of the file
            with open(file_path, "r") as file:
                lines = file.readlines()
                if len(lines) >= 3:
                    question_name = lines[0].strip("# ").strip()
                    difficulty = lines[1].strip("# ").strip()
                    status = lines[2].strip("# ").strip()

                    # Capitalize the first letter of difficulty and status
                    difficulty = capitalize_first_letter(difficulty)
                    status = capitalize_first_letter(status)

                    # Update counters for Kanban board and pie chart
                    status_counts[status] = status_counts.get(status, [])
                    status_counts[status].append((question_name, file_name))
                    difficulty_counts[difficulty] = (
                        difficulty_counts.get(difficulty, 0) + 1
                    )

    # Create Kanban board columns
    for status, questions in status_counts.items():
        status_color = "#6a5acd" if status == "Confident" else "#ffa500"
        markdown_content += f'  <div style="border: 2px solid {status_color}; border-radius: 10px; padding: 15px; width: 30%; background-color: #3e3e3e; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);">\n'
        markdown_content += f'    <h3 style="color: {status_color}; text-align: center; font-family: Arial, sans-serif;">{status}</h3>\n'
        markdown_content += '    <ul style="list-style-type: none; padding: 0;">\n'
        for question_name, file_name in questions:
            markdown_content += f'      <li style="margin: 10px 0;"><a href="{file_name}" style="text-decoration: none; color: #dcdcdc; font-weight: bold;">{question_name}</a></li>\n'
        markdown_content += "    </ul>\n"
        markdown_content += "  </div>\n"

    markdown_content += "</div>\n"

    # Generate and save the pie chart
    pie_chart_path = os.path.join(directory, "pie-chart.png")
    generate_pie_chart(difficulty_counts, pie_chart_path)

    # Add the pie chart image to the markdown
    markdown_content += f"\n---\n\n## Pie Chart: Difficulty Split\n\n![Difficulty Split]({os.path.basename(pie_chart_path)})\n"

    # Write the markdown content to the file
    with open(markdown_file_path, "w") as markdown_file:
        markdown_file.write(markdown_content)

    console.log(
        f"[bold green]Kanban board and chart have been successfully updated in:[/bold green] {directory}"
    )


def find_directories_with_questions(base_directory):
    directories_with_questions = []

    for root, dirs, files in os.walk(base_directory):
        if any(file.startswith("Question-") and file.endswith(".py") for file in files):
            directories_with_questions.append(root)

    return directories_with_questions


if __name__ == "__main__":
    base_directory = os.path.dirname(
        os.path.abspath(__file__)
    )  # Automatically get the script's directory
    directories = find_directories_with_questions(base_directory)
    for directory in directories:
        generate_markdown(directory)
