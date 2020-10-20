FROM python:3.8-alpine AS build
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk update \
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple -r /requirements.txt \
    && mkdir -p /install/lib/python3.8/site-packages \
    && cp -rp /usr/local/lib/python3.8/site-packages /install/lib/python3.8

FROM python:3.8-alpine
COPY --from=build /install/lib /usr/local/lib
WORKDIR /app
COPY app.py /app
COPY templates /app/templates
COPY util.py /app
EXPOSE 6200
CMD python app.py