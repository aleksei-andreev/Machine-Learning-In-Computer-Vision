FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    python3.8 python3-pip python3.8-venv python3.8-dev
RUN apt-get install -y --fix-missing ffmpeg libsm6 libxext6
RUN rm -rf /var/cache/apt/archives \
    && rm -rf /var/lib/apt/lists

RUN python3 -m pip install --upgrade pip

COPY dist/MachineLearninginComputerVision-0.3.0-py3-none-any.whl .
RUN python3 -m pip install MachineLearninginComputerVision-0.3.0-py3-none-any.whl

WORKDIR /demo
COPY src/MachineLearninginComputerVision/web.py /demo

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["web.py"]
