FROM alpine:3.20

RUN apk add --no-cache curl

WORKDIR /client

COPY pinger.sh .
RUN chmod +x pinger.sh

CMD ["./pinger.sh"]

