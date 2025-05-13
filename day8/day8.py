from flask import Flask, request, jsonify, Response
import random

app = Flask(__name__)

@app.route('/w/<city>')
def weather(city):
    response_format = request.args.get('format', 'json').lower()
    temperature = f"{random.randint(15, 45)}°C"

    if response_format == 'xml':
        xml_response = f"""
        <weather>
            <city>{city}</city>
            <temperature>{temperature}</temperature>
            <unit>celsius</unit>
        </weather>
        """
        return Response(xml_response.strip(), mimetype='application/xml')
    else:
        return jsonify({
            "city": city,
            "temperature": temperature,
            "unit": "celsius"
        })

if __name__ == '__main__':
    app.run(debug=True)
