#!/bin/bash

wget -O sample.data.gz  https://ai.stanford.edu/~btaskar/ocr/letter.data.gz
untar -xzf sample.data.gz
mv letter.data ../sample
rm sample.data.gz