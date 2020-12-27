# Copy right free reverse image search

Spice up your creation with original infrequently used unsplash photo's!


## Dataset

Run `bash setup.sh` to download the [dataset](https://github.com/unsplash/datasets) of of 25k nature-themed Unsplash photos.


## Image Embeddings

Create the python envirment

Run script to generate image embeddings for the dataset and train an annoy index


## Deployment

Build the image, copying in the annoy index

Database to lookup image ID's.


### Run on AWS



## Improvments

- Retrain annoy index for new photos
- Endpoint to store new photos to S3, retrain when # of photos passes threshold
- Kubernetes clusters to load Annoy index from S3






