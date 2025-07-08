from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
import os
from django.conf import settings


# Create your views here.
def home(request):
    return render (request,"home.html")

def about (request):
    return render (request,"about.html")

def degree(request):
    degres_show = [
        {
            'period': 'August 2024 – Present',
            'degree': 'Master’s in General Computer Science with Internship Option',
            'institution': 'Université de Montréal, Faculty of Arts and Science, Montreal, Canada',
            'courses': [
                'IFT 6390: Foundations of Machine Learning Course, Professor Ioannis (Yannis) Mitliagkas.',
                'IFT 6758: Data Science Course , Professor(s) Gauthier Gidel and Glen Berseth.',
                'IFT 6135: representation learning Course , Professor Aaron Courville.',
                'IFT 6289: Natural Language Processing with Deep Learning Course , Professor Bang Liu.',
            ],
            'poster_link': 'https://tonlien.com/poster_if6289'  # Remplace par ton vrai lien
        },
        {
            'period': 'August 2021 – June 2023',
            'degree': 'Master’s Degree in Data Science and Decision-Making Support',
            'institution': 'Cadi Ayyad University, Faculty of Sciences and Techniques of Marrakech (FSTG), Morocco.',
            'mention': 'Mention : Bien',
            'courses': [
                'Statistiques Avancées',
                'Data Mining',
                'Programmation Python pour Data Science',
                'Modélisation et Simulation',
                'Bases de Données',
            ],
            'poster_link': 'https://tonlien.com/poster_master_datascience'  # Remplace par ton vrai lien
        },
        {
            'period': 'August 2017 – June 2021',
            'degree': 'Bachelor\'s Degree (Fundamental License) in Mathematical and Computer Sciences',
            'institution': 'Cadi Ayyad University, Semlalia Faculty of Sciences, Marrakech, Morocco',
            'courses': [
                'Mathématiques Discrètes',
                'Algèbre Linéaire',
                'Programmation Orientée Objet',
                'Introduction aux Bases de Données',
                'Analyse Numérique',
            ],
            'poster_link': 'https://tonlien.com/poster_licence'  # Remplace par ton vrai lien
        },
        {
            'period': 'August 2016 – June 2017',
            'degree': 'High School Diploma in Mathematics – Option A',
            'institution': 'Rahhali Farouk High School, El Attaouia, Kelaa des Sraghna, Morocco',
            'courses': [
                'Mathématiques',
                'Physique',
                'Chimie',
                'Informatique de base',
            ],
            'poster_link': 'https://tonlien.com/poster_bac'  # Remplace par ton vrai lien
        },
    ]

    return render(request, "degree.html", {'degres_show': degres_show})


def projects (request):
    projects_show=[
        {
            'title': 'Analyzing , comparing, customizing and enhancing Emotion Recognition Models.',
            'Course': 'IFT6289 - Winter 2025',
            'Objective': 'This project explores the design and evaluation of emotion recognition models in text, combining psychological insights, deep learning, and hybrid architectures. The goal is to improve emotion detection accuracy while also ensuring models are efficient and deployable in resource-constrained environments.',
            'path': 'images/poster_nlp.jpg',
            'report': 'upload/Final_Repport_IFT6289.pdf',
            'github': 'https://github.com/ouakibamine/IFT6289-H25/tree/main',
            
        },
        {
            'title': 'Predictive Analysis of NHL Games: Data extraction, cleaning, interactive debugging, modeling (XGBoost, LightGBM, SVM, etc.), and performance evaluation (ROC, confusion matrix, accuracy).',
            'Course': 'IFT6390 - Automn 2024',
            'Objective': 'This project leverages NHL data for in-depth game analysis, interactive visualizations, and performance modeling. It involves multiple milestones focusing on data acquisition, processing, modeling, and deployment of predictive models.',
            'path': 'images/rapport3.png',
            'report': 'upload/Final_Repport_IFT6289.pdf',
            'github': 'https://github.com/ouakibamine/nlh-canada-project',
            
        },
         {
            'title': 'Binary text classification (Kaggle) using TF-IDF vectorization and machine learning models, optimized for macro F1-score.',
            'Course': 'IFT6390A - automn 2024',
            'Objective': 'This project explores the design and evaluation of emotion recognition models in text, combining psychological insights, deep learning, and hybrid architectures. The goal is to improve emotion detection accuracy while also ensuring models are efficient and deployable in resource-constrained environments.',
            'path': 'images/rapport.jpg',
            'report': 'upload/Rapport.pdf',
            'github': 'https://github.com/ouakibamine/text-classification',
            
        },
         {
            'title': 'Automatic detection of retinal diseases on OCT images (Kaggle) using convolutional neural networks and transfer learning.',
            'Course': 'IFT6390A - Automn 2024',
            'Objective': 'This project explores the design and evaluation of emotion recognition models in text, combining psychological insights, deep learning, and hybrid architectures. The goal is to improve emotion detection accuracy while also ensuring models are efficient and deployable.',
            'path': 'images/rapport2.jpg',
            'report': 'upload/Rapport2.pdf',
            'github': 'https://github.com/ouakibamine/text-classification',
            
        },
        {
            'title': 'American Key Retailer Data Analytics Project.',
            'Course': 'Data Wherhouse',
            'Objective': 'This is a comprehensive data analytics project focusing on American Key Retailer data. The project involves web scraping, data cleaning, transformation, dashboard building, and insights extraction. We aim to analyze the retailer\'s data to derive insights that can inform decision-making and strategy development.',
            'path': 'images/bi.PNG',
            'report': 'upload/Final_Repport_IFT6289.pdf',
            'github': 'https://github.com/ouakibamine/Data-Analyst-Project-Using-PowerBI/tree/main',
            
        },
        {
            'title': 'Cricket 2022 World Cup Data Analytics Project.',
            'Course': 'Data Wharehouse',
            'Objective': 'This is an end-to-end data analytics project. In this project, we analyze cricket 2022 World Cup data (2022) to assemble the best 11 players team that could potentially play against aliens. The project involves web scraping, data cleaning, transformation, dashboard building, and insights extraction.',
            'path': 'images/page1.PNG',
            'report': 'upload/Final_Repport_IFT6289.pdf',
            'github': 'https://github.com/ouakibamine/Data-Analyst-Project-cricket-world-cup/tree/main',
            
        },
        {
            'title': 'Timetable Scheduler',
            'Objective':'',
            'path': 'images/timtable.PNG',
        },
        {
            'title': 'CRUD',
            'Objective':'',
            'path': 'images/CRUD.PNG',
        },

         {
            'title': 'Photo Uploader',
            'Objective':'',
            'path': 'images/photo_uploader.PNG',
        },
          {
            'title': 'To do list',
            'Objective':'',
            'path': 'images/todolist.PNG',
        },
         {
            'title': 'Portfolio',
            'Objective':'',
            'path': 'images/portfolio.PNG',
        },
                  {
            'title': 'Labour Hiring',
            'Objective':'',
            'path': 'images/labour_hiring.PNG',
        },

    ]
    return render (request,"projects.html",{"projects_show": projects_show})


