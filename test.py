from flask import Flask
import pickle
import os
import sys

# This new Flask app is just for testing
app = Flask(__name__)

# This is the only route we will use
@app.route('/test')
def test_load_route():
    """
    This function directly tests if the .pkl files can be loaded.
    It bypasses all your other code to find the root cause of the error.
    """
    try:
        print("\n--- STARTING TEST ---")
        
        # Build absolute paths to be 100% sure we are looking in the right place
        preprocessor_path = os.path.abspath(os.path.join('artifacts', 'preprocessor.pkl'))
        model_path = os.path.abspath(os.path.join('artifacts', 'model.pkl'))

        print(f"[*] Attempting to load preprocessor from: {preprocessor_path}")
        
        # Explicitly check if the file exists
        if not os.path.exists(preprocessor_path):
            error_message = f"FILE NOT FOUND: The preprocessor file does not exist at the path: {preprocessor_path}"
            print(f"!!! {error_message} !!!")
            return f"<h1>Error</h1><p>{error_message}</p>"

        # Load the preprocessor
        with open(preprocessor_path, "rb") as file_obj:
            preprocessor = pickle.load(file_obj)
        print("[+] Preprocessor loaded successfully.")

        print(f"[*] Attempting to load model from: {model_path}")
        
        if not os.path.exists(model_path):
            error_message = f"FILE NOT FOUND: The model file does not exist at the path: {model_path}"
            print(f"!!! {error_message} !!!")
            return f"<h1>Error</h1><p>{error_message}</p>"
            
        # Load the model
        with open(model_path, "rb") as file_obj:
            model = pickle.load(file_obj)
        print("[+] Model loaded successfully.")
        
        print("--- TEST PASSED ---")
        return "<h1>✅ Success!</h1> <p>Both model.pkl and preprocessor.pkl were loaded without errors.</p>"

    except Exception as e:
        # If any error happens during the `try` block, it will be caught and displayed
        print(f"\n--- !!! TEST FAILED !!! ---")
        # repr(e) gives a more detailed error representation
        error_details = repr(e) 
        print(error_details)
        
        return f"""
            <h1>❌ Test Failed: An Error Occurred</h1>
            <p>The application crashed while trying to load the model files.</p>
            <p><b>This is the error we were looking for.</b></p>
            <hr>
            <h2>Error Details:</h2>
            <p><b>Error Type:</b> {type(e).__name__}</p>
            <p><b>Message:</b></p>
            <pre style="background-color:#eee; padding:10px; border-radius:5px;">{error_details}</pre>
            <hr>
            <p>Please check your terminal for the full traceback.</p>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)