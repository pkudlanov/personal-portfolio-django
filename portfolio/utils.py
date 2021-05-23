def msg_constructor(name, from_email, subject, messsage):
    constructed_msg = (
        'Someone has requested that you hear out their voice!!!!\n'
        '\n'
        'Name:\n'
        f'       {name}\n'
        'From E-Mail:\n'
        f'       {from_email}\n'
        'Subject:\n'
        f'       {subject}\n'
        '\n'
        'Message:\n'
        '....................\n'
        f'{messsage}\n'
        '....................'
    )
    return constructed_msg
