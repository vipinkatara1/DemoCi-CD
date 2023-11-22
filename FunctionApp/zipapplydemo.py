Personal_info_keys = ['fname', 'lname', 'picture_url', 'gender', 'yob',
                      'experience_years', 'phones', 'address', "summary"]


async def collect_phoneno_info(data):
    final_data = []
    for i in data:
        test_dict = {}
        for j in ["phone"]:
            test_dict[j] = i[j]
        final_data.append(test_dict)
    return final_data


async def collect_personal_info(data):
    new_data = dict()
    for i in list(data):
        if i == "address":
            if data[i]:
                new_data[i] = dict()
                drop_address_keys = ["state_id", "city_id", "lat", "lon"]
                for keys in list(data[i]):
                    if keys in drop_address_keys:
                        data[i].pop(keys)
                new_data[i].update(data[i])
            else:
                new_data[i] = []
        elif i == "phones":
            if data[i]:
                phones_process = await collect_phoneno_info(data[i])
                new_data[i] = phones_process
            else:
                new_data[i] = []
        else:
            new_data[i] = data[i]
    return new_data


async def collect_experiences_info(data):
    keys = ["company_fullname", "is_current", "title"]
    final_data = []
    for i in data:
        test_dict = {}
        for key in keys:
            test_dict.update({key: i[key]})
        final_data.append(test_dict)
    return final_data


async def collect_educations_info(data):
    final_data = []
    for i in data:
        test_dict = {}
        for j in ["organization", "degree", "major"]:
            test_dict[j] = i[j]
        final_data.append(test_dict)
    return final_data


async def collect_skills_info(data):
    final_data = []
    for i in data:
        test_dict = {}
        for j in ["name"]:
            test_dict[j] = i[j]
        final_data.append(test_dict)
    return final_data


async def collect_militaries_info(data):
    final_data = []
    for i in data:
        test_dict = {}
        for j in ["name"]:
            test_dict[j] = i[j]
        final_data.append(test_dict)
    return final_data


async def main_func(data):
    final_data = dict()
    final_data["Personal Information"] = dict()
    for i in Personal_info_keys:
        final_data["Personal Information"].update({i: data.pop(i)})
    personal_info_process = await collect_personal_info(
        final_data["Personal Information"])
    final_data["Personal Information"].update(personal_info_process)
    exp_process = await collect_experiences_info(data["experiences"])
    final_data["experiences"] = exp_process
    skill_process = await collect_skills_info(data["skills"])
    final_data["skills"] = skill_process
    if data["educations"]:
        education_process = await collect_educations_info(data["educations"])
        final_data["educations"] = education_process
    else:
        final_data["educations"] = []
    if data["militaries"]:
        militaries_process = await collect_militaries_info(data["militaries"])
        final_data["About Military Servings"] = militaries_process
    else:
        final_data["About Military Servings"] = []
    return final_data
