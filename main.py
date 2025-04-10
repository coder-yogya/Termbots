
import sys
import logging
import datetime
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Setup logging to record conversation history and errors
logging.basicConfig(
    filename='chatbot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

console = Console()
conversation_history = []

def print_help():
    console.print("[bold cyan]Available Commands:[/bold cyan]")
    console.print("- [yellow]exit[/yellow]: Exit the chatbot")
    console.print("- [yellow]help[/yellow]: Show this help message")
    console.print("- [yellow]history[/yellow]: Show conversation history")
    console.print("- [yellow]reset[/yellow]: Reset conversation history")
    console.print("- [yellow]clear[/yellow]: Clear the terminal screen")

def display_history():
    if not conversation_history:
        console.print("[italic]No conversation history yet.[/italic]")
        return
    table = Table(title="Conversation History")
    table.add_column("Timestamp", style="dim", width=12)
    table.add_column("Speaker", style="green")
    table.add_column("Message", style="white", overflow="fold")
    for entry in conversation_history:
        table.add_row(entry["time"], entry["speaker"], entry["message"])
    console.print(table)

def clear_history():
    global conversation_history
    conversation_history = []
    console.print("[bold magenta]Conversation history has been reset.[/bold magenta]")

def log_message(speaker, message):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    conversation_history.append({"time": timestamp, "speaker": speaker, "message": message})
    logging.info(f"{speaker}: {message}")

def build_context_history(limit=5):
    recent_history = conversation_history[-limit:]
    return "\n".join([f"{entry['speaker']}: {entry['message']}" for entry in recent_history])

def main():
    console.print("[bold green]Welcome to Terminal Chatbot![/bold green]")
    console.print("[italic]Powered by LangChain Core Templates, Ollama, and Rich[/italic]\n")

    model_name = console.input("[bold blue]Enter the model name: [/bold blue]")

    try:
        llm = OllamaLLM(model=model_name)
        console.print(f"[green]Using model:[/green] {model_name}")
    except Exception as e:
        console.print("[red]Error connecting to the Ollama server.[/red]")
        console.print("[red]Ensure you've started the Ollama server and instlled the model that you've given in the model input.[/red]")
        sys.exit(1)

    template = (
        "You are a hyper super chatbot with extensive knowledge, a vibrant personality, "
        "and the ability to maintain context over multiple interactions.\n"
        "Below is the recent conversation history (if any), followed by the user's new query.\n\n"
        "Conversation History:\n{history}\n\n"
        "User Query: {user_input}\n"
        "Response:"
    )
    prompt_template = PromptTemplate(template=template, input_variables=["history", "user_input"])

    console.print("\n[bold cyan]Chat Interface[/bold cyan] (type 'help' for available commands)")

    while True:
        user_input = console.input("[bold yellow]You:[/bold yellow] ").strip()

        if user_input.lower() in ["exit", "quit"]:
            console.print("[bold magenta]Goodbye![/bold magenta]")
            break
        elif user_input.lower() == "help":
            print_help()
            continue
        elif user_input.lower() == "history":
            display_history()
            continue
        elif user_input.lower() == "reset":
            clear_history()
            continue
        elif user_input.lower() == "clear":
            console.clear()
            continue

        log_message("User", user_input)
        history_context = build_context_history(limit=5)
        prompt = prompt_template.format(history=history_context, user_input=user_input)

        try:
            #
            response = llm.invoke(prompt)
        except Exception as e:
            console.print("[red]An error occurred while processing your input.[/red]")
            console.print("[red]Ensure you've started the Ollama server. and entered the model name that you've installed via ollama.[/red]")
            logging.error("LLM error: " + str(e))
            continue

        log_message("Bot", response)
        md = Markdown(response)
        console.print(md)

if __name__ == "__main__":
    main()
