from flask import ( Blueprint, request )
from . import models

bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

@bp.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        submitter = request.form['submitter']
        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        conservation_status = request.form['conservation_status']
        native_habitat = request.form['native_habitat']
        fun_fact = request.form['fun_fact']

        new_reptile = models.Reptile(submitter=submitter, common_name = common_name, scientific_name = scientific_name, conservation_status = conservation_status, native_habitat = native_habitat, fun_fact = fun_fact)
        models.db.session.add(new_reptile)
        models.db.session.commit()
        
        return 'Submitted!'
    
    results = models.Reptile.query.all()
    
    user_dict = {
        'data': []
    }

    for result in results:
        user_dict['data'].append({
            'id': result.id,
            'submitter': result.submitter,
            'common_name': result.common_name,
            'scientific_name': result.scientific_name,
            'conservation_status': result.conservation_status,
            'native_habitat': result.native_habitat,
            'fun_fact': result.fun_fact
        })

    return user_dict

@bp.route('/<int:id>')
def show(id):
    result = models.Reptile.query.filter_by(id=id).first()
    
    result_dict = {
        'id': result.id,
        'submitter': result.submitter,
        'common_name': result.common_name,
        'scientific_name': result.scientific_name,
        'conservation_status': result.conservation_status,
        'native_habitat': result.native_habitat,
        'fun_fact': result.fun_fact
    }

    return result_dict