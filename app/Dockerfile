FROM python:3.11.3-alpine

LABEL Maintainer='Ilnur T.'

RUN apk add --no-cache tini

RUN adduser -D runner

RUN mkdir -p /home/runner/app/ && chown -R runner:runner /home/runner/app
WORKDIR /home/runner/app

USER runner

COPY --chown=runner:runner ./app.py ./app.py

EXPOSE 8000

ENTRYPOINT [ "/sbin/tini", "--" ]

CMD [ "python3", "./app.py" ]