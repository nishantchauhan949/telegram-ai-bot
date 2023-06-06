from setuptools import setup, find_packages


def get_long_description():
    with open("README.md", encoding="UTF-8") as f:
        long_description = f.read()
        return long_description


def get_requirements():
    with open("requirements.txt", 'r') as f:
        pass


setup(
    name="telegram-ai-bot",
    version="0.0.1",
    author="Nishant",
    author_email="nishantchauhan949@hotmail.com",
    description="A python package that create a running Telegram AI Bot using Google Bard",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/nishantchauhan949/telegram-ai-bot",
    packages=find_packages(exclude=['*.env', '*/__pycache__/*', '*.pyc']),
    python_requires=">=3.7",
    install_requires=[
        "httpx[http2]",
        "python-telegram-bot[all]",
        "openai",
        "requests",
        "pyTelegramBotAPI",
        "python-dotenv"
    ],
    dependency_links=[
        'git+https://github.com/dsdanielpark/Bard-API.git',
    ],
    keywords="Python, API, Bard, Google Bard, Large Language Model, Chatbot API, Google API, Chatbot",
    entry_points={"console_scripts": ["telegram_bot=src.ai_telegram_bot_async:main"]},
)
