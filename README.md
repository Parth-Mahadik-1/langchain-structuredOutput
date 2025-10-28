# LangChain Structured Output

This repository explores the **Structured Output** concept in **LangChain**, focusing on how different parser types help extract structured data from language model responses. The goal is to understand and demonstrate how to convert raw model outputs into well-defined formats like **Pydantic**, **TypedDict**, and **JSON** — especially when working with **open-source models** that are not highly fine-tuned.

---

## 🚀 Overview

LangChain provides a way to get **structured responses** from models instead of plain text.  
This project explores and implements the following:

- **Structured Output** in LangChain  
- **Output Parsers** — `StrOutputParser`, `PydanticOutputParser`, and `JsonOutputParser`  
- **Data Types** — `TypedDict`, `Pydantic`, and `JSON` formats  
- Demonstration using **open-source Hugging Face models** (not fine-tuned for structured data but integrated with LangChain’s parsing utilities)

---

## 📚 Topics Covered

### 1. Structured Output
Understanding the concept of structured outputs and why they’re important when working with LLMs for predictable and machine-readable results.

### 2. Output Types
- **TypedDict Output**
- **Pydantic Model Output**
- **JSON Output Format**

### 3. Parsers
Exploration of different parser types and their usage:
- `StrOutputParser`
- `PydanticOutputParser`
- `JsonOutputParser`

### 4. Demonstration
A hands-on example showing how to use **`StrOutputParser`** to convert LLM responses into structured text formats.

---

## 🧠 Example Demonstration

Here’s a simple demonstration using **`StrOutputParser`**:

```
from langchain.output_parsers import StrOutputParser

# Initialize parser
parser = StrOutputParser()

# Example model output (simulated)
raw_output = "User Name: Parth Mahadik, Role: Data Scientist"

# Parsing raw text
structured_output = parser.parse(raw_output)

print(structured_output)
```
---
```
output 
## User Name: Parth Mahadik, Role: Data Scientist
```

📸 Parser Output Screenshots
Below are the four main demonstrations with their outputs.
Replace the placeholders below with your actual screenshot paths after uploading them to the screenshots/ folder.

### 1️  Normal StrOutputParser using result.content
  
<p align="center">
  <img src="https://github.com/Parth-Mahadik-1/langchain-structuredOutput/blob/main/normal%20str%20output.png" />
</p>

---

### 2️ LangChain Core StrOutputParser function
  
<p align="center">
  <img src="https://github.com/Parth-Mahadik-1/langchain-structuredOutput/blob/main/normal%20str%20output.png" />
</p>

---

### 3️ JsonOutputParser
  
<p align="center">
  <img src= />
</p>

---

### 4 PydanticOutputParser
  
<p align="center">
  <img src="https://github.com/Parth-Mahadik-1/langchain-structuredOutput/blob/main/pydantic%20ouput%20.png" />
</p>

---
