# Design Overview

The code is designed to create a simple Django REST API that can store paragraphs and their corresponding words, and can search for the paragraphs that contain a given word.

The code consists of the following files:

> Dockerfile: This file defines the Docker image that the application will run in.
> docker-compose.yml: This file defines the Docker Compose configuration for the application.
> requirements.txt: This file lists the Python dependencies required by the application.
> manage.py: This is the main Django management script.
> codemonk/: This is the main Django application directory.
> settings.py: This file contains the main Django settings for the application.
> urls.py: This file defines the main URL routes for the application.
> views.py: This file contains the main view functions for the application.
> models.py: This file defines the Django models used by the application.

The application consists of two main models: **Paragraph** and **Word**. The Paragraph model represents a paragraph of text, and contains a text field that stores the actual text of the paragraph. The Word model represents a word within a paragraph, and contains a word field that stores the word itself, as well as foreign keys to the Paragraph and Position models to indicate the position of the word within the paragraph.

The main view functions of the application are defined in views.py. These functions handle the creation of new paragraphs and words, as well as the search functionality.

Running the Code
To run the code, you will need to have Docker and Docker Compose installed on your system. Once you have those installed, follow these steps:

Clone the repository to your local machine:

> git clone https://github.com/DeepVasoya08/codemonk.git
> cd codemonk/
> docker-compose up

# API USAGE & DOCS

> https://documenter.getpostman.com/view/13201003/2s93Y3vLZ3
