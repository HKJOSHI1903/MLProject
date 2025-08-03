# In app.py

from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# It's better to instantiate the pipeline once
predict_pipeline = PredictPipeline()

## Route for a home page

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Correctly get data from the form
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')), # FIX: Was writing_score
            writing_score=float(request.form.get('writing_score'))  # FIX: Was reading_score
        )
        
        pred_df = data.get_data_as_data_frame()
        print("Input DataFrame:")
        print(pred_df)

        try:
            results = predict_pipeline.predict(pred_df)
            # Render the result on the same page
            return render_template('home.html', results=round(results[0], 2))
        except Exception as e:
            print(f"An error occurred during prediction: {e}")
            # Optionally, return an error message to the user
            return render_template('home.html', error=f"Prediction failed: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True) # Use debug=True for development