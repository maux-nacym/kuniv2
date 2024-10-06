from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Customer, Subscription, Bill

bp = Blueprint('dashboard', __name__)

@bp.route('/')
@login_required
def index():
    total_customers = Customer.query.count()
    total_subscriptions = Subscription.query.count()
    total_bills = Bill.query.count()
    return render_template('dashboard.html', 
                           total_customers=total_customers,
                           total_subscriptions=total_subscriptions,
                           total_bills=total_bills)