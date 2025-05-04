# TERMBOTS

[![GitHub](https://img.shields.io/badge/Visit-GitHub-black?style=for-the-badge&logo=github)](https://github.com/coder-yogya/Termbots)  
[![Python](https://img.shields.io/badge/Python-3.12.9-yellow?style=for-the-badge&logo=python)](https://www.python.org/)  
[![Pip](https://img.shields.io/badge/Pip-25.0.1-brightgreen?style=for-the-badge)](https://pip.pypa.io/)  
[![Ollama](https://img.shields.io/badge/Ollama-Server-blueviolet?style=for-the-badge)](https://ollama.com/)  
[![LangChain](https://img.shields.io/badge/LangChain-Community-critical?style=for-the-badge)](https://python.langchain.com/)  
[![Rich](https://img.shields.io/badge/Rich-10.0.0-blueviolet?style=for-the-badge)](https://github.com/willmcgugan/rich)

A **terminal chatbot** built using **LangChain Core Templates**, **Ollama**, and **Rich**. This project provides an interactive, context-aware chat interface right in your terminal, complete with advanced commands, conversation history, logging, and dynamic prompt generation.

---

## Overview

This terminal chatbot allows you to:
- Interact with a large language model via the Ollama server.
- Enjoy a colorful terminal UI powered by Rich.
- Maintain context with recent conversation history using LangChain prompt templating.
- Use advanced commands such as `help`, `history`, `reset`, `clear`, and `exit`.
- Change the template in `main.py` to suit your needs.

---

## Prerequisites

- **Ollama**  
  Make sure you have the [Ollama](https://ollama.com/) installed and running on your system.
  
- **System Requirements for Ollama:**  
  The required model for Ollama full may need a specific amount of RAM. Ensure your system meets the necessary RAM requirements for the model you plan to use.

- **Python 3.12.9 (for no errors) & pip 25.0.1 or higher**
- **git**
	for cloning the repo

## Installation (all systems)

1. **Clone the Repository**

   ```bash
   git clone https://github.com/coder-yogya/Termbots.git
   cd Termbots
   pip install -r libs.txt
   ollama serve
   # in a new session run :
   cd Termbots
   python main.py
   ```
---
### How to run it in Termux:
> - Install termux from f-droid
> - **Run the commands below:**
```bash
apt upgrade -y ; apt install binutils python rust clang -y ; apt install python-numpy git -y ; git clone https://github.com/coder-yogya/Termbots.git ; cd Termbots ; pip install -r libs.txt ; clear && python main.py 
```
---
**😁 Fun Fact:** `I've created it in TERMUX :)`

