FROM alpine:3.14

RUN apk update
RUN apk upgrade
RUN apk add bash

COPY loop.sh loop.sh
ENTRYPOINT ["/bin/bash"]
CMD ["loop.sh"]
