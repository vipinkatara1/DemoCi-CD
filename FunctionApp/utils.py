import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_CV_response(input):

    data = "{'Personal Information': {'fname': 'John', 'lname': 'Garnett', 'picture_url': None, 'gender': 'MALE', 'yob': None, 'experience_years': None, 'phones': [], 'address': {'address_line1': '', 'address_line2': '', 'city': 'Seattle', 'state': 'Washington', 'postal_code': '', 'country_code': 'US', 'country': 'United States'}, 'summary': None}, 'job_desc':{'company_name':'Qualcom','job_title':'Marketing Head','job_location':'Chicago,US','job_type':'Ful Time','job_qualifications':'Work experience as Marketing Professional is preferrable\nExperience running successful marketing campaigns\nLeadership skills with the ability to set and prioritize goals\nAnalytical mind','job_responsibilities':'Craft strategies for all Marketing teams, including Digital, Advertising, Communications and Creative\nPrepare and manage monthly, quarterly and annual budgets for the Marketing department\nSet, monitor and report on team goals\nDesign branding, positioning and pricing strategies\nEnsure our brand message is strong and consistent across all channels and marketing efforts (like events, email campaigns, web pages and promotional material)\nAnalyze consumer behavior and determine customer personas\nIdentify opportunities to reach new market segments and expand market share\nCraft quarterly and annual hiring plans\nMonitor competition (acquisitions, pricing changes and new products and features)\nCoordinate sales and marketing efforts to boost brand awareness\nParticipate in the quarterly and annual planning of company objectives','job_benefits':'Dental insurance\nFlexible spending account\nHealth insurance\nHealth savings account\nLife insurance\nPaid time off\nRetirement plan\nVision insurance'},'experiences': [{'company_fullname': 'Amazon', 'is_current': True, 'title': 'Marketing Professional'}, {'company_fullname': 'Amazon.com, Inc', 'is_current': True, 'title': 'Software Development Engineer'}, {'company_fullname': 'Amazon', 'is_current': True, 'title': 'Team Management'}, {'company_fullname': 'Amazon', 'is_current': True, 'title': 'Sr. Regional Maintenance Manager'}, {'company_fullname': 'Amazon', 'is_current': True, 'title': 'Cofounder'}, {'company_fullname': 'Amazon', 'is_current': True, 'title': 'International Business'}], 'skills': [{'name': 'Management'}, {'name': 'Strategy'}, {'name': 'Financial Analysis'}, {'name': 'Financial Modeling'}, {'name': 'Leadership'}, {'name': 'Strategic Planning'}, {'name': 'Business Strategy'}, {'name': 'Customer Service'}, {'name': 'Logistics'}, {'name': 'Project Management'}, {'name': 'Supply Chain'}], 'educations': [], 'About Military Servings': []}"
    input_ex1 = data

    output_ex1 = f"Dear Hiring Manager,\n\nI am excited to apply for the position of Marketing Head at Qualcom, as advertised on your company's career portal. My name is John Garnett, and I have a diverse background in marketing and leadership roles at Amazon.\n\nWith my experience as a Marketing Professional at Amazon, I have successfully executed and managed various marketing campaigns, resulting in increased brand awareness and customer engagement. I have a strong understanding of crafting effective marketing strategies across multiple channels, including digital, advertising, communications, and creative. Additionally, I have a proven track record of setting and achieving team goals, managing budgets, and analyzing consumer behavior to identify market opportunities.\n\nIn my role as a Software Development Engineer at Amazon.com, Inc, I gained valuable experience in leveraging technology and data analytics to drive marketing initiatives. This experience has equipped me with a unique perspective on integrating technology into marketing strategies to deliver impactful results.\n\nAs a Sr. Regional Maintenance Manager at Amazon, I honed my leadership skills and developed a strategic mindset. I successfully managed teams and collaborated with cross-functional stakeholders to ensure the smooth operation of maintenance processes.\n\nFurthermore, my experience as a co-founder and in international business at Amazon has provided me with a well-rounded understanding of the business landscape and the ability to adapt to diverse environments.\n\nI possess a wide range of skills, including management, strategy development, financial analysis and modeling, leadership, and strategic planning. I am confident that these skills, combined with my strong background in marketing and team management, make me a valuable asset for your organization.\n\nI am impressed by Qualcom's reputation as an industry leader and its commitment to innovation. I am excited about the opportunity to contribute to the growth and success of your company.\n\nThank you for considering my application. I have attached my resume for your review, and I would welcome the opportunity to discuss how my skills and qualifications align with your company's needs. I look forward to the possibility of joining your team.\n\nSincerely,\n\nJohn Garnett"

    input_ex2 = """{"Personal Information": {"fname": "Joseph", "lname": "Mcfarland", "picture_url": "NULL", "gender": "MALE", "yob": "NULL", "experience_years": "NULL", "phones": [], "address": {"address_line1": "", "address_line2": "", "city": "Harford County", "state": "Maryland", "postal_code": "", "country_code": "US", "country": "United States"}, "summary": "Area Maintenance Manager at Air Products"},"job_desc":{"company_name":"Deloitte","job_title":"Area Manager","job_location":"Ohio","job_type":"Ful Time","job_qualifications":"Previous managerial experience is a bonus.\nGood understanding of the technical features of plumbing, carpentry, and electrical systems.\nStrong knowledge facilities machines and equipment.\nExcellent organizational and leadership abilities.\nExceptional communication and interpersonal skills.","job_responsibilities":"Supervising and leading all maintenance processes and operations.\nTracking expenses and overseeing the budget for maintenance.\nMaintaining all machinery to ensure it’s at working standards.\nCreating and implementing maintenance procedures.\nConducting regular inspections of the facilities to detect and resolve problems.\nPlanning and managing all repair and installation activities.\nEnsuring all department workers adhere to the safety policies and procedures.\nAssigning repair schedules and evaluating repair cost estimates.\nDocumenting and preparing daily progress reports and maintenance logs.\nOverseeing equipment stock and placing orders for new supplies when necessary.\n","job_benefits":"Dental insurance\nFlexible spending account\nHealth insurance\nHealth savings account\nLife insurance\nPaid time off\nRetirement plan\nVision insurance"}, "experiences": [{"company_fullname": "Air Products", "is_current": true, "title": "Area Maintenance Manager"}], "skills": [], "educations": [], "About Military Servings": []}"""
    output_ex2 = "Dear Hiring Manager,\n\nI am writing to express my interest in joining your esteemed organization Deloitte for the position of Area Manager , as advertised on your company's career portal. My name is Joseph McFarland, and I am currently working at Air Products in the role of Area Maintenance Manager.\n\nWith my experience in this role, I have developed a strong understanding of maintenance operations of the technical features of plumbing, carpentry, and electrical systems, and I have successfully maintained all machinery to ensure it is at working standards. I have a proven track record of implementing preventive maintenance programs, optimizing equipment performance, and reducing downtime. My expertise lies in identifying and resolving maintenance issues promptly and effectively, while ensuring compliance with safety regulations.Additionally, I have created and implemented maintenance procedures, conducted regular inspections of facilities, and planned and managed repair and installation activities.\n\nI am highly skilled in coordinating with cross-functional teams and external vendors to ensure the timely completion of maintenance projects. I have a keen eye for detail and possess excellent problem-solving abilities, which have enabled me to identify and rectify potential issues before they escalate.\n\nMy commitment to excellence and my ability to work under pressure have consistently allowed me to exceed expectations in my current role. I am confident that my skills and experience make me a strong candidate for the Area Manager position at your organization.\n\nI have attached my resume for your review, and I would welcome the opportunity to discuss how my skills and qualifications align with your company's needs. Thank you for considering my application. I look forward to the possibility of contributing to the success of your organization.\n\nSincerely,\n\nJoseph McFarland"

    prompt = f"""You are excellent in reading resume in json format and converting it into cover letter.
    You will be given the JSON object of the user Resume, your task is to convert that JSON object of that user Resume into cover letter. 
    Please do give importance to the user experiences , skills and military services if any in the cover letter.

    Please refer the "job_desc" key for the Job description for which the user is applying for.

    But if any details is not given or is NULL then kindly ignore it and don't mention in Cover letter. For example if the number of years of experience is not given then no need to give that information.
    
    The cover letter you generate should not exceed 250 words."""

    messages = [
        {"role": "system",
         "content": prompt},
        {"role": "user",
         "content": str(input_ex1),
         },
        {"role": "assistant",
         "content": str(output_ex1)
         },
        {"role": "user",
         "content": str(input_ex2),
         },
        {"role": "assistant",
         "content": str(output_ex2)
         }
    ]

    messages.append({"role": "user", "content": str(input)})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        temperature=0.5
    )
    reply = {"content": completion.choices[0].message.content, "prompt_tokens": completion.usage.prompt_tokens,
             "completion_tokens": completion.usage.completion_tokens, "total_tokens": completion.usage.total_tokens}
    return reply
