# Cloud Machine Learning Engine

https://github.com/cloudacademy/ml-engine-doing-more
https://cloud.google.com/ml-engine/docs/tensorflow/getting-started-training-prediction

```
BUCKET_NAME=gayaba8aa5
REGION=us-east1
gsutil mb -l $REGION gs://$BUCKET_NAME
```

```
gsutil cp "C:\Users\GyanT\Documents\GitHub\BrainSpec\ML\INTERPRET_LC\Database\INTERPRET_DOD_DB.bin" gs://gayaba8aa5/Database/INTERPRET_DOD_DB.bin
```

```
BUCKET_NAME=gayaba8aa5
REGION=us-east1
DATASET=gs://$BUCKET_NAME/Database/INTERPRET_DOD_DB.bin
JOB_NAME=train_interpret22
OUTPUT_PATH=gs://$BUCKET_NAME/$JOB_NAME
```

```
gcloud ml-engine jobs submit training $JOB_NAME \
    --job-dir $OUTPUT_PATH \
    --runtime-version 1.8 \
    --module-name trainer.task \
    --package-path trainer/ \
    --region $REGION \
    --config custom.yaml \
    -- \
    --data-file $DATASET \
    --train-steps 1000 \
    --eval-steps 100 \
    --verbosity DEBUG
```

`gsutil cp -r gs://gayaba8aa5/train_interpret17 C:\Users\GyanT\Documents\GitHub\Artificial-Neural-Network\TensorFlow\TensorFlowGuide\Estimators\interpret\nn`
