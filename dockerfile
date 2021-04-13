FROM continuumio/miniconda3

ENTRYPOINT []
CMD [ "/bin/bash" ]

# Remove (large file sizes) MKL optimizations.
RUN conda install -y nomkl

# install packages by conda
RUN conda install -y numpy scipy scikit-learn cython pandas

# install other dependencies by pip
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt

ADD . /opt/ml_in_app
WORKDIR /opt/ml_in_app

CMD gunicorn webApp:app