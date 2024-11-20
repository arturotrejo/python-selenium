from enum import Enum


class Button:
    APPLY_TO_DRIVE = 'Apply to drive'
    SUBMIT = 'Submit'

class Messages:
    INVALID_PHONE_NUMBER_MESSAGE = 'Error submitting form: Please enter a valid phone number.'

class WaitTimes(Enum):
    WEB_ELEMENT_TIMEOUT = 10
