FROM python:3.10

ENV HOME /app_inst
WORKDIR $HOME

COPY requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]