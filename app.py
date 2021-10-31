from flask import Flask, jsonify

app = Flask(__name__)

students = [{"name":"AMGOTH PUSHPALATHA", "id":"20Q61A6601", "DOB": "2003-04-18", "email":"AMGOTHPUSHPALATHA47@GMAIL.COM", "mobile number":6281339106, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"BALAGONI ANILGOUD", "id":"20Q61A6602", "DOB": "2002-06-02", "email":"Balagonianilgoud@gmail.com", "mobile number":9014156204, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"RUTHVIK BEMIDI", "id":"20Q61A6603", "DOB": "2003-06-12", "email":"ruthvik4215@gmail.com", "mobile number":8978897687, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"DURGAM SWAMY", "id":"20Q61A6604", "DOB": "2002-02-13", "email":"DURGAMSWAMY30@GMAIL.COM", "mobile number":9381984083, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"G DIWAKAR", "id":"20Q61A6605", "DOB": "2003-06-08", "email":"DEEPAKREDDY8038@GMAIL.COM", "mobile number":7093768540, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"GANURE DINESH", "id":"20Q61A6606", "DOB": "2002-02-19", "email":"DINESHGANURE143@GMAIL.COM", "mobile number":9100821043, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"JELLA PRIYANKA", "id":"20Q61A6607", "DOB": "2002-09-29", "email":"PRIYANKAJELLA632@GMAIL.COM", "mobile number":96031545281, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"KALALI VINESH GOUD", "id":"20Q61A6608", "DOB": "2003-06-05", "email":"VINESHKALALI93@GMAIL.COM", "mobile number":8688704203, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"KARAKATLA VYSHNAVI", "id":"20Q61A6609", "DOB": "2003-04-08", "email":"VYSHNAVIKARAKATLA@GMAIL.COM", "mobile number":9014514763, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"KAVALI MADHU", "id":"20Q61A6610", "DOB": "2001-06-29", "email":"mudhirajmadhu25@gmail.com", "mobile number":8106047282, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":None, "id":"20Q61A6611", "DOB": None, "email": None, "mobile number": None, "Aadhaar": None, "branch": None, "collage": None},
            {"name":"LOLAM SRIHARI", "id":"20Q61A6612", "DOB": "2000-01-01", "email":"KAPILLOLAM@GMAIL.COM", "mobile number":8499047325, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"MOHAMMED UMAN", "id":"20Q61A6613", "DOB": "2002-04-26", "email":"UMAN4U26@GMAIL.COM", "mobile number":7032349731, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"NELAVALLI DINESH CHOWDARY", "id":"20Q61A6614", "DOB": "2003-05-26", "email":"DINESHCHOWDARYNELAVALLI@GMAIL.COM", "mobile number":9347783989, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"PARSHA VAMSHI KRISHNA", "id":"20Q61A6615", "DOB": "2002-07-21", "email":"KANNAPATELP0105@GMAIL.COM", "mobile number":9949153930, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"PARUPALLY GIRIJA", "id":"20Q61A6616", "DOB": "2002-10-18", "email":"PARUPALLYGIRIJA@GMAIL.COM", "mobile number":7036347237, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"SAPAVATH LOKESH", "id":"20Q61A6617", "DOB": "2002-11-29", "email":"LOKESHSAPAVATH@GMAIL.COM", "mobile number":9392611868, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"SHARMA MEENAKSHI", "id":"20Q61A6618", "DOB": "2001-10-13", "email":"KITTUSHARMA1105@GMAIL.COM", "mobile number":6303060236, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"SURYADEVARA UJWALA", "id":"20Q61A6619", "DOB": "2001-11-11", "email":"UJWALACHOWDARY8@GMAIL.COM", "mobile number":9347614929, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"VENKAIAHGARI VINAY", "id":"20Q61A6620", "DOB": "2003-07-16", "email":"VINAYVENKAIAHGARI@GMAIL.COM", "mobile number":7993590823, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"YELPULA SAITEJA", "id":"20Q61A6621", "DOB": "2002-08-11", "email":"YELPULASAITEJA11@GMAIL.COM", "mobile number":8247014793, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"BHAGATH VAMSHI", "id":"20Q61A6622", "DOB": "2002-11-17", "email":"VAMSHIBHAGATHKING@GMAIL.COM", "mobile number":9014266539, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"CHINTHAKINDI MURARI", "id":"20Q61A6623", "DOB": "2002-12-17", "email":"MURARIIGOUD46@GMAIL.COM", "mobile number":9676283486, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"DUDDUKURI SANDEEP", "id":"20Q61A6624", "DOB": "2001-11-07", "email":"SANDEEP123CHOWDARY@GMAIL.COM", "mobile number":8179102595, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"GOSHIKA SHIVA KRISHNA", "id":"20Q61A6625", "DOB": "2001-08-21", "email":"SHIVAKRISHNAGOSHIKA@GMAIL.COM", "mobile number":7032646508, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"KATEPALLY SAI KUMAR", "id":"20Q61A6626", "DOB": "2002-09-25", "email":"SAIKUMARKATEPALLY58@GMAIL.COM", "mobile number":9515326229, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"KOPISETTI JOSHNA SATWIKA", "id":"20Q61A6627", "DOB": "2003-05-21", "email":"JOSHNASATWIK@GMAIL.COM", "mobile number":9030508289, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"ODDHI VIGNESH", "id":"20Q61A6628", "DOB": "2003-08-11", "email":"VIGNESHODDHI@GMAIL.COM", "mobile number":9391638527, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"PADAMATI KARTHIK REDDY", "id":"20Q61A6629", "DOB": "2002-06-15", "email":"KJARTHIREDDY1650@GMAIL.COM", "mobile number":9951935939, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"SANKU VAISHNAVI", "id":"20Q61A6630", "DOB": "2002-04-01", "email":"YSHNAVI.SANKU@GMAIL.COM", "mobile number":9493685484, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"SUNKOJU HARINI", "id":"20Q61A6631", "DOB": "2003-08-22", "email":"adityakadali988@gmail.com", "mobile number":8328339842, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"VEERAMALLA RAMU", "id":"20Q61A6632", "DOB": "2003-04-09", "email":"VIRAMALLARAMUGOUD5655@GMAIL.COM", "mobile number":9133929998, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"},
            {"name":"BALU REDDY PRAKASH", "id":"20Q61A6633", "DOB": "2003-04-11", "email":"BALUREDDYPRAKASH582@GMAIL.COM", "mobile number":9550963652, "Aadhaar":275589540151, "branch":"CSM", "collage":"AVIH"}]

@app.route('/')
def index():
  return f"Hello my name is ruthvik"


@app.route('/students', methods=['GET'])
def get():
  return jsonify(students)

@app.route('/student/<student_id>', methods=['GET'])
def get_student_details(student_id):
  for i in students:
    if(student_id.upper() == i['id']):
      data = i;
  return jsonify(data)

if __name__ == "__main__":
  app.run(debug=True)