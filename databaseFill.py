# coding: utf-8

# In[5]:


import sys
import getopt
import http.client
import urllib
import json
from random import randint
from random import choice
from datetime import date
from time import mktime


# In[33]:


def main(argv):
    # Server Base URL and port
    baseurl = "localhost"
    port = 4000

    # Python array containing name and email and password
    names = ['Kelvin', "james", "john", "robert", "michael", "william", "david", "richard", "charles", "joseph"]

    # Server to connect to (1: url, 2: port number)
    conn = http.client.HTTPConnection(baseurl, port)

    # HTTP Headers
    headers = {"Content-type": "application/json", "Accept": "text/plain"}

    # Array of user IDs
    userIDs = []
    userNames = []
    userEmails = []

    for i in range(len(names)):
        params = json.dumps(
            {'isStudent': 'false', 'name': names[i], 'email': names[i] + "@illinois.edu", 'password': '123'})

        # POST the user
        conn.request("POST", "/api/user/create", params, headers)
        response = conn.getresponse()
        data = response.read()
        d = json.loads(data)

        # Store the users id
        userIDs.append(str(d['data']['_id']))
        userNames.append(str(d['data']['name']))
        userEmails.append(str(d['data']['email']))

    graderPost = [
        {'userId': userIDs[0],
         'jobName': 'CS101 Intro Computing: Engrg & Sci grader',
         'salary': 1,
         'major': [5, 6, 7, 10],
         'standing': [1, 2, 3],
         'contactEmail': 'Davis@illinois.edu',
         'contactName': 'Davis, N',
         },
        {'userId': userIDs[0],
         'jobName': 'CS 126 Software Design Studio grader',
         'salary': 1,
         'major': [6],
         'standing': [0, 1, 2, 3],
         'contactEmail': 'Evans@illinois.edu',
         'contactName': 'Evans, G',
         },
        {'userId': userIDs[0],
         'jobName': 'CS 242 Programming Studio grader',
         'salary': 1,
         'major': [6],
         'standing': [1, 2, 3],
         'contactEmail': 'Woodley@illinois.edu',
         'contactName': 'Woodley, M',
         },
        {'userId': userIDs[0],
         'jobName': 'CS 357 Numerical Methods I grader',
         'salary': 1,
         'major': [5, 6, 10],
         'standing': [1, 2, 3],
         'contactEmail': 'Silva@illinois.edu',
         'contactName': 'Silva, M',
         },
        {'userId': userIDs[1],
         'jobName': 'CS 374 Introduction to Algorithms & Models of Computation assistants',
         'salary': 1,
         'major': [5, 6],
         'standing': [1, 2, 3],
         'contactEmail': 'Borisov@illinois.edu',
         'contactName': 'Borisov, N',
         },
        {'userId': userIDs[1],
         'jobName': 'CS 410 Text Information Systems grader',
         'salary': 1,
         'major': [5, 6],
         'standing': [1, 2, 3],
         'contactEmail': 'Zhai@illinois.edu',
         'contactName': 'Zhai, C',
         },
        {'userId': userIDs[1],
         'jobName': 'CS 412 Introduction to Data Mining grader',
         'salary': 1,
         'major': [5, 6],
         'standing': [1, 2, 3],
         'contactEmail': 'jiawei@illinois.edu',
         'contactName': 'Han, J',
         },
        {'userId': userIDs[1],
         'jobName': 'CS 413 Intro to Combinatorics grader',
         'salary': 1,
         'major': [5, 6],
         'standing': [1, 2, 3],
         'contactEmail': 'james@illinois.edu',
         'contactName': 'james, J',
         },
        {'userId': userIDs[2],
         'jobName': 'CS 450 Numerical Analysis',
         'salary': 1,
         'major': [5, 6, 10],
         'standing': [1, 2, 3],
         'contactEmail': 'Olson@illinois.edu',
         'contactName': 'Olson, L',
         },
        {'userId': userIDs[5],
         'jobName': 'CS498AML grader',
         'salary': 1,
         'major': [5, 6],
         'standing': [1, 2, 3],
         'contactEmail': 'William@illinois.edu',
         'contactName': 'William, K',
         },
        {'userId': userIDs[5],
         'jobName': 'CS 425 Distributed Systems grader',
         'salary': 1,
         'major': [5, 6, 7],
         'standing': [1, 2, 3],
         'contactEmail': 'Gupta@illinois.edu',
         'contactName': 'Gupta, I',
         },
        {'userId': userIDs[5],
         'jobName': 'CS 438 Communication Networks',
         'salary': 1,
         'major': [5, 6],
         'standing': [1, 2, 3],
         'contactEmail': 'AlHassani@illinois.edu',
         'contactName': 'Al-Hassanieh, H',
         },
        {'userId': userIDs[6],
         'jobName': 'CHEM 102 General Chemistry I grader',
         'salary': 1,
         'major': [1, 2, 3, 11],
         'standing': [0, 1, 2, 3],
         'contactEmail': 'Huang@illinois.edu',
         'contactName': 'Huang, T',
         },
        {'userId': userIDs[6],
         'jobName': 'CHEM 104 General Chemistry II grader',
         'salary': 1,
         'major': [1, 2, 3, 11],
         'standing': [0, 1, 2, 3],
         'contactEmail': 'Marville@illinois.edu',
         'contactName': 'Marville, K',
         },
        {'userId': userIDs[7],
         'jobName': 'PHYS 211 University Physics: Mechanics grader',
         'salary': 1,
         'major': [0, 4, 8, 9, 12],
         'standing': [0, 1, 2, 3],
         'contactEmail': 'Gadway@illinois.edu',
         'contactName': 'Gadway, B',
         },
        {'userId': userIDs[7],
         'jobName': 'PHYS 212 University Physics: Elec & Mag grader',
         'salary': 1,
         'major': [0, 4, 8, 9, 12],
         'standing': [1, 2, 3],
         'contactEmail': 'Stelzer@illinois.edu',
         'contactName': 'Stelzer, T',
         },
        {'userId': userIDs[8],
         'jobName': 'TAM 212 Introductory Dynamics assistants',
         'salary': 1,
         'major': [3, 4, 10, 11, 13],
         'standing': [1, 2, 3],
         'contactEmail': 'William@illinois.edu',
         'contactName': 'William, K',
         },
        {'userId': userIDs[8],
         'jobName': 'TAM 335 Introductory Fluid Mechanics assistants',
         'salary': 1,
         'major': [3, 4, 10, 11, 13],
         'standing': [1, 2, 3],
         'contactEmail': 'Freund@illinois.edu',
         'contactName': 'Freund, J',
         }
    ]
    for i in range(len(graderPost)):
        graderPost[i][
            'description'] = 'Grading Quizzes, Exams, require less than 6 hr/week, Must getting A and above for the course'
        graderPost[i]['type'] = 0
        graderPost[i]['term'] = 2

    # Loop 'taskCount' number of times
    for i in range(len(graderPost)):
        # POST the task
        conn.request("POST", "/api/posts/add", json.dumps(graderPost[i]), headers)
        response = conn.getresponse()
        data = response.read()
        d = json.loads(data)

    researchPost = [
        {'userId': userIDs[9],
         'jobName': 'UNDERGRADUATE RESEARCH ASSISTANT (Energy Transport Research Laboratory)',
         'description': 'This project involves flow boiling of refrigerants in modified internal tubes. Heat transfer coefficients, pressure drops and temperature fluctuations would be measured to compare the performance of these modified tubes to those of internal tubes. \n The undergraduate researcher\'s primary responsibility would be to assist in running the experiments. The student would be trained and shown how to run tests for the first few weeks. Surface fabrication and data analysis would also be integral components of this project. Start date is summer and research credits via an independent study would be given for summer. The researcher can opt to stay on for future semesters, if interested. ',
         'type': 2,
         'salary': 1,
         'major': [3, 9, 11],
         'standing': [1, 2, 3],
         'term': 1,
         'contactEmail': userEmails[0],
         'contactName': userNames[0],
         },
        {'userId': userIDs[9],
         'jobName': 'RESEARCH ASSISTANT (Radiation Surface Science and Engineering Laboratory)',
         'description': 'Work with a state-of-the-art surface analysis facility to evaluate material response/evolution as they are subject to different simulated environments, in particular, those pertaining to plasma-material interactions in fusion energy applications. Design, manufacture and characterize novel material systems with enhanced performance in the harsh environments found in fusion energy devices.',
         'type': 2,
         'salary': 1,
         'major': [11, 13],
         'standing': [1, 2, 3],
         'term': 2,
         'contactEmail': 'kapat2@illinois.edu',
         'contactName': 'Aveek Kapat',
         },
        {'userId': userIDs[8],
         'jobName': 'RESEARCH ASSISTANT (Data Analysis and Programming)',
         'description': 'Fertilizer use remains below recommended rates in most of Sub-Saharan Africa, contributing to low agricultural productivity, pervasive poverty, and food insecurity. Small farmers have voiced suspicion that fertilizer is often adulterated, and evidence suggests that these suspicions lead to inefficient fertilizer use: too much in some cases, and too little in others. A key problem is that the quality and efficacy of mineral fertilizer, its available nutrient content, is unobservable to the uninformed eye at the point of purchase. For example: though urea fertilizer should contain 46% nitrogen, that content cannot be evaluated with the naked eye. This problem, along with weak regulation and poor enforcement of product standards, provides opportunities for cheating in the market by adulteration (dilution); and awareness of that possibility seems to drive suspicion among farmers.\n We have developed and will field-test a machine-learning based, automated, rapid-response fertilizer quality verification service that farmers in sub-Saharan Africa can use to accurately assess the nutrient content of fertilizer at the point of purchase. A farmer transmitting a photograph of mineral fertilizer for sale receives, via text message, an immediate evaluation of the fertilizer’s nutrient content. This service will allow farmers to identify adulterated fertilizer prior to purchase. The tool allows farmers to improve their understanding of unobservable nutrient quality and by serving as de facto quality certification, the tool will ameliorate asymmetric information problems between agro-dealers and farmers, thereby improving market functioning and decreasing incentives for sellers to adulterate fertilizer.\nWe are looking for a student to work with us on developing the front-end and back-end of a website. Front-end integration includes the capabilities for a farmer to upload a fertilizer photo to the website via text message. On clicking the "submit" button a web-service would be called which will predict the adulteration status by running our machine learning model (already built) and display/send via text this result back to the farmer. Back-end integration includes the creation of a database to store all received photos and the corresponding model output for each photo. We also want to collect and store information about the geo-location of the farmer uploading the query and the results of the analysis.',
         'type': 2,
         'salary': 1,
         'major': [5, 6, 10, 14],
         'standing': [1, 2, 3],
         'term': 2,
         'contactEmail': 'hopecm@illinois.edu',
         'contactName': 'Hope Michelson',
         },
        {'userId': userIDs[8],
         'jobName': 'SUMMER UNDERGRADUATE RESEARCH IN PHARMACOLOGY & CANCER BIOLOGY',
         'description': 'Duke University\'s Department of Pharmacology and Cancer Biology runs the Summer Undergraduate Research in PHarmacology and Cancer Biology (SURPH) fellowship program, which targets rising juniors and seniors at any U.S. university or college who are interested in future graduate study to obtain a PhD.\nThe 10-week summer research experience focuses on learning how scientific discovery at the bench can be translated to treatment of disease. Students will train with a faculty mentor and carry out an independent research project in Duke’s Department of Pharmacology and Cancer Biology.\nSURPH fellows will be 1) immersed in areas of biomedical science such as pharmacology that are not readily accessible on undergraduate campuses, 2) exposed to the connection between biomedical research and drug discovery, and 3) given networking opportunities to pursue graduate study in biomedical science.',
         'type': 2,
         'salary': 0,
         'major': [2, 3],
         'standing': [1, 2],
         'term': 1,
         'contactEmail': userEmails[8],
         'contactName': userNames[8],
         },
        {'userId': userIDs[7],
         'jobName': 'RESEARCH ASSISTANT (Sottos-White Research Group)',
         'description': ' The research project proposes to develop microcapsules that exhibit controlled response to pH stimuli (i.e., acidic/basic conditions). These microcapsules can then be incorporated into other materials for developing smart multifunctional materials or drug carriers. One of the applications being explored here is the use of these microcapsules to develop smart self-protecting and self-healing coating systems which can release anti-corrosive agents to local sites when an acidic pH is encountered during the onset of pitting corrosion. This can drastically reduce maintenance and testing costs associated with corrosion due to increased lifetime of these coatings.\nThe goals of the project include to synthesize pH responsive polymers and then successfully encapsulate model cargo materials in these polymeric shells. These microcapsules would then be incorporated into commercial coatings and its stability will be investigated. The release profiles would also be characterized by studying the dissolution of the polymer in acidic aqueous media.',
         'type': 2,
         'salary': 1,
         'major': [3, 11, 12],
         'standing': [1, 2, 3],
         'term': 1,
         'contactEmail': 'thakare2@illinois.edu',
         'contactName': 'Dhawal Thakare',
         },
        {'userId': userIDs[7],
         'jobName': 'RESEARCH ASSISTANT (Jensen Lab)',
         'description': 'Successful candidates will help us combine robotics, machine learning, and computational biology to automate biomedical discovery. The software engineering team will\n 1. Design databases for storing, processing, and mining phenotypic and imaging data \n 2. Interface commercial and custom laboratory robots, sensors, and instruments\n 3. Build workflows and interfaces for managing large biological screening experiments\n Multiple openings for undergraduate software engineers. ',
         'type': 2,
         'salary': 1,
         'major': [5, 6],
         'standing': [1, 2, 3],
         'term': 1,
         'contactEmail': 'openings@jensenlab.net',
         'contactName': 'Paul Jensen',
         },
        {'userId': userIDs[6],
         'jobName': 'REU ON THE INTERNET OF THINGS (IoT) AT UCF',
         'description': 'The Computer Science Department at the University of Central Florida (Orlando, FL) will hold an 8‐week, 2019 Summer Research Experience for Undergraduates (REU) on the Internet of Things (IoT). REU students will be trained in research‐based theory and applications of IoT technologies, which extends the connected nature of computing devices to objects of the physical world. The REU students will join well‐established research groups under the close supervision of faculty with expertise in various IoT research areas such as smart cities, smart healthcare, and smart grids. Many of the research topics will require the students to utilize state-of-the-art techniques of artificial intelligence, machine learning and data analytics.',
         'type': 2,
         'salary': 2,
         'major': [4, 5, 6, 7, 12],
         'standing': [1, 2, 3],
         'term': 1,
         'contactEmail': 'turgut@cs.ucf.edu',
         'contactName': 'Damla Turgut',
         },
        {'userId': userIDs[6],
         'jobName': 'RESEARCH ASSISTANT (Smart Structures Technology Laboratory)',
         'description': 'Image annotator. The Smart Structures Technology Laboratory (SSTL) is looking for an hourly research assistant to help with image annotation for research towards automated image-based inspection of civil infrastructure. The research assistant will be expected to annotate a few hundred images per week by precisely painting over or highlighting with input tools (similar to MS paint or Photoshop) regions in the image that correspond to certain structural defects or structural components using software tools developed by SSTL researchers. The research assistant will be acknowledged in published research articles and online.',
         'type': 2,
         'salary': 2,
         'major': [4],
         'standing': [0, 1, 2, 3],
         'term': 2,
         'contactEmail': 'hoskere2@illinois.edu',
         'contactName': 'Vedhus Hoskere',
         },
        {'userId': userIDs[5],
         'jobName': 'RESEARCH ASSISTANT (Health Care Engineering Systems Center)',
         'description': 'Summer 2019 part-time undergraduate hourly positions in the area of medical simulation and virtual reality. Experience working in UNITY; prior experience using Steam VR plugin for HTC Vive is highly preferred. Prior knowledge or experience in virtual reality. Willingness to learn and explore new applications for virtual reality in Health Care.',
         'type': 2,
         'salary': 1,
         'major': [2, 5, 6, 7],
         'standing': [1, 2, 3],
         'term': 1,
         'contactEmail': 'hcesc@illinois.edu',
         'contactName': userNames[5],
         },
        {'userId': userIDs[5],
         'jobName': 'UNDERGRADUATE OFFICE ASSISTANT (Undergraduate Research, Engineering)',
         'description': ' Engineering Undergraduate Research is looking for undergraduate students to assist in day-to-day administrative activities during the 2019-2020 academic year. The student assistant will report directly to the coordinator of undergraduate research. This is a paid hourly position with up to 15 hours per week that starts in fall 2019. \nPrimary responsibilities include creating, maintaining and entering information into databases, gathering research-related information, helping prepare for events, performing general office work and other activities as needed.',
         'type': 2,
         'salary': 2,
         'major': [4, 5, 6, 7, 10, 14],
         'standing': [0, 1, 2, 3],
         'term': 2,
         'contactEmail': 'nmamaril@illinois.edu',
         'contactName': 'Dr. Natasha Mamaril',
         }
    ]

    for i in range(len(researchPost)):
        # POST the task
        conn.request("POST", "/api/posts/add", json.dumps(researchPost[i]), headers)
        response = conn.getresponse()
        data = response.read()
        d = json.loads(data)

    # Exit gracefully
    conn.close()
    print(str(len(names)) + " users added at " + baseurl + ":" + str(port))


if __name__ == "__main__":
    main(sys.argv[1:])