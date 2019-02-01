"""locations views module.
@todo #29:30min Location page: implement list_locations(),
 create(), edit() and delete() methods, using SQLAlchemy and the location
 model.
@todo #29:30min In the index page it should be possible to sort and filter for
 every column. locations management page should be accessed through the
 Locations page.
@todo #29:30min Update html templates when methods are implemented. Create more
 tests for all methods.
"""
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint("location", __name__, url_prefix="/locations")

@bp.route("/")
def list_locations():
    # remove this dummy locations object and use db
    locations = [{
        "id": 1,
        "location": "Test location",
        "description": "This is a test"
        }]
    return render_template("restaurants/locations/list.html", locations=locations)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        flash("Create not yet implemented")
    action = "create"
    return render_template("restaurants/locations/create_edit.html", action=action)

@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        flash("Edit not yet implemented")
    action = "edit"
    return render_template("restaurants/locations/create_edit.html", action=action)

@bp.route("/delete", methods=["POST"])
def delete():
    flash("Delete not yet implemented")
    return redirect(url_for("location.list_locations"))
