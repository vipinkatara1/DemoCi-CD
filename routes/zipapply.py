from fastapi import APIRouter, Depends, status, Request, HTTPException
from fastapi.responses import JSONResponse
from repository import zipapplyrepository
from repository.utils import generate_CV_response
from schemas.schema import MainBody
from fastapi.encoders import jsonable_encoder
from loggers.logconfig import formatter, handler
import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

router = APIRouter(prefix="/task", tags=['Zipapply'])


@router.post('/cv_gen', status_code=status.HTTP_200_OK)
async def cv_generation(body: MainBody):
    try:
        logger.info(
            f"------------- Post Request for Cover letter generation received -------------")
        body = body.model_dump()
        logger.info(
            f"------------- Request body received is: '{body}' -------------")
        logger.info(
            f"------------- Now calling main_func function to extract relevant information from the request body -------------")
        relevant_body = await zipapplyrepository.main_func(body)
        logger.info(
            f"------------- Relevant body extracted is: '{relevant_body}' -------------")
        logger.info(
            f"------------- Now calling generate_CV_response function to get response from ai -------------")
        start = time.time()
        res = generate_CV_response(relevant_body)
        end = time.time()
        prompt_response = res["content"]
        prompt_tokens = res["prompt_tokens"]
        prompt_completion_tokens = res[
            "completion_tokens"]
        prompt_total_tokens = res[
            "total_tokens"]
        logger.info(
            f"------------- Response has been received from ai and took '{end-start} seconds' -------------")
        logger.info(
            f"------------- Prompt tokens taken is: '{prompt_tokens}' -------------")
        logger.info(
            f"------------- Prompt completion tokens taken is: '{prompt_completion_tokens}' -------------")
        logger.info(
            f"------------- Total tokens taken is: '{prompt_total_tokens}' -------------")
        logger.info(
            f"------------- Post Request for Cover letter generation is ended -------------")
        return jsonable_encoder({"ai_response": prompt_response})
    except Exception as e:
        logger.error(
            f"------------- Exception occured by error : '{e}' -------------")
        logger.info(
            f"------------- Post Request for Cover letter generation is ended -------------")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
