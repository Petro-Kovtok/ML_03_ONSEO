import logging
from  fastapi import FastAPI
from fastapi.responses import JSONResponse

from .modules.api_data_models  import Message, TextInput, TextOutput
from .modules.simple_ml_models import SentimentModel

DEFAULT_RESPONSES = {
    500: {"model": Message}
}

logging.basicConfig(
    format="[%(asctime)s][%(name)s][%(levelname)s]~%(message)s",
    level=logging.INFO
)

logger = logging.getLogger()

app = FastAPI()
app.model = SentimentModel() # assign model as a field of FastAPI-class object 

@app.get("/api/v1/health", response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info("Health check.")

    return Message(message="Success.")

@app.post("/api/v1/predict", response_model=TextOutput, responses={**DEFAULT_RESPONSES})
def predict(text_input: TextInput):
    logger.info("Predict.")

    try:
        sentiment, score = app.model(text=text_input.content).values()        
        return TextOutput(sentiment=sentiment, score=score)
        
    except Exception as exception:
        logger.exception(str(exception))
        return JSONResponse(status_code=500, content={"message":  str(exception)})
        
