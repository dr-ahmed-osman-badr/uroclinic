from curses import echo
import datetime
import uuid
from email.policy import default
from venv import create
from xmlrpc.client import boolean
from django.db import models

# from django.db import models

   
    
class Patient(models.Model):
    class gender_choices(models.IntegerChoices):
        Male = 0, ('Male')
        Female = 1, ('Female')
    class insurance_choices(models.IntegerChoices):
        Pension = 0, ('Pension')
        Worker = 1, ('Worker')
        Child = 2, ('Child') 
        Widow = 3, ('Widow') 
        
    class place_choices(models.IntegerChoices):
        giza = 0, ('Giza')
        cairo = 1, ('Cairo')
        banisweef = 2, ('Bani sweef')
        elfayoom = 3, ('Elfayoom')
        elmania  = 4, ('Elmania')
        asyut  = 5, ('Asyut')
        sohag  = 6, ('Sohag')
        luxor  = 7, ('Luxor')
        qina  = 8, ('Qina')
        aswan  = 9, ('Aswan')
        elwahat  = 10, ('Elwahat')
        eldelta  = 11, ('Eldelta')
        elqahira_elgedida  = 12, ('Elqahira_Elgedida')
        others  = 13, ('Others')
    
    class tel_choices(models.IntegerChoices):
        Himself = 0, ('Himself')
        Child = 1, ('Son OR Daughter')
        Parent = 2, ('Parent')
        Brother = 3, ('Brother')
        Other = 4, ('Other')
        
    class medical_choices(models.IntegerChoices):
        No_med = 0, ('None')
        HTN = 1, ('HTN')
        DM = 2, ('DM')
        IHD = 3, ('IHD')
        CKD = 4, ('CKD')
        Liver = 5, ('Liver')
        Thyroid = 6, ('Thyroid')
        Chest = 7, ('Chest')
        Immune = 8, ('Immune Diseases')
        Other = 9, ('Other')
        
    class virus_choices(models.IntegerChoices):
        No_virus = 0, ('None')
        HCV = 1, ('HCV')
        HBV = 2, ('HBV')
        AIDS = 3, ('AIDS')
        Other = 4, ('Other')
        
    class drug_choices(models.IntegerChoices):
        No_drug = 0, ('None')
        Anticoaglants = 1, ('Anticoaglants')
        Aspocid = 2, ('Aspocid')
        HTN = 3, ('HTN')
        DM = 4, ('DM')
        IHD = 5, ('IHD')
        Neuro = 6, ('Neuro')
        Thyroid = 7, ('Thyroid')
        Other = 8, ('Other')
        
        
        
    name = models.CharField(max_length=200, unique=True) ###########
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    serial_number = models.IntegerField(unique=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        if self.serial_number is None:
            max_serial = Patient.objects.aggregate(models.Max('serial_number'))['serial_number__max']
            self.serial_number = (max_serial or 0) + 1
        super().save(*args, **kwargs)
    
    
    gender = models.IntegerField( choices=gender_choices.choices, default=gender_choices.Male)
    birthday_month = models.IntegerField(default=1)
    birthday_year = models.IntegerField(default=1900)
    places = models.IntegerField( choices=place_choices.choices, default=place_choices.giza)
    insurance = models.IntegerField( choices=insurance_choices.choices, default=insurance_choices.Pension)
    insurance_nu = models.CharField(max_length=200, default='')
    admission_day_nu = models.IntegerField( null=True, blank=True, default= 0)
    admission_day_nu_day = models.DateField(auto_now=False, auto_now_add=False,default=datetime.date(2000, 1, 1))
    
    tel1 = models.CharField(max_length=200,null=True, blank=True, default= '0')
    tel1_ch = models.IntegerField( choices=tel_choices.choices, default=tel_choices.Himself)
    tel2 = models.CharField(max_length=200,null=True, blank=True, default= '0')
    tel2_ch = models.IntegerField( choices=tel_choices.choices, default=tel_choices.Himself)
    tel3 = models.CharField(max_length=200,null=True, blank=True, default= '0')
    tel3_ch = models.IntegerField( choices=tel_choices.choices, default=tel_choices.Himself)
    tel4 = models.CharField(max_length=200,null=True, blank=True, default= '0')
    tel4_ch = models.IntegerField( choices=tel_choices.choices, default=tel_choices.Himself)
    
    
    medical_history1 = models.IntegerField( choices=medical_choices.choices, default=medical_choices.No_med)
    medical_history2 = models.IntegerField( choices=medical_choices.choices, default=medical_choices.No_med)
    medical_history3 = models.IntegerField( choices=medical_choices.choices, default=medical_choices.No_med)
    medical_history4 = models.IntegerField( choices=medical_choices.choices, default=medical_choices.No_med)
    medical_history_notes = models.TextField(null=True, blank=True)
    
    virus_1 = models.IntegerField( choices=virus_choices.choices, default=virus_choices.No_virus)
    virus_2 = models.IntegerField( choices=virus_choices.choices, default=virus_choices.No_virus)
    virus_notes = models.TextField(null=True, blank=True)
    
    drug_history1 = models.IntegerField( choices=drug_choices.choices, default=drug_choices.No_drug)
    drug_history2 = models.IntegerField( choices=drug_choices.choices, default=drug_choices.No_drug)
    drug_history3 = models.IntegerField( choices=drug_choices.choices, default=drug_choices.No_drug)
    drug_history4 = models.IntegerField( choices=drug_choices.choices, default=drug_choices.No_drug)
    drug_history5 = models.IntegerField( choices=drug_choices.choices, default=drug_choices.No_drug)
    drug_history_notes = models.TextField(null=True, blank=True)
    
    surgical_history = models.TextField(null=True, blank=True)
    
    
    # date_cr = models.DateTimeField(auto_now_add=True)
    # date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    

    

class Admission(models.Model):
    class Admission_for_choices(models.IntegerChoices):
        operation = 0, ('Operation')
        medical = 1, ('Medical treatment')
        investigation = 2, ('Investigation')
        observation = 3, ('Under observation')
        
    class From_where_admission(models.IntegerChoices):
        clinic = 0, ('Clinic')
        er = 1, ('ER')
        request = 2, ('Request from others')
        
    class Admission_status(models.IntegerChoices):
        listed = 0,('Decisioned for Operation')
        appointment = 1, ('Appointment has taken')
        processing = 2, ('Processing admission')
        impending = 3, ('Impending admission')
        admitted = 4, ('Admitted')
        discharged = 5, ('Discharged')
        rejected = 6, ('Rejected')
        referred = 7, ('Referred')
    class Operation_choices(models.IntegerChoices):
        no_op = 0, ('No Operation')
        viu = 1, ('VIU')
        urethroplasty = 2, ('Urethroplasty')
        hypospadius = 3, ('Hypospadius')
        meatoplasty = 4, ('Meatoplasty')
        urethro_litholapexy = 5, ('Urethro_litholapexy')
        
        cysto_litholapexy = 6, ('Cysto_litholapexy')
        cysto_lithotomy = 7, ('Cysto_lithotomy')
        turt_first = 8, ('TURT first time')
        turt_folowup = 9, ('TURT follow up')
        turp = 10, ('TURP')
        postturp_obst = 11, ('Post_TURP obstruction')
        tvp = 12, ('Transvesical prostatectomy tvp')
        bladder_injury = 13, ('Exploration bladder injury')
        
        pcnl = 14, ('PCNL')
        pcn = 15, ('PCN')
        dj_fix = 16, ('DJ fixation')
        dj_remove = 17, ('DJ removal')
        dj_exchange = 18, ('DJ exchange')
        urs_rgp = 19, ('URS + RGP')
        uretero_litholapexy = 20, ('URS')
        uretero_lithotomy = 21, ('Uretero_lithotomy')
        flexible_laser = 22, ('Flexible and Laser')
        renal_injury = 23, ('Exploration Renal injury')
        uretero_uretral_anastomosis = 24, ('Uretero_uretral anastomosis')
        endo_ureterotomy = 25,('Endo_ureterotomy')
        
        
        pyeloplasty = 26, ('Pyeloplasty')
        endo_pyelotomy = 27, ('Endo_pyelotomy')
        pyelo_lithotomy = 28, ('Pyelo_lithotomy')
        utertro_lithotomy_upper = 29, ('Utertro_lithotomy upper')
        utertro_lithotomy_middel = 30, ('Utertro lithotomy middel')
        utertro_lithotomy_lower = 31, ('Utertro lithotomy lower')
        ureteral_injury = 32, ('Exploration ureteral injury')
        
        nephrectomy = 33, ('Nephrectomy')
        nephro_ureterectomy = 34, ('Nephro_ureterectomy')
        hydrocele = 35, ('Hydrocele')
        varicocele = 36, ('Varicocele')
        orchiaectomy = 37, ('Orchiaectomy')
        testicular_abcess = 38,('Testicular abcess')
        testicular_haematoma_evacuation = 39, ('Testicular_haematoma_evacuation')
        cystectomy = 40, ('Cystectomy')
        
        suprapubic = 41, ('Suprapubic')
        catheterfix = 42, ('Catheter fixation')
        
    class Case_choises(models.IntegerChoices):
        no_op = 0,('No Operation')
        short = 1, ('Short case')
        long = 2, ('Long case')
        dr_mahmoud = 3, ('Dr Mahmoud Ahmed')
        
    class Side_choices(models.IntegerChoices):
        nad = 0, ('NOT Applicable')
        right = 1, ('Right')
        left = 2, ('Left')
        bil = 3,('Bilateral')
        
        
    class Fitness_choices(models.IntegerChoices):
        fit = 0, ('FIT')
        not_assessed = 1, ('Not assessed')
        sent = 2, ('Sent for assessment')
        
    class urgent_choises(models.IntegerChoices):
        no_op = 0, ('No Operation')
        elective = 1, ('Elective')
        urgent = 2, ('Urgent')
        emergent = 3, ('Emergent')
        
    class Operation_status_choises(models.IntegerChoices):
        preparation = 0, ('Preparation for operation')
        done = 1, ('Done')
        postponed = 2, ('Postponed')


    
        

    admission_for = models.IntegerField(choices=Admission_for_choices.choices, default=Admission_for_choices.operation)
    labs_ECG_consultation_of_admission_are_ready = models.BooleanField(default=False)
    papers_of_admission = models.BooleanField(default=False)
    fitness = models.IntegerField(choices=Fitness_choices.choices, default=Fitness_choices.fit)
    day_of_appointement = models.DateField(auto_now=False, auto_now_add=False) ######
    expected_day_of_admission = models.DateField(auto_now=False, auto_now_add=False) ######
    waiting_list = models.BooleanField(default=False) ##################
    reason = models.CharField(max_length=200, default='',null=True, blank=True)
    is_admission_postponed = models.BooleanField(default=False)
    cause_of_postpone = models.CharField(max_length=200, default='',null=True, blank=True)
    
    
    operation_choice = models.IntegerField( choices=Operation_choices.choices, default=Operation_choices.no_op)
    side_of_operation = models.IntegerField(choices=Side_choices.choices, default=Side_choices.nad)
    case_type_short_or_long = models.IntegerField( choices=Case_choises.choices, default=Case_choises.no_op)#########
    urgent_or_cold = models.IntegerField(choices=urgent_choises.choices, default=urgent_choises.no_op)
    details_of_planned_operation_on_admission = models.TextField(null=True, blank=True)
    surgeon_planned_for_operation = models.CharField(max_length=200, default='',null=True, blank=True)
    
    
    
    admission_status = models.IntegerField( choices=Admission_status.choices, default=Admission_status.listed)######
    day_pt_admitted = models.DateField(auto_now=False, auto_now_add=False)
    from_where_admitted =  models.IntegerField( choices=From_where_admission.choices, default=From_where_admission.clinic)  
    
    
    operation_list_day = models.DateField(auto_now=False, auto_now_add=False) ################  
    
    Operation_status = models.IntegerField(choices=Operation_status_choises.choices, default=Operation_status_choises.preparation)
    
    more_care = models.BooleanField(default=False)

    day_pt_discharged = models.DateField(auto_now=False, auto_now_add=False)
    
    patient = models.ForeignKey(Patient, related_name='admission2patient',on_delete=models.CASCADE)###########
    
    
    
    
    def __str__(self) -> str:
        return f'{Admission.Operation_choices.choices[self.operation_choice][1]}/{self.patient.name}'
    
class Operation(models.Model):
    class Operation_choices(models.IntegerChoices):
        no_op = 0, ('No Operation')
        viu = 1, ('VIU')
        urethroplasty = 2, ('Urethroplasty')
        hypospadius = 3, ('Hypospadius')
        meatoplasty = 4, ('Meatoplasty')
        urethro_litholapexy = 5, ('Urethro_litholapexy')
        
        cysto_litholapexy = 6, ('Cysto_litholapexy')
        cysto_lithotomy = 7, ('Cysto_lithotomy')
        turt_first = 8, ('TURT first time')
        turt_folowup = 9, ('TURT follow up')
        turp = 10, ('TURP')
        postturp_obst = 11, ('Post_TURP obstruction')
        tvp = 12, ('Transvesical prostatectomy tvp')
        bladder_injury = 13, ('Exploration bladder injury')
        
        pcnl = 14, ('PCNL')
        pcn = 15, ('PCN')
        dj_fix = 16, ('DJ fixation')
        dj_remove = 17, ('DJ removal')
        dj_exchange = 18, ('DJ exchange')
        urs_rgp = 19, ('URS + RGP')
        uretero_litholapexy = 20, ('URS')
        uretero_lithotomy = 21, ('Uretero_lithotomy')
        flexible_laser = 22, ('Flexible and Laser')
        renal_injury = 23, ('Exploration Renal injury')
        uretero_uretral_anastomosis = 24, ('Uretero_uretral anastomosis')
        endo_ureterotomy = 25,('Endo_ureterotomy')
        
        
        pyeloplasty = 26, ('Pyeloplasty')
        endo_pyelotomy = 27, ('Endo_pyelotomy')
        pyelo_lithotomy = 28, ('Pyelo_lithotomy')
        utertro_lithotomy_upper = 29, ('Utertro_lithotomy upper')
        utertro_lithotomy_middel = 30, ('Utertro lithotomy middel')
        utertro_lithotomy_lower = 31, ('Utertro lithotomy lower')
        ureteral_injury = 32, ('Exploration ureteral injury')
        
        nephrectomy = 33, ('Nephrectomy')
        nephro_ureterectomy = 34, ('Nephro_ureterectomy')
        hydrocele = 35, ('Hydrocele')
        varicocele = 36, ('Varicocele')
        orchiaectomy = 37, ('Orchiaectomy')
        testicular_abcess = 38,('Testicular abcess')
        testicular_haematoma_evacuation = 39, ('Testicular_haematoma_evacuation')
        cystectomy = 40, ('Cystectomy')
    
        suprapubic = 41, ('Suprapubic')
        catheterfix = 42, ('Catheter fixation')
        
    class Case_choises(models.IntegerChoices):
        no_op = 0,('No Operation')
        short = 1, ('Short case')
        long = 2, ('Long case')
        dr_mahmoud = 3, ('Dr Mahmoud Ahmed')
    class Stent_choices(models.IntegerChoices):
        no = 0, ('No Stent')
        right_catheter = 1, ('Right Stent')
        long_right_catheter = 2, ('Yearly Right Stent')
        left_catheter = 3, ('Left Stent')
        long_left_catheter = 4, ('Yearly Left Stent')
        bilateral_catheter = 5, ('Bilateral Stent')
        long_bilateral_catheter = 6, ('Yearly Bilateral Stent')
    class Side_choices(models.IntegerChoices):
        nad = 0, ('NOT Applicable')
        right = 1, ('Right')
        left = 2, ('Left')
        bil = 3,('Bilateral')
        
    operation_choice = models.IntegerField( choices=Operation_choices.choices, default=Operation_choices.no_op)
    side_of_operation = models.IntegerField(choices=Side_choices.choices, default=Side_choices.nad)
    date_of_operation_done = models.DateField(auto_now=False, auto_now_add=False)
    
    case_type_short_or_long = models.IntegerField( choices=Case_choises.choices, default=Case_choises.no_op)#########
    surgeon_done_it = models.CharField(max_length=200, default='',null=True, blank=True)
    
    
    
    procedure_done_details = models.TextField(default='',null=True, blank=True)
    future_procedure = models.TextField(default='',null=True, blank=True)
    
    
    
    stent = models.IntegerField( choices=Stent_choices.choices, default=Stent_choices.no )
    catheter_fixed = models.BooleanField(default=False)
    drain_1_fixed =  models.BooleanField(default=False)
    drain_2_fixed = models.BooleanField(default=False)
    drain_3_fixed = models.BooleanField(default=False)
    nephrostomy_left_fixed = models.BooleanField(default=False)
    nephrostomy_right_fixed = models.BooleanField(default=False)
    
    
    
    Patient = models.ForeignKey(Patient, related_name='operation2patient',on_delete=models.CASCADE)###########
    admission = models.ForeignKey(Admission, related_name='operation2admission',on_delete=models.CASCADE)################
    
def __str__(self) -> str:
        return f'{self.date_of_operation_done}/{Admission.Operation_choices.choices[self.operation_choice][1]}'
    
    
    
class One_day_inward(models.Model):
    
   
        
    day_nu = models.IntegerField()
    post_op_day_nu = models.IntegerField(default=0)
    bed_in_depart = models.BooleanField(default=True)########
    if_outside_where = models.CharField(max_length=200, default='',null=True, blank=True)###########
    
    catheter_amount =  models.TextField( default='',null=True, blank=True)
    
    drain_1_amount =  models.TextField( default='',null=True, blank=True)
    
    drain_2_amount = models.TextField( default='',null=True, blank=True)
    
    drain_3_amount = models.TextField( default='',null=True, blank=True)
    
    nephrostomy_left_amount = models.TextField(default='',null=True, blank=True)
    
    nephrostomy_right_amount = models.TextField(default='',null=True, blank=True)
    
    local_examination = models.TextField( default='',null=True, blank=True)

    instructions = models.TextField( default='',null=True, blank=True)
    requests = models.TextField( default='',null=True, blank=True)
    drugs_blood_dialysis = models.TextField( default='',null=True, blank=True)
    discharge = models.BooleanField(default=False)
    admission = models.ForeignKey(Admission,related_name='onedayinward2admission', on_delete=models.CASCADE)################
    date = models.DateField(auto_now=False, auto_now_add=True)####################
    
    def __str__(self) -> str:
        return f'{self.admission}'
    
class Labs(models.Model):
    
    hb = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    htc = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    tlc = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    plt = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    urea = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    creat = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    na = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    k = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    alt = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    ast = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    pc = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    psa = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    inr = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    
    otherlabs = models.TextField(default='',null=True, blank=True)
    
    Patient = models.ForeignKey(Patient, related_name='labs2patient',on_delete=models.CASCADE)#############
    admission = models.ForeignKey(Admission,related_name='labs2admission', on_delete=models.CASCADE, null=True,blank=True)############
    one_day_inward = models.ForeignKey(One_day_inward,related_name='labs2onedayinward', on_delete=models.CASCADE, null=True,blank=True)#############
    
    date = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.date}'
        
