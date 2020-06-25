from flask import Flask, render_template, session, url_for, redirect, flash
import pickle
from form import DSForm
from model import return_prediction


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route("/",methods=['GET','POST'])
def index():

    form = DSForm()

    if form.validate_on_submit():
        try:
            session['Rating'] = float(form.Rating.data)
            session['num_comp'] = float(form.num_comp.data)
            session['hourly'] = float(form.hourly.data)
            session['same_state'] = float(form.same_state.data)
            session['age'] = float(form.age.data)
            session['python_yn'] = float(form.python_yn.data)
            session['spark'] = float(form.spark.data)
            session['aws'] = float(form.aws.data)
            session['excel'] = float(form.excel.data)
            desc_len = len(form.desc.data)
            session['desc_length'] = float(desc_len)
            session['size'] = form.size.data
            session['type_of_ownership'] = form.type_of_ownership.data
            session['Industry'] = form.Industry.data
            session['Sector'] = form.Sector.data
            session['Revenue'] = form.Revenue.data
            session['job_state'] = form.job_state.data
            session['job_simp'] = form.job_simp.data
            session['seniority'] = form.seniority.data

            return redirect(url_for("predict"))

        except ValueError:
            flash('Invalid Input', 'danger')

    return render_template('home.html',form=form)

file_name = "models/model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

@app.route('/predict', methods=['GET'])
def predict():
    content = {}
    hourly_yn = 0
    try:
        content['Rating'] = float(session['Rating'])
        content['num_comp'] = float(session['num_comp'])
        content['hourly'] = float(session['hourly'])
        content['same_state'] = float(session['same_state'])
        content['age'] = float(session['age'])
        content['python_yn'] = float(session['python_yn'])
        content['spark'] = float(session['spark'])
        content['aws'] = float(session['aws'])
        content['excel'] = float(session['excel'])
        content['desc_length'] = float(session['desc_length'])
        content['size'] = session['size']
        content['type_of_ownership'] = session['type_of_ownership']
        content['Industry'] = session['Industry']
        content['Sector'] = session['Sector']
        content['Revenue'] = session['Revenue']
        content['job_state'] = session['job_state']
        content['job_simp'] = session['job_simp']
        content['seniority'] = session['seniority']

        if content['hourly'] == 1.0:
            hourly_yn = 1


        results = return_prediction(model, content)
    except KeyError:
        flash('Please give some input first.', 'danger')
        return redirect(url_for("index"))

    return render_template('prediction.html', results=results, hourly_yn=hourly_yn)

@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)