# Databases

# Person
    name (String)
    description (TextField)            
    birthdate (datetime.Date)        
    nationality (String)
    languages (ArrayField(String))
    skills (ArrayField(String))


# Work
    company_name (String)
    start_date (datetime.Date)
    end_date (datetime.Date)
    job_title_
    job_description (TextField)


# Project
    name (String)
    short_description (String)
    description (TextArea)
    image (ImageField)

# Education
    course (String)
    course_type (Enum)
    institution_name (String)
    start_date (datetime.Date)
    end_date (datetime.Date)

# Certifications
    name (String)
    provider (String)
    date (datetime.Date)

# Awards
    name (String)
    provider (String)
    date (datetime.Date)

# Social links
    name (String)
    url (String)
    icon (ImageField)