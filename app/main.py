from fastapi import FastAPI

app = FastAPI(
    title='Space Events API',
    description='A read-only REST API that ingests, cleans, and serves space event data from multiple public sources.',
    version='1.0.0',
)
