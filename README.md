# 🚀 CrewAI Article Generator

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)  
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](../../issues)  
[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange)](https://streamlit.io/)

> 👋 **Developer's Note**: As a beginner developer passionate about AI, I created this project as part of my learning journey. I'm excited to grow and improve my skills while contributing to the AI community. Any feedback or suggestions are greatly appreciated!

---

## 📑 Table of Contents

- [✨ Features](#features)
- [🔧 Prerequisites](#prerequisites)
- [📥 Installation](#installation)
- [🚀 Usage](#usage)
- [🧩 How It Works](#how-it-works)
- [📂 Project Structure](#project-structure)
- [📚 Dependencies](#dependencies)
- [🤝 Contributing](#contributing)
- [📄 License](#license)
- [🙏 Acknowledgments](#acknowledgments)

---

## ✨ Features<a name="features"></a>

- **🧠 Multi-Agent Collaboration**
  - **Content Planner**: Strategizes and outlines the article using real-time web research.
  - **Content Writer**: Crafts the main content with creativity and up-to-date information.
  - **Editor**: Refines, polishes, and fact-checks content against reliable sources.
  
- **🌐 Intelligent Web Research**
  - Real-time web searching for current information
  - Fact verification from multiple sources
  - Integration with Serper API for accurate search results

- **🎨 User-Friendly Interface**
  - Built with **Streamlit** for a smooth, intuitive experience.

- **⚡ Groq Integration**
  - Powered by **Groq's llama3-8b-8192** model for blazing-fast content generation.

- **📈 Real-Time Progress**
  - See dynamic updates during article generation and research.

---

## 🔧 Prerequisites<a name="prerequisites"></a>

- Python **3.12** or higher
- A valid **Groq API key** ([Sign up here](https://groq.com))
- A valid **Serper API key** ([Sign up here](https://serper.dev))
- `pip` installed (Python package manager)

---

## 📥 Installation<a name="installation"></a>

Follow these steps to get started:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd CREW_AI
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

---

## 🚀 Usage<a name="usage"></a>

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

3. Enter your desired article topic, click **"Generate Article"**, and watch as the AI crew:
   - Researches current information about your topic
   - Gathers relevant facts and examples
   - Creates a well-structured article with verified information

---

## 🧩 How It Works<a name="how-it-works"></a>

| Phase            | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Research**     | The agents gather current information from the web using Serper search.     |
| **Planning**     | The **Content Planner** structures the article using researched material.    |
| **Writing**      | The **Content Writer** creates content with verified facts and examples.     |
| **Editing**      | The **Editor** fact-checks and refines the article for accuracy.            |

---

## 📂 Project Structure<a name="project-structure"></a>

```
CREW_AI/
├── app.py             # Main application file
├── requirements.txt   # List of dependencies
├── .env               # Environment variables (user-created)
└── README.md          # Project documentation
```

---

## 📚 Dependencies<a name="dependencies"></a>

- `crewai==0.28.8`
- `crewai_tools==0.1.6`
- `langchain_community==0.0.29`
- `langchain-groq==0.0.1`
- `python-dotenv==1.0.0`
- `beautifulsoup4>=4.12.3`
- `requests>=2.31.0`

---

## 🤝 Contributing<a name="contributing"></a>

As an aspiring developer eager to learn and grow, I warmly welcome contributions of all kinds! Whether you're an experienced developer or a fellow learner, your insights can help make this project better.

Ways to contribute:
- Provide feedback and suggestions for improvement
- Share best practices and coding tips
- Report bugs or issues
- Submit pull requests
- Offer mentorship and guidance

Let's learn and build together! 🌱

---

## 📄 License<a name="license"></a>

This project is licensed under the **MIT License**.  
See the full license details [here](./LICENSE).

---

## 🙏 Acknowledgments<a name="acknowledgments"></a>

- 💡 [CrewAI](https://github.com/joaomdmoura/crewAI) — for the powerful multi-agent framework
- 🎨 [Streamlit](https://streamlit.io/) — for providing a beautiful and simple front-end platform
- ⚡ [Groq](https://groq.com/) — for the robust and high-speed LLM APIs

---

> Crafted with passion and technology 💻✨ by leveraging the power of collaborative AI.

