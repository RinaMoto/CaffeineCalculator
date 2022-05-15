from flask import Flask
from flask_restful import Api, Resource, reqparse
from pkg_resources import require

PORT_NUM = 3000
MAX_DENSITY = 6       # 6mg/kg of caffeine max
LBS_TO_KG = 0.453592  # kgs per lb

app = Flask(__name__)
api = Api(app)

MaxServings_parser = reqparse.RequestParser()
MaxServings_parser.add_argument("weight", type=float,
help="Weight of person as float is required", required=True)
MaxServings_parser.add_argument("weight_units", type=str,
help="Units of weight as string is required", required=True)
MaxServings_parser.add_argument("content", type=float,
help="Caffeine content of drink as float is required", required=True)
MaxServings_parser.add_argument("content_units", type=str,
help="Units of caffeine content as string is required", required=True)

class MaxServings(Resource):
  def post(self):
    args = MaxServings_parser.parse_args()

    # Convert weight into units of kg
    weight_kg = None
    if args['weight_units'].lower() == 'kg':
      weight_kg = args['weight']
    elif args['weight_units'].lower() in {'lb', 'lbs'}:
      weight_kg = args['weight'] * LBS_TO_KG
    else:
       return {"message": "weight_units not recognized"}, 400

    # Convert drink caffeine content to units of mg
    caffeine_content_mg = None
    if args['content_units'].lower() == 'mg':
      caffeine_content_mg = args['content']
    elif args['content_units'].lower() == 'g':
      caffeine_content_mg = args['content'] * 1000
    else:
      return {"message": "content_units not recognized"}, 400

    # Calculate max servings
    try:
      max_servings = weight_kg * MAX_DENSITY / caffeine_content_mg
      fraction = max_servings - int(max_servings)
      if fraction < 0.25:
        max_servings = f"{int(max_servings)}"
      elif fraction < 0.5:
        max_servings = f"{int(max_servings)}.25"
      elif fraction < 0.75:
        max_servings = f"{int(max_servings)}.5"
      else:
        max_servings = f"{int(max_servings)}.75"
      # Return data
      return {"maxServings": max_servings}, 200
    except:
      return {"message": "calculation failed"}, 400

api.add_resource(MaxServings, "/max")


if __name__ == '__main__':
  app.run(debug=True, port=PORT_NUM)
