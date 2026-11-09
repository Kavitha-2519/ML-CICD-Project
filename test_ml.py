from ml_app import model

def test_prediction():
    prediction = model.predict([[6]])

    assert abs(prediction[0] - 12) < 0.01

    print("Test Passed Successfully!")

if __name__ == "__main__":
    test_prediction()