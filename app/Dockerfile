# Необходимо написать Dockerfile для полученного приложения 
# в соответствии с принятыми в сообществе best-practice.

# docker build -f Dockerfile -t http-app:latest .
# docker run -p 5001:8000 http-app

FROM Python:3.11.3

LABEL Maintainer='Ilnur T.'

RUN mkdir /app
WORKDIR /app
ADD app.py /app/

EXPOSE 8000

ENTRYPOINT [ '/sbin/tini', '--', 'python3' ]
CMD [ './app.py' ]