from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import pickle
import pandas as pd

# load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

tier_1_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata', 'Pune', 'Ahmedabad', 'Surat']
tier_2_cities = ['Lucknow', 'Kanpur', 'Nagpur', 'Indore', 'Thane', 'Bhopal', 'Visakhapatnam', 'Pimpri-Chinchwad',
 'Patna', 'Vadodara', 'Ghaziabad', 'Ludhiana', 'Agra', 'Nashik', 'Faridabad', 'Meerut', 'Rajkot', 'Kalyan-Dombivli', 
 'Vasai-Virar', 'Varanasi', 'Srinagar', 'Aurangabad', 'Dhanbad', 'Amritsar', 'Navi Mumbai', 'Allahabad', 'Ranchi', 'Howrah', 'Coimbatore',
 'Jabalpur', 'Gwalior', 'Vijayawada', 'Jodhpur', 'Madurai', 'Raipur', 'Kota', 'Guwahati', 'Chandigarh', 'Solapur']

# pydantic model for validating the incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user in years")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user in kg")]
    height: Annotated[float, Field(..., gt=0, description="Height of the user in meters")]
    income_lakh_per_annum: Annotated[float, Field(..., gt=0, description="Annual income of the user in lakhs")]
    smoker: Annotated[bool, Field(..., description="Whether the user is a smoker (True/False)")]
    city: Annotated[str, Field(..., description="City where the user resides")]
    occupation: Annotated[Literal['Engineer', 'Doctor', 'Manager', 'Teacher', 'Business', 'Lawyer', 'Designer', 'IT Specialist', 'Trader', 'Student', 'Clerk'], Field(..., description="Occupation of the user")]

    # computed field to calculate BMI
    @computed_field
    @property
    def bmi(self) -> float:
        bmi_value = self.weight / (self.height ** 2)
        return round(bmi_value, 2)
    
    # computed field to compute age_group
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'young'
        elif self.age < 45:
            return 'adult'
        elif self.age < 60:
            return 'middle_aged'
        else:
            return 'senior'
        
    # computed field to compute lifestyle_risk
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return 'high'
        elif self.smoker and self.bmi > 27:
            return 'medium'
        else:
            return 'low'
        
    # computed field to compute city_tier
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
# prediction endpoint
@app.post('/predict')
def predict_premium(user_input: UserInput):
    # prepare the input data for prediction
    input_df = pd.DataFrame([{
        'bmi': user_input.bmi,
        'age_group': user_input.age_group,
        'lifestyle_risk': user_input.lifestyle_risk,
        'city_tier': user_input.city_tier,
        'income_lakh_per_annum': user_input.income_lakh_per_annum,
        'occupation': user_input.occupation,

    }])

    # make the prediction
    predicted_premium_category = model.predict(input_df)[0]

    # return the predicted premium category in json format
    return JSONResponse(status_code=200, content={"predicted_premium_category": predicted_premium_category})