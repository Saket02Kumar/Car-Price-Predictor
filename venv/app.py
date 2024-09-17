# from flask import Flask,render_template
# import pandas as pd


# app = Flask(__name__)
# car = pd.read_csv("Cleaned_Car_data.csv")
# @app.route('/')
# def index():
#     companies=sorted(car['company'].unique())
#     car_models=sorted(car['name'].unique())
#     year=sorted(car['year'].unique(),reverse=True)
#     fuel_type=car['fuel_type'].unique()
#     return render_template('index.html',companies=companies,car_models=car_models,years=year,fuel_type=fuel_type)

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template
# import pandas as pd

# app = Flask(__name__)
# car = pd.read_csv("Cleaned_Car_data.csv")

# @app.route('/')
# def index():
#     companies = sorted(car['company'].unique())
#     car_models = sorted(car['name'].unique())
#     year = sorted(car['year'].unique(), reverse=True)
#     fuel_type = car['fuel_type'].unique()
#     return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_type=fuel_type)

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the car data
car = pd.read_csv("Cleaned_Car_data.csv")

# @app.route('/')
# def index():
#     companies = sorted(car['company'].unique())
#     car_models = sorted(car['name'].unique())
#     years = sorted(car['year'].unique(), reverse=True)
#     fuel_types = car['fuel_type'].unique()
    
#     # Render template with car data
#     return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_types=fuel_types)

# if __name__ == '__main__':
#     app.run(debug=True)



@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()
    
    print('Companies:', companies)  # Add this line
    print('Car Models:', car_models)  # Add this line
    print('Years:', years)  # Add this line
    print('Fuel Types:', fuel_types)  # Add this line

    return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_types=fuel_types)

