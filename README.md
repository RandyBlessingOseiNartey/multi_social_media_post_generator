MULTI-SOCIAL MEDIA CONTENT GENERATOR


A LangChain-powered application that takes any text/content, generates a brief summary, and simultaneously creates tailored posts for LinkedIn and Instagram using parallel processing chains.


Features
Sequential Chain: Summarizes the content using Google's Gemini 2.5 Flash Lite.
Parallel Processing: Uses RunnableParallel to generate social media content for multiple platforms at once, reducing total execution time.
Custom Prompt Templates: Specifically tuned "System" messages for LinkedIn (professional) and Instagram (engaging) personas.


Prerequisites
Python 3.9+
Google Gemini API Key


Installation
Clone the repository:
git clone https://github.com/RandyBlessingOseiNartey/multi_social_media_post_generator.git
cd your-repo-name

Install dependencies:
Bash
uv init ( to initialiaze the project)
uv add langchain-google-genai python-dotenv langchain

Set up environment variables:
Create a .env file in the root directory and add your API key:

Plaintext
GOOGLE_API_KEY=your_actual_api_key_here 

How It Works
The project utilizes the LangChain Expression Language (LCEL). The flow is as follows:

Input: Takes a movie title from the user.

Summary: A RunnableLambda generates a summary.

Branching: The summary is passed into RunnableParallel, which triggers two separate chains:

LinkedIn Chain: Formats content for a professional audience.

Instagram Chain: Formats content for a visual/social audience.

Output: Both posts are printed to the console.

Usage
Run the script and enter a movie name when prompted:

Bash
python main.py