class Images(models.Model):
    
    class Image_choises(models.IntegerChoices):
        us_abdomenal = 0, ('Abdomenal ultrasoun')
        ctut = 1, ('CTUT')
        ct_with_contrast = 2, ('CT with contrast')
        renal_scan = 3, ('Renal scan')
        trus = 4, ('TRUS')
        trus_biopsy = 5, ('TRUS biopsy')
        ivp = 6, ('IVP')
        ascendin_cysto_urethrogram = 7, ('Ascendin cysto_urethrogram')
        nephrostogram = 8, ('Nephrostogram')
        bone_scan = 9, ('Bone Scan')
        pet_scan = 10 , ('PET scan')
        us_scrotal = 11, ('Scrotal ultrasound')
        us_duplex_scrotal = 12, ('Duplex scrotal')
        us_doppler_ll = 13, ('Doppler lower limb')
        echo_cardio = 14, ('Echo')
        ecg = 15, ('ECG')
        chest_xray = 16, ('Chest xray')
        chest_ct = 17, ('CT Chest')
        other = 18, ('Other')
        
    image_type = models.IntegerField(choices=Image_choises.choices, default=Image_choises.us_abdomenal)
    details = models.TextField( default='',null=True, blank=True)
    
    Patient = models.ForeignKey(Patient,related_name='images2patient', on_delete=models.CASCADE)############
    admission = models.ForeignKey(Admission,related_name='images2admission', on_delete=models.CASCADE, null=True,blank=True)############
    one_day_inward = models.ForeignKey(One_day_inward,related_name='images2onedayinward', on_delete=models.CASCADE, null=True,blank=True)##############
    
    date = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self) -> str:
        return f'{self.date} / {Images.Image_choises.choices[self.image_type][1]}'
    
