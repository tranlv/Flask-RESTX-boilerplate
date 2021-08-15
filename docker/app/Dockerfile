FROM pypy:3

WORKDIR /opt

ENV PYTHONUNBUFFERED 1

COPY ./app/requirements.txt /opt/

RUN apt-get update -y && apt-get install -y libmemcached-dev

RUN pypy3 -m pip install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt --ignore-installed

ENV TZ=Asia/Ho_Chi_Minh

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime

RUN addgroup app && groupmod -g 1000 app && useradd -ms /usr/sbin/nologin app -g app && usermod -u 1000 app

COPY --chown=app:app . /opt/

WORKDIR /opt

USER app

RUN chmod +x /opt/docker/app/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/opt/docker/app/entrypoint.sh"]