def experience(request):
    experience = [

     {
    "date": "June 2025 – Present",
    "company": "Dollarama, Montreal, Canada",
    "position": "Cashier and Stock Clerk",
    "tasks": [
        "Handled customer transactions at the register.",
        "Restocked shelves and managed inventory.",
        "Assisted customers with inquiries and provided excellent service.",
        "Maintained cleanliness and organization in the store and stockroom."
    ]
},   
    {
        "date": "September 2024 – Present",
        "company": "Université de Montréal (SAFIRE)",
        "position": "Teaching Assistant",
        "tasks": [
            "Proctored written exams.",
            "Enforced evaluation protocols.",
            "Managed examination procedures."
        ]
    },
    {
        "date": "September 2024 – May 2025",
        "company": "Université de Montréal (DIRO)",
        "position": "Teaching Assistant – Data Structures",
        "tasks": [
            "Led practical sessions on data structures.",
            "Graded and evaluated assignments and Managed examination procedures."
        ]
    },
    {
        "date": "February 2024 – August 2024",
        "company": "TOUM AI, Rabat, Morocco",
        "position": "Data Science Intern",
        "tasks": [
            "Developed an audio transcription model (Moroccan dialect) using PyTorch/TensorFlow.",
            "Fine-tuned models (Whisper, Wav2Vec2) and integrated Azure Cognitive Services.",
            "Performed audio data web scraping from YouTube and built an ETL pipeline."
        ]
    },
    {
        "date": "August 2023 – February 2024",
        "company": "CIMA Solution, Casablanca, Morocco",
        "position": "Data Analyst",
        "tasks": [
            "Collected, analyzed, and visualized data.",
            "Created dashboards with Power BI to analyze trends.",
            "Automated reports using Python and SQL."
        ]
    },
    {
        "date": "February – June 2023",
        "company": "L2IS Lab, Faculty of Sciences and Technology Gueliz (FSTG), Cadi Ayyad University, Morocco",
        "position": "Research Assistant in AI – Water Quality Modeling",
        "tasks": [
            "Preprocessed data: cleaning, normalization, and rebalancing.",
            "Built models for classification, regression, and forecasting.",
            "Performed advanced model optimization (cross-validation, regularization) using Python (TensorFlow, scikit-learn, Pandas, Jupyter, Seaborn)."
        ]
    },
    {
        "date": "May – July 2021",
        "company": "Mathematics and Computer Science Laboratory, Faculty of Sciences Semlalia, Cadi Ayyad University, Morocco",
        "position": "Research Assistant in AI – Computer Vision",
        "tasks": [
            "Designed and deployed a web application for fruit image classification.",
            "Collected and annotated a fruit image dataset.",
            "Developed a CNN model using transfer learning (InceptionV3).",
            "Created an interactive web interface using Flask.",
            "Technologies: Python, TensorFlow, Keras, OpenCV, HTML/CSS, JavaScript."
        ]
    }
]

    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render (request, "certificate.html")



def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)




def upload(request, path):
    # Exemple de fichier attendu : "myapp/Final_Repport_IFT6289.pdf"
    static_path = os.path.join(settings.BASE_DIR,'resume', path)
    
    if os.path.exists(static_path):
        with open(static_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='application/pdf')
    else:
        raise Http404("Report not found")