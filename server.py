from flask import Flask, render_template, request
import csv
app = Flask(__name__)
@app.route('/')
def home ():
     return render_template('index.html');

@app.route('/<string:page_name>')
def html_page (page_name):
     return render_template(page_name);


def write_to_csv(data):
     with open('database.csv', mode='a') as database1:
          email = data['email']
          subject = data['subject']
          message = data['message']
          csv_writer = csv.writer(database1, delimiter ='|',quotechar='"',quoting=csv.QUOTE_MINIMAL )
          csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data =  request.form.to_dict()
        write_to_csv(data)
        return('Thanks!.. We received your message and we will get back to you soon')
    else:
        return 'Something went wrong, try again'

if __name__ == '__main__':
     app.run(debug = True)
