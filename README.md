# avhs-boys-hockey-redirect

## 1. Introduction

This is a simple project to redirect avhockey.com to SportsEngine hosted by the youth organization.



## 2. Development environment setup

Local development can be done using [functions-framework](https://cloud.google.com/functions/docs/functions-framework)

 - Install Python 3.7+
 - Install the dependencies

  ```bash
  pip install functions-framework
  ```

## 3. Run and test the app locally

```bash
./local-dev.sh
```

## 4. Production
The application is packaged in a Docker image and deployed to Cloud Run using a Cloud Build pipeline.

The environment is hosted in the project [avhs-boys-hockey](https://console.cloud.google.com/?project=avhs-boys-hockey)