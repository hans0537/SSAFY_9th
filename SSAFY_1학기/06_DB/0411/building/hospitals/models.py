from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name} 전문의'
    
class Patient(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    # 하나의 관계테이블에 서로 역참조 이므로
    # 객체.필드명.all() 하려면 Doctor에도 patients를 주어야 하므로
    # through를 통해 추가 정보를 담은 관계 테이블도 연결 가능
    # doctors = models.ManyToManyField(Doctor, related_name='patients')
    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 관계 테이블 따로 생성
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id} 번 의사의 {self.patient_id}번 환자'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id} 번 의사의 {self.patient_id}번 환자'
