FROM python:3

ADD src /src

RUN pip install -r requirements.txt

CMD [ "python", "-m", "unittest", "discover", "-s", "unitTests"]