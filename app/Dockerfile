# docker build -f Dockerfile -t http-app:latest .
# docker run -p 8001:8000 http-app
# docker build -t http-app-img ./app

FROM Python:3.11.3

LABEL Maintainer='Ilnur T.'

RUN mkdir /app
WORKDIR /app
ADD app.py /app/

EXPOSE 8000

ENTRYPOINT [ '/sbin/tini', '--', 'python3' ]
CMD [ './app.py' ]