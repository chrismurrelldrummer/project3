# Project 3

Web Programming with Python and JavaScript


********** added to 'notifications_tags.py' by C Murrell **************************************************

def notifications_unread_list(context):
    user = user_context(context)
    if not user:
        return ''
    return user.notifications.unread()


if StrictVersion(get_version()) >= StrictVersion('2.0'):
    notifications_unread_list = register.simple_tag(takes_context=True)(
        notifications_unread_list)  # pylint: disable=invalid-name
else:
    notifications_unread_list = register.assignment_tag(takes_context=True)(notifications_unread_list)  # noqa

**********************************************************************