class Consultation(models.Model):
    type_of_consultation = models.CharField(max_length=200,default='')
    respond = models.TextField( default='',null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    Patient = models.ForeignKey(Patient,related_name='consultation2patient', on_delete=models.CASCADE)############
    admission = models.ForeignKey(Admission,related_name='consultation2admission', on_delete=models.CASCADE, null=True,blank=True)############
    one_day_inward = models.ForeignKey(One_day_inward,related_name='consultation2onedayinward', on_delete=models.CASCADE, null=True,blank=True)##############
    
    def __str__(self) -> str:
        return f'{self.date}/ {self.type_of_consultation}'
    
class Calender_appointments(models.Model):
    
    date = models.DateField(auto_now=False, auto_now_add=False)#################
    
    surgeon_notes = models.CharField(max_length=250, default='',null=True, blank=True)
    
    holiday_detail =  models.CharField( max_length=200,default='',null=True, blank=True)
    holiday_in_admission_day_detail = models.CharField( max_length=200,default='',null=True, blank=True)
    
    holiday =  models.BooleanField( default=False)
    holiday_in_admission_day =  models.BooleanField( default=False)
    deep_clean =  models.BooleanField( default=False)
    ramadan = models.BooleanField(default=False)
    
    
    
    
    dr_Mahmoud_op1 = models.OneToOneField(Admission,related_name='dr_mahmoud_op1', on_delete=models.SET_NULL,null=True, blank=True)
    dr_Mahmoud_op2 = models.OneToOneField(Admission,related_name='dr_mahmoud_op2', on_delete=models.SET_NULL,null=True, blank=True)
    long_op1 = models.OneToOneField(Admission,related_name='long_op1', on_delete=models.SET_NULL,null=True, blank=True)
    long_op2 = models.OneToOneField(Admission,related_name='long_op2', on_delete=models.SET_NULL,null=True, blank=True)
    long_op3 = models.OneToOneField(Admission,related_name='long_op3', on_delete=models.SET_NULL,null=True, blank=True)
    long_op4 = models.OneToOneField(Admission,related_name='long_op4', on_delete=models.SET_NULL,null=True, blank=True)
    short_op1 = models.OneToOneField(Admission,related_name='short_op1', on_delete=models.SET_NULL,null=True, blank=True)
    short_op2 = models.OneToOneField(Admission,related_name='short_op2', on_delete=models.SET_NULL,null=True, blank=True)
    short_op3 = models.OneToOneField(Admission,related_name='short_op3', on_delete=models.SET_NULL,null=True, blank=True)
    short_op4 = models.OneToOneField(Admission,related_name='short_op4', on_delete=models.SET_NULL,null=True, blank=True)
    short_op5 = models.OneToOneField(Admission,related_name='short_op5', on_delete=models.SET_NULL,null=True, blank=True)
    short_op6 = models.OneToOneField(Admission,related_name='short_op6', on_delete=models.SET_NULL,null=True, blank=True)
    short_op7 = models.OneToOneField(Admission,related_name='short_op7', on_delete=models.SET_NULL,null=True, blank=True)
    short_op8 = models.OneToOneField(Admission,related_name='short_op8', on_delete=models.SET_NULL,null=True, blank=True)
    short_op9 = models.OneToOneField(Admission,related_name='short_op9', on_delete=models.SET_NULL,null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.date)




class List_of_days_inward(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)###########
    day_related = models.ManyToManyField(One_day_inward, blank=True)#############3
    
    def __str__(self) -> str:
        return str(self.date)   
    
    
