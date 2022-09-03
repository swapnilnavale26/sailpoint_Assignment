FROM python:latest

RUN pip install requests
RUN pip install PrettyTable

WORKDIR /usr/app/src

COPY listPullRequest.py ./

CMD [ "python3", "./listPullRequest.py"]
