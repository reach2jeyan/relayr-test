
FROM python:3.7
ADD . /tests
WORKDIR /tests
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN pytest webtest_google.py --headful --browser firefox
RUN pytest --html=genreapireport.html backendtest_genre.py || pytest --html=storyapireport.html backendtest_story.py 
# || to ensure the docker does not exit