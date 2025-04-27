import streamlit as st
from crewai import Crew, Agent, Task
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from langchain.tools import Tool

load_dotenv()
llm = ChatGroq(model="llama3-8b-8192", api_key=os.getenv("GROQ_API_KEY"))

# Initialize search tool with proper configuration
search_tool = Tool(
    name="Search",
    func=SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))._run,
    description="Useful for searching the internet for current information. Input should be a search query string."
)

# Define agents with enhanced capabilities
planner = Agent(
    role="Content Planner",
    goal="Research and plan comprehensive content on {topic}",
    backstory="Expert content strategist with years of experience in research and planning. Uses latest information from the web to create comprehensive content plans.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role="Content Writer",
    goal="Write an informative and engaging blog post on {topic} using latest information",
    backstory="Experienced writer with expertise in creating engaging content. Uses research and current information to write comprehensive articles.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

editor = Agent(
    role="Editor",
    goal="Edit and fact-check the blog post ensuring accuracy and quality",
    backstory="Meticulous editor with fact-checking expertise. Verifies information and enhances content quality.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# Define tasks with clear tool usage instructions
plan = Task(
    description="Research the topic thoroughly and create a detailed content plan. Use the Search tool with direct search queries to find current information and trends.",
    expected_output="Detailed content plan with current information and key points to cover.",
    agent=planner
)

write = Task(
    description="Write a comprehensive blog post following the plan. Use the Search tool with specific queries to verify facts and find relevant examples.",
    expected_output="Well-researched blog post in markdown format with current information.",
    agent=writer
)

edit = Task(
    description="Review and fact-check the blog post. Use the Search tool to verify claims and ensure accuracy.",
    expected_output="Polished and fact-checked blog post in markdown format.",
    agent=editor
)

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

st.title("CrewAI Article Generator")
topic = st.text_input("Enter Topic")
if st.button("Generate Article"):
    with st.spinner("Generating article..."):
        try:
            result = crew.kickoff(inputs={"topic": topic})
            st.markdown(result)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            if os.getenv("SERPER_API_KEY") is None:
                st.warning("Please make sure you have set the SERPER_API_KEY in your .env file")