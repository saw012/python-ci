FROM python:3.9.1

ENV ARG1 1
ENV ARG2 2

WORKDIR /app/
COPY ./requirements.txt .
COPY ./srcs/math_add.py math_add.py

RUN pip install --upgrade pip \
&& pip install -r requirements.txt \
&& groupadd -r test && useradd -r -g test testuser

USER testuser
ENTRYPOINT [ "python","math_add.py"]
CMD ["${ARG1}", "${ARG2}"]