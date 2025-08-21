from django.urls import path
from . import views

urlpatterns = [
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('doctor-list/', views.doctor_list, name='doctor_list'),
    path('patient-list/', views.patient_list, name='show_patients'),
    path('delete-patient/', views.delete_patient, name='delete_patient'),
    path('show-doctors/', views.show_doctors, name='show_doctors'),
]
