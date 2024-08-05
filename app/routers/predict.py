from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/prediction", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/prediction", response_class=HTMLResponse)
async def predict_datapoint(request: Request, 
                            gender: str = Form(...), 
                            ethnicity: str = Form(...), 
                            parental_level_of_education: str = Form(...),
                            lunch: str = Form(...), 
                            test_preparation_course: str = Form(...), 
                            reading_score: int = Form(...), 
                            writing_score: int = Form(...)):
    data = CustomData(gender=gender, 
                      race_ethnicity=ethnicity, 
                      parental_level_of_education=parental_level_of_education, 
                      lunch=lunch, 
                      test_preparation_course=test_preparation_course, 
                      reading_score=reading_score, 
                      writing_score=writing_score)
    pred_df = data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    return templates.TemplateResponse("index.html", {"request": request, "results": results})
