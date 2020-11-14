FROM python:latest
RUN apt-get update -y
RUN apt-get install -y vim jq
COPY . /public_api_automation_project/
WORKDIR /public_api_automation_project
RUN pip install -r /public_api_automation_project/requirements.txt
ENTRYPOINT [ "python3" ]
STOPSIGNAL SIGINT