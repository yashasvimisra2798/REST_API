from flask import Flask, jsonify

app = Flask(__name__)

courses = [{'name': "Python Programming Certification",
            'course_id':"0",
            'Description':"Python programming certification helps you learn",
            'price':"visit coursera"},
            {'name': "Perl Programming Certification",
            'course_id':"1",
            'Description':"Perl programming certification helps you learn",
            'price':"visit coursera"},
            {'name': "C++ Programming Certification",
            'course_id':"2",
            'Description':"C++ programming certification helps you learn",
            'price':"visit coursera"}
            ]
# using the GET method
@app.route('/')
def index():
    return "Welcome To The Course API"

@app.route('/courses', methods=['GET'])
def get():
    return jsonify({'Courses':courses})

@app.route("/courses/<int:course_id>",methods=['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})

# using the POST method
@app.route("/courses", methods=['POST'])
def create():
    course = {'name': "C Programming Certification",
            'course_id':"4",
            'Description':"C programming certification helps you learn",
            'price':"visit coursera"}
    
    courses.append(course)
    return jsonify({'Created': course})


#using PUT method
@app.route("/courses/<int:course_id>",methods=["PUT"])
def course_update(course_id):
    courses[course_id]['Description'] = "XYZ"
    return jsonify({'course':courses[course_id]})

#using DELETE nethod
# @app.route("/courses/<int:course_id>",methods=["DELETE"])
# def course_update(course_id):
#     courses.remove(courses[course_id])
#     return jsonify({'result': True})

if __name__ == "__main__":
    app.run(debug=True)