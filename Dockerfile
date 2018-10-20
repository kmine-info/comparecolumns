FROM python:3.5-alpine

ENV PROJECT_Folder /kmine/Vlookup


ADD requirements.txt /requirements.txt
 
RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
            gcc \
            make \
            libc-dev \
            musl-dev \
            linux-headers \
            pcre-dev \
    && pyvenv /venv \
    && /venv/bin/pip install -U pip \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r /requirements.txt" \
    && runDeps="$( \
            scanelf --needed --nobanner --recursive /venv \
                    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                    | sort -u \
                    | xargs -r apk info --installed \
                    | sort -u \
    )" \
    && apk add --virtual .python-rundeps $runDeps \
    && apk del .build-deps
RUN apk add nginx

WORKDIR ${PROJECT_Folder}

EXPOSE 80

RUN mkdir -p /run/nginx
 
ADD . $PROJECT_Folder

WORKDIR src

RUN mkdir media static logs

COPY ./docker-entrypoint.sh /
COPY ./django_nginx.conf /etc/nginx/conf.d/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ENTRYPOINT ["sh","/docker-entrypoint.sh"]