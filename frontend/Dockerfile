FROM nginx:1.21-alpine

RUN rm -rf /usr/share/nginx/html/*

ADD . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]