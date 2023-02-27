def get_subject(subject):
    subject_parts = []
    subjects = email.header.decode_header(subject)
    for content, encoding in subjects:
        try:
            subject_parts.append(content.decode(encoding or "utf8"))
        except:
            subject_parts.append(content)
    return "".join(subject_parts)