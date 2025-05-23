import sys
from rich.console import Console
from translator.translate import translate

console = Console()


def main():

    input_file_path = "input.txt"
    output_file_path = "output.txt"

    try:

        with open(input_file_path, "r", encoding="utf-8") as input_file:
            text_to_translate = input_file.read()

        console.print(f"[bold green]Translating content from {input_file_path}...[/bold green]")
        translated_text = translate(text_to_translate)

        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(translated_text)

        console.print("Translation completed successfully!", style="bold green")

    except FileNotFoundError:
        console.print(f"[red bold]Error: Could not find {input_file_path}. Please make sure the file exists.[/red bold]")

    except ValueError as e:
        console.print(f"[red bold]{str(e)}[/red bold]")
        sys.exit(1)
        
    except Exception as e:
        console.print(f"[red bold]An error occurred: {str(e)}[/red bold]")

if __name__ == "__main__":
    main